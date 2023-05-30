#120191099 임태희

# 변수 이름은 대부분 언더바(_)로 정의하거나 첫문자마다 대문자를 쓰는 낙타체를 많이씀.
# 변수 이름은 가시성을 위해 동사+명사의 형태로 쓰는 것이 좋음.
use_underbar_var = 1
UseCamelVar = 2



print("1. ---------------------------------------------------------")

test_int = 101
test_str = 'test1 test11'
test_tup = (102,'test2')
test_list = [103, 'test3', [1033, 'test3-1']]
test_dict = { 104:"test4", 1044:"test4-1" }
'''
  one line comment : #
  multi line comment : 'x3
'''

print("hi")
get_input = input("input : ")

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

print("2. ---------------------------------------------------------")

modint = 10

modint += 1 #modint = modint + 1
print(modint)
modint -= 1 #modint = modint - 1
print(modint)
modint *= 2 #modint = modint * 2
print(modint)
modint //= 2 #modint = modint // 2
print(modint)
modint /= 2 #modint = modint / 2
print(modint)

modint = 10
modint %= 3 #modint = modint % 3
print(modint)
modint ^= 2 #modint = modint ^ 2
print(modint)

print("3. ---------------------------------------------------------")

num_conv = 17

print(bin(num_conv))# 2진수
print(oct(num_conv))# 8진수
print(num_conv)     # 10진수
print(hex(num_conv))# 16진수

print("4. ---------------------------------------------------------")

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


print("5. ---------------------------------------------------------")

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

print("6. ---------------------------------------------------------")

test_list = [103, 'test3', [1033, 'test3-1']]

for i in range(10):
        print(i)
        
for j in test_list:
        print(j)

print("7. ---------------------------------------------------------")

test_str = 'test1 test11'

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

if 1 != 2:
        print("5yes")
else:
        print("5no")


if 0 == True:
        print("6yes")
elif 1 == True:
        print("6no")


if 1 == True:
        print("7yes")
else:
        print("7no")


if "k" in test_str:
        print("8yes")
elif "t" in test_str:
        print("8no")
else:
        print("..")


if "t" not in test_str:
        print("9yes")
else:
        print("9no")

print("8. ---------------------------------------------------------")

counter = 0
while 1:
        counter += 1
        print(counter)
        if counter == 10:
                break
        
print("9. ---------------------------------------------------------")

enumerate_list = ["hi","my","name","is","LTH"]

# 2개의 값중 첫번째 값은 인덱스(순서) 두번째 값은 값을 반환함.
for ind, val in enumerate(enumerate_list):
        print(ind, " --- ", val)


format_num = 100
# f'{}'는 문자안에 변수를 사용하고 싶을때 사용함.
print(f"this is format_number : {format_num}")

# .split("??") ??값을 기준으로 나눈후 리스트 형태로 저장함.
split_this_strings = "split this strings with space using the split func"
print(split_this_strings.split(" "))

# "??".join(!!) !!에 있는 값들을 ??를 이용해서 붙인후 문자열로 반환함.
list_to_strings = ["what","are","you","doing"]
print(" ".join(list_to_strings))
print("+".join(list_to_strings))

# map(??,!!)은 for문의 축약 형태이며 !!에 있는 각각의 값들에 ??함수를 적용함.
mapping_this_list = ["a","b","c","d","z"]
print(list(map(ord,mapping_this_list)))

# for문을 줄여 쓸수 있음.
comprehension_list = ["tail","alphabet","egg","horse","elment","error"]
result_comp_list1 = [i for i in comprehension_list]
result_comp_list2 = [i[0] for i in comprehension_list]
print(result_comp_list1)
print(result_comp_list2)


print("10. ---------------------------------------------------------")


def no_para_no_ret():
        a = 1
        print("no_para_no_ret")

def no_para_yes_ret():
        a = 1
        print("no_para_yes_ret")
        return a
        
#get_para처럼 def의 소괄호 안에 있는 값은 복사 개념으로 생각하면 됨.
def yes_para_no_ret(get_para):
        get_para += 1
        print("yes_para_no_ret")

def yes_para_yes_ret(get_para):
        get_para += 1
        print("yes_para_no_ret")
        return get_para


send_para = 50

no_para_no_ret()
receive1_return = no_para_yes_ret()
yes_para_no_ret(send_para)
receive2_return = yes_para_yes_ret(send_para)

print(receive1_return)
print(receive2_return)


print("11. ---------------------------------------------------------")

'''
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
        print(1/0)
        
except ZeroDivisionError as ex:
        print("can you divide 1 with zero?")
        print("so you can see this ZeroDivisionError")
        print("+++++++++++++++++++++++++++++++++++++")
        print(ex)
        print("+++++++++++++++++++++++++++++++++++++")
        
finally:
        print("ending")


print("12. ---------------------------------------------------------")

with open("test.txt","w") as newfile:
        for k in range(10):
                newfile.write(str(k)+str(k)+str(k)+"\n")
newfile.close()

with open("test.txt","r") as savedfile:
        print(savedfile)
        #read() 모든 값을 형태 그대로 읽어옴.
        print(savedfile.read())

with open("test.txt","r") as savedfile1:
        #readline() 한줄씩만 읽어옴.
        print(savedfile1.readline())
        print(savedfile1.readline())

with open("test.txt","r") as savedfile2:
        #readlines() 모든 줄을 각각의 형태로 리스트로 저장함.
        print(savedfile2.readlines())
savedfile.close()

print("13. ---------------------------------------------------------")

class makeclass():
  def __init__:
    print("you make this object")
    
  def printdef(self,hellow):
    print("!!printdef!!")
    print(hellow)


newobject = makeclass()
newobject.printdef("print this")
