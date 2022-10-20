# 4장 암호화 기법으로 안전한 메시지 전송하기 – “해독 불가능한 암호문을 작성해보자”
# 켄 폴릿의 베스트셀러 스파이 소설인 『레베카의 열쇠』에 나오는 원타임 패드 방식을 디지털 방식으로 재구성해서, 
# 아무도 깰 수 없는 암호문을 여러분의 친구와 함께 공유한다. Collections 모듈을 활용

from collections import Counter
import re
import requests
import bs4
import nltk
from nltk.corpus import stopwords

def main():
    # 웹스크래핑을 사용하여 텍스트를 얻기
    url = 'http://www.analytictech.com/mb021/mlk.htm'
    page = requests.get(url)
    page.raise_for_status()
    # HTML, XML, HTML5 등 데이터 추출에 사용
    soup = bs4.BeautifulSoup(page.text, 'html.parser')
    p_elems = [element.text for element in soup.find_all('p')]

    speech = ' '.join(p_elems)  # Make sure to join on a space!

    # 오타를 수정하고 추가 공백, 숫자 및 구두점을 제거
    speech = speech.replace(')mowing', 'knowing')
    speech = re.sub('\s+', ' ', speech) 
    speech_edit = re.sub('[^a-zA-Z]', ' ', speech)
    speech_edit = re.sub('\s+', ' ', speech_edit)

    # 입력을 요청
    while True:
        max_words = input("Enter max words per sentence for summary: ")
        num_sents = input("Enter number of sentences for summary: ")
        if max_words.isdigit() and num_sents.isdigit():
            break
        else:
            print("\nInput must be in whole numbers.\n")
                      
    # 문장 점수를 생성하는 함수를 실행
    speech_edit_no_stop = remove_stop_words(speech_edit)
    word_freq = get_word_freq(speech_edit_no_stop)
    sent_scores = score_sentences(speech, word_freq, max_words)

    # 최상위 문장을 출력
    counts = Counter(sent_scores)
    summary = counts.most_common(int(num_sents))
    print("\nSUMMARY:")
    for i in summary:
        print(i[0])

# """문자열에서 중지 단어를 제거하고 문자열을 반환"""
def remove_stop_words(speech_edit):
    stop_words = set(stopwords.words('english'))
    speech_edit_no_stop = ''
    for word in nltk.word_tokenize(speech_edit):
        if word.lower() not in stop_words:
            speech_edit_no_stop += word + ' '  
    return speech_edit_no_stop

# """문자열에서 단어 빈도 사전을 반환"""
def get_word_freq(speech_edit_no_stop):
    word_freq = nltk.FreqDist(nltk.word_tokenize(speech_edit_no_stop.lower()))
    return word_freq

# """단어 빈도에 따라 문장 점수의 사전을 반환"""
def score_sentences(speech, word_freq, max_words):
    sent_scores = dict()
    sentences = nltk.sent_tokenize(speech)
    for sent in sentences:
        sent_scores[sent] = 0
        words = nltk.word_tokenize(sent.lower())
        sent_word_count = len(words)
        if sent_word_count <= int(max_words):
            for word in words:
                if word in word_freq.keys():
                    sent_scores[sent] += word_freq[word]
            sent_scores[sent] = sent_scores[sent] / sent_word_count
    return sent_scores

if __name__ == '__main__':
    main()


