import cv2
import numpy as np

from table_ocr.extract_tables import extract_tables
from table_ocr.extract_cells import extract_cells
from table_ocr.ocr_from_cell import ocr_from_cell

def infer():
    print("[INFO] Start OCR process.")
    image = cv2.imread("simple2.png", cv2.IMREAD_GRAYSCALE)
    print("[INFO] Find table in single image.")
    tables = extract_tables(image)

    for idx, table in enumerate(tables):
        print(f"Processing tables {idx+1}")
        rows = extract_cells(table)

        for i, row in enumerate(rows):
            for j, cell in enumerate(row):
                # cv2.imwrite(f"test/test_{i}_{j}.png", cell)
                txt = ocr_from_cell(cell)
                print("text : ", txt)

    return tables


if __name__ == "__main__":
    output = infer()