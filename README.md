# python4

A modular interpreter with auto-correction, REPL, console, and extended features – designed for accessibility and experimentation.

## ✨ Features
- **Compiler with auto-correction**: fixes typos (`pritn` → `print`) and missing syntax (e.g. `:`).
- **Activation mode**: `Compiler.activate()` enables global auto-correction for all subsequent code.
- **REPL**: interactive input with instant execution.
- **Console**: buffered output via `py4_print()`, with `show()` and `clear()`.
- **Extended features**: pattern matching, lambdas, decorators, async/await, OOP, f-strings, comprehensions.

## 📂 Project Structure
python4/
├── main.py
├── python4_core.py
├── console.py
├── repl.py
└── features.py

## 🚀 Installation
git clone https://github.com/<your-username>/python4.git
cd python4
python3 main.py

## 🖥 Usage

### Activate Compiler
from python4_core import Compiler

Compiler.activate()   # enable auto-correction globally
Compiler.run('pritn("Hello World")')   # corrected automatically

### REPL
from repl import repl
from python4_core import Compiler

Compiler.activate()
repl()

### Console
from console import py4_print, console

py4_print("Hello World")
py4_print("Sum:", 2+3)
console.show()

## 📖 Note
This is an experimental project – intended as a learning environment and proof-of-concept.  
Best run in **Carnets Plus** on iPad or locally with Python 3.9+.
