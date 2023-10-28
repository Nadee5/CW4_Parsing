
if __name__ == '__main__':
    while True:
        print('Приветствую! Я умею искать вакансии на сайтах HeadHunter и SuperJob.')
        print('Выбери цифру, на каком ресурсе начнём искать новую работу.')
        print("1 - HH\n2 - SJ\n3 - HH и SJ")
        site = int(input())
        print("Okey, let's go")
        print("Введи ключевое слово для поиска (например, python)")
        word = (input()).lower().replace(" ", "")
        print(word)


        print("Если среди найденых вакансий не нашлось подходящего варианта, напиши 'да', и мы продолжим поиски")
        user_answer = input().lower().replace(" ", "")
        if user_answer == 'да':
            continue
        else:
            print("Я рад, что нам получилось найти достойный вариант для тебя :)")
            break

