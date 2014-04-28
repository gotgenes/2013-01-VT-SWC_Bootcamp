# Python Exercise 1

By completing this task, you will have successfully understood and implemented
the fundamentals of strings, lists, files, functions, and modules.

We have a collection of files in `data/`. The files contain strings, but
they're written vertically (one character per line) instead of
horizontally. For example, we will convert a file containing

    S
    o
    m
    e

    w
    o
    r
    d
    s
    .

to a file containing

    Some words.

We're going to write some code to convert this text from a
vertical format to normal horizontal format.

Create a module called `vtoh.py`. Write a function in this module
called `vfile_to_hstring` that takes a file handle to a file containing
vertical text, converts the text to a normal horizontal string, and
returns this string.

Next, write a script called `vfile_converter.py`, which takes as
command line arguments one or more files. (HINT: There is also a Python
library module to help you get command line <b>sys</b>tem <b>arg</b>uments.)
`vfile_convertert.py` should then do the following for each file

1. open the file
2. call the `vtoh.vfile_to_hstring` function with the open file handle
   as an argument, and
3. Output the horizontal text string to a file with the same base name
   as the original, but the extension `.out` instead of `.txt` (e.g.,
   `somefile.txt` will have its output written to `somefile.out`) (HINT:
   There is a Python library module to help you work with <b>o</b>perating
   <b>s</b>ystem <b>path</b>s that can **split** filenames into their basename
   (e.g., `somefile`) and extension (e.g., `.txt`)


Use `data/smart.txt` and `data/hang.txt` as test files.

