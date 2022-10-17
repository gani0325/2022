# 3장 NLTK로 텍스트 요약하기 – “핵심 문장을 뽑아내고 단어 구름을 만들어보자”

# 마틴 루터의 ‘나에게는 꿈이 있습니다’와 같은 유명한 연설을 인터넷에서 긁어와서 요점을 요약
# 소설 본문을 멋진 광고나 판촉 글로 변환
# BeautifulSoup, Requests, regex, NLTK, Collections, wordcloud, matplotlib 등을 활용


"""
To run this program install Gensim 3.8.3 (https://pypi.org/project/gensim/3.8.3/)
"""

from collections import Counter
import re
import requests
import bs4
import nltk
from nltk.corpus import stopwords

# 웹스크래핑을 사용하여 텍스트를 얻는다
def main():
    # Use webscraping to obtain the text.
    url = 'http://www.analytictech.com/mb021/mlk.htm'
    page = requests.get(url)
    page.raise_for_status()
    soup = bs4.BeautifulSoup(page.text, 'html.parser')
    p_elems = [element.text for element in soup.find_all('p')]

    speech = ' '.join(p_elems)  # Make sure to join on a space!

    # 오타를 수정하고 추가 공백, 숫자 및 구두점을 제거
    speech = speech.replace(')mowing', 'knowing')
    speech = re.sub('\s+', ' ', speech) 
    speech_edit = re.sub('[^a-zA-Z]', ' ', speech)
    speech_edit = re.sub('\s+', ' ', speech_edit)

    # Request input.
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
    """Remove stop words from string and return string."""
    stop_words = set(stopwords.words('english'))
    speech_edit_no_stop = ''
    for word in nltk.word_tokenize(speech_edit):
        if word.lower() not in stop_words:
            speech_edit_no_stop += word + ' '  
    return speech_edit_no_stop

# """문자열에서 단어 빈도 사전을 반환"""
def get_word_freq(speech_edit_no_stop):
    """Return a dictionary of word frequency in a string."""
    word_freq = nltk.FreqDist(nltk.word_tokenize(speech_edit_no_stop.lower()))
    return word_freq

# """단어 빈도에 따라 문장 점수의 사전을 반환"""
def score_sentences(speech, word_freq, max_words):
    """Return dictionary of sentence scores based on word frequency."""
    sent_scores = dict()

    # 문장 토큰화
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