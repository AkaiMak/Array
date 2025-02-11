import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QScrollArea,  # Import QScrollArea
)
from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtCore import Qt
from mfi20 import *  # Import the MFI20 class from another file

class Welcome(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(940, 780)  # Adjusted height for better viewing
        self.setWindowTitle("Множества в Python")

        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(220, 230, 240))  # Light grayish-blue
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        # Title Label
        self.title_label = QLabel("Множества в Python")
        title_font = QFont("Arial", 18, QFont.Bold)  # Set font and style
        self.title_label.setFont(title_font)
        self.title_label.setAlignment(Qt.AlignCenter)  # Center the title

        # Theory Text
        self.theory_label = QLabel(
            "Класс set (множество) — это одна из ключевых структур данных в Python.\n\n"
            "   Оно представляет собой неупорядоченную коллекцию уникальных элементов. "
            "Класс set, в некоторой степени, соответствует математическому множеству. "
            "Многие широко используемые математические операции, применимые к множествам, существуют и в Python. "
            "Часто вычисления, производимые над множествами, оказываются гораздо быстрее, чем альтернативные операции со списками. \n\n"
            "   Создать объект set в Python можно двумя путями: \n\n"
            "   1.    Использовать фигурные скобки {} \n\n"
            "   2.    Использовать встроенную функцию set() \n\n"
            "Множество создается при размещении всех элементов внутри фигурных скобок {}, как показано на примере ниже. \n\n"
            "   s1 = {}  # Это создаст пустое множество \n\n"
            "   s2 = {1, 'pythonru', 20.67} \n\n"
            "Еще один способ создать (или определить) множество Python — использовать функцию set(). Пример ниже. \n\n"
            "   s1 = set()  # Это создаст пустое множество \n\n"
            "   s2 = set({1, 'pythonru', 20.67}) \n\n"
            "Нет ограничений на количество элементов в объекте set, но запрещено добавлять элементы изменяемых типов, такие как список или словарь. "
            "Если попробовать добавить список (с набором элементов), интерпретатор выдаст ошибку. \n\n"
            "Добавление элементов в множества Python \n\n"
            "Объекты set в Python поддерживают добавление элементов двумя путями: по одному с помощью метода add() или группами с помощью update(). Оба описаны дальше. \n\n"
            "Один элемент можно добавить с помощью метода add(). Такой код выглядит следующим образом: \n\n"
            "   set1 = {1, 3, 4} \n"
            "   set1.add(2) \n"
            "   print(set1) \n"
            "   {1, 2, 3, 4} \n\n"
            "Добавление нескольких элементов в множество Python \n\n"
            "Больше одного элемента можно добавить с помощью update(). Код следующий:\n\n"
            "   set2 = {1, 2, 3} \n"
            "   set2.update([4, 5, 6]) \n"
            "   print(set2)  #  {1, 2, 3, 4, 5, 6} \n\n"
            "Удаление элементов из множеств Python \n\n"
            "Один или несколько элементов можно удалить из объекта set с помощью следующих методов. Их отличие в виде возвращаемого значения. \n\n"
            "   remove()\n\n"
            "   discard()\n\n"
            "   pop()\n\n"
            "   remove()\n\n"
            "Метод remove() полезен в тех случаях, когда нужно удалить из множества конкретный элемент и вернуть ошибку в том случае, если его нет в объекте. "
            "Следующий код показывает метод remove() в действии. \n\n"
            "   set1 = {1, 2, 3, 4, 'a', 'p'} \n"
            "   set1.remove(2) \n"
            "   ['__and__', '__class__', '__contains__', '__delattr'"  # Truncated for brevity
        )
        self.theory_label.setWordWrap(True)

        # Scroll Area
        scroll_area = QScrollArea()  # Create QScrollArea
        scroll_area.setWidgetResizable(True)  # Make scroll area resizable
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)
        scroll_layout.addWidget(self.theory_label)
        scroll_widget.setLayout(scroll_layout)
        scroll_area.setWidget(scroll_widget)  # Add widget to scroll area

        # Start Button
        self.start_button = QPushButton("Начать тест")
        self.start_button.clicked.connect(self.open_test_form)
        button_font = QFont("Arial", 12, QFont.Bold)  # Font for the button
        self.start_button.setFont(button_font)

        # Main Layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.title_label)  # Add the title
        main_layout.addWidget(scroll_area)  # Add the scroll area
        main_layout.addWidget(self.start_button)
        self.setLayout(main_layout)

    def open_test_form(self):
        # Import the test form file
        self.test_form = MFI20()
        self.test_form.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    welcome = Welcome()
    welcome.show()
    sys.exit(app.exec_())
