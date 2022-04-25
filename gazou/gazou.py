#!/usr/bin/env python3

# ライブラリのインポート
import cv2
import numpy as np
import os
os.environ["QT_LOGGING_RULES"] = "*=false"

# 画像を読み込む
image = cv2.imread("banana.jpg")

# 円の大きさを決める（数字を大きくすると円が大きくなる）
ookisa = 100

# 画像の中に円を描画する
cv2.circle(image, (300, 300), ookisa, (0, 0, 0), thickness=2, lineType=cv2.LINE_AA)

# 円が追加された画像を保存する
cv2.imwrite("banana_gousei.jpg", image)
print("画像を加工して保存しました。")
