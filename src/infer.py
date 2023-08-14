import cv2
import numpy as np
import pandas as pd

from table_ocr.extract_tables import extract_tables
from table_ocr.extract_cells import extract_cells
from table_ocr.ocr_from_cell import ocr_from_cell

def infer():
    print("[INFO] Start OCR process.")
    image = cv2.imread("simple5.png", cv2.IMREAD_GRAYSCALE)
    print("[INFO] Find table in single image.")
    tables = extract_tables(image)
    df = pd.DataFrame(index=range(0),columns=['test','a','b','c','d','e'])
    print("dataframe shape: ",df.shape)
    for idx, table in enumerate(tables):
        print(f"Processing tables {idx+1}")
        rows, width, height = extract_cells(table)

        for i, row in enumerate(rows):
            column = []
            for j, cell in enumerate(row):
                # OCR
                txt = ocr_from_cell(cell)
                # Make column
                if txt == "": txt = "undefined"
                column.append(txt)

            if i == 0:
                df = pd.DataFrame(index=range(0), columns=column)
            else:
                df.loc[i-1] = column
        print(df)
    return df


if __name__ == "__main__":
    output = infer()