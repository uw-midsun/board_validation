set -e

echo "Installing miniconda"
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
bash ~/miniconda.sh -b -p $HOME/miniconda
eval "$(${HOME}/miniconda/bin/conda shell.bash hook)"


PROJECT_DIR=~/shared/board_validation

echo "Cloning board_validation project"
git clone https://github.com/uw-midsun/board_validation.git ${PROJECT_DIR}

echo "Creating Conda environment."
conda create -n board_validation python=3 -y
conda activate board_validation

echo "Installing dependencies:"
cd ${PROJECT_DIR}
pip install -r build_requirements.text

echo "Done"
