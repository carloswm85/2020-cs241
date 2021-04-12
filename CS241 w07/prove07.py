# 0,
# 1, 1, 2, 3, 5,
# 8, 13, 21, 34, 55,
# 89, 144, 233, 377, 610,
# 987, 1597, 2584, 4181, 6765,
# 10946, 17711, 28657, 46368, 75025,
# 121393, 196418, 317811, ...


def fib(n):
    if n < 1:
        return 0
    if n == 1:
        return 1

    return fib(n-2) + fib(n-1)


def main():
    q = True

    while q:
        num = int(input('Enter a Fibonacci index: '))
        num = fib(num)
        print('The Fibonacci number is: {}'.format(num))


if __name__ == '__main__':
    main()
