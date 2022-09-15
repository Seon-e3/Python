Collatz_number = list()

number = int(input("숫자를 입력하세요 : "))


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

print(Collatz_number)