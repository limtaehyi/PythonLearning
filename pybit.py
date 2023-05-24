import pyupbit

# 시세 조회를 위한 함수
def get_current_price(ticker):
    try:
        # 현재가 조회
        response = pyupbit.get_orderbook(ticker=ticker)['orderbook_units'][0]['ask_price']
        return response
    except Exception as e:
        print(e)
        return None

# 메인 함수
def main():
    # 원하는 암호화폐의 ticker 입력
    ticker = "KRW-BTC"  # 예시로 비트코인(BTC)을 사용합니다. 다른 암호화폐로 변경 가능합니다.

    # 시세 조회
    current_price = get_current_price(ticker)
    if current_price is not None:
        print(f"{ticker}의 현재 가격은 {current_price} 원입니다.")
    else:
        print("시세 조회에 실패하였습니다.")

# 메인 함수 실행
if __name__ == "__main__":
    main()
