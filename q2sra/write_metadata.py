import pandas as pd

def write_metadata(field_vals, study_name):
    manifest = pd.read_csv(f'{study_name}_manifest.txt', sep = '\t')

    num_samples = manifest.shape[0]

    metadata = pd.DataFrame()

    metadata['sample-id'] = manifest['sample-id']

    for field, val in field_vals.items():
        metadata[field] = [val] * num_samples
    
    metadata.to_csv(f'{study_name}_metadata.txt', sep = '\t', index = False)