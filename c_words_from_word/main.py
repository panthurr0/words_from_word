from utilis import load_random_word
from Player import Player

string = load_random_word()  # берет экземпляр из Utilis.py


def main():
    user_input = input("Введите ваше имя ")
    player = Player(user_input)  # делает экземпляр игрока
    print(f"Привет, {player.name}!")
    print(f"Составьте {len(string)} слов из слова {string.word}")
    print("Слова должны состоять из 3 или 4 букв")
    print('Чтобы закончить игру, угадайте все слова или напишите "stop"')
    print("Поехали, ваше первое слово?\n")

    count = 0
    while count != len(string):
        count += 1
        user_string = input("").lower()

        if user_string in ("stop", "стоп"):
            break
        elif len(user_string) < 3:
            print("Слишком короткое слово\n")
        elif len(user_string) > 4:
            print("Слишком длинное слово\n")
        elif string.word_isnt_subword(user_string):
            print("Неверно\n")
        elif player.word_usage(user_string):
            print("Уже использовано\n")

        else:
            player.add_answer(user_string)
            print("Верно\n\n")

    print(f"Игра завершена, вы угадали {len(player)} слов")


if __name__ == "__main__":
    main()
