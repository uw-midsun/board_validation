eval "$(${HOME}/miniconda/bin/conda shell.bash hook)"
conda activate board_validation
export PYTHONPATH=$PYTHONPATH:src
python src/main.py
