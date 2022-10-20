# 5장 OpenCV로 이미지 차이 분석하기 – “천체 이미지로 명왕성을 찾아보자”
# 클라이드 톰보가 1930년 명왕성을 발견할 때 사용한 장치인 ‘반짝 비교정’을 복원한다.
# 현대적인 컴퓨터 비전 기술을 사용해 자동으로 행성이나 운석과 같이 별 시야에서 이동 중인 순간적인 천체를 찾아낸다. 
# OpenCV와 NumPy를 활용

import os
from pathlib import Path
import numpy as np
import cv2 as cv

MIN_NUM_KEYPOINT_MATCHES = 50

# """페어링된 이미지가 있는 2개의 폴더를 순환하고 이미지를 등록하고 깜박임"""
def main():
    night1_files = sorted(os.listdir('./night_1'))
    night2_files = sorted(os.listdir('./night_2'))             
    path1 = Path.cwd() / './night_1'
    path2 = Path.cwd() / './night_2'
    path3 = Path.cwd() / './night_1_registered'

    for i, _ in enumerate(night1_files):    
        img1 = cv.imread(str(path1 / night1_files[i]), cv.IMREAD_GRAYSCALE)
        img2 = cv.imread(str(path2 / night2_files[i]), cv.IMREAD_GRAYSCALE)

        print("Comparing {} to {}.\n".format(night1_files[i], night2_files[i]))

        # 핵심 포인트와 그들 사이의 가장 좋은 일치를 찾기
        kp1, kp2, best_matches = find_best_matches(img1, img2)
        img_match = cv.drawMatches(img1, kp1, img2, kp2,
                                   best_matches, outImg=None)
        
        # 두 이미지 사이에 선을 그림
        height, width = img1.shape
        cv.line(img_match, (width, 0), (width, height), (255, 255, 255), 1)
        QC_best_matches(img_match)      # 무시하려면 주석 처리

        # 키포인트를 사용하여 왼쪽 이미지를 등록   
        img1_registered = register_image(img1, img2, kp1, kp2, best_matches)

        # QC 등록 및 등록된 이미지 저장(선택 단계):
        blink(img1, img1_registered, 'Check Registration', num_loops=5)  
        out_filename = '{}_registered.png'.format(night1_files[i][:-4])
        cv.imwrite(str(path3 / out_filename), img1_registered)      # 덮어쓴다

        cv.destroyAllWindows()

        # 깜박임 비교기 실행
        blink(img1_registered, img2, 'Blink Comparator', num_loops=15)


# """두 이미지에 대한 키포인트 목록과 가장 잘 일치하는 목록을 반환"""
def find_best_matches(img1, img2):
    orb = cv.ORB_create(nfeatures=100)      # ORB 개체를 시작

    # ORB로 키포인트와 디스크립터를 찾기
    kp1, desc1 = orb.detectAndCompute(img1, mask=None)
    kp2, desc2 = orb.detectAndCompute(img2, mask=None)
    
    # Brute Force Matcher를 사용하여 키포인트 일치를 찾기
    bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
    matches = bf.match(desc1, desc2)

    # 거리의 오름차순으로 일치 항목을 정렬하고 최상의 n개 일치 항목을 유지
    matches = sorted(matches, key=lambda x: x.distance)
    best_matches = matches[:MIN_NUM_KEYPOINT_MATCHES]
              
    return kp1, kp2, best_matches

# """컬러 라인으로 연결된 최상의 키포인트 일치를 그린다"""
def QC_best_matches(img_match):
    cv.imshow('Best {} Matches'.format(MIN_NUM_KEYPOINT_MATCHES), img_match)
    cv.waitKey(2500)            # 창을 2.5초 동안 활성 상태로 유지
        
# """두 번째 이미지에 등록된 첫 번째 이미지를 반환"""
def register_image(img1, img2, kp1, kp2, best_matches):
    if len(best_matches) >= MIN_NUM_KEYPOINT_MATCHES:
        src_pts = np.zeros((len(best_matches), 2), dtype=np.float32)
        dst_pts = np.zeros((len(best_matches), 2), dtype=np.float32)

        for i, match in enumerate(best_matches):
            src_pts[i, :] = kp1[match.queryIdx].pt
            dst_pts[i, :] = kp2[match.trainIdx].pt
        
        # findHomography : 두 평면 사이의 투시 변환(Perspective transform)을 의미, homography matrix, H 추출
        h_array, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC)
        height, width = img2.shape       # 이미지 2의 치수를 가져오기
        # warpPerspective : 원근 맵 행렬에 대한 기하학적 변환을 수행
        img1_warped = cv.warpPerspective(img1, h_array, (width, height))

        return img1_warped

    else:
        print("WARNING: Number of keypoint matches < {}\n".format
              (MIN_NUM_KEYPOINT_MATCHES))
        return img1

# """두 개의 이미지로 깜박임 비교기를 복제"""
def blink(image_1, image_2, window_name, num_loops):
    for _ in range(num_loops):
        cv.imshow(window_name, image_1)
        cv.waitKey(330)
        cv.imshow(window_name, image_2)
        cv.waitKey(330)
        
if __name__ == '__main__':
    main()
