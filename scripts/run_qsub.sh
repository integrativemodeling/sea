#!/bin/bash
#
#$ -S /bin/bash
#$ -cwd
#$ -r y
#$ -j y
#$ -l mem_free=2G
#$ -l arch=linux-x64
#$ -l netapp=5G,scratch=5G
#$ -l scrapp=500G
#$ -l scrapp2=500G
#$ -l h_rt=335:59:59
#$ -R y
#$ -V
##$ -q lab.q
#$ -l hostname="i*"                 #-- anything based on Intel cores
##$ -l hostname="!opt*"			    #-- anything but opt*
##$ -m e                            #-- uncomment to get email when the job finishes
##$ -t 1-1000                        #-- specify the number of tasks

#usage : run_qsub.sh REPEAT1 REPEAT2 N_COPY SYMMETRY
date
hostname
echo

# Do any necessary setup to find IMP Python packages
#module load imp

RMF_NFRAMES=500
#FLAG_RMF_SLICE=1
FLAG_RMF_SLICE=0
#FLAG_REFINE=1
FLAG_REFINE=0
IMP_RUN="python ../scripts/sj_SEA_multi_layers.py"
PROCESS_RUN="../scripts/process_output_sj.py"
FILE1="models.rmf"
FILE2="stat.dat"
XL="../SEAcmplx_XL.txt"
export WEIGHT=1.0
export PWD_PARENT=$(pwd)
echo "PWD = $PWD_PARENT"

if [ -z $1 ]; then
    REPEAT1=50000
else
    REPEAT1=$1
fi
echo "INITIAL Monte Carlo Runs : $REPEAT1"

if [ -z $2 ]; then
    REPEAT2=20000
else
    REPEAT2=$2
fi
echo "REFINEMENT Monte Carlo Runs : $REPEAT2"

if [ -z $3 ]; then
    N_COPY=3
else
    N_COPY=$3
fi
echo "Copy numbers (Stoichiometry) of SEA4 and Seh1 : $N_COPY"

if [ -z $4 ]; then
    SYMMETRY="False"
else
    SYMMETRY="$4"
fi
echo "Symmetry of SEA4 and Seh1 : $SYMMETRY"

############################################################################
# Unpack tar.gz files
############################################################################
echo "========================================================================"
if [ -f $FILE1.tar.gz ] && [ -f $FILE2.tar.gz ]; then
    echo "Files of both $FILE1.tar.gz and $FILE2.tar.gz do exist !"

    tar xzf $FILE1.tar.gz
    rm -rf $FILE1.tar.gz
    tar xzf $FILE2.tar.gz
    rm -rf $FILE2.tar.gz
fi

############################################################################
# INITIAL Monte Carlo job, with crosslinks and minimal domain mapping data
############################################################################
if [ -f $FILE1 ] && [ -f $FILE2 ]; then
    echo "Files of both $FILE1 and $FILE2 do exist !"
    echo "Retrieving the best scoring frame, from both $FILE1 and $FILE2"
else
    echo "File $FILE1 and/or $FILE2 do(es) NOT exist !"
    echo "Running an initial Monte Carlo job, with crosslinks and minimal domain mapping data"
    echo "========================================================================"

    $IMP_RUN -r $REPEAT1 -w $WEIGHT -x $XL -o $FILE1 -s $FILE2 --REFINE False --copy $N_COPY --sym $SYMMETRY
fi

$PROCESS_RUN -f $FILE2 -s ConnectivityCrossLinkMS_Score_None ExcludedVolumeSphere_None SimplifiedModel_Total_Score_None PartialScore1 PartialScore2 > output.log
export NUMOFLINES=$(expr $(cat output.log | wc -l) - 1)

if [ $NUMOFLINES -lt 1 ]; then
    echo NUMOFLINES = $NUMOFLINES
    $PROCESS_RUN -f $FILE2 -s ConnectivityCrossLinkMS_Score_None ExcludedVolumeSphere_None SimplifiedModel_Total_Score_None ConnectivityRestraint_Npr2_dNpr2_497_615_P > output_original.log
    awk '{print $1, $2, $3, $4, $5, $5, $3 + ENVIRON["WEIGHT"] * $6}' output_original.log > output.log
fi

sort -r -n -k 3 output.log | awk '{print ENVIRON["PWD_PARENT"], $1, $2, $3, $4, $5, $6, $7}' > output_XL_sorted.log
sort -r -n -k 7 output.log | awk '{print ENVIRON["PWD_PARENT"], $1, $2, $3, $4, $5, $6, $7}' > output_PS2_sorted.log
echo "========================================================================"

############################################################################
# Retrieving the best scoring frame from the INITIAL Monte Carlo job
############################################################################
if [ $FLAG_RMF_SLICE -eq 1 ]; then
    export NUMOFLINES=$(expr $(cat output.log | wc -l) - 1)
    echo "Processing $NUMOFLINES cycles from the previous run"

    FRAME=$(awk '{if (NR == ENVIRON["NUMOFLINES"]) print $2}' output_PS2_sorted.log)
    if [ $FRAME == "#" ]; then
        export NUMOFLINES=$(expr $(cat output.log | wc -l))
        FRAME=$(awk '{if (NR == ENVIRON["NUMOFLINES"]) print $2}' output_PS2_sorted.log)
    fi
    echo "The best scoring FRAME by (XL + minimal domain mapping data) : $FRAME"
    awk '{if (NR == ENVIRON["NUMOFLINES"]) print $1, $2, $3, $4, $5, $6, $7, $8}' output_PS2_sorted.log

    RMF_NO=$(expr $( expr $FRAME - 1 ) / $RMF_NFRAMES)
    RMF_FRAME=$(expr $( expr $FRAME - 1 ) % $RMF_NFRAMES)
    RMF_FILE="models.$RMF_NO.rmf"

    rmf_slice $RMF_FILE models_$FRAME.rmf -f $RMF_FRAME -s 1000000
    #rmf_slice $FILE1 models_$FRAME.rmf -f $FRAME -s 1000000

    tar czf $FILE2.tar.gz $FILE2
    rm -rf $FILE2
    tar czf $FILE1.tar.gz models.*.rmf
    #tar czf $FILE1.tar.gz $FILE1
    rm -rf models.*.rmf
    #rm -rf $FILE1
fi

############################################################################
# REFINEMENT Monte Carlo job, with crosslinks and ALL domain mapping data
############################################################################
if [ $FLAG_REFINE -eq 1 ]; then
    echo "========================================================================"
    echo "Running the REFINEMENT Monte Carlo job, with crosslinks and ALL domain mapping data"

    RMF_OUTPUT=REFINED_models.rmf
    STAT_OUTPUT=REFINED_stat.dat

    $IMP_RUN -f models_$FRAME.rmf -n 0 -r $REPEAT2 -w $WEIGHT -x $XL -o $RMF_OUTPUT -s $STAT_OUTPUT --REFINE True --copy $N_COPY --sym $SYMMETRY

    $PROCESS_RUN -f $STAT_OUTPUT -s ConnectivityCrossLinkMS_Score_None ExcludedVolumeSphere_None SimplifiedModel_Total_Score_None PartialScore1 PartialScore2 > REFINED_output.log

    sort -r -n -k 3 REFINED_output.log | awk '{print ENVIRON["PWD_PARENT"], $1, $2, $3, $4, $5, $6, $7}' > REFINED_output_XL_sorted.log
    sort -r -n -k 7 REFINED_output.log | awk '{print ENVIRON["PWD_PARENT"], $1, $2, $3, $4, $5, $6, $7}' > REFINED_output_PS2_sorted.log
    echo "========================================================================"

    ############################################################################
    # Retrieving the best scoring frame from the REFINEMENT Monte Carlo job
    ############################################################################
    if [ $FLAG_RMF_SLICE -eq 1 ]; then
        export NUMOFLINES=$(expr $(cat REFINED_output.log | wc -l) - 1)
        echo "Processing $NUMOFLINES cycles from the previous run"

        FRAME_REFINED=$(awk '{if (NR == ENVIRON["NUMOFLINES"]) print $2}' REFINED_output_PS2_sorted.log)
        if [ $FRAME_REFINED == "#" ]; then
            export NUMOFLINES=$(expr $(cat REFINED_output.log | wc -l))
            FRAME_REFINED=$(awk '{if (NR == ENVIRON["NUMOFLINES"]) print $2}' REFINED_output_PS2_sorted.log)
        fi
        echo "The best scoring FRAME by (XL + all domain mapping) data : $FRAME_REFINED"
        awk '{if (NR == ENVIRON["NUMOFLINES"]) print $1, $2, $3, $4, $5, $6, $7, $8}' REFINED_output_PS2_sorted.log

        RMF_NO=$(expr $( expr $FRAME_REFINED - 1 ) / $RMF_NFRAMES)
        RMF_FRAME=$(expr $( expr $FRAME_REFINED - 1 ) % $RMF_NFRAMES)
        RMF_FILE="REFINED_models.$RMF_NO.rmf"

        rmf_slice $RMF_FILE REFINED_models_${FRAME_REFINED}.rmf -f $RMF_FRAME -s 1000000
        #rmf_slice $RMF_OUTPUT REFINED_models_${FRAME_REFINED}.rmf -f $FRAME_REFINED -s 1000000

        tar czf $STAT_OUTPUT.tar.gz $STAT_OUTPUT
        rm -rf $STAT_OUTPUT
        tar czf $RMF_OUTPUT.tar.gz REFINED_models.*.rmf
        #tar czf $RMF_OUTPUT.tar.gz $RMF_OUTPUT
        rm -rf REFINED_models.*.rmf
        #rm -rf $RMF_OUTPUT
    fi
fi

echo
date
hostname
