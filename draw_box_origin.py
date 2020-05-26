# coding:utf-8
import cv2
import os
import sys
import shutil


def chang_neg(str):
    try:
        num = float(str)
    except:
        num = 0
    return num


def get_img_box(filepath):
    img_box = dict()
    with open(filepath) as file:
        lines = file.readlines()
    for line in lines:
        info = line.strip().split()
        print(line.strip())
        if info[0] in img_box:
            img_box[info[0]].append(
                {"x": chang_neg(info[1]), "y": chang_neg(info[2]), "w": chang_neg(info[3]), "h": chang_neg(info[4]),
                 "id": info[5], "color": info[5]})
        else:
            img_box[info[0]] = [
                {"x": chang_neg(info[1]), "y": chang_neg(info[2]), "w": chang_neg(info[3]), "h": chang_neg(info[4]),
                 "id": info[5], "color": info[5]}]
    return img_box


def draw_box(img_box, save_folder, img_folder):
    for one_box in img_box.items():
        img_name = one_box[0]
        for info in one_box[1]:
            img_save_path = os.path.join(save_folder, img_name)
            if not os.path.exists(img_save_path):
                shutil.copy(os.path.join(img_folder, img_name), img_save_path)
            img = cv2.imread(img_save_path)
            if info['color'] == "脸":
                cv2.putText(img, info["id"], (int(info["x"]), int(info["y"])), cv2.FONT_HERSHEY_SIMPLEX, 0, (0, 0, 225),
                            2)
                # cv2.rectangle(img, (int(info["x"]), int(info["y"])),
                # (int(info["x"] + info["w"]), int(info["y"] + info["h"])), (0, 0, 225), 0)
                cv2.rectangle(img, (int(info["x"]), int(info["y"])),
                              (int(info["w"]), int(info["h"])), (0, 0, 225), 2)
                cv2.imwrite(img_save_path, img)
            else:
                cv2.putText(img, info["id"], (int(info["x"]), int(info["y"])), cv2.FONT_HERSHEY_SIMPLEX, 0, (0, 0, 225),
                            2)
                # cv2.rectangle(img, (int(info["x"]), int(info["y"])),
                # (int(info["x"] + info["w"]), int(info["y"] + info["h"])), (0, 0, 225), 0)
                cv2.rectangle(img, (int(info["x"]), int(info["y"])),
                              (int(info["w"]), int(info["h"])), (0, 225, 0), 2)
                cv2.imwrite(img_save_path, img)


if __name__ == '__main__':
    img_save_path = sys.argv[1]
    img_folder = sys.argv[2]
    filepath = sys.argv[3]
    img_box = get_img_box(filepath)
    draw_box(img_box, img_save_path, img_folder)
