for i in range (0,21):
    last_digit = i % 10
    if i != 11 and last_digit == 1:
        print(f'{i} процент')
    elif i != 12 and i != 13 and i != 14 and last_digit >= 2 and i % 10 <= 4:
        print(f'{i} процента')
    else:
        print(f'{i} процентов')

"""
В этой задаче все оказалось совсем элементарно,в первый раз честно говоря даже не думал (испугался звездочки)
"""