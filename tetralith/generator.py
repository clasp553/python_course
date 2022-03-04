import os

class Generator:           
    
    @classmethod    
    def inp_writer(cls):
        runner = cls()
        runner.xyz_reader()
        xyzfile = runner.xyzfile
        charge = input("Complex charge: ")
        mult = input("Complex multiplicity: ")
        print("\nCreating .inp file...")
        
        #Give a title to calculation
        title = input("Title of calculation:")
        print("\n"+title)
        
        #Define type of simulation, functional and appproximations
        try:
            calc = int(input("Please define simulation parameters:\nFormat example: TPSS def2-TZVP def2/J D3BJ TightOpt UseSym freq CPCM(THF)\n"))
        except ValueError: #sets default parameters if no input
            calc = "TPSS def2-TZVP def2/J D3BJ TightOpt UseSym freq CPCM(THF)"
        print(calc)
        
        lines = ["# " + title, 
                 "! " + calc, 
                 "% pal nprocs 8 end", #to be implemented
                 "%maxcore 2000\n", #to be implemented
                 "*xyzfile  " + charge + " "+ mult + " " + xyzfile
                 ]
        
        with open("test.inp", "w") as f:
           f.write("\n".join(lines))
        print("\nYour .inp file has been created!")
        
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
        xyzfile = self.xyzfile
        return xyzfile