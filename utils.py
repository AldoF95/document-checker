from math import floor
from typing import Literal
from const import SCALES, SCALES_LEVELS
import fitz
import os

def convert_awl_ratio(awl)->Literal[0,1,2,3,4]:
    if awl<=5: return 0
    if awl<=15: return 1
    if awl<=25: return 2
    if awl<=35: return 3
    else: return 4


def scale(awl, lfwl):
    index_x = convert_awl_ratio(awl)
    index_y = lfwl
    index_y = floor(index_y)
    if index_y>4:index_y=4
    score = SCALES[int(index_y)][int(index_x)]
    return SCALES_LEVELS[score]

def load_doc(path):
    doc = fitz.Document(path)
    if doc.is_pdf:
        return doc
    return False

def remove_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("No file", filename)