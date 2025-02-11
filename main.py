import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

class InitialWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()

    def initUI(self):
        self.label = QLabel("Python | Списки")
        self.label.setStyleSheet("font-size: 18px; font: bold")
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.explanation_label = QLabel("Список (list) — это один из самых важных и часто используемых типов данных в Python. Список представляет собой упорядоченную коллекцию элементов, \nкоторые могут быть любого типа: числа, строки, другие списки и т.д. Списки являются изменяемыми, что означает, что вы можете изменять их содержимое после создания.\n"
                                        "Verify \nRun \nCopy code \nmy_list = [1, 2, 3, 'Python', True]"
                                        "\n\nСпособы создания списков: \n"
                                        "- Прямое создание списка:\n"
                                        "fruits = ['apple', 'banana', 'cherry']\n"
                                        "- Создание списка с помощью функции list():\n"
                                        "numbers = list(range(1, 6))  # [1, 2, 3, 4, 5]\n"
                                        "- Создание пустого списка: \n"
                                        "empty_list = []\n"
                                        "- Инициализация списков с помощью генераторов: \n"
                                        "\n\nОсновные операции со списками \n"
                                        "squares = [x**2 for x in range(10)]  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] \n"
                                        "- Доступ к элементам списка: Элементы списка индексируются, начиная с 0. Можно использовать отрицательные индексы для доступа к элементам с конца списка.\n"
                                        "fruits = ['apple', 'banana', 'cherry'] \nprint(fruits[0])  # apple \nprint(fruits[-1])  # cherry \n"
                                        "- Изменение элементов списка: \n"
                                        "fruits[1] = 'orange' \nprint(fruits)  # ['apple', 'orange', 'cherry'] \n"
                                        "- Срезы (slicing): Срезы позволяют получить подсписок из списка. \n"
                                        "numbers = [1, 2, 3, 4, 5] \nprint(numbers[1:3])  # [2, 3] \nprint(numbers[:3])   # [1, 2, 3] \nprint(numbers[2:])   # [3, 4, 5] \n"
                                        "- Длина списка: \n"
                                        "print(len(numbers))  # 5\n"
                                        "- Проверка наличия элемента в списке: \n"
                                        "print('apple' in fruits)  # True\n"
                                        "\n\nМетоды списков"
                                        "\n\nДобавление элементов:\n"
                                        "- append(): добавляет элемент в конец списка. \nfruits.append('grape')\n"
                                        "- insert(): вставляет элемент на определенную позицию. \nfruits.insert(1, 'kiwi')\n"
                                        "- extend(): добавляет несколько элементов в конец списка. \nfruits.extend(['mango', 'pineapple'])\n"
                                        "\n\nУдаление элементов:\n"
                                        "- remove(): удаляет первый найденный элемент. \nfruits.remove('banana')\n"
                                        "- pop(): удаляет элемент по индексу (по умолчанию последний). \nfruits.pop(1)\n"
                                        "- clear(): очищает весь список. \nfruits.clear()\n")
        self.explanation_label.setStyleSheet("font-size: 14px;")

        self.start_button = QPushButton("Проверить знания")
        self.start_button.setStyleSheet("font-size: 16px;")

        layout = QVBoxLayout()
        layout.addWidget(self.label, alignment=Qt.AlignLeft)
        layout.addWidget(self.explanation_label, alignment=Qt.AlignLeft)
        layout.addWidget(self.start_button, alignment=Qt.AlignCenter)
        self.setLayout(layout)

    def connects(self):
        self.start_button.clicked.connect(self.start_test)

    def set_appear(self):
        self.setWindowTitle("Python | Списки")
        self.resize(700, 600)
        self.move(100, 100)

    def start_test(self):
        from test import QuestionsWindow
        self.hide()
        self.questions_window = QuestionsWindow()
        self.questions_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InitialWindow()
    sys.exit(app.exec_())