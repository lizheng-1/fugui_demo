import cv2
import numpy as np

global img
global point1, point2

roi_points = []
def on_mouse(event, x, y, flags, param):
    global img, point1, point2
    # img2 = img.copy()
    if event == cv2.EVENT_LBUTTONDOWN:  # 左键点击
        point1 = (x, y)
        cv2.circle(img, point1, 4, (255, 255, 0), 3)
        print("point1: ", point1)
        roi_points.append([x, y])
        cv2.imshow('image', img)


def main():
    global img

    # Load the video
    video = cv2.VideoCapture("rtsp://admin:1111111a@192.168.16.222")
    while True:
        success, img = video.read()
        # img = cv2.imread(frame)
        cv2.namedWindow('image')
        cv2.imshow('image', img)
        cv2.setMouseCallback('image', on_mouse)
        cv2.waitKey(0)
        print(roi_points)
        cv2.polylines(img, [np.array(roi_points)], True, (0, 255, 0), 2)
        cv2.imshow('image', img)
        cv2.waitKey(0)
        break


if __name__ == '__main__':
    main()
