# Copyright (c) OpenMMLab. All rights reserved.
from argparse import ArgumentParser
import os
import numpy
import cv2

from mmocr.apis.inferencers import MMOCRInferencer


def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        'inputs', type=str, help='Input image file or folder path.')
    parser.add_argument(
        '--out-dir',
        type=str,
        default='results/',
        help='Output directory of results.')
    parser.add_argument(
        '--det',
        type=str,
        default=None,
        help='Pretrained text detection algorithm. It\'s the path to the '
        'config file or the model name defined in metafile.')
    parser.add_argument(
        '--det-weights',
        type=str,
        default=None,
        help='Path to the custom checkpoint file of the selected det model. '
        'If it is not specified and "det" is a model name of metafile, the '
        'weights will be loaded from metafile.')
    parser.add_argument(
        '--rec',
        type=str,
        default=None,
        help='Pretrained text recognition algorithm. It\'s the path to the '
        'config file or the model name defined in metafile.')
    parser.add_argument(
        '--rec-weights',
        type=str,
        default=None,
        help='Path to the custom checkpoint file of the selected recog model. '
        'If it is not specified and "rec" is a model name of metafile, the '
        'weights will be loaded from metafile.')
    parser.add_argument(
        '--kie',
        type=str,
        default=None,
        help='Pretrained key information extraction algorithm. It\'s the path'
        'to the config file or the model name defined in metafile.')
    parser.add_argument(
        '--kie-weights',
        type=str,
        default=None,
        help='Path to the custom checkpoint file of the selected kie model. '
        'If it is not specified and "kie" is a model name of metafile, the '
        'weights will be loaded from metafile.')
    parser.add_argument(
        '--device',
        type=str,
        default=None,
        help='Device used for inference. '
        'If not specified, the available device will be automatically used.')
    parser.add_argument(
        '--batch-size', type=int, default=1, help='Inference batch size.')
    parser.add_argument(
        '--show',
        action='store_true',
        help='Display the image in a popup window.')
    parser.add_argument(
        '--print-result',
        action='store_true',
        help='Whether to print the results.')
    parser.add_argument(
        '--save_pred',
        action='store_true',
        help='Save the inference results to out_dir.')
    parser.add_argument(
        '--save_vis',
        action='store_true',
        help='Save the visualization results to out_dir.')

    call_args = vars(parser.parse_args())

    init_kws = [
        'det', 'det_weights', 'rec', 'rec_weights', 'kie', 'kie_weights',
        'device'
    ]
    init_args = {}
    for init_kw in init_kws:
        init_args[init_kw] = call_args.pop(init_kw)

    return init_args, call_args


def main():
    init_args, call_args = parse_args()
    ocr = MMOCRInferencer(**init_args)
    result = ocr(**call_args)

    image = cv2.imread("test_image.jpg")
    result = result['predictions'][0]
    # print(f"rec_text: {aa['rec_texts']}, lenght: {len(aa['rec_texts'])}")
    # print(f"rec_score: {aa['rec_scores']}, lenght: {len(aa['rec_scores'])}")
    # print(f"det_polygons: {aa['det_polygons']}, lenght: {len(aa['det_polygons'])}")
    text = result['rec_texts']
    coor = result['det_polygons']
    rects = []
    for idx,value in enumerate(coor):
        x = [x_coor for i, x_coor in enumerate(value) if i % 2 == 0 ]
        y = [x_coor for i, x_coor in enumerate(value) if i % 2 == 1 ]
        rect = [int(min(x)), int(min(y)), int(max(x) - min(x)), int(max(y) - min(y))]

        image = cv2.rectangle(image, (rect[0], rect[1]), (rect[0]+rect[2], rect[1]+rect[3]), (255,0,0), 3)
        # rects.append(rect)
        # print(f"{text[idx]}, {rect}")
        # print(value)
    cv2.imwrite("test.jpg", image)


if __name__ == '__main__':
    main()
