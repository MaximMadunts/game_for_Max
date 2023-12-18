import os

from func import read_words, shuffle_letters, show_top_players, user_to_file, max_points

points = 0

name = input("Введите ваше имя: ")

with open('words.txt', 'rt', encoding='utf-8') as file:
    word_list = read_words(file)

# перебираем слова в списке и опредеяем рекорд

for word in word_list:
    i = shuffle_letters(word)
    print(f"Угадайте слово: {i}")
    user_answer = input().lower().strip()
    if user_answer == word.lower().strip():
        points += 10
        print(f"Верно! Вы получаете 10 очков.")
    else:
        print(f"Неверно! Верный ответ – {word}")
print()
print(f"{name} вы набрали {points} очков")
print()
user_to_file(name, points)
show_top_players()
print(f"Максимальный рекорд: {max_points()}")

os.startfile(r'C:\Users\maxim\PycharmProjects\max_game\Queen.mp3')



