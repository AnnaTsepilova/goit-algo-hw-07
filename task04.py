class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    # Метод для додавання відповіді до коментаря
    def add_reply(self, reply):
        self.replies.append(reply)

    # Метод для видалення коментаря
    def remove_reply(self):
        self.text = "Цей коментар було видалено."
        self.is_deleted = True

    # Метод для рекурсивного виведення коментаря та його відповідей
    def display(self, indent=0):
        # Виводимо поточний коментар з відступами
        print(" " * indent + f"{self.author}: {self.text}")
        
        # Рекурсивно виводимо відповіді на коментар
        for reply in self.replies:
            reply.display(indent + 4)  # Збільшуємо відступ для відповідей


# Приклад використання:
root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

# Додаємо відповіді на кореневий коментар
root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

# Додаємо відповідь до першого коментаря-відповіді
reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

# Видаляємо перший коментар-відповідь
reply1.remove_reply()

# Виводимо всю ієрархію коментарів
root_comment.display()
