 
ls = [
    ("Путин президент мира?", "нет"),
    ("Обэмэ черножопый?", "да"),
    ("Байден конч?", "да"),
    ("Данза кудуро топ?", "да")
]
answers_counter = [0,0] 

for q, a in ls:
    print(q, '[да/нет]') 
    answer = input().strip().lower()
    if answer == a:
        print("правильный ответ")
        answers_counter[0] += 1 
        answers_counter[1] += 1 
    else:
        print("неправильный ответ")
        answers_counter[0] += 1 
print("\nДано ответов: {}, Верных ответов: {}".format(answers_counter[0], answers_counter[1]))
input()
