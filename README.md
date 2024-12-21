# Notebook Repository
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jlperla/quarto_example_notebooks/HEAD)
This repository is a public notebook repo associated with the [Quarto Example Slides](https://jlperla.github.io/quarto_example/)

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