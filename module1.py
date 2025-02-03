import sys
import random
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QGridLayout,
    QPushButton,
    QMessageBox,
    QRadioButton,
    QVBoxLayout,
)
from PyQt5.QtCore import Qt

from questions import questions

class ManyTest(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Тест Множества")
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.question_label = QLabel(self.questions[0]["text"])
        self.question_label.setAlignment(Qt.AlignCenter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = ManyTest()
    ex.show()
    sys.exit(app.exec_())