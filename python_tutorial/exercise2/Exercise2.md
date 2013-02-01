# Python Exercise 2

By successfully completing this exercise, you will have demonstrated
competence in working with dictionaries and exceptions, and doing test-driven
design (TDD) and design by contract (DBC).

The [FASTA format](http://en.wikipedia.org/wiki/FASTA_format) is
commonly used to store biological (DNA, RNA, or protein) sequence
information.  In this exercise, you will write a module which is capable
of converting a FASTA file to a dictionary structure, conversely, taking
a FASTA-based dictionary structure and converting selected records in it
back to FASTA file format.


## Test-driven development

At all points along the way, you should be testing your module against
the provided tests in the test script under tests.  Specifically, run
the following command from the exercise2 directory:

nosetests tests

At this point, you should see that all tests are failing, with a description
of each test and output to help you trace why the test failed.  The codes for
the tests are:

* `.`: Test passed
* `F`: Test failed, output expected did not meet output from your code
* `E`: Error, there was an error during the execution of the test; inspect
  your code for bugs

When you see a '.' for all tests against your function, you know it fulfills
its design contract, and that you are done coding that function.


## Design by contract

1. Flesh out the function called `fasta_to_dict` to accept a file handle for
an open FASTA file as input and return a dictionary as its output. The output
dictionary should contain the header lines as keys, without the leading `>`
character, and the values of the dictionary should be the sequence strings
themselves, without any whitespace (e.g., newline characters).

2. In the event `fasta_to_dict` parses a file that contains multiple
records with the same header, it should raise a `DuplicateRecordError`
exception. (Because we have not yet covered object-oriented programming,
the exception has already been provided to you in the template.)

3. Next, build the function called `retrieve_records` that accepts as its
arguments a dictionary, of the structure output by `parse_fasta`, and a list
of record names (i.e., the text in the header lines) and . The function
`retrieve_records` returns a string of those requested records in FASTA
format.  Ensure that the sequence is restricted to a maximum width of 60
characters per row, while the header is allowed to span a greater length if
necessary, as typical of FASTA format files. (HINT: Do not code a function to
wrap text to 60 characters yourself. There is already a Python Standard
Library module for **text**-**wrap**ping available to you.)

4. In the event that `retrieve_records` receives a request for a record not
present in the FASTA records dictionary, it should raise a
`RecordNotFoundError` exception.  Again, this exception has been provided for
you in the template.  Use the example given in the Quality Assurance lecture
notes for demonstration on how to raise the `RecordNotFound` exception.

At this point, all your tests should be passing. Congratulations! You can
be assured your code behaves expectedly and precisely to specifications!
Commit your module to the repository and pat yourself on the back for a job
well done.

