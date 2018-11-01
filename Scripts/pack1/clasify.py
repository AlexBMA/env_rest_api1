# import the necessary packages

from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import cv2
import imutils
import pickle
import os


from cv2 import *


class ImgClassifier:

    path_model = "model4.h5"
    path_pickle = "lb.pickle3"

    @classmethod
    def transform_image(cls,image):
        image = cv2.resize(image, (32, 32))
        image = image.astype("float") / 255.0
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)

        return image

    @staticmethod
    def classify_img(path_img, path_model, path_pickle):
        image = cv2.imread(path_img)
        output = image.copy()

        image = ImgClassifier.transform_image(image)

        # load the trained convolutional neural network and the label
        # binarizer
        print("[INFO] loading network...")
        model = load_model(path_model)

        lb = pickle.loads(open(path_pickle, "rb").read())

        # classify the input image
        print("[INFO] classifying image...")
        proba = model.predict(image)[0]
        print(proba)
        idx = np.argmax(proba)
        label = lb.classes_[idx]

        print(path_img)
        print(label)

        # filename = path_img.rsplit("\\", 2)[1]
        # print(filename)

        # correct = "correct" if filename.rfind(label) != -1 else "incorrect"

        # build the label and draw the label on the image
        label = "{}: {:.2f}% ({})".format(label, proba[idx] * 100, "")
        output = imutils.resize(output, width=400)
        cv2.putText(output, label, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # show the output image
        print("[INFO] {}".format(label))
        #cv2.imshow("Output", output)
        #cv2.waitKey(0)

        return label


def main():
    print("main")

#main()
#path_img2 = "C:\\Users\\Alexandru\\Desktop\\validation\\banana\\img3.jpg"

#rez = path_img2

#ImgClassifier.classify_img(rez, ImgClassifier.path_model, ImgClassifier.path_pickle)