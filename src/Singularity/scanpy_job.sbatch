#!/bin/bash                                                                       
#SBATCH -n 20                                                                      
#SBATCH -N 1                                                                      
#SBATCH -A lsens2018-3-3                                                                
#SBATCH -p dell                                                                     
#SBATCH -t 2-12                                                                   
#SBATCH -J SC_arches_train
#SBATCH -o SC_preprocess_%j.out
#SBATCH -e SC_preprocess_%j.err
module purge
module use /projects/fs1/common/modules/

singularity exec --bind /home/parashar/david_sing_course/mydata:/workspace scarches.sif python /workspace/test_scanpy.py /workspace/pbmc_data.h5
