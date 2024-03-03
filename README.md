# Q2SRA

## Prerequisites
- [`Python`](https://www.python.org/downloads/release/python-3116/) v3.11.6+
- [`QIIME 2`](https://qiime2.org/) v2024.2+
- [`SRA Toolkit`](https://hpc.nih.gov/apps/sratoolkit.html) v3.0.0+
- [`pandas`](https://pypi.org/project/pandas/) v2.1.2+

### Conda Installation

```bash
$ wget https://data.qiime2.org/distro/amplicon/qiime2-amplicon-2024.2-py38-linux-conda.yml
$ conda env create \
    -n qiime2-amplicon-2024.2 \
    --file qiime2-amplicon-2024.2-py38-linux-conda.yml
$ rm qiime2-amplicon-2024.2-py38-linux-conda.yml
```

`pandas` comes pre-installed with the [Anaconda](https://docs.anaconda.com/free/anaconda/index.html) Distribution. Users running the [Miniconda](https://docs.anaconda.com/free/miniconda/) Distribution should execute the command:
```bash
$ conda install -c conda-forge pandas
```

### Installing `SRA Toolkit`
Instructions can be found [here](https://github.com/ncbi/sra-tools/wiki/01.-Downloading-SRA-Toolkit).


## Creating a `Q2SRA` Project
```python
>>> from q2sra import Proj
>>> proj = Proj('My_proj')
```

### Adding Fields
```python
>>> proj.add_field('Phylum')
>>> proj.add_field('Country', required = True)
```

### Saving a Pre-configured Project
```python
>>> proj.save()
```

### Loading a Pre-configured Project
```python
>>> proj = Proj.load('my_proj')
```


## Adding Studies
```python
>>> proj.run('smith_2022', 'PRJ12345678')
```


## Aggregating studies
```python
>>> proj.merge()
```