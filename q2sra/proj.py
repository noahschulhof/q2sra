import pickle
import os
import shutil
from filter_fastq import *
from manifest import *
from write_metadata import *
from merge_metadata import *
from prefetch import *
from demux import *
from deblur import *


class proj():

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

        study_dir = f'{self.name}/{study_name}'

        if not os.path.exists(self.name):
            os.mkdir(self.name)
            os.mkdir(study_dir)
        else:
            if not os.path.exists(study_dir):
                os.mkdir(study_dir)
            else:
                for file in os.listdir(study_dir):
                    try:
                        os.remove(f'{study_dir}/{file}')
                    except:
                        shutil.rmtree(f'{study_dir}/{file}')

        prefetch(accession, study_dir)

        filter_fastq(include, exclude, self.paired, self.nsamples)

        manifest(study_name, self.paired)

        write_metadata(field_vals, study_name)

        artifact = demux(self.paired, f'{study_name}_manifest.txt')

        deblur(study_name, artifact)


    def merge(self):
        merge_metadata(self.name)

        # merge tables and repseqs here