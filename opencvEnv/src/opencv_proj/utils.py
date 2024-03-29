import os

import cv2
import numpy as np

from .noiser import Noiser

# create more effects with Noiser


def get_filtered_image(image, action):

    im = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #im = cv2.imread(image)
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    filtered = None
    ns = Noiser(None)
    if action == 'CAUCASIAN_GRADIENT':
        #filtered = image

        ns.change_image(im)
        ns.gradient_gaussian()
        filtered = ns.noised_image

    elif action == 'FOLD':
        ns.change_image(im)
        ns.fold()
        filtered = ns.noised_image

    elif action == 'DRUMROLL':
        ns.change_image(im)
        ns.drumroll()
        filtered = ns.noised_image

    elif action == 'BOOK_BINDING':
        ns.change_image(im)
        ns.book_bindings()
        filtered = ns.noised_image

    elif action == 'COLORIZED':
        filtered = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    elif action == 'GRAYSCALE':
        filtered = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    elif action == 'BLURRED':
        width, height = img.shape[:2]
        if width > 500:
            k = (50, 50)
        elif width > 200 and width <= 500:
            k = (25, 25)
        else:
            k = (10, 10)
        blur = cv2.blur(img, k)
        filtered = cv2.cvtColor(blur, cv2.COLOR_BGR2RGB)
    elif action == 'BINARY':
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, filtered = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    elif action == 'INVERT':
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, img = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
        filtered = cv2.bitwise_not(img)
    return filtered
