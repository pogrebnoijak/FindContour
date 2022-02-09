import cv2
import numpy as np


# task1 - частный случай task2

def task2(name: str, input_dir: str = "./temp", output_dir: str = "./out"):
    img = cv2.imread(f'{input_dir}/{name}')
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mean = gray_img.mean()
    boards = (0.1, 0.3)
    try:
        points = np.argwhere(gray_img < mean)
        if 1 - boards[1] <= points.shape[0] / gray_img.size <= 1 - boards[0]:
            points = np.argwhere(gray_img > mean)
        elif not (boards[0] <= points.shape[0] / gray_img.size <= boards[1]):
            raise Exception("wrong ratio")
        x1, x2 = points[:, 0].min(), points[:, 0].max()
        y1, y2 = points[:, 1].min(), points[:, 1].max()
        img2 = cv2.rectangle(img, (y1, x1), (y2, x2), color=(0, 0, 255))
        cv2.imwrite(f'{output_dir}/{name}', img2)
        print(f"{name}: ok")
    except Exception as er:
        print(f"{name}: {er}, skipped")


if __name__ == "__main__":
    for i in range(1, 6):
        task2(f'{i}.jpg')
    task2(f'jpg.jpg')
    task2(f'1_.jpg')
