import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

class FinalWindow(QWidget):
    def __init__(self, score, total, elapsed_time):
        super().__init__()
        self.score = score
        self.total = total
        self.elapsed_time = elapsed_time 
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Итоги теста") 
        self.resize(300, 200)
        layout = QVBoxLayout()
        

        result_label = QLabel(f"Вы ответили правильно на {self.score} из {self.total} вопросов.")
        
        time_label = QLabel(f"Время прохождения: {self.elapsed_time}")  
        
        layout.addWidget(result_label)
        layout.addWidget(time_label)
        
        exit_button = QPushButton("Закрыть")
        exit_button.clicked.connect(self.close)
        layout.addWidget(exit_button)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    score = 3 
    total = 5 
    elapsed_time = "00:00:00" 
    final_window = FinalWindow(score, total, elapsed_time)
    final_window.show()
    sys.exit(app.exec_())