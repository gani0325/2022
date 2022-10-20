import matplotlib.pyplot as plt
import cv2

imgBGR = cv2.imread('./star.bmp')
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
imgGray = cv2.imread('./star.bmp', cv2.IMREAD_GRAYSCALE)

plt.subplot(211), plt.axis('off'), plt.imshow(imgRGB)
plt.subplot(212), plt.axis('off'), plt.imshow(imgGray, cmap='gray')
plt.show()