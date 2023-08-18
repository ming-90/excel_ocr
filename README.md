# Table OCR in image

## Description
This is a webapp that OCRs a table from an image and creates a dataframe.
It is based on [image-table-ocr](https://github.com/eihli/image-table-ocr).
The output data is converted to a dataframe in pandas on the backend and to a dataframe in danfo.js on the frontend. This means you can freely edit the data on the frontend as well.


## Demo Video

https://github.com/ming-90/excel_ocr/assets/48505409/82177cff-d565-4739-b9f7-b867e704113a


## How to use
```bash
make env
conda activate excel_ocr
make setup
```
### Inference test
```bash
make ocr
```
### Start server
```bash
make server
```

# Referece
- [image-table-ocr](https://github.com/eihli/image-table-ocr)