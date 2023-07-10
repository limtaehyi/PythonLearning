#-*- encoding: utf-8 -*-
import random

def main():
    number_list = [1,2,3,4,5,6]
    
    top = int(input(">"))
    bottom = 7 - top

    number_list.remove(top)
    number_list.remove(bottom)

    left = random.choice(number_list)
    right = 7 - left

    number_list.remove(left)
    number_list.remove(right)

    body = number_list[0]
    foot = number_list[1]

    
    
    print(f"""
                    ---
                   | {top} |
                --- --- ---
               | {left} | {body} | {right} |
                --- --- ---
                   | {bottom} |
                    ---
                   | {foot} |
                    ---
""")

if __name__ == "__main__":
    main()
