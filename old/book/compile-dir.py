import os, compileall

def main():
    chdir = "/home/raihan/Documents/Python"
    compileall.compile_dir(chdir)
    print("Compilation complete.")

if __name__ == "__main__":
    main()