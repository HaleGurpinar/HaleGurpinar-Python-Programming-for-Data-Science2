# Download PyCharm Community edition.
# Anaconda.com --> Products --> Individual Edition --> Install Windows-->PyCharm Community

# Virtual Environments :venv, virtualenv, pipenv, *conda
# Package Management: pip(requirements.txt), pipenv(pipfile), *conda(environment.yaml)

# venv and virtualenv use pip as a package management tool.(pip is use just pack. manage.)
# Both pipenv and conda can   Virtual Environments and Package Management.

# ########      CONDA          ################## #
# Virtual Env. List : conda env list
# Create VE: conda create -n myenv
# Delete env: conda env remove -n myenv
# Activate this environment: conda activate myenv
# Deactivate this environment: conda deactivate
# List of loaded package: conda list
# Install pack. : conda install numpy
# Install many pack. : conda install scipy pandas
# Delete pack. : conda remove numpy
# Install spec. version pack. : conda install numpy=1.25.2
# Upgrade: conda upgrade numpy
# Up. all: conda upgrade -all

# Create a VE with just a environment.yaml file:
# 1. conda env create -f environment.yaml
# 2. conda activate myenv

# To transfer all info create yaml: conda env export > environment.yaml
# See files: dir

# ######     PIP    #################################
# Install pack. : pip install pandas
# Install spec. version pack. : pip install pandas==2.2.1 (önceki versiyonu kaldırır bunu koyar)


print("Hello Python!")