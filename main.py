from tetralith.generator import Generator

def main():
    gen = Generator()
    print("Welcome to the Tetralith files generator!\n")
    gen.inp_writer()
    print("\nYour .inp file has been created!\n")
    gen.sh_writer()
    print("\nYour .sh file has been created!\nNow you can run your simulation.")
    
if __name__ == "__main__":
    main()
