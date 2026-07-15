def number_to_day(num=100):
    if num == 0:
        day='今日'
    elif num == 1:
        day='明日'
    elif num==-1:
        day='昨日'
    else :
        day='今日より1日を超えて離れた日'
    return day

print(number_to_day(0))
print(number_to_day(1))
print(number_to_day(-1))
print(number_to_day(10))
