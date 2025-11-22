# python4

A modular interpreter with auto-correction, REPL, editor, and console – designed as a proof-of-concept for a more accessible, interactive programming language.

## ✨ Features
- **Compiler with auto-correction**: fixes typos (`pritn` → `print`) and missing syntax (e.g. `:`).
- **REPL**: interactive input with instant execution.
- **Editor**: tabs, undo/redo, syntax highlighting, error markers.
- **Console**: manages output (`py4_print`) with buffer, `show()`, and `clear()`.
- **Community features**: pattern matching, lambdas, decorators, async/await, OOP, f-strings, comprehensions, and more.

## 📂 Project Structure

python4/ 
├── python4_core.py        # Lexer, parser, AST, interpreter, compiler with auto-correction
├── console.py             # Console module with print() wrapper 
├── repl.py                # Interactive REPL with auto-correction 
├── features.py            # Extended language features └── main.py                # Entry point

