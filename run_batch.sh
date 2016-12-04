#!/bin/bash
#
#$ -S /bin/bash
#$ -cwd
#$ -r y
#$ -j y
#$ -l mem_free=2G
#$ -l arch=linux-x64
#$ -l netapp=5G,scratch=5G
#$ -l scrapp=250G
#$ -l scrapp2=250G
#$ -l h_rt=335:59:59
#$ -R y
#$ -V
##$ -q lab.q
#$ -l hostname="i*"                 #-- anything based on Intel cores
##$ -l hostname="!opt*"			    #-- anything but opt*
##$ -m e                            #-- uncomment to get email when the job finishes
#$ -t 1-100                         #-- specify the number of tasks
SGE_TASK_ID=1
#let "SLEEP_TIME=$SGE_TASK_ID*2"
#sleep $SLEEP_TIME

date
hostname
#echo

PWD_PARENT=$(pwd)

#for DIR in modeling*; do
    i=$(expr $SGE_TASK_ID)
    DIR=modeling$i

    if [ ! -d $DIR ]; then
        mkdir $DIR
    fi
    cd $DIR

    PWD=$(pwd)
    echo $PWD_PARENT : $PWD

    if [ $PWD_PARENT != $PWD ]; then

        #usage : run_qsub.sh REPEAT1 REPEAT2 N_COPY SYMMETRY
        ../run_qsub.sh 50000 20000 3 True
        #../run_qsub.sh 50000 20000 3 False
        #../run_qsub.sh 50000 20000 1 False
        #../run_qsub.sh 50 20 1 False
        cd ..
    fi
#done

#echo
date
hostname
