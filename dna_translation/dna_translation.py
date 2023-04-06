"""
In this project, we I will translate sequence of DNA into sequence of Amino acids.
Example:
    DNA sequence: ATACAATGGCAA
    Amino acids sequence: IQWQ

Tasks:
    1. Import the DNA data into Python
    2. Create an algorithm to translate the DNA
    3. Check if translation matches amino acid sequence

"""

def read_seq(inputfile):
    """ Reads and returns the input sequence with special characters removed."""
    with open(inputfile, "r") as f:
        seq = f.read()
    seq = seq.replace("\n", "")
    seq = seq.replace("\r", "")
    return seq
    

def translate(seq):
    """ Translate a string containing a nucleotide sequence into a string containing the corresponding sequence
        of amino acids. Nucleotides are translated in triplets using the table dictionary; each amino acid is 
        encoded with a string of length 1.
    """
    
    # nucleotide triplets or codons table
    table = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',}
    
    
    protein = ""
    seq_len = len(seq)
    # check if the sequence length is divisible by 3 
    if seq_len % 3 == 0:
        # Look up each 3-letter string (called nucleotide triplets or codons) in table and store the result
        for i in range(0, seq_len, 3):
            codon = seq[i:i+3]
            protein += table[codon]
    return protein
  


dna_seq = read_seq("dna.txt")
protein_seq = read_seq("protein.txt")

# DNA sequence starts at 21 position and stops at 938 according to NCBI database
translated_dna = translate(dna_seq[20:938])[:-1] 
                                                    
print(translated_dna)
print()
print(protein_seq)
print()

# Check if translation matches amino acid sequence
print(translated_dna == protein_seq)