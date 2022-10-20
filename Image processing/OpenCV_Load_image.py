import cv2
import sys
# 이미지를 불러와 img 변수에 저장
img = cv2.imread('./알파카.jpg')

# 영상 파일 불러오기를 실패하면 에러 메시지를 출력하고 종료
if img is None:
    print('Image load failed!')
    sys.exit()

# "image"라는 이름의 새 창을 만들고, 이 창에 img 영상을 출력하고, 키보드 입력이 있을 때까지 대기
cv2.namedWindow('image')
cv2.imshow('image', img)
cv2.waitKey()
# 생성된 모든 창을 닫음
cv2.destroyAllWindows()