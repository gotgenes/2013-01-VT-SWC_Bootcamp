# Shell Exercises

## Current

List all files (including hidden files) in `shell_tutorial` and all of
its subdirectories.

* * * *

## To Do

Print the contents of the `dictionary.txt` file out to the terminal.
What does this file contain?

* * * *

Use the commands we've learned so far to figure out how to search
backwards while using `less`.

* * * *

1.  Copy the `.hidden_directory` subdirectory and all its contents to a
    new directory called `unhidden`
2.  Remove the `.hidden` directory.
3.  Rename `unhidden` to `.hidden_directory`.

* * * *

Sort the names in `names.txt` by last name, in reverse reverse order.

* * * *

1.  Use the `echo` command and redirection to append your name to
    `names.txt`.
2.  Print the contents of `names.txt`, sorted by first name, to a new
    file, `sorted_names.txt`.

* * * *

1.  Use cut and sort to get the list of payments from `userpayment.csv`.
    How many times was American Express used?
2.  How can you figure out the same thing using only sort?

* * * *

Use a combination of pipes between tail, cut, sort, uniq, and wc to
figure out how many different drinking levels exist in `userprofile.csv`.

* * * *

For each of the following, use a single `ls` command to:

1.  list all of the files in `shell_tutorial` that contain the letter `e`
2.  list all of the files in `shell_tutorial` that contain the letter `e` or
    the letter `i`
3.  list all of the files in `shell_tutorial` that contain the letter `e`
    FOLLOWED BY the letter `i`

* * * *

1. Use `>` to concatenate all the data in the `shell_tutorial/data/Bert`
   subdirectory to a file called `all_data` under `data/`.

2. Use `>>` to append the contents of all of the files which contain the
   number 4 in the directory `shell_tutorial/data/gerdal` to the
   existing `all_data` file.

When you are done, `all_data` should contain all of the experiment data
from Bert and any experimental data file from gerdal that contains the
number 4.

* * * *

Combine the `wc`, `sort`, `head` and `tail` commands so that only the
`wc` information for the largest file is listed

Hint: To print the smallest file, use:

    wc Bert/* | sort -k 3 -n | head -n 1


* * * *

## Completed

