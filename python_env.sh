conda create -n comp-dev python=3.7 --yes
source activate comp-dev
conda install -c anaconda --file conda-requirements.txt --yes
pip install -r requirements.txt
