#!/usr/bin/bash
#
# Author: Han Qiu
# Updated: December 12, 2021
# 79: -------------------------------------------------------------------------

# slurm options: --------------------------------------------------------------
#SBATCH --job-name=ps8_q0
#SBATCH --mail-user=itskeira@umich.edu
#SBATCH --mail-type=BEGIN,END
#SBATCH --cpus-per-task=5
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem-per-cpu=5GB 
#SBATCH --time=10:00
#SBATCH --account=stats507f21_class
#SBATCH --partition=standard
#SBATCH --output=/home/%u/logs/%x-%j-4.log

# application: ----------------------------------------------------------------
n_procs=5

# modules 
module load tensorflow

# the contents of this script
cat ps8_q0.sh

# run the script
date

cd /home/itskeira/Stats507/demo/
python ps8_q0.py $n_procs


date
echo "Done."
