def solution(number):
    sum = 0
    for n in range(number):
        if n % 3 == 0 or n % 5 == 0:
            sum += n
        elif number < 0:
            return 0
    return sum