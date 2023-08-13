PYTHON=3.8
BASENAME=$(shell basename $(CURDIR))
CONDA_CH=conda-forge defaults
CURRENT_DIR = $(shell pwd)


env:
	conda create -n $(BASENAME) -y python=$(PYTHON) $(addprefix -c ,$(CONDA_CH))

setup:
	pip install -U openmim
	mim install mmengine
	mim install mmcv
	mim install mmdet

server:
	PYTHONPATH=server uvicorn src.main:app --host 192.168.0.2 --port 50000 --reload --debug

test:
	python infer.py test_image.jpg --det DBNetpp  --rec MASTER