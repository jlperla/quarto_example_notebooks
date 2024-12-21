# Notebook Repository
This repository is a public notebook repo associatd with 

## Installation
Conda environments ar recommended
```bash
conda create -n quarto_example_notebooks python=3.11
conda activate quarto_example_notebooks
pip install -r requirements.txt
```
If using Julia
```bash
julia -e 'using Pkg; Pkg.add(["IJulia", "Revise"]); Pkg.build("IJulia");'
julia --project --threads auto -e 'using Pkg; Pkg.instantiate();'
```