numbers = list(map(int, input().split()))
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(max_num)
