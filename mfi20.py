import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QGridLayout,
    QRadioButton,
    QButtonGroup,
    QPushButton,
    QMessageBox,
)


class MFI20(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Шкала оценки астении МFI-20")
        self.questions = [
            "Я чувствую себя измотанным, как будто у меня нет сил.",
            "Я чувствую себя очень утомленным, даже если я не делал ничего особенного.",
            "У меня нет сил, чтобы начать что-то делать.",
            "Я легко устаю.",
            "Я чувствую себя уставшим, когда встаю утром.",
            "Я легко раздражаюсь, когда я устаю.",
            "Я испытываю трудности с концентрацией.",
            "Мне трудно думать ясно.",
            "У меня проблемы с памятью.",
            "Я чувствую себя беспокойным, когда я устаю.",
            "Я чувствую себя подавленным, когда я устаю.",
            "Я чувствую себя тревожным, когда я устаю.",
            "У меня проблемы со сном.",
            "Я просыпаюсь утром чувствуя себя невыспавшимся.",
            "Я чувствую себя сонным в течение дня.",
            "Я чувствую себя вялым.",
            "У меня нет энергии.",
            "Я чувствую себя слабым.",
            "Я чувствую себя истощенным.",
            "Я чувствую себя немощным.",
        ]

        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.radio_groups = []
        for i, question in enumerate(self.questions):
            label = QLabel(question)
            self.grid.addWidget(label, i, 0)

            group = QButtonGroup()
            radio_buttons = [
                QRadioButton("Никогда"),
                QRadioButton("Иногда"),
                QRadioButton("Часто"),
                QRadioButton("Всегда"),
            ]
            for j, button in enumerate(radio_buttons):
                group.addButton(button)
                but = len(radio_buttons)
                self.grid.addWidget(button, i, j + 1)
            self.radio_groups.append(group)

        self.submit_button = QPushButton("Отправить")
        self.submit_button.clicked.connect(self.submit_results)
        self.grid.addWidget(self.submit_button, len(self.questions), 0, 1, 5)
    def next_question(self):
        if not any(button.isChecked() for button in self.radio_buttons):
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, выберите ответ на текущий вопрос.")
            return
    def timer_final(self):
       global time
       time = QTime(0,1,0)
       self.timer = QTimer()
       self.timer.timeout.connect(self.timer3Event)
       self.timer.start(1000)
    def timer3Event(self):
       global time
       time = time.addSecs(-1)
       self.text_timer.setText(time.toString("hh:mm:ss"))
       self.text_timer.setFont(QFont("Times", 26, QFont.Bold))
       if int(time.toString("hh:mm:ss")[6:8]) <= 15:
           self.text_timer.setStyleSheet("color: rgb(0,255,0)")
       elif int(time.toString("hh:mm:ss")[6:8]) >= 45:
           self.text_timer.setStyleSheet("color: rgb(0,255,0)")
       else:
           self.text_timer.setStyleSheet("color: rgb(0,0,0)")
       if time.toString("hh:mm:ss") == "00:00:00":
           self.timer.stop()


    def submit_results(self):
        score = 0
        for group in self.radio_groups:
            checked_button = group.checkedButton()
            if checked_button:
                score += group.id(checked_button)
        QMessageBox.information(self, "Результаты", f"Ваш балл по МFI-20: {score}\n{items_select}")
        if score >= -30:
            level = "Астения отсутствует"
        elif score >= -50:
            level = "Легкая астения"
        elif score >= -70:
            level = "Умеренная астения"
        elif score >= -90:
            level = "Тяжелая астения"

        QMessageBox.information(
            self,
            "Результаты",
            f"Ваш балл по МFI-20: {score}\n\nУровень астении: {level}\n\n"
            "Рекомендуется обратиться к врачу для получения консультации.",
        )
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mfi20 = MFI20()
    mfi20.show()
    sys.exit(app.exec_())