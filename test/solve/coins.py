#-*- encoding: utf-8 -*-

def main():
    wallet_money = 1000
    baek5 = 0
    baek1 = 0
    ship5 = 0
    ship1 = 0

    
    price_money = int(input("가격을 넣으세요 : "))
    result_money = wallet_money - price_money
    print(f"{result_money}의 거스름돈이 나왔습니다.")

    if result_money >= 500:
        result_money -= 500
        baek5 = 1
    if result_money >= 100:
        baek1 = result_money // 100
        result_money %= 100
    if result_money >= 50:
        ship5 = result_money // 50
        result_money %= 50
    if result_money >= 10:
        ship1 = result_money // 10
        result_money %= 10
    
    result_coins = baek5 + baek1 + ship5 + ship1

    print(f"500원 : {baek5}개, 100원 : {baek1}개, 50원 : {ship5}개, 10원 : {ship1}개")
    print(f"거스름돈 동전의 최소 개수는 총 {result_coins}개 입니다.")

if __name__ == "__main__":
    main()
