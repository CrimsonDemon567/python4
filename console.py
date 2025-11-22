# console.py
# Console module for Python 4

class Console:
    def __init__(self):
        self.buffer = []

    def write(self, text: str):
        """Write text to buffer and also print it."""
        self.buffer.append(text)
        print(text)

    def show(self):
        """Show all buffered output with line numbers."""
        for i, line in enumerate(self.buffer, start=1):
            print(f"{i:02d}: {line}")

    def clear(self):
        """Clear the buffer."""
        self.buffer = []
        print("[Console cleared]")

# Global console instance
console = Console()

def py4_print(*args):
    """Wrapper for print that writes to console buffer."""
    text = " ".join(str(a) for a in args)
    console.write(text)
