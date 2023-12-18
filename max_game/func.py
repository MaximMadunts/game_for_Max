import random


def shuffle_letters(word):
    """перемешиваем
     буквы в слове"""
    letters = [i for i in word if i != "\n"]
    random.shuffle(letters)
    shuffle_word = ''.join(letters)
    return shuffle_word


def read_words(file):
    """функция читает слова
    в файле и записывает их в список"""
    word_list = []
    for line in file:
        word = line.rstrip('\n')
        word_list.append(word)
    return word_list


def show_top_players():
    """функция показывает кол-во игр"""
    with open('history.txt', 'r', encoding='utf-8') as file:
        count_lines = len(file.readlines())
        print(f"Всего игр сыграно: {count_lines}")


def user_to_file(name, points):
    """функция добавляет
     юзера в список игроков"""
    with open('history.txt', 'a', encoding='utf-8') as file:
        file.write(f"{name} {points}\n")


def max_points():
    """ функция вывода рекорда
    по истории набранных очков"""
    with open('history.txt', 'r', encoding='utf-8') as file:
        points_list = []
        for item_data in file:
            name, points = item_data.strip().split(' ')
            points_list.append(int(points))
        return max(points_list)