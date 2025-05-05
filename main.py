from contextlib import contextmanager

@contextmanager
def file_open(path, mode):
    try:
        f = open(path, mode)
    except Exception as e:
        print(f"Error while openning file '{path}: '{e}'")
    
    print("Working with file started")
    try:
        yield f
    finally:
        print("Closing file in progress")
        f.close()
        print("File closed")


