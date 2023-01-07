from sum_op import sum_op_func


if sum_op_func(2, 2) != 3:
    raise Exception('Функция работает неверно')


print('Все тесты пройдены')