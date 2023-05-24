import requests
from stem import Signal
from stem.control import Controller

# Tor 프록시 설정
proxies = {
    'http': 'socks5://localhost:9050',
    'https': 'socks5://localhost:9050'
}

# Tor 회로 갱신 함수
def renew_tor_circuit():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)

# Tor를 통한 요청 함수
def make_tor_request(url):
    renew_tor_circuit()  # 각 요청 전에 Tor 회로 갱신
    response = requests.get(url, proxies=proxies)
    return response

# 예제 사용법
if __name__ == '__main__':
    url = 'https://example.com'  # 원하는 URL로 대체해주세요
    response = make_tor_request(url)
    
    if response.status_code == 200:
        print(response.content)
    else:
        print('요청 실패.')
