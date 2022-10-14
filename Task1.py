# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и выводит название этого дня недели.
# 6 –> да
# 7 –> да
# 1 –> нет

def get_int_number(): return int(input())

def is_weekend(n: int):
    """
    Проверить, является ли номер дня выходным"
    :param n: int
    :return: bool
    >>> is_weekend(1)
    False
    >>> is_weekend(2)
    False
    >>> is_weekend(3)
    False
    >>> is_weekend(4)
    False
    >>> is_weekend(5)
    False
    >>> is_weekend(6)
    True
    >>> is_weekend(7)
    True
    """

    assert 0 < n < 8, "Введите номер дня в диапазоне от 1 до 7: " + str(n)
    if n in (6, 7):
        return True
    else: # n in [1:5]
        return False

def print_result(day: int):
    """
    print 'да', если этот день является выходным print 'нет'
    :param day: int
    :return: None
    >>> print_result(1)
    нет
    >>> print_result(2)
    нет
    >>> print_result(3)
    нет
    >>> print_result(4)
    нет
    >>> print_result(5)
    нет
    >>> print_result(6)
    да
    >>> print_result(7)
    да
    """
    if is_weekend(day):
        print('да')
    else:
        print('нет')

def main():
    import doctest
    # doctest.testmod()

    day = -1
    while day < 1 or day > 7:
        print('Введите номер дня:')
        try:
            day = get_int_number()
        except Exception:
            print('Пожалуйста, введите номер от 1 до 7')

    print_result(day)

if __name__ == '__main__':
    main()                                    