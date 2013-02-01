#!/usr/bin/env python

"""A module for working with FASTA files as dictionaries."""


class DuplicateRecordError(Exception):
    """Exception raised when a duplicate record name is encoutered."""

    pass


class RecordNotFoundError(Exception):
    """Exception raised when a record is not found."""

    pass


def fasta_to_dict(infile_h):
    """Takes an open FASTA file and converts it to a dictionary.

    In the event of duplicate record entries in the FASTA file, it
    raises a DuplicateRecordError.

    """
    pass


def retrieve_records(fasta_dict, records_to_retrieve):
    """
    Takes a FASTA dictionary and a list of record names and returns a
    string in FASTA format.

    In the event a record is requested which is not present in the
    dictionary, it raises a RecordNotFoundError.

    """
    pass

