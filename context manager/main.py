# Code 1
from  contextlib import  contextmanager
@contextmanager
def my_context_manager():
    print("Entering the context")

    try:
        yield

    finally:
        print("Exiting the context")

with my_context_manager():
    print("Code in the middle-1")
    print("Code in the middle-2")
    print("Code in the middle-3")

# Code 2
class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self
    def __init__(self):
        self.name = "sandun"
        print("constructor was executed")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the context")

with MyContextManager() as obj:
    print("Code below the with statement")
    print(obj.name)

