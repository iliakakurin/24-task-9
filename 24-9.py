N = int(input())
summa = 1
while N > 0:
    d = N % 10
    N = N // 10
    summa = summa + 1
print(summa)
