import cv2
import numpy as np
import pandas as pd

from src.backend.table_ocr.extract_cells import extract_cells
from src.backend.table_ocr.extract_tables import extract_tables
from src.backend.table_ocr.ocr_from_cell import ocr_from_cell


def image_ocr(image: np.ndarray):
    print("[INFO] Start OCR process.")
    print(f"[INFO] Image size : {image.shape}")
    print("[INFO] Find table in single image.")
    tables = extract_tables(image)
    ocr_result = []
    for idx, table in enumerate(tables):
        print(f"Processing tables {idx+1}")
        rows, width, height = extract_cells(table)

        for i, row in enumerate(rows):
            column = []
            for j, cell in enumerate(row):
                # OCR
                txt = ocr_from_cell(cell)
                # Make column
                if txt == "":
                    txt = "undefined"
                column.append(txt)

            if i == 0:
                df = pd.DataFrame(index=range(0), columns=column)
            else:
                df.loc[i - 1] = column
        ocr_result.append(df)
    return ocr_result

