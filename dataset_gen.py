import os
import sys
import shutil
#from PIL import Image
import cv2
import numpy as np



N = 1000 # number of images
NCLASSES = 2 # number of classes
IMG_W = 32
IMG_H = 32
IMG_CH = 1
DIM_TOL = 5 # dimension tolerance
DST_PATH = "./gen_dataset_%d_samples_%d_classes/" % (N, NCLASSES)

if os.path.exists(DST_PATH):
    shutil.rmtree(DST_PATH)
os.makedirs(DST_PATH)
os.makedirs(DST_PATH + "yes/")
os.makedirs(DST_PATH + "no/")

MAX_W = 0
MAX_H = 0

for i in range(N):
    label = np.round(np.random.random())
    label = np.array(label, dtype=np.uint8)

    low = IMG_W - np.floor(DIM_TOL/2)
    high = IMG_W + np.ceil(DIM_TOL/2)
    img_w = np.random.randint(low, high)
 
    low = IMG_H - np.floor(DIM_TOL/2)
    high = IMG_H + np.ceil(DIM_TOL/2)
    img_h = np.random.randint(low, high)

    img = 255 * np.random.random((img_w, img_h, IMG_CH))
    img = np.round(img).astype('uint8')

    if MAX_W < img_w:
        MAX_W = img_w
    if MAX_H < img_h:
        MAX_H = img_h

    if label == 1:
        dst_path = DST_PATH + ("yes/img%d.png" % (i))
    else:
        dst_path = DST_PATH + ("no/img%d.png" % (i))

    cv2.imwrite(dst_path, img)

f = open(DST_PATH + "metadata.txt", "w")
f.write("%d\n" % MAX_W)
f.write("%d\n" % MAX_H)
f.close()
