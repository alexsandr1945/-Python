import data_structures
def is_braces_sequence_correct(s:str):
    """
    Проверяет корректность скобочной последовательности из круглых и квадратных скобок

    >>> is_braces_sequence_correct("(([()]))[]")
    True
    >>> is_braces_sequence_correct("([)]")
    False
    >>> is_braces_sequence_correct("(")
    False
    >>> is_braces_sequence_correct("]")
    False

    :return: 
    """


    for brace in s:
        if brace not in "()[]": # Проверяем на наличие лишних символов
            continue
        if brace in '([':
            data_structures.push(brace)
        else:
            assert brace in ')]', 'Ожидалась закрывающая скобка ' + str(brace)
            if data_structures.is_empty():
                return False
            left = data_structures.pop()
            assert left in '([','Ожидалась закрывающая скобка ' + str(brace)
            if left == '(':
                right = ')'
            elif left == '[':
                right = ']'
            if right != brace:
                return False
    return  data_structures.is_empty()
    #return  True


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)