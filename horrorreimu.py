import winsound
import cv2
import time
import threading

def func1():
    winsound.PlaySound("reimu.wav", winsound.SND_FILENAME)

def func2():
    time.sleep(20)
    img = cv2.imread('reimu.png')
    cv2.imshow('', img)
    cv2.waitKey(0)

if __name__ == "__main__":
    thread_1 = threading.Thread(target=func1)
    thread_2 = threading.Thread(target=func2)

    thread_1.start()
    thread_2.start()
