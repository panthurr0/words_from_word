class Player:
    def __init__(self, name):
        """
        Инициализация игрока

        Переменные:
        name -- имя игрока (str)
        player_answers -- ответы игрока(list)

        """
        self.name = name
        self.player_answers = []

    def __len__(self):
        return len(self.player_answers)

    def add_answer(self, answer):
        """
        Добавляет ответ в player_answers
        """
        self.player_answers.append(answer)

    def word_usage(self, answer):
        """
        Проверка использования слова до этого
        """
        return answer in self.player_answers

    def __repr__(self):
        return f"Player(name={self.name!r}, player_answers={self.player_answers!r})"
