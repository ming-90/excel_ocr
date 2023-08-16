PYTHON=3.8
BASENAME=$(shell basename $(CURDIR))
CONDA_CH=conda-forge defaults
CURRENT_DIR = $(shell pwd)


env:
	conda create -n $(BASENAME) -y python=$(PYTHON) $(addprefix -c ,$(CONDA_CH))

setup:
	pip install -r requirements.txt

server:
	PYTHONPATH=server uvicorn src.backend.main:app --host 192.168.0.2 --port 50000 --reload --debug

test-server:
	PYTHONPATH=server uvicorn src.main:app --host 192.168.219.109 --port 50000 --reload --debug

ocr:
	python src/infer.py