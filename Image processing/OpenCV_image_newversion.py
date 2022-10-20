# 1. 영상 생성
import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = np.empty((480, 640), dtype=np.uint8) # grayscale image
img2 = np.zeros((480, 640, 3), dtype=np.uint8) # color image
img3 = np.ones((480, 640), dtype=np.uint8) * 255 # white
img4 = np.full((480, 640, 3), (0, 255, 255), dtype=np.uint8) # yellow

plt.subplot(411), plt.axis('off'), plt.imshow(img1)
plt.subplot(412), plt.axis('off'), plt.imshow(img2)
plt.subplot(421), plt.axis('off'), plt.imshow(img3)
plt.subplot(422), plt.axis('off'), plt.imshow(img4)
plt.show()

# 2. 영상 복사
img1 = cv2.imread('./알파카.jpg')
img2 = img1 # img1 데이터를 참조
img3 = img1.copy() # 복사본 새로 생성
plt.subplot(311), plt.axis('off'), plt.imshow(img1)
plt.subplot(312), plt.axis('off'), plt.imshow(img2)
plt.subplot(313), plt.axis('off'), plt.imshow(img3)

plt.show()

# 3. 영상 부분 추출
img1 = cv2.imread('./알파카.jpg')
img2 = img1[40:120, 30:150] # numpy.ndarray의 슬라이싱
img3 = img1[40:120, 30:150].copy()

img2.fill(0) # img1과 참조하는 관계이므로 img1에도 영향

plt.subplot(311), plt.axis('off'), plt.imshow(img1)
plt.subplot(312), plt.axis('off'), plt.imshow(img2)
plt.subplot(313), plt.axis('off'), plt.imshow(img3)

plt.show()