#120191099 임태희

# !! -- 필수파일 -- !!
# !! -- txts/test.txt -- !!
# !! -- firstfolder/firstfile.py -- !!
# !! -- firstfolder/secondfolder/secondfile.py -- !!

# !! -- 필수모듈 -- !!
# !! -- pip install chainmap -- !!

# 변수 이름은 대부분 언더바(_)로 정의하거나 첫문자마다 대문자를 쓰는 낙타체를 많이씀.
# 변수 이름은 가시성을 위해 동사+명사의 형태로 쓰는 것이 좋음.

'''
  주석은 한 줄은 샵으로 하고 여러줄 주석은 세미콜론 3개로 사용함.
  one line comment : #
  multi line comment : 'x3
'''

use_underbar_var = 1
UseCamelVar = 3

'''
 1. 변수 이름은 문자(a-zA-Z), 숫자(0-9), 밑줄(_)로 구성해야 합니다.
 2. 변수 이름은 숫자로 시작할 수 없습니다.
 3. Python은 대소문자를 구분하기 때문에 동일한 알파벳의 대문자와 소문자는 다른 변수로 취급됩니다.
 4. 특별한 예약어는 변수 이름으로 사용할 수 없습니다. 예약어는 Python의 기능이나 명령어로 사용되기 때문입니다. 일반적인 예약어 및 키워드에는 True, False, None, if, else, elif, while, for, return, def, class 등이 포함됩니다.
 5. 변수 이름은 의미 있는 이름을 사용해 코드의 가독성과 관리를 쉽게 하는 것이 좋습니다.

 올바른 변수 이름: name, age, counter_1, _private_variable
 잘못된 변수 이름: 1counter, variable@1, my-name
'''

print("1. -------------------------------------------------------------------")

test_int = 101
test_str = 'test1 test11'
test_tup = (102,'test2')
test_list = [103, 'test3', [1033, 'test3-1']]
test_dict = { 104:"test4", 1044:"test4-1" }

print("hi")
get_input = input("input : ")

# 매우 긴 문자열을 넣어야 할때는 역슬래쉬(또는 원싸인\)을 통해 아직 안 끝났다고 정의 할 수 있음. 하지만 역슬래쉬 뒤에 주석 불가
very_long_string = "very very long string very very long string very very long string very very long string very very long string very very long string very very long string very very long string "\
                   "very very long string very very long string very very long string very very long string very very long string very very long string very very long string very very long string "\
                   "very very long string very very long string very very long string very very long string very very long string very very long string very very long string very very long string "
print(very_long_string)

print("string1","comma","string2")
print("string1"+"plus"+"string2")

print("input tab : a\tb")
print("input newline : a\nb")
print("input backslash : a\\b")
print("input single quote : a\'b")
print("input double quote : a\"b")
print("input null : a\000b")

print(test_int)
print(test_str)
print(test_tup)
print(test_list)
print(test_dict)

print(type(test_int))
print(type(test_str))
print(type(test_tup))
print(type(test_list))
print(type(test_dict))

'''
 is 함수들로 변수 타입 판별 가능, 맞으면 true 반환
 - isnumeric : 숫자로만 이루어져 있는지 판별. 수학 기호, 분수, 지수, 로마 숫자도 숫자로 인식
 - isdecimal : 숫자로만 이루어져 있는지 판별. 소수점, 마이너스 기호, 달러등 문자가 하나라도 들어가 있으면 false 
 - isdigit : 숫자로만 이루어져 있는지 판별. 소수점, 마이너스 기호, 달러등 문자가 하나라도 들어가 있으면 false 
 - isalpha : 알파벳 문자로만 이루어져 있는지 판별. 숫자, 특수문자가 하나라도 들어가 있으면 false
 - isalnum : 알파벳, 숫자로만 이루어져 있는지 판별. 특수 문자가 들어가 있으면 false
'''

test_int.isnumeric


print("2. -------------------------------------------------------------------")

modint = 10

modint += 1 # modint = modint + 1, 덧셈
print(modint)
modint -= 1 # modint = modint - 1, 뺄셈
print(modint)
modint *= 2 # modint = modint * 2, 곱셈
print(modint)
modint //= 2 # modint = modint // 2, 나머지 무시하는 나눗셈의 몫
print(modint)
modint /= 2 # modint = modint / 2, 소수점까지 구하는 나눗셈
print(modint)

modint = 10
modint %= 3 # modint = modint % 3, 나누고 난 후의 나머지
print(modint)
modint ^= 2 # modint = modint ^ 2, 제곱
print(modint)

print("3. -------------------------------------------------------------------")

num_conv = 17

print(bin(num_conv)) # 2진수
print(oct(num_conv)) # 8진수
print(num_conv)      # 10진수
print(hex(num_conv)) # 16진수

print("4. -------------------------------------------------------------------")

test_int = 101
test_str = 'test1 test11'
print(len(test_str))

change_int_to_str = str(test_int)
print(type(change_int_to_str))

try:
        #문자를 숫자로 변환(string 값을 int로)은 불가능 하기 때문에 오류인 except로 넘어감.
        change_str_to_int = int(test_str)
except Exception as ex:
        print(ex)


print(ord('A'))
print(ord('Z'))
print(ord('a'))
print(ord('z'))


print(chr(65))
print(chr(90))
print(chr(97))
print(chr(122))


print("5. -------------------------------------------------------------------") # 2023.07.04

test_str = 'test1 test11'
test_list = [103, 'test3', [1033, 'test3-1']]

# 인덱스의 뜻은 [여기번째 이상:여기번째 미만:(여기 글자씩 건너 뜀)]
print(test_str[2])
print(test_str[0:9])
print(test_str[:9])
print(test_str[2:8])
print(test_str[::2])


print(test_list[2])
print(test_list[2][0])


test_list.append("append_test")
print(test_list)
test_list.remove("test3")
print(test_list)

test_list.insert(2,"insert_test")
print(test_list)

# 맨 뒤에 값 삭제
test_list.pop()
print(test_list)

print("6. -------------------------------------------------------------------")

test_list = [103, 'test3', [1033, 'test3-1']]
empty_list = []

for i in range(10):
        print(i)

for a in range(1,10):
        print(a)


for j in range(2):
        for k in range(3):
                empty_list.append((j,k))
print(empty_list)
        
for n in test_list:
        print(n)

print("7. -------------------------------------------------------------------")

if 1 == 1:
        print("1yes")
else:
        print("1no")

if 1 == 1 and 2 == 2:
        print("2yes")
else:
        print("2no")

if 1 == 2 or 3 == 3:
        print("3yes")
else:
        print("3no")

if (1 == 2 and 2 == 2) or (1 == 3 or 4 == 4):
        print("4yes")
else:
        print("4no")

if 1 == 2:
        print("5yes")
else:
        print("5no")

if 1 == 0:
        print("6yes")
else:
        print("6no")

if "1" == "2":
        print("7yes")
else:
        print("7no")


if 0 == False:
        print("8_1")
if 1 == True:
        print("8_2")
if 2 == True:
        print("8_3")
if "anystrings" == True:
        print("8_4")


test_str = 'test1 test11'

if "k" in test_str:
        print("9yes")
elif "t" in test_str:
        print("9no")
else:
        print("..")


if "t" not in test_str:
        print("10yes")
else:
        print("10no")

print("8. -------------------------------------------------------------------")

counter = 0
while 1:
        counter += 1
        print(counter)
        if counter == 10:
                break
        else:
                continue


iterator_num = iter(range(3))
print("1 :",next(iterator_num))
print("2 :",next(iterator_num))
print("3 :",next(iterator_num))
try:
        print("4.",next(iterator_num))
except Exception as ex:
        print("you over 3 times")
        print(ex)
        
print("9. -------------------------------------------------------------------")

enumerate_list = ["hi","my","name","is","LTH"]

# 2개의 값중 첫번째 값은 인덱스(순서) 두번째 값은 값을 반환함.
for index, value in enumerate(enumerate_list):
        print(index, " --- ", value)


format_num1 = 100
format_num2 = 200
# f'{}'는 문자안에 변수를 사용하고 싶을때 사용함.
print(f"1. this is format_number1 : {format_num1}, format_number2 : {format_num2}")
print("2. this is format_number1 : {}, format_number2 : {}".format(format_num1, format_num2))

format_string = "stringsu"
format_num3 = 3.141592
print("3. this is format_string : %s, format_string[5] : %c" %(format_string, format_string[5]))
print("4. this is format_num3: %f, format_num3 : %.3f, format_num3 : %07.13f" %(format_num3, format_num3, format_num3))

# .split("??") ??값을 기준으로 나눈후 리스트 형태로 저장함.
split_this_strings = "Split this string using spaces by utilizing the split function."
print(split_this_strings.split(" "))

# "??".join(!!) !!에 있는 값들을 ??를 이용해서 붙인후 문자열로 반환함.
list_to_strings = ["what","are","you","doing"]
print(" ".join(list_to_strings))
print("+".join(list_to_strings))

# map(??,!!)은 for문의 축약 형태이며 !!에 있는 각각의 값들에 ??함수를 적용함.
mapping_this_list = ["a","b","c","d","z"]
print(list(map(ord,mapping_this_list)))

# filter(??,!!)은 map과 비슷한 형태이지만 True, False로 포함할지를 결정 가능함.
filtering_this_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_even(n):
    return True if n % 2 == 0 else False

print(list(filter(is_even, filtering_this_list)))


# for문을 줄여 쓸수 있음.
comprehension_list = ["tail","alphabet","egg","horse","elment","error"]
result_comp_list1 = [i for i in comprehension_list]
result_comp_list2 = [i[0] for i in comprehension_list]
result_comp_list3 = [(i, j) for i in range(3) for j in range(4)]
print(result_comp_list1)
print(result_comp_list2)
print(result_comp_list3)

#문자 바꾸기
swap_a = 100
swap_b = 300
print(f"Before swap swap_a, swap_b : {swap_a}, {swap_b}")

swap_a, swap_b = swap_b, swap_a
print(f"After swap swap_a, swap_b : {swap_a}, {swap_b}")


print("10. -------------------------------------------------------------------")


def no_para_no_ret():
        a = 1
        print("no_para_no_ret")

def no_para_yes_ret():
        a = 2
        print("no_para_yes_ret")
        return a
        
#get_para처럼 def의 소괄호 안에 있는 값은 직접 가져가는 것이 아니라 복사 개념이고 return으로 값을
#받아와서 덮어 쓰는 방법이 있음.

def yes_para_no_ret(get_para):
        get_para += 3
        print("yes_para_no_ret")

def yes_para_yes_ret(get_para):
        get_para += 4
        print("yes_para_no_ret")
        return get_para


send_para = 50

no_para_no_ret()
receive1_return = no_para_yes_ret()
yes_para_no_ret(send_para)
receive2_return = yes_para_yes_ret(send_para)

print(receive1_return)
print(receive2_return)


print("11. -------------------------------------------------------------------")


# 파이썬 함수에서 매개변수를 지정할 수 있는 함수의 종류는 6가지 이다.

# 1. 필수인자
# 함수 정의시 지정된 순서 대로 정확한 개수의 인자를 전달해야 하며 개수가 맞지 않으면 TypeError 발생
def greet(name):
        print(f"hello, {name}")

greet("LTH")


# 2. 기본인자
# 함수 정의 시 매개변수에 기본 값을 넣을 수 있으며 함수 호출시 해당 인자를 생략하면 기본값이 사용됨
# 기본 인자는 무조건 필수 인자 뒤에 위치 해야 함
def power(base, exponent=2):
        return base ** exponent

print(power(4))
print(power(4, 3))


# 3. 가변 인자 리스트
# 임의의 개수의 위치 인자를 받을 수 있도록 하며 * 기호를 통해 정의 함, 관례적으로는 args를 사용 하며 함수 내에 튜플로 처리 됨
def sum_all(*args):
        total = 0
        for num in args:
                total += num
        return total

print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3, 4, 5))


# 4. 키워드 인자 리스트
# 임의의 개수의 키워드 인자를 받을 수 있도록 하며 ** 기호를 통해 정의 함, 관례적으로 kwargs를 사용 하며 함수 내에서 딕셔너리로 처리 됨
def print_info(**kwargs):
        for key, value in kwargs.items():
                print(f"{key}: {value}")

print_info(name="Bob", age=30, city="New York")


# 5. 키워드 전용 인자
# 함수 호출시 반드시 키워드 형태로 전달해야 하며, *args 뒤에 위치하거나 * 기호만 사용하여 정의
def divide(x, y, *, integer_divide=False):
        if integer_divide:
                return x // y
        else:
                return x / y

print(divide(10, 2))
print(divide(10, 2, integer_divide=True))
try:
        print(divide(10, 2, True))
except:
        print("Third parameter is not a keyword, it's a positional argument")


# 6. 위치 전용 인자
# 함수 호출시 반드시 위치 인자 형태로 전달되어야 한다.
# / 기호를 사용하며, / 앞에 있는 인자들이 위치 전용 인자가 됨
def combine(a, b, /, c, d):
        return a + b + c + d

print(combine(1, 2, 3, 4))
print(combine(1, 2, c=5, d=7))

try:
        print(combine(a=1, b=2, c=3, d=4))
except:
        print("First and Second parameters are must be arguments")


print("12. -------------------------------------------------------------------")

'''
 SyntaxError : 문법적으로 잘못 되었을때 발생
 ValueError: 잘못된 값을 입력했을 때 발생
 TypeError: 잘못된 데이터 유형을 사용할 때 발생
 NameError: 정의되지 않은 변수나 함수를 호출할 때 발생
 KeyError: 딕셔너리에서 잘못된 키를 사용할 때 발생
 IndexError: 리스트나 튜플에서 잘못된 인덱스를 사용할 때 발생
 AttributeError: 객체에 잘못된 속성을 사용할 때 발생
 ZeroDivisionError: 0으로 나누기를 시도할 때 발생
 FileNotFoundError: 존재하지 않는 파일을 열려고 할 때 발생
 ImportError: 모듈을 가져올 수 없을 때 발생
 KeyboardInterrupt: 사용자가 프로그램을 중지시킬 때 발생
'''

try:
        print("can you divide 1 with zero?")
        print(1/0)
        
except ZeroDivisionError as ex:

        print("can you see this ZeroDivisionError?")
        print("+++++++++++++++++++++++++++++++++++++")
        print(ex)
        print("+++++++++++++++++++++++++++++++++++++")
        
finally:
        print("ending")


print("13. -------------------------------------------------------------------")

with open("test.txt","w") as newfile:
        for k in range(10):
                newfile.write(str(k)+str(k)+str(k)+"\n")
newfile.close()

with open("test.txt","r") as savedfile:
        #test.txt의 파일 정보를 출
        print(savedfile)
        #read() 모든 값을 형태 그대로 읽어옴.
        print(savedfile.read())

with open("test.txt","r") as savedfile1:
        #readline() 한줄씩만 읽어옴.
        print(savedfile1.readline())
        print(savedfile1.readline())

with open("test.txt","r") as savedfile2:
        #readlines() 모든 줄의 각각의 형태를 리스트로 저장함.
        print(savedfile2.readlines())
savedfile.close()

print("14. -------------------------------------------------------------------")

class makeclass:
        #__init__은 생성자로서 객체가 생성될 때 실행 됨.
        #self는 이 클래스로 인해 만들어진 객체가 들어가며 id 함수를 통해 메모리 주소를 확인 할 수 있다. 
        def __init__(self):
                print(self)
                print(id(self))
                print("you make this object")
                
        def printdef(self,hellow):
                print("!!printdef!!")
                print("received : "+hellow)


newobject = makeclass() #이때 생성자 실행
print(id(newobject)) #self 값이 객체가 맞는지 확인
newobject.printdef("i will give this parameter to you")

otherobject = makeclass()
print(id(newobject))
otherobject.printdef("i will give this parameter too")


'''
 magic method
  - 매직 매소드는 파이썬에서만 사용되는 특별한 매소드이며 이미 파이썬 내 정의 되어 있고 클래스 내부에서 메소드를 
    오버라이딩 해서 사용할 수 있다.
  - 또한 직접 호출하지 않고 정해진 규칙에 따라 호출된다.

  __new__ : 객체 생성시 호출되고 init보다 먼저 실행됨
  __init__ : 생성자
  __del__ : 객체 소멸시
  __str__, __repr__ : 객체의 문자열 표현
  __iter__ : iterable 객체를 만들 때
  __next__ : iterator 를 만들 때
  __len__ : 객체 길이
  __bool__ : bool
  __add__, __sub__, __mul__, __truediv__ : 사칙연산

  외에도 다양한 매직 메소드가 있다.
'''

class Makeiteasy(object):
        def __init__(self, name, price):
                self._name = name
                self._price = price

apple = Makeiteasy("apple", 10000)
banana = Makeiteasy("banana", 20000)
#print(apple._price + banana._price) 정상적으로 작동하지만 보기 좋지 않다.


class Makeiteasy(object):
        def __init__(self, name, price):
                self._name = name
                self._price = price

        def __add__(self, target):
                return self._price + target._price

        def __sub__(self, target):
                return self._price - target._price

apple = Makeiteasy("apple", 10000)
banana = Makeiteasy("banana", 20000)
print(apple + banana)
print(apple - banana)
print(f"{apple} and {banana}")





print("15. -------------------------------------------------------------------")

'''
  import의 검색 순서는 sys.modules, built-in modules, sys.path 순서이다.
   - sys.modules : Python이 Module/Package를 찾기 위해 가장 먼저 확인하는 곳입니다.
                   단순한 Directory로 이미 import된 module과 Package를 저장하고 있습니다.
   - built-in modules : Python에서 제공하는 공식 Library 들 입니다.Python Standard Library(os,  sys, time 등)이
                        여기에 해당됩니다.
   - sys.path : package의 __init__ 변수와 같이 String Value로된 list 입니다.

   *중요 : import는 보통 함수 밖, 맨 위에 전역변수로 선언하는 것이 일반적이며 import를 함수 안에 선언하면 그 함수 내에서만 사용 가능하며 함수가 return이 되면 import는 풀린다.
'''

from firstfolder.firstfile import firstprint #or *
import firstfolder.secondfolder.secondfile as sf

firstprint()
sf.secondprint()

print("16. -------------------------------------------------------------------")
'''
   - 동기는 차례대로 앞의 작업이 끝나면 처리하는 방식이다.
   - 순차적인 작업을 할때 사용된다. (python 프로그램)
   ============================================ 
     1번째 작업 | 2번째 작업        | 3번째 작업 
     ---------->
                  ---------------->
                                   ------------>
   ============================================


   - 비동기는 동시에 실행시키고 일단 되는대로 결과를 나타내는 방식이다.
   - 병렬적으로 한번에 처리되는 작업을 해야 할때 사용된다. (웹브라우저 페이지 로드)
   ============================================
     ---------->        1번째 작업
     ---------------->  2번째 작업
     ------------>      3번째 작업
   ============================================
'''
import asyncio

async def my_coroutine(name, seconds_to_wait):
    print(f'{name} 시작됨.')
    await asyncio.sleep(seconds_to_wait)
    print(f'{name} 종료됨.')

async def asyncmain():
    tasks = [
        asyncio.ensure_future(my_coroutine("첫 번째 작업", 2)),
        asyncio.ensure_future(my_coroutine("두 번째 작업", 3)),
        asyncio.ensure_future(my_coroutine("세 번째 작업", 1))
    ]
    await asyncio.gather(*tasks)


asyncio.run(asyncmain())

print("17. -------------------------------------------------------------------")

numbers = [1, 2, 3, 4, 5]
squares = map(lambda x: x ** 2, numbers)

print(list(squares))

print(list(filter(lambda x: x < 5, range(10))))

print("18. -------------------------------------------------------------------")

import time
start_time = time.time()

#20000의 약수를 구하는 간단한 코드
decimal_list = []
for i in range(2, 20000):
        if 20000 % i != 0:
                continue
        else:
                decimal_list.append(i)

print(decimal_list)

end_time = time.time()
print(end_time - start_time)

print("19. -------------------------------------------------------------------")

# test는 인자를 2개를 받는데 y=[], y=0 처럼 default값을 지정해 줄 수가 있다.
# 하지만 python의 특이한 특성이 있는데 처음 실행은 default이지만 두번째 실행시 y는 메모리에 가지고 있기
# 때문에 지역변수이지만 전역변수처럼 남아 계속 수정된다. ★x5

def test(x, y=[]):
        y.append(x)
        return y

print(test(1)) # test(x=1, y=[])
print(test(2)) # test(x=2, y=[1])  <- 위에 함수에서 return y가 리스트 '[1]' 로 메모리에 저장되어있다.
print(test(3, [])) # test(x=3, y=[1,2], [])  <- y는 메모리 어딘가에 계속 있고 다시 아무 리스트를 준곳에 append된다.
print(test(4)) # test(x=4, y=[1,2])


print("20. -------------------------------------------------------------------")

# 추가 지식들

# 언더바 사용
# 1. 숫자의 콤마 대신 사용으로 자릿수 구분
hard_to_count = "1000000000000"
easy_to_count = "1_000_000_000_000"

# 2. 값의 무시 가능
underbar_tup = (1, 2, 3, 4, 5)
a, b, c, _, e = underbar_tup # 또는 a, *_, b = underbar_tup 으로 여러 값 무시 가능
print(a, b, c, e)

# 3. 이 모듈(파일)내에서만 사용하는 함수 선언
# 외부에서 이 파일(cheatsheet.py)를 import 해서 _hi()를 실행하면 에러 발생
def _hi():
        print("hi")

# 4. 파이썬 키워드와의 충돌 회피
def print_(args):
        print("this is not print func, this is print_ func")
        print(args)

print_([1, 2, 3, 4])


# 튜플, 리스트, 딕셔너리의 병합
print([1, 2, 3] + [4, 5, 6])

print((1, 2, 3) + (4, 5, 6))

new_list = [1, 2, 3]
new_list += [4, 5, 6]
print(new_list)

new_tup = (1, 2, 3)
new_tup += (4, 5, 6)
print(new_tup)

print({1, 2, 3} & {1, 4}) # 교집합(and)
print({1, 2, 3} | {1, 4}) # 합집합(or)
print({1, 2, 3} - {1, 4}) # 차집합(-)
print({1, 2, 3} ^ {1, 4}) # 대칭차집합(xor)

print({'a': 1} | {'a' : 3, 'b' : 2}) # 중복 값은 오른쪽 기준

new_dict = {'a' : 1}
new_dict |= {'a' : 3, 'b' : 2}
print(new_dict)


# 3로 나누어 떨어지면 "three", 5으로 나누어 떨어지면 "five", 둘다면 "threefive"
for i in range(100):
        match(i % 3, i % 5):
                case(0, 0) : print("threefive")
                case(0, _) : print("three")
                case(_, 0) : print("five")
                case _: print(i)


print("21. -------------------------------------------------------------------")

from collections import ChainMap

example_account = {'id' : "IDX7326363752634", "type" : "account"}
example_profile = {"name" : "Lim taehyi", "type" : "profile"}

user = ChainMap(example_account, example_profile) # 두 딕셔너리를 병합후 객체로 출력

print(user['id'])
print(user['name'])
print(user['type']) # 단 중복된 경우 왼쪽 기준

user["created_on"] = "2000" # 추가도 가능

print(user)