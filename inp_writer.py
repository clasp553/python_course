"""
This module creates .inp files using the selected coordinate files
"""
def inp_writer():
    print("Creating .inp file...")
    
    #Give a title to calculation
    try:
        title = input("Title of calculation:")
    except ValueError: #Sets empty title if no imput
        title = ""  
    print("\n"+title)
    
    #Define type of simulation, functional and appproximations
    try:
        calc = int(input("Simulation parameters:\nExample format: TPSS def2-TZVP def2/J D3BJ TightOpt UseSym freq CPCM(THF)"))
    except ValueError: #sets default parameters if no input
        calc = "TPSS def2-TZVP def2/J D3BJ TightOpt UseSym freq CPCM(THF)"
    print("\n"+calc)
    
    lines = ["# " + title, 
             "! " + calc, 
             "% pal nprocs 8 end",
             "%maxcore 2000\n",
             "*xyzfile  -2 2 Cu-4gly.xyz"
             ]
    
    with open("test.inp", "w") as f:
       f.write("\n".join(lines))
    

