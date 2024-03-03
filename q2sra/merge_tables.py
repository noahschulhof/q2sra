import os
from qiime2 import Artifact
from qiime2.plugins.feature_table.methods import merge

def merge_tables(proj_name):
    tables = []

    for root, _, files in os.walk(proj_name):
        for file in files:
            if file.endswith('table.qza'):
                tables.append(Artifact.load(os.path.join(root, file)))
    
    merged_tables = merge(tables)

    merged_tables.merged_table.save(os.path.join(proj_name, f'{proj_name}_table_merged.qza'))