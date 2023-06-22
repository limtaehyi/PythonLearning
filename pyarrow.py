import arrow

# 예제 1. 현재 시간 가져오기
now = arrow.utcnow()
print("현재 시간:", now)

# 예제 2. 현재 시간을 지역 시간으로 변환
local_now = now.to('Asia/Seoul')
print("지역 시간:", local_now)

# 예제 3. 문자열에서 시간 개체 만들기
time_str = '2023-01-01 12:00:00'
dt = arrow.get(time_str, 'YYYY-MM-DD HH:mm:ss')
print("문자열에서 시간 개체:", dt)

# 예제 4. 시간 개체에서 문자열 만들기
time_str = local_now.format('YYYY-MM-DD HH:mm:ss')
print("시간 개체에서 문자열:", time_str)

# 예제 5. 시간 더하기/빼기
one_week_later = now.shift(weeks=1)
print("한 주 후:", one_week_later)

one_week_before = now.shift(weeks=-1)
print("한 주 전:", one_week_before)

# 예제 6. 두 날짜간의 차이
dt1 = arrow.get('2022-12-31 23:59:59', 'YYYY-MM-DD HH:mm:ss')
dt2 = arrow.get('2023-01-01 00:00:00', 'YYYY-MM-DD HH:mm:ss')

diff = (dt2 - dt1).total_seconds()
print("두 날짜 간의 차이(초):", diff)
