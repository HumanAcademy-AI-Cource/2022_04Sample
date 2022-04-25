#!/usr/bin/env python3

# ライブラリのインポート
import cv2
import numpy as np

# 画像を読み込む
image = cv2.imread("banana.jpg")

# 画像の中に円を描画する
cv2.circle(image, (300, 300), 100, (0, 0, 0), thickness=2, lineType=cv2.LINE_AA)

# 円が追加された画像を保存する
cv2.imwrite("banana_gousei.jpg", image)
print("画像を加工して保存しました。")
