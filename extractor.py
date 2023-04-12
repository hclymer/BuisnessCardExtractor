import os
import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

from pytesseract import pytesseract
from PIL import Image

import spacy
from spacy import displacy
from spacy import tokenizer

nlp = spacy.load("en_core_web_sm")




path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

folder = r"C:\Users\Henry\Personal Codes\Business card extractor\images\Free logo creator samples\1.png"

pytesseract.tesseract_cmd = path_to_tesseract

full_text = []

img = Image.open(folder)

text1 = pytesseract.image_to_string(img)
print(text1)

text1 = text1.strip()
text2 = text1.split('\n')


for i in text2:
    if(len(i)==0):
        text2.remove(i)

# text2 = " ".join(text2)
print(text2)



doc = nlp(text2[6])
sentences = list(doc.sents)
print(sentences)

for token in doc:
    print(token.text)

# ents = [(e.text, e.start_char, e.end_char, e.label_) for e in doc.ents]
# print(ents)

# displacy.render(doc, style="ent", jupyter=True)
# dfs = []
# i = 0

# for file in os.listdir(folder):
#     f = os.path.join(folder, file)
#     res = reader.readtext(f,paragraph="False")
#     img_df = pd.DataFrame(res, columns=['bbox','text'])
#     dfs.append(img_df)
#     print(res)
#     easyocr_df = pd.concat(dfs)


# with pd.option_context('display.max_rows', None,
#                        'display.max_columns', None,
#                        'display.precision', 3,
#                        ):
#     print(easyocr_df)








