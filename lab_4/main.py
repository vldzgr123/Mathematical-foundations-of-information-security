from os import system


def clear():
    system("cls||clear")

p=None
q=None
clear()
while True:
    print("1.Генерация ключей")
    print("2.Получить частоты k-граммы")
    print("3.Вычислить энтропию k-граммы")
    print("4.Вычислить Hk(T)/k для k от 1 до n и вывести график зависимости Hk(T)/k от k")
    print("5.Выход")
    match (int(input())):
        case 1:
            clear()
            p = int(input("Введите p: ")) 
            q = int(input("Введите q: "))
            
            input()
        case 2:
            clear()
            k = int(input("Введите k: "))
            text = input("Введите текст: ")
            print(calculate_frequency_kgram(text=text, k=k))
            input()
        case 3:
            clear()
            k = int(input("Введите k: "))
            text = input("Введите текст: ")
            print(calculate_entropy_kgrams(text=text, k=k))
            input()
        case 4:
            clear()
            k = int(input("Введите n: "))
            text = input("Введите текст: ")
            plot_entropy_vs_k(text, k)
            input()
            break
        case 5:
            break
        case _:
            break
    clear()

#Я был разбужен спозаранку Щелчком оконного стекла. Размокшей каменной баранкой В воде Венеция плыла. Все было тихо, и, однако, Во сне я слышал крик, и он Подобьем смолкнувшего знака Еще тревожил небосклон.