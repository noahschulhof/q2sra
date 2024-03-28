import pickle
import os
from .filter_fastq import *
from .manifest import *
from .write_metadata import *
from .prefetch import *
from .demux import *
from .dada2 import *
from .merge_metadata import *
from .merge_tables import *
from .merge_repseqs import *

class Proj():

    def __init__(self, name):
        self.name = name
        self.fields = {}
        self.nsamples = 30
        self.paired = True


    def add_field(self, field: str, required = False):
        self.fields[field] = required
    

    def save(self):
        with open(f'{self.name}.pkl', 'wb') as file:
            pickle.dump(self, file)
    

    @classmethod
    def load(self, name: str):
        with open(f'{name}.pkl', 'rb') as file:
            return pickle.load(file)
    

    def run(self, study_name: str, accession, include = [], exclude = []):

        field_vals = {}

        for field in self.fields:

            if self.fields[field] == True:
                val = None
                while not val:
                    val = input(f'[Required] {field}: ')

            else:
                val = input(f'{field}: ')

            field_vals[field] = val

        study_dir = os.path.join(self.name, study_name)

        os.makedirs(study_dir)

        start = os.getcwd()

        prefetch(accession, study_dir)

        filter_fastq(include, exclude, self.paired, self.nsamples)

        manifest(study_name, self.paired)

        write_metadata(field_vals, study_name)

        artifact = demux(self.paired, f'{study_name}_manifest.txt')

        dada2(study_name, artifact)
        
        os.chdir(start)


    def merge(self):
        merge_metadata(self.name)

        merge_tables(self.name)

        merge_repseqs(self.name)