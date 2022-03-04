"""
This module creates .sh files using the previously created .inp file
"""
def sh_writer():
    print("Creating .sh file...")
    
    lines = ["#!/bin/bash", 
             "#SBATCH -A snic2021-5-305", 
             "#SBATCH -N 1",
             "#SBATCH -n 8",
             "#SBATCH --mem=20000",
             "#SBATCH --time=04:00:00\n",
             "module purge\nmodule load ORCA/.5.0.2-nsc1\n",
             'echo "Copying files to local scratch..."\ncp *.inp *.gbw *.xyz *.hess *.opt *.allxyz $SNIC_TMP/\n',
             "cd $SNIC_TMP\n",
             "trap "+"'echo "+'"ABNORMAL stop, copying out files..."'+" ; cp *.gbw *.xyz *.hess *.opt *.cis *.dat *.log *.inp *.interp *.csv *.allxyz $SLURM_SUBMIT_DIR' SIGTERM\n",
             'echo "Starting ORCA..."',
             "orca.run Cu-4gly.inp > $SLURM_SUBMIT_DIR/Cu-4gly.out & wait\n",
             "orca_status=$?\n",
             'echo "Normal stop, copying out files..." ; cp *.gbw *.xyz *.hess *.cis *.opt *.dat *.log *.inp *.interp *.csv *.allxyz $SLURM_SUBMIT_DIR\n',
             "exit $orca_status"
             ]
    
    with open("test.sh", "w") as f:
       f.write("\n".join(lines))