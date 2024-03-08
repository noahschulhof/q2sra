import pandas as pd

def write_metadata(field_vals, study_name):
    manifest = pd.read_csv(f'{study_name}_manifest.txt', sep = '\t')

    if not 'sample_id' in manifest.columns:
        manifest = pd.read_csv(f'{study_name}_manifest.txt')

    num_samples = manifest.shape[0]

    try:
        metadata = pd.DataFrame({'sample-id': manifest['sample-id']})

        for field, val in field_vals.items():
            metadata[field] = [val] * num_samples
        
        metadata.to_csv(f'{study_name}_metadata.txt', sep = '\t', index = False)
    except:
        pass