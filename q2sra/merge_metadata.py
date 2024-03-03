import pandas as pd
import os

def merge_metadata(proj_name):
    merged_metadata = pd.DataFrame()

    for root, _, files in os.walk(proj_name):
        for file in files:
            if file.endswith('metadata.txt'):
                try:
                    metadata = pd.read_csv(os.path.join(root, file), sep = '\t')

                    merged_metadata = pd.concat(merged_metadata, metadata)
                except:
                    print(f'Omitting invalid metadata file: {file}')

    merged_metadata.to_csv(os.path.join(proj_name, f'{proj_name}_metadata_merged.txt'), sep = '\t')