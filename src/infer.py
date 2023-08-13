import cv2

from table_ocr.extract_tables import extract_tables
from table_ocr.extract_cells import extract_cells

def infer():
    print("[INFO] Start OCR process.")
    image = cv2.imread("simple3.png", cv2.IMREAD_GRAYSCALE)
    print("[INFO] Find table in single image.")
    tables = extract_tables(image)

    for idx, table in enumerate(tables):
        print(f"Processing tables {idx+1}")
        cells = extract_cells(table)

        for cell_idx, cell in enumerate(cells):
            print(f"Processing cells {cell_idx+1}")
            print(cell)

    return tables


if __name__ == "__main__":
    output = infer()
    print(output)