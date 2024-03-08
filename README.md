# Q2SRA

## Prerequisites
- [`Python`](https://www.python.org/downloads/release/python-3116/) v3.11.6+
- [`QIIME 2`](https://qiime2.org/) v2023.7+
- [`SRA Toolkit`](https://hpc.nih.gov/apps/sratoolkit.html) v3.0.0+


### Installing QIIME 2 with Conda

```bash
$ wget https://data.qiime2.org/distro/core/qiime2-2023.7-py38-linux-conda.yml
$ conda env create \
    -n qiime2-2023.7 \
    --file qiime2-2023.7-py38-linux-conda.yml
$ rm qiime2-2023.7-py38-linux-conda.yml
```


### Installing `SRA Toolkit`
Instructions can be found [here](https://github.com/ncbi/sra-tools/wiki/01.-Downloading-SRA-Toolkit).


## Creating a `Q2SRA` Project
```python
>>> from q2sra import Proj
>>> proj = Proj('my_proj')
```

## Adding Fields

### Arguments
- `field` - Name of field
- `required` - Whether the field is required [default=`False`]
```python
>>> proj.add_field('Phylum')
>>> proj.add_field('Country', required = True)
```


## Saving a Pre-configured Project
```python
>>> proj.save()
```


## Loading a Pre-configured Project

### Arguments
- `name` - Name of project to load

```python
>>> proj = Proj.load('my_proj')
```


## Adding Studies

### Arguments
- `study_name` - Name of study
- `accession` - Study accession number in [NCBI SRA database](https://www.ncbi.nlm.nih.gov/sra)
- `include` - List of strings that must be included when filtering `.fastq` files [default=`[]`]
- `exclude` - List of strings that must be excluded when filtering `.fastq` files [default=`[]`]

```python
>>> proj.run('smith_2022', 'PRJ12345678')
```


## Aggregating Studies
```python
>>> proj.merge()
```