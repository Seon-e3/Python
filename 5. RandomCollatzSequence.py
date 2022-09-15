import random
import os

Collatz_number = list()

number = int(random.randint(1,9999))

os.system("cls")
#if문 사용해서 코드짜기 
if number % 2 == 0:
    Collatz_number.append(number / 2)
else:
    Collatz_number.append(3 * number + 1)

for num in Collatz_number:
    if num == 1:
        break
    else:
        if num % 2 == 0:
            Collatz_number.append(num / 2)
        else:
            Collatz_number.append(3 * num + 1)

print("*" * 194)
print(f"시작하는 수는 {number} 입니다.")
print(Collatz_number)
print("*" * 194)