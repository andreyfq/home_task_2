cub_list = [el ** 3 for el in list(range(1, 1001, 2))]
sum_cubes = 0
print('Id cub_list:', id(cub_list))
for i in cub_list:
    i += 17
    sum_dig = 0
    i_copy = i
    while i > 0:
        sum_dig += i % 10
        i //= 10
    if sum_dig % 7 == 0:
            sum_cubes += i_copy
print(f'Result, id: {sum_cubes} {id(sum_cubes)}')

'''
В первый раз ошибся что не создал копию переменной 
и не догодался вынести обнуление за цикл 
с вычелсением десятков и списком проблем не возникло 
'''