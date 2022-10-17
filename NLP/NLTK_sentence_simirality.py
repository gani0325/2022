# 2장 NLTK로 문서 간 유사도 측정하기 - “이 소설의 원작자는 누구일까”

# 자연어 처리를 통해 아서 코난 도일이나 H. G. 웰스 중 누가 『잃어버린 세계』를 썼는지를 결정한다.
# NLTK, matplotlib 등의 모듈은 물론이고 불용어(stop words), 품사, 어휘의 풍부함, 자카드 유사성(Jaccard similarity) 등의 
# 스타일로메트리(stylometry) 기법을 활용

# punctuation 히트맵 만들기
import math
from string import punctuation      # 따옴표,마침표 물음표 등등 이런류의 문장부호
import nltk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import seaborn as sns

PUNCT_SET = set(punctuation)

def main():  
    # 작성자가 사전에 텍스트 파일을 로드
    strings_by_author = dict()
    strings_by_author['doyle'] = text_to_string('hound.txt')
    strings_by_author['wells'] = text_to_string('war.txt')
    strings_by_author['unknown'] = text_to_string('lost.txt')

    # 문장 부호만 보존한 텍스트 문자열을 토큰화
    punct_by_author = make_punct_dict(strings_by_author)

    # punctuation을 숫자 값으로 변환하고 히트맵을 표시
    plt.ion()

    for author in punct_by_author:
        heat = convert_punct_to_number(punct_by_author, author)
        arr = np.array((heat[:6561])) # 정사각형 배열의 가장 큰 크기로 자르기
        arr_reshaped = arr.reshape(int(math.sqrt(len(arr))),
                                   int(math.sqrt(len(arr))))
        fig, ax = plt.subplots(figsize=(7, 7))
        sns.heatmap(arr_reshaped,
                    cmap=ListedColormap(['blue', 'yellow']),    # 인자로 주어진 색상을 그래프상에 표시하기 위한 객체
                    square=True,
                    ax=ax)
        ax.set_title('Heatmap Semicolons {}'.format(author))
    plt.show()    

# # """텍스트 파일을 읽고 문자열 목록을 반환"""
# def text_to_string(filename):
#     strings = []
#     with open(filename) as f:
#         strings.append(f.read())
#     return '\n'.join(strings)

# """텍스트 파일을 읽고 문자열을 반환"""
def text_to_string(filename):
    """Read a text file and return a string."""
    with open(filename) as infile:
        return infile.read()

# """저자가 말뭉치에 의해 토큰화된 punctuation 사전을 반환"""
def make_punct_dict(strings_by_author):
    """Return dictionary of tokenized punctuation by corpus by author."""
    punct_by_author = dict()

    for author in strings_by_author:
        # 단어 단위로 나누기
        tokens = nltk.word_tokenize(strings_by_author[author])
        
        # punct_by_author : 문장 부호만 보존한 텍스트 문자열을 토큰화
        punct_by_author[author] = ([token for token in tokens
                                    if token in PUNCT_SET])
        print("Number punctuation marks in {} = {}"
              .format(author, len(punct_by_author[author])))
    return punct_by_author  


# """숫자 값으로 변환된 punctuation 목록을 반환"""
def convert_punct_to_number(punct_by_author, author):
    """Return list of punctuation marks converted to numerical values."""
    heat_vals = []
    for char in punct_by_author[author]:
        if char == ';':
            value = 1
        else:
            value = 2
        heat_vals.append(value)
    return heat_vals

if __name__ == '__main__':
    main()






















