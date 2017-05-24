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
#$ -l hostname="io*"                 #-- anything based on Intel cores
##$ -l hostname="!opt*"			    #-- anything but opt*
##$ -m e                            #-- uncomment to get email when the job finishes
##$ -t 1-3                         #-- specify the number of tasks

date
hostname
echo
#SGE_TASK_ID=1

module load sali-libraries

#for (( SGE_TASK_ID=1; SGE_TASK_ID<=3; SGE_TASK_ID++ )); do
    setup_environment.sh python ./sj_analyze_three_sym.py
    #setup_environment.sh python ./sj_analyze_three_sym_cluster.py > sj_analyze_three_sym_cluster.log
#done

echo
date
hostname
