from lex import Lexer
from emit import Emitter
from parse import Parser
import sys, time

def main():
    print("Programmatrix Compiler")

    if len(sys.argv) != 2:
        sys.exit("You idiot: Put a file in.")
    with open(sys.argv[1], 'r') as inputFile:
        inputF = inputFile.read()
    # Initialise the lexer, emitter, and parser.
    lexer = Lexer(inputF)
    emitter = Emitter("out.c")
    parser = Parser(lexer, emitter)

    parser.program() # Start the parser.
    emitter.writeFile() # Write the output to file.
    print("Compiling completed.")



if __name__ == "__main__":
    main()
