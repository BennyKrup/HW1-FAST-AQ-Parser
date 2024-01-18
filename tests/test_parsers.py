# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    out_fasta = FastaParser("data/test.fa")
    assert out_fasta.filename == "data/test.fa"
    Nucleotides = ["A", "C", "G", "T", "U"]
    for seq in out_fasta:
        assert isinstance(seq[1], str)                  # the sequence is a string

        assert set(seq[1]).issubset(Nucleotides)        # all nucleotides are valid

        assert seq[1] != ""                             # fasta is not blank

    with pytest.raises(ValueError) as info:
        FastaParser("data/empty.fa")
        assert "Empty file" in str(info.value)

    with pytest.raises(ValueError) as info:
        FastaParser("data/bad.fa")
        assert "non nucleotide in sequence line" in str(info.value)

    


def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    fastq = "data/test.fq"
    fasta = "data/test.fa"
    out_fasta = FastaParser(fastq)
    out_fastq = FastqParser(fasta)
    assert out_fasta[0][0] == None
    assert out_fastq[0][0] != None



def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    example_fastq = "data/test.fq"
    out_fastq = FastqParser(example_fastq)
    assert parser.filename == example_fastq
    Nucleotides = ["A", "C", "G", "T", "U"]
    # all characters allowed in fastq which are letters, numbers, and symbols
    chrs = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~")

    for seq in out_fastq:
        assert isinstance(seq[1], str)                  # the sequence is a string

        assert set(seq[1]).issubset(Nucleotides)        # all nucleotides are valid

        assert seq[1] != ""                             # fastq is not blank

        assert isinstance(seq[2], str)                  # the quality is a string

        assert set(seq[2]).issubset(chrs)               # all characters are valid

        assert seq[2] != ""                             # quality is not blank
    
def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    fastq = "data/test.fq"
    fasta = "data/test.fa"
    out_fasta = FastaParser(fastq)
    out_fastq = FastqParser(fasta)
    assert out_fasta[0][0] == None
    assert out_fastq[0][0] != None
    
    