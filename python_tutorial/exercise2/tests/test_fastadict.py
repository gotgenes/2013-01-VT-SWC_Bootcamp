#!/usr/bin/env python

"""Tests for fastadict.py"""


import os
from StringIO import StringIO
import sys
import unittest

from exercise2 import fastadict


#TESTDIR = os.path.dirname(os.path.abspath(__file__))
#PROJECTDIR = os.path.dirname(TESTDIR)
#sys.path.append(PROJECTDIR)
#module_to_import = sys.argv[1]
#if module_to_import.endswith('.py'):
    #module_to_import = module_to_import[:-3]
#fastadict = __import__(module_to_import)


class CaseHolderMixin(object):
    """Holds cases for use in unit tests."""

    cases = (
        (
# record with one nucleotide
""">gene1
A
""",
            {'gene1': 'A'}
        ),
        (
# record with a full line of nucleotides
""">gene2
CCAACTGGTTGTGGCCTATCGAAAAGTGAACTTCATAACACATGCTGTCCCACGCACATC
""",
            {
                'gene2':
'CCAACTGGTTGTGGCCTATCGAAAAGTGAACTTCATAACACATGCTGTCCCACGCACATC'
            }
        ),
        (
# record with two lines of nucleotides
""">gene3
GGATGATTTGGACAAATTTGATTCGAGTCTGATCAACCTTCACACAGATCTAGAATCGAA
A
""",
            {
                'gene3':
'GGATGATTTGGACAAATTTGATTCGAGTCTGATCAACCTTCACACAGATCTAGAATCGAAA'
            }
        ),
        (
# record with two full lines of nucleotides
""">gene4
TAAACGTTGGTCCGTCTGAACCGCCATCCAGGATCACGTCGCCCTGAAAAAAAGATATCA
GGAACTCTCCTCCTCAGCAGTCTGGTCTATGGAAACTACAGGACTAACCTTCCTGGCAAC
""",
            {
                'gene4':
'TAAACGTTGGTCCGTCTGAACCGCCATCCAGGATCACGTCGCCCTGAAAAAAAGATATCAGGAACTCTCCTCCTCAGCAGTCTGGTCTATGGAAACTACAGGACTAACCTTCCTGGCAAC'
            }
        ),
        (
# record with many lines of nucleotides
""">gene5
CGGGGGCTGGGAATCTGTCACATGAGTCAAGGTATTTGCTCGATAATCTATACTCCAGGC
ATCTAACTTTTCCCACTGCCTTAAGCGGGCCTGCCCTTTCTGCCTGTCGATCCATAGGAC
TCGTGCCAACGCGCAGGCTTAGTTCGAGGAGAAATATCCGGGGCCAAAGACAACCAGCAT
CTGTTTTCGAAATTACCCTTTAAGCGCGGGTATTGAACCAGGCTTATGCCCAAGATCGTA
GCAAGCAGACTCAAACAAGATATATTTTGCCCGCCTTACAGACGAAACTAGTTGGAGGTT
ATGGAGCATACTATCACGTGGGCGGCCACTGGTGAGTTACTACACCCCAGGGGCAACGTT
GATGCTCCTAAAAAACTCTGGCTGGACGCAAGCCGTAACACCCGTGTCACTTCATAATCG
TTTGCAATTCAGGGCTTGATCTACACTGGATTGCCATTCT
""",
            {
                'gene5':
'CGGGGGCTGGGAATCTGTCACATGAGTCAAGGTATTTGCTCGATAATCTATACTCCAGGCATCTAACTTTTCCCACTGCCTTAAGCGGGCCTGCCCTTTCTGCCTGTCGATCCATAGGACTCGTGCCAACGCGCAGGCTTAGTTCGAGGAGAAATATCCGGGGCCAAAGACAACCAGCATCTGTTTTCGAAATTACCCTTTAAGCGCGGGTATTGAACCAGGCTTATGCCCAAGATCGTAGCAAGCAGACTCAAACAAGATATATTTTGCCCGCCTTACAGACGAAACTAGTTGGAGGTTATGGAGCATACTATCACGTGGGCGGCCACTGGTGAGTTACTACACCCCAGGGGCAACGTTGATGCTCCTAAAAAACTCTGGCTGGACGCAAGCCGTAACACCCGTGTCACTTCATAATCGTTTGCAATTCAGGGCTTGATCTACACTGGATTGCCATTCT'
            }
        ),
        (
# record with a really long description
""">gene6 has a lot that is particularly interesting about it so back up
CGGGGGCTGGGAATCTGTCACATGAGTCAAGGTATTTGCTCGATAATCTATACTCCAGGC
GATGCTCCTAAAAAACTCTGGCTGGACGCAAGCCGTAACACCCGTGTCACTTCATAATCG
TTTGCAATTCAGGGCTTGATCTACACTGGATTGCCATTCT
""",
            {
'gene6 has a lot that is particularly interesting about it so back up':
'CGGGGGCTGGGAATCTGTCACATGAGTCAAGGTATTTGCTCGATAATCTATACTCCAGGCGATGCTCCTAAAAAACTCTGGCTGGACGCAAGCCGTAACACCCGTGTCACTTCATAATCGTTTGCAATTCAGGGCTTGATCTACACTGGATTGCCATTCT'
            }
        ),
    )


    def _join_dicts(self, dictionaries):
        """Combine multiple dictionaries into one."""

        out_dict = {}
        for dictionary in dictionaries:
            out_dict.update(dictionary)
        return out_dict


class FastaToDictTests(unittest.TestCase, CaseHolderMixin):
    """Tests for parse_fasta()"""

    # all these strings should pass


    def _set_up_multi_cases(self, multi_cases):
        """Set up multiple cases."""

        out_cases = []
        for multi_case in multi_cases:
            case_strings = []
            case_dicts = []
            for fasta_string, case_dict in multi_case:
                case_strings.append(fasta_string)
                case_dicts.append(case_dict)

            case_string = ''.join(case_strings)
            case = StringIO(case_string)

            expected = self._join_dicts(case_dicts)
            out_cases.append((case, expected))

        return out_cases


    def test_single_records(self):
        """fasta_to_dict() single cases"""

        for case_string, expected in self.cases:
            case = StringIO(case_string)
            self.assertEqual(fastadict.fasta_to_dict(case),
                    expected)


    def test_multiple_records(self):
        """fasta_to_dict() multiple records"""

        multi_cases = (
            # simple two records
            (self.cases[0], self.cases[1]),
            # sanity check that order doesn't matter
            (self.cases[1], self.cases[0]),
            # another simple two records
            (self.cases[1], self.cases[2]),
            # all records
            [case for case in self.cases],
        )

        for case, expected in self._set_up_multi_cases(multi_cases):
            self.assertEqual(fastadict.fasta_to_dict(case),
                    expected)


    def test_raises_duplicate_record_error(self):
        """fasta_to_dict() raises DuplicateRecordError"""

        multi_cases = (
            # simple immediate repetition
            (self.cases[0], self.cases[0]),
            (self.cases[1], self.cases[1]),
            # broken repetition
            (self.cases[0], self.cases[1], self.cases[0]),
            (self.cases[1], self.cases[2], self.cases[1]),
            # repetition after
            (self.cases[1], self.cases[2], self.cases[2]),
        )

        for multi_case in multi_cases:
            case_strings = [case[0] for case in multi_case]
            case_string = ''.join(case_strings)
            case = StringIO(case_string)
            self.assertRaises(
                fastadict.DuplicateRecordError,
                fastadict.fasta_to_dict,
                case
            )


class RetrieveRecordsTests(unittest.TestCase, CaseHolderMixin):
    """Tests for retrieve_records()"""

    def _set_up_multi_cases(self, multi_cases):
        """Set up multiple cases."""

        out_cases = []
        for multi_case, expected_cases in multi_cases:
            input_dicts = [case[1] for case in multi_case]
            case_dict = self._join_dicts(input_dicts)

            recs_to_retrieve = []
            fasta_strings = []
            for case in expected_cases:
                for key in case[1].keys():
                    recs_to_retrieve.append(key)
                fasta_strings.append(case[0])

            expected = ''.join(fasta_strings)

            out_cases.append((case_dict, recs_to_retrieve, expected))

        return out_cases


    def test_single_records(self):
        """retrieve_records() single records"""

        for case in self.cases:
            record_name = case[1].keys()
            expected = case[0]
            self.assertEqual(
                fastadict.retrieve_records(case[1], record_name),
                expected
            )


    def test_multiple_records(self):
        """retrieve_records() multiple records"""

        multi_cases = (
            # cases 0 and 1, retrieve for the key in case 0
            ((self.cases[0], self.cases[1]), (self.cases[0],)),
            # ... retrieve for key in case 1
            ((self.cases[0], self.cases[1]), (self.cases[0],)),
            # ... retrieve keys for both cases
            (
                (self.cases[0], self.cases[1]),
                (self.cases[0], self.cases[1])
            ),
            # all cases, one key
            ([case for case in self.cases], (self.cases[1],)),
            # all cases, all keys
            (
                [case for case in self.cases],
                [case for case in self.cases]
            ),
        )


        for case_dict, recs_to_retrieve, expected in (
                self._set_up_multi_cases(multi_cases)):
            self.assertEqual(
                fastadict.retrieve_records(
                    case_dict,
                    recs_to_retrieve
                ),
                expected
            )


    def test_raises_record_not_found_error(self):
        """retrieve_records() raises RecordNotFoundError"""

        cases = []
        # empty dictionary
        cases.append({})
        # individual records
        for case in self.cases:
            cases.append(case[1])

        multi_cases = (
            (self.cases[0][1], self.cases[1][1]),
            (self.cases[4][1], self.cases[3][1], self.cases[2][1])
        )

        for multi_case in multi_cases:
            cases.append(self._join_dicts(multi_case))

        for case in cases:
            self.assertRaises(
                fastadict.RecordNotFoundError,
                fastadict.retrieve_records,
                case,
                'nonexistent gene'
            )


if __name__ == '__main__':
    argv = [sys.argv[0]] + sys.argv[2:]
    unittest.TestProgram(argv=argv)
