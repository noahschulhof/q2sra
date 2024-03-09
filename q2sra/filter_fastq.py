import os
import shutil
import re

def filter_fastq(include, exclude, paired, nsamples):
    include_pattern = re.compile('|'.join(include))
    exclude_pattern = re.compile('|'.join(exclude))

    for file in os.listdir():
        if '.fastq' in file:
            if (not paired and '2.fastq' in file ) or (include != [] and not include_pattern.search(file)) or (exclude != [] and exclude_pattern.search(file)):
                os.remove(file)

    if paired and len([file for file in os.listdir() if '2.fastq' in file]) == 0:
        paired = False

    if paired:
        for file in os.listdir():
            if '.fastq' in file and '_1.fastq' not in file and '_2.fastq' not in file:
                os.remove(file)
        while len([file for file in os.listdir() if '.fastq' in file]) > 2 * nsamples:
            os.remove([file for file in os.listdir() if '1.fastq' in file][0])
            os.remove([file for file in os.listdir() if '2.fastq' in file][0])
    else:
        for file in os.listdir():
            if '2.fastq' in file:
                os.remove(file)
        while len([file for file in os.listdir() if '.fastq' in file]) > nsamples:
            os.remove([file for file in os.listdir() if '.fastq' in file][0])

    os.mkdir('fastq-files')

    for file in os.listdir():
        if '.fastq' in file:
            shutil.move(file, 'fastq-files')