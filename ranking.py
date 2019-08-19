for n in range(1, 1000000):
    for i in range(2, n-1):
        if n % i == 0:
            break
        elif i == n-2:
            break
            # print("%d" % n)
            # print("\nDONE!")
