import sys
import glob
import cv2

# images에 있는 모든 jpg 파일을 img_files 리스트에 추가
img_files = glob.glob('./image/*.jpg')

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

cnt = len(img_files)
idx = 0
print(cnt)
while True:
    img = cv2.imread(img_files[idx])
    if img is None:
        print('Image load failed!')
        break
    cv2.imshow('image', img)
    if cv2.waitKey(1000) >= 0:
        break # 임의의 키가 눌리면 슬라이드 종료
    idx += 1
    if idx >= cnt:
        idx = 0