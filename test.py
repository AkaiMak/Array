
import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QRadioButton, QPushButton
from PyQt5.QtCore import QTimer
from final import FinalWindow 

class QuestionsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.current_question = 0
        self.score = 0
        self.start_time = time.time()  
        self.timer = QTimer(self)  
        self.timer.timeout.connect(self.update_timer)  
        self.timer.start(1000)  
        self.questions = [
            {
                "question": "1. Что такое список в Python?",
                "options": [
                    "Неупорядоченная коллекция элементов.",
                    "Упорядоченная коллекция элементов, которая может содержать элементы разных типов.",
                    "Коллекция элементов, которая не может быть изменена после создания.",
                    "Коллекция элементов, которая может содержать только числа."
                ],
                "answer": 1 
            },
            {
                "question": "2. Какой метод добавляет элемент в конец списка?",
                "options": [
                    "insert()",
                    "append()",
                    "extend()",
                    "add()"
                ],
                "answer": 1
            },
            {
                "question": "3. Какой метод удаляет элемент по индексу?",
                "options": [
                    "remove()",
                    "delete()",
                    "pop()",
                    "clear()"
                ],
                "answer": 2
            },
            {
                "question": "4. Какой метод возвращает индекс первого найденного элемента в списке?",
                "options": [
                    "find()",
                    "index()",
                    "search()",
                    "locate()"
                ],
                "answer": 1
            },
            {
                "question": "5. Какой метод сортирует список по возрастанию?",
                "options": [
                    "sort()",
                    "order()",
                    "sorted()",
                    "arrange()"
                ],
                "answer": 0
            },
            {
                "question": "6. Какой метод очищает весь список?",
                "options": [
                    "delete()",
                    "remove()",
                    "clear()",
                    "empty()"
                ],
                "answer": 2
            },
            {
                "question": "7. Какой оператор используется для проверки наличия элемента в списке?",
                "options": [
                    "in",
                    "contains",
                    "has",
                    "exist"
                ],
                "answer": 0
            },
            {
                "question": "8. Какой метод добавляет несколько элементов в конец списка?",
                "options": [
                    "append()",
                    "insert()",
                    "extend()",
                    "add_all()"
                ],
                "answer": 2
            },
            {
                "question": "9. Какой метод переворачивает список?",
                "options": [
                    "reverse()",
                    "flip()",
                    "rotate()",
                    "invert()"
                ],
                "answer": 0
            },
            {
                "question": "10. Какой метод возвращает количество вхождений элемента в списке?",
                "options": [
                    "count()",
                    "occurrences()",
                    "find_all()",
                    "total()"
                ],
                "answer": 0
            }
        ]
        self.show_question()

    def initUI(self):
        self.setWindowTitle("Тест по теории списков")
        self.resize(400, 300)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.timer_label = QLabel("Время: 00:00:00")
        self.layout.addWidget(self.timer_label)

    def show_question(self):
        self.clear_layout()  
        self.layout.addWidget(self.timer_label) 
        self.layout.addWidget(QLabel(self.questions[self.current_question]["question"]))
        self.radio_buttons = []
        for i, option in enumerate(self.questions[self.current_question]["options"]):
            radio_button = QRadioButton(option)
            self.radio_buttons.append(radio_button)
            self.layout.addWidget(radio_button)
        self.submit_button = QPushButton("Ответить")
        self.submit_button.clicked.connect(self.check_answer)
        self.layout.addWidget(self.submit_button)

    def check_answer(self):
        selected_option = next((i for i, rb in enumerate(self.radio_buttons) if rb.isChecked()), None)
        if selected_option is not None:
            if selected_option == self.questions[self.current_question]["answer"]:
                self.score += 1
            self.current_question += 1
            if self.current_question < len(self.questions):
                self.show_question() 
            else:
                self.show_result()

    def clear_layout(self):
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget is not None and widget != self.timer_label:
                widget.deleteLater()

    def update_timer(self):
        elapsed_time = time.time() - self.start_time 
        hours = int(elapsed_time // 3600)
        minutes = int((elapsed_time % 3600) // 60)
        seconds = int(elapsed_time % 60)
        formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"  
        self.timer_label.setText(f"Время: {formatted_time}") 

    def show_result(self):
        self.timer.stop()  
        elapsed_time = time.time() - self.start_time  
        hours = int(elapsed_time // 3600)
        minutes = int((elapsed_time % 3600) // 60)
        seconds = int(elapsed_time % 60)
        formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"  
        # self.clear_layout()
        self.hide()
        

        self.final_window = FinalWindow(self.score, len(self.questions), formatted_time) 
        self.final_window.show()
         

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QuestionsWindow()
    window.show()
    sys.exit(app.exec_())