import requests
from random import choice
from Word import BasicWord


def get_json():
    """
    Возвращает json-файл
    """
    response = requests.get("https://www.jsonkeeper.com/b/98ML")
    response_json = response.json()
    return response_json


def load_random_word():
    """
    Достает случайное слово из response_json, затем создает из него экземпляр BasicWord
    """
    json_word = choice(get_json())
    full_word = json_word["word"]  # переменная full_word для слова
    all_subwords = json_word["subwords"]  # переменная all_subwords для подслов
    word = BasicWord(full_word, all_subwords)
    return word
