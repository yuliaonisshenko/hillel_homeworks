"""
Implement your own print function. It should work on all operating systems.
You can't use build-in print function
"""
import sys
def custom_print(*args, sep=' ', end='\n', file=sys.stdout, flush=False):
    output = sep.join(str(arg) for arg in args) + end

    if file is sys.stdout or file is sys.stderr:
        file.write(output)
        if flush:
            file.flush()
    else:
        with open(file, 'a') as f:
            f.write(output)

# just to try
custom_print("Hello", "world!")
