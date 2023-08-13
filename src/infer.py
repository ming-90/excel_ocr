import cv2
from util import find_tables

def infer():
    print("[INFO] Start OCR process.")
    image = cv2.imread("simple3.png", cv2.IMREAD_GRAYSCALE)
    print("[INFO] Find table in single image.")
    tables = find_tables(image)
    return tables


if __name__ == "__main__":
    output = infer()
    print(output)