n = int(input("Input N (range is (0; 27)):"))
if n>0 and n<27:
    for i in range(100, 1000, 1):
        if ((i // 100 + (i % 100) // 10 + i % 10) == n):
            print(str(i))
else:
    print("N must be grower than 0 and lower than 27!")
k = input()