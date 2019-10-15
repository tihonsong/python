# 2) Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
#    город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
#    данных о пользователе одной строкой.


def make_string(**kwargs):
    string = ""
    by_russian = {"name": "имя", "family": "фамилия", "birth_year": "год рождения",
                  "city": "город проживания", "email": "email", "tel": "телефон"}
    for key, val in kwargs.items():
        string += f"{by_russian[key]}:{val},"
    return string[:-1]


print(make_string(name=input("имя :"), family=input("фамилия: "), birth_year=input("год рождения: "),
                  city=input("город проживания: "), email=input("email: "), tel=input("телефон :")))
