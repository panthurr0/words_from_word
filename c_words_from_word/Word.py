class BasicWord:
    def __init__(self, word, subwords):
        """
        Инициализация слова

        Переменные:
        word -- само слово(str)
        subwords -- подслова(list)
        """
        self.word = word
        self.subwords = subwords

    def __len__(self):
        return len(self.subwords)

    def word_isnt_subword(self, user_word):
        """
        Проверяет введенное слово в списке допустимых
        подслов (возвращает True, если слово НЕ в списке)
        """
        if user_word not in self.subwords:
            return True

    def __repr__(self):
        return f"BasicWord(word={self.word!r}, subwords={self.subwords!r})"
