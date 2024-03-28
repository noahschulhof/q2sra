# q2sra
Conventional [microbiome](https://www.niehs.nih.gov/health/topics/science/microbiome) bioinformatics workflows are riddled with inefficiencies, as users must navigate a variety of fragmented tools, command-line utilities, and file management systems. In the contemporary research setting, with multiple individuals contribtuting to a singular project, issues with uniformity often arise, complicating subsequent data aggregation/analysis. The `q2sra` package reconciles these obstacles by providing a streamlined, centralized, and standardized framework for microbiome data analysis with [`QIIME 2`](https://qiime2.org/).


## Installation
```bash
$ pip install q2sra
```


## Prerequisites
- [`Python`](https://www.python.org/downloads/release/python-3116/) v3.11.6+
- [`QIIME 2`](https://qiime2.org/) v2023.7+
- [`SRA Toolkit`](https://hpc.nih.gov/apps/sratoolkit.html) v3.0.0+


### Installing `QIIME 2` with Conda

```bash
$ wget https://data.qiime2.org/distro/core/qiime2-2023.7-py38-linux-conda.yml
$ conda env create \
    -n qiime2-2023.7 \
    --file qiime2-2023.7-py38-linux-conda.yml
$ rm qiime2-2023.7-py38-linux-conda.yml
```


### Installing `SRA Toolkit`
Instructions can be found [here](https://github.com/ncbi/sra-tools/wiki/01.-Downloading-SRA-Toolkit).


## Creating a `q2sra` Project
To create a project, simply initialize a `q2sra.Proj` object, supplying the intended project name as the sole parameter.

```python
>>> from q2sra import Proj
>>> proj = Proj('my_proj')
```

### `q2sra` Project Attributes
| Attribute   | Type         | Default         | Description            |
|-------------|--------------|-----------------|------------------------|
| `name`      | String       | None            | Project name           |
| `fields`    | List of str  | [ ]              | Metadata fields        |
| `nsamples`  | Integer      | 30             | Maximum number of samples from each study |
| `paired`    | Boolean      | True            | Whether to use forward and reverse reads or exclusively forward reads |

## Adding Metadata Fields
```python
q2sra.Proj.add_field(field: str, required: bool) -> None
```
### Arguments
- `field` - Name of field
- `required` - Whether the field is required [default=`False`]

### Example Run
```python
>>> proj.add_field('Phylum')
>>> proj.add_field('Country', required = True)
```


## Saving a Project
```python
>>> proj.save()
```

### Output
`<proj name>.pkl` - a `pickle` file storing the project's attributes.


## Loading a Pre-configured Project
Any existing `q2sra` project saved in `.pkl` format (see previous step) can later be loaded to perform additional actions (adding more studies, merging runs, etc.).

```python
q2sra.proj.load(name: str) -> None
```

### Arguments
- `name` - Name of project to load

### Example Run
```python
>>> proj = Proj.load('my_proj')
```


## Adding Studies
```python
q2sra.Proj.run(study_name: str, accession: str, include: list, exclude: list) -> None
```

### Arguments
- `study_name` - Name of study
- `accession` - Study accession number in the [NCBI SRA database](https://www.ncbi.nlm.nih.gov/sra)
- `include` - List of substrings that **must** be included when filtering `.fastq` files [default=`[]`]
- `exclude` - List of substrings that **must** be excluded when filtering `.fastq` files [default=`[]`]

### Example Run (w/ user input)
```python
>>> proj.run('takagi_2022', 'PRJNA809527')
Phylum: Chordata
[Required] Country: Japan
```


## Aggregating Studies
After compiling a satisfactory number of studies, individual metadata files and `QIIME 2` feature tables/representative sequences can be merged for further analysis using the following method:

```python
>>> proj.merge()
```