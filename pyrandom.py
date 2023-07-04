import random

# 무작위 실수 생성
rand_float = random.random()
print("Random float between 0 and 1:", rand_float)

rand_float_range = random.uniform(1, 10)
print("Random float between 1 and 10:", rand_float_range)

# 무작위 정수 생성
rand_integer = random.randint(1, 100)
print("Random integer between 1 and 100:", rand_integer)

rand_integer_range = random.randrange(1, 100, 5)
print("Random integer between 1 and 100, multiple of 5:", rand_integer_range)

# 시퀀스에서 무작위 선택
choices = ['apple', 'banana', 'cherry', 'orange']

rand_choice = random.choice(choices)
print("Random choice from list:", rand_choice)

rand_sample = random.sample(choices, 2)
print("Random sample of 2 items from list:", rand_sample)

# 시퀀스 섞기
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(numbers)
print("Shuffled list:", numbers)

# 가중치 적용
choices = ['A', 'B', 'C', 'D', 'E']
weights = [0.1, 0.2, 0.5, 0.15, 0.05]
rand_choice_weighted = random.choices(choices, weights, k=3)
print("Weighted random selection from list:", rand_choice_weighted)
