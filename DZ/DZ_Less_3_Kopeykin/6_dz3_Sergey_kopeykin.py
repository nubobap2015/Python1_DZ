# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово
# должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().


# из разряда "THE BEST"
int_func = lambda a_text: str(a_text).capitalize()


def int_func2(a_text):
    if len(a_text) > 0:
        return str(a_text[0]).upper() + a_text[1:]
    else:
        return ''


# a_string = input('Тут нужна строка из слов, разделенных пробелом: ')

a_string = 'тут нужна строка из слов, разделенных пробелом:    ff'
a_string2 = ''
for item in a_string.split(' '):
    a_string2 += int_func(item) + ' '
print(a_string)
print(a_string2[:-1])
