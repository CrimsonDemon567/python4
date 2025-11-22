# main.py
# Entry point for Python 4 (Experimental)
# Quiet by default, only executes when called.

from python4_core import Compiler

def main():
    # Beispiel: Compiler aktivieren
    Compiler.activate()

    # Danach kannst du beliebigen Code korrigiert ausführen:
    Compiler.run('pritn("Hello World")')
    Compiler.run('if 1 print("Yes")')

if __name__ == "__main__":
    main()

