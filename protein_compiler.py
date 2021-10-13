import typing
import random
import io

protein_codon = {
	"A": ["GCU", "GCC", "GCA", "GCG"],
	"R": ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"],
	"N": ["AAU","AAC"],
	"D": ["GAU", "GAC"],
	"B": ["AAU", "AAC", "GAU", "GAC"],
	"C": ["UGU", "UGC"],
	"Q": ["CAA", "CAG"],
	"E": ["GAA", "GAG"],
	"Z": ["CAA", "CAG", "GAA", "GAG"],
	"G": ["GGU", "GGC", "GGA", "GGG"],
	"H": ["CAU", "CAC"],
	"I": ["AUU", "AUC", "AUA"],
	"L": ["CUU", "CUC", "CUA", "CUG", "UUA", "UUG"],
	"K": ["AAA", "AAG"],
	"M": ["AUG"],
	"F": ["UUU", "UUC"],
	"P": ["CCU", "CCC", "CCA", "CCG"],
	"S": ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"],
	"T": ["ACU", "ACC", "ACA", "ACG"],
	"W": ["UGG"],
	"Y": ["UAU", "UAC"],
	"V": ["GUU", "GUC", "GUA", "GUG"]
}
start_codons = ["AUG"]
stop_codons = ["UAA", "UGA", "UAG"]

def get_possible_start_codons() -> list[str]:
	return start_codons

def get_possible_stop_codons() -> list[str]:
	return stop_codons

def get_possible_amino_codons(protein_letter: str) -> list[str]:
	return protein_codon[protein_letter]

def choose_codon(possible_codons: list[str]) -> str:
	return random.choice(possible_codons)

def translate_amino_acid_to_codon(amino_acid: str) -> str:
	return choose_codon(get_possible_amino_codons(amino_acid))

def compile_protein_sequence(amino_acid_sequence: str) -> str:
	# To prevent quadratic performance degradation, a mutable string is used to store
	# the output of compiling our amino acid chain.
	output = io.StringIO()
	# A start codon is needed to signal the ribosome to start the process of
	# translating mRNA into a protein.
	output.write(choose_codon(get_possible_start_codons()))
	for amino_acid in amino_acid_sequence:
		output.write(translate_amino_acid_to_codon(amino_acid))
	# A stop codon is needed to signal the ribosome to stop translating mRNA
	# into a protein.
	output.write(choose_codon(get_possible_stop_codons()))
	return output.getvalue()