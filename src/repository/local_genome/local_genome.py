from abstract import AbstractRepository
from pathlib import Path
import os


class LocalGenomeRepository(AbstractRepository):
    """A simple repository to call for genomes from genbank files."""
    def __init__(self):
        self.genome_locations = self._get_genome_locations()
    
    def _get_genome_locations(self):
        """Populate an in-memory map of genome names to their GB files."""
        genome_map = {}
        all_fixture_filenames = [os.listdir("./fixtures/")]
        for filename in all_fixture_filenames:
            genome_id = filename.split(".")[0]
            genome_map[genome_id] = Path(f"./fixtures/{filename}")
        return genome_map

    def get(self, reference_id: str) -> Path:
        """Get the file path for any given reference ID."""
        return self.genome_locations[reference_id]