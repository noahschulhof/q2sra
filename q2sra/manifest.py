import os
import pandas as pd

def manifest(study_name, paired, fastq_dir = 'fastq-files'):
    abs_filepaths = [os.path.abspath(os.path.join(fastq_dir, file)) for file in os.listdir(fastq_dir)]

    if paired:
        forward = [file for file in abs_filepaths if '_1.fastq' in file]
        reverse = [file for file in abs_filepaths if '_2.fastq' in file]

        sample_ids = [f'{study_name}{i}' for i in range(len(forward))]

        table = pd.DataFrame({'sample-id': sample_ids, 'forward-absolute-filepath': forward, 'reverse-absolute-filepath': reverse})

        table.to_csv(f'{study_name}_manifest.txt', sep = '\t', index = False)
    
    else:
       sample_ids = [f'{study_name}{i}' for i in range(len(abs_filepaths))]
       directions = ['forward'] * len(abs_filepaths)

       table = pd.DataFrame({'sample-id': sample_ids, 'absolute-filepath': abs_filepaths, 'direction': directions})

       table.to_csv(f'{study_name}_manifest.txt', index = False)