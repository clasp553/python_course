#!/bin/bash
#SBATCH -A snic2021-5-305
#SBATCH -N 1
#SBATCH -n 8
#SBATCH --mem=20000
#SBATCH --time=04:00:00

module purge
module load ORCA/.5.0.2-nsc1

echo "Copying files to local scratch..."
cp *.inp *.gbw *.xyz *.hess *.opt *.allxyz $SNIC_TMP/

cd $SNIC_TMP

trap 'echo "ABNORMAL stop, copying out files..." ; cp *.gbw *.xyz *.hess *.opt *.cis *.dat *.log *.inp *.interp *.csv *.allxyz $SLURM_SUBMIT_DIR' SIGTERM

echo "Starting ORCA..."
orca.run Cu-4gly.inp > $SLURM_SUBMIT_DIR/Cu-4gly.out & wait

orca_status=$?

echo "Normal stop, copying out files..." ; cp *.gbw *.xyz *.hess *.cis *.opt *.dat *.log *.inp *.interp *.csv *.allxyz $SLURM_SUBMIT_DIR

exit $orca_status


