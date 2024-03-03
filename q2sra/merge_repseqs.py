import os
from qiime2 import Artifact
from qiime2.plugins.feature_table.methods import merge_seqs

def merge_repseqs(proj_name):
    repseqs = []

    for root, _, files in os.walk(proj_name):
        for file in files:
            if file.endswith('repseqs.qza'):
                repseqs.append(Artifact.load(os.path.join(root, file)))
    
    merged_repseqs = merge_seqs(repseqs)

    merged_repseqs.merged_data.save(os.path.join(proj_name, f'{proj_name}_repseqs_merged.qza'))