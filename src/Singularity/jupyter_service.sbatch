#!/bin/bash
#SBATCH -n 20
#SBATCH -N 1
#SBATCH -A lsens2018-3-3
#SBATCH -p dell
#SBATCH -t 2-12
#SBATCH -J SC_arches_train
#SBATCH -o logs/SC_arches_train%j.out
#SBATCH -e logs/SC_arches_train%j.err
module purge
module use /projects/fs1/common/modules/
module load Singularity/default

singularity exec --bind /home/davhg96/Desktop/SCAML/files:/workspace scarches.sif bash -c "cd /workspace && jupyter lab --port 3333 --ip=0.0.0.0 --allow-root --no-browser"
