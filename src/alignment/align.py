from typing import Tuple
from repository.local_genome.local_genome import LocalGenomeRepository
from Bio import SeqIO
from Bio.Seq 
def align(sequence: str, genome_name: str) -> Tuple[str, str, int, int]:
    genome_repository = LocalGenomeRepository()
    gb_filepath = genome_repository(genome_name)
    genome_record = SeqIO.parse(gb_filepath)
    sequence_record = SeqRecord()
    return genome_name, protein_name, start_bp, end_bp``