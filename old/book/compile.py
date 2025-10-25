import os, py_compile

def main():
    os.chdir("/home/raihan/Documents/Python")
    py_compile.compile("hello-world.py")
    print("Compilation complete.")

if __name__ == "__main__":
    main()