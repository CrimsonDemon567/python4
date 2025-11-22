# features.py
# Extended language features for Python 4

# --- Pattern Matching ---
def match_example(value):
    match value:
        case 0:
            return "Zero"
        case 1:
            return "One"
        case _:
            return "Other"

# --- Lambda Example ---
square = lambda x: x * x

# --- Decorator Example ---
def debug(func):
    def wrapper(*args, **kwargs):
        print(f"[DEBUG] Calling {func.__name__} with {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@debug
def add(a, b):
    return a + b

# --- Async Example ---
import asyncio

async def async_hello():
    await asyncio.sleep(1)
    print("Hello from async!")

# --- OOP Example ---
class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

# --- f-string Example ---
def fstring_example(name, age):
    return f"{name} is {age} years old."

# --- Comprehension Example ---
def comprehension_example():
    return [x*x for x in range(5)]
