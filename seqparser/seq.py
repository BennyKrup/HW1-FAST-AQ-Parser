# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    # upper case nucleotides
    seq = seq.upper()
    # checking if all inputs are allowed nucleotides
    if not set(seq).issubset(ALLOWED_NUC):
        raise ValueError("Invalid nucleotide in sequence")
    
    transcribed = "".join([TRANSCRIPTION_MAPPING[nuc] for nuc in seq])
    # reverse
    if reverse:
        transcribed = transcribed[::-1]
    return transcribed


def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    # Hey this is my comment
    # Again!
    seq = transcribe(seq, reverse=True) # transcribe and reverse
    return seq