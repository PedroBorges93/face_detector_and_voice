import cv2
import numpy as np

WHITE = [255, 255, 255]


def draw_box(frame, x, y, w, h):
    cv2.line(frame, (x, y), (x + (int(w/5)) ,y), WHITE, 2)
    cv2.line(frame, (x+((int(w/5)*4)), y), (x+w, y), WHITE, 2)
    cv2.line(frame, (x, y), (x, y+(int(h/5))), WHITE, 2)
    cv2.line(frame, (x+w, y), (x+w, y+int((h/5))), WHITE, 2)
    cv2.line(frame, (x, (y+int((h/5*4)))), (x, y+h), WHITE, 2)
    cv2.line(frame, (x, (y+h)), (x + int((w/5)) ,y+h), WHITE, 2)
    cv2.line(frame, (x+(int((w/5)*4)), y+h), (x + w, y + h), WHITE, 2)
    cv2.line(frame, (x+w, (y+int((h/5*4)))), (x+w, y+h), WHITE, 2)