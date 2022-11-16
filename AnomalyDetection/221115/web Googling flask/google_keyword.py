import requests
from bs4 import BeautifulSoup

def get_search_count(keyword):
    url = "https://www.google.com/search?q={}".format(keyword)
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
    res = requests.get(url, headers=headers)

    # HTML 소스코드, 사용할 parser
    soup = BeautifulSoup(res.text, 'lxml')
    number = soup.select_one('#result-stats').text
    
    # print(number) # 검색결과 약 7,320,000개 (0.47초) 
    # 개수만 남기기위해 슬라이싱
    number = number[number.find('약')+2:number.rfind('개')] # 7,320,000
    number = int(number.replace(',','')) # 7320000

    # 검색어와 검색 결과 수에 대한 결과를 dict으로 반환
    return {'keyword':keyword, 'number':number}

if __name__ == '__main__':
    print(get_search_count("나루토"))