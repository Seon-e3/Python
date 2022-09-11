#Sigma
#n1 = n ^ 1, n2 = n^2, n3 = n^3

start = int(input("start : "))
end = int(input("end : "))
sum_n1 = 0
sum_n2 = 0
sum_n3 = 0

for i in range(start, end + 1):
    sum_n1 += i
    sum_n2 = i * (i + 1) * (2*i + 1) / 6
    sum_n3 = (i * (i + 1) / 2 )**2

print(f"Result sum_n1 : {sum_n1}")
print(f"Result sum_n2 : {sum_n2}")
print(f"Result sum_n3 : {sum_n3}")