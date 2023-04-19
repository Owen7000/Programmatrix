from lex import *
from emit import *
from parse import *
import sys, time

def main():
    print("Programmatrix Compiler")

    if len(sys.argv) != 2:
        sys.exit("You idiot: Put a file in.")
    with open(sys.argv[1], 'r') as inputFile:
        inputF = inputFile.read()
    # Initialize the lexer, emitter, and parser.
    lexer = Lexer(inputF)
    emitter = Emitter("out.c")
    parser = Parser(lexer, emitter)

    parser.program() # Start the parser.
    emitter.writeFile() # Write the output to file.
    print("Compiling completed.")

    time.sleep(10)


if __name__ == "__main__":
    main()
