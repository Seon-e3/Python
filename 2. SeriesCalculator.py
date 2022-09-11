number = int(input("밑을 입력하세요> "))
exponent = int(input("지수를 입력하세요> "))
result = list()

for i in range(1, exponent + 1):
    print(int(number), "^", i, "=", int(number)**i)
    result.append(int(number)**i)

sum = 0

for num in result:
    sum += num

print(f"거듭제곱의 합은 : {sum}")




