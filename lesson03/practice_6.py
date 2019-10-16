# 6) Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной
#    первой буквой. Например, print(int_func(‘text’)) -> Text.
#    Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово
#    состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с
#    заглавной буквы. Необходимо использовать написанную ранее функцию int_func().


def int_func(str_from_user):
    str_change = ''
    for idx_char in range(len(str_from_user)):
        str_change += str_from_user[idx_char].upper() if idx_char == 0 else str_from_user[idx_char]

    return str_change


is_end = False

while is_end is False:
    words_chunk = input("Вводите несколькие словы с провелом ('*' завершит программу) : ")
    list_words = words_chunk.split()
    for word in list_words:
        if word == '*':
            is_end = True
            break
        print(int_func(word))
