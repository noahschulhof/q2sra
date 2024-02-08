import os
import shutil
import subprocess

def prefetch(accession, study_dir):
    os.chdir(study_dir)

    try:
        subprocess.run(['prefetch', '-v', accession])

        for dir in os.listdir('./'):
            try:
                subprocess.run(['fasterq-dump', dir])
                shutil.rmtree(dir)
            except:
                continue
    
    except:
        raise ValueError('Invalid accession provided.')