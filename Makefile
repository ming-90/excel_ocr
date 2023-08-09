PYTHON=3.8
BASENAME=$(shell basename $(CURDIR))
CONDA_CH=conda-forge defaults
CURRENT_DIR = $(shell pwd)


env:
	conda create -n $(BASENAME) -y python=$(PYTHON) $(addprefix -c ,$(CONDA_CH))

setup:
	pip install -r requirements.txt
	conda install pytorch torchvision cpuonly -c pytorch

server:
	PYTHONPATH=server uvicorn src.main:app --host 192.168.0.2 --port 50000 --reload --debug