import matplotlib.pyplot as plt
import cv2

src = cv2.imread('sea.jpg', cv2.IMREAD_COLOR)
logo = cv2.imread('whale.png', cv2.IMREAD_UNCHANGED)

mask = logo[:, :, 3]    # mask는 알파 채널로 만든 마스크 영상
logo = logo[:, :, :-1]  # logo는 b, g, r 3채널로 구성된 컬러 영상
h, w = mask.shape[:2]
crop = src[10:10+h, 10:10+w]  # logo, mask와 같은 크기의 부분 영상 추출

dst = cv2.copyTo(logo, mask, crop)

# plt.subplot(311), plt.axis('off'), plt.imshow(logo)
# plt.subplot(312), plt.axis('off'), plt.imshow(mask)
# plt.subplot(313), plt.axis('off'), plt.imshow(crop)

cv2.imshow('image', dst)
cv2.waitKey()
# 생성된 모든 창을 닫음
cv2.destroyAllWindows()