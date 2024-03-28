from setuptools import setup, find_packages

setup(
    name = 'q2sra',
    version = '1.0.0',
    description = 'Fetch, process, analyze, and aggregate microbiome sequencing data with SRA Toolkit and QIIME 2.',
    author = 'Noah Schulhof',
    author_email = 'nschulhof@u.northwestern.edu',
    packages = find_packages(),
    python_requires = '>=3.8',
    install_requires = ['pandas >= 1.5.3'],
    project_urls = {'Documentation': 'https://github.com/noahschulhof/q2sra/blob/main/README.md'}                    
)