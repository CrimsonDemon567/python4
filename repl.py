# repl.py
# Interactive REPL for Python 4

from python4_core import Compiler

def repl():
    """Start an interactive REPL loop for Python 4."""
    print("Python 4 REPL (type 'exit' to quit)")
    while True:
        try:
            line = input(">>> ")
            if line.strip().lower() in ("exit", "quit"):
                break
            Compiler.run(line)
        except KeyboardInterrupt:
            print("\n[Interrupted]")
            break
        except EOFError:
            print("\n[EOF]")
            break
