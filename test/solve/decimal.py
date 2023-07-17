#-*- encoding: utf-8 -*-
import time

def main():
    input_val = int(input("숫자를 입력하세요 : "))
    start_t = time.time()
    decimal_list = []
    for i in range(2, input_val):
        if input_val % i != 0:
            continue
        else:
            decimal_list.append(i)
    end_t = time.time()
    
    if not decimal_list:
        print(f"{input_val}은 소수입니다.")
        print(decimal_list)
        print("result time : {}".format(end_t - start_t))
    else:
        print(f"{input_val}은 소수가 아닙니다.")
        print(decimal_list)
        print("result time : {}".format(end_t - start_t))

if __name__ == "__main__":
    main()
