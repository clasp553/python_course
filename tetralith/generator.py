import os

class Generator:         
    
    def __init__(self):
        self.xyzfile = "dummy"
        self.filename = "dummy.inp"
    
    
    def xyz_reader(self):
        print("Paste directory path where coordinates are located:")
        directory = input("directory = ")
        directory = directory.strip('"')
        
        sorted_files = sorted(os.listdir(directory))
        
        print("\nCoordinate files in your directory:\n")
        for file in sorted_files:
            if file.endswith(".xyz"):
                print(file)
        
        xyzfile = input("\nSelected file: ")
        self.xyzfile = xyzfile+".xyz"
        #xyzfile = self.xyzfile
        return self.xyzfile
    
    
    def inp_writer(self):
        xyzfile = self.xyz_reader()
        charge = input("Complex charge: ")
        mult = input("Complex multiplicity: ")
        print("\nCreating .inp file...")
        
        #Name of the .inp file
        filename = input("Input file name: ")
        filename = filename + ".inp"
       
        #Give a title to calculation
        title = input("Title of calculation:")
        print("\n"+title)
        
        #Define type of simulation, functional and appproximations
        try:
            calc = int(input("Please define simulation parameters:\n(Default: TPSS def2-TZVP def2/J D3BJ TightOpt UseSym freq CPCM(THF))\n"))
        except ValueError: #sets default parameters if no input
            calc = "TPSS def2-TZVP def2/J D3BJ TightOpt UseSym freq CPCM(THF)"
        print(calc)
        
        lines = ["# " + title, 
                 "! " + calc, 
                 "% pal nprocs 8 end", #to be implemented
                 "%maxcore 2000\n", #to be implemented
                 "*xyzfile  " + charge + " "+ mult + " " + xyzfile
                 ]
        
        with open(filename, "w") as f:
           f.write("\n".join(lines))
        self.filename = filename
        return self.filename
        
    
    def sh_writer(self):
        print("Creating .sh file...")
        
        #Number of nodes to use
        try:
            n_proc = int(input("# nodes (Default: 8): "))
        except ValueError: #sets default parameters if no input
            n_proc = "8"
            
        #Max time for calculation
        try:
            time = int(input("Time (Default: 04:00:00): "))
        except ValueError: #sets default parameters if no input
            time = "04:00:00"
            
        #Output file name
        try:
            out = input("Output file name (Default: same as input file): ")
        except ValueError: #sets default parameters if no input
            out = self.filename
        out = out.replace(".inp", "")
        
        lines = ["#!/bin/bash", 
                 "#SBATCH -A snic2021-5-305", 
                 "#SBATCH -N 1",
                 "#SBATCH -n " + n_proc,
                 "#SBATCH --mem=20000", #to implement from .inp file
                 "#SBATCH --time="+ time +"\n",
                 "module purge\nmodule load ORCA/.5.0.2-nsc1\n",
                 'echo "Copying files to local scratch..."\ncp *.inp *.gbw *.xyz *.hess *.opt *.allxyz $SNIC_TMP/\n',
                 "cd $SNIC_TMP\n",
                 "trap "+"'echo "+'"ABNORMAL stop, copying out files..."'+" ; cp *.gbw *.xyz *.hess *.opt *.cis *.dat *.log *.inp *.interp *.csv *.allxyz $SLURM_SUBMIT_DIR' SIGTERM\n",
                 'echo "Starting ORCA..."',
                 "orca.run " + self.filename + " > $SLURM_SUBMIT_DIR/" + out + ".out & wait\n",
                 "orca_status=$?\n",
                 'echo "Normal stop, copying out files..." ; cp *.gbw *.xyz *.hess *.cis *.opt *.dat *.log *.inp *.interp *.csv *.allxyz $SLURM_SUBMIT_DIR\n',
                 "exit $orca_status"
                 ]
        
        with open(self.filename.replace(".inp", "")+".sh", "w") as f:
           f.write("\n".join(lines))