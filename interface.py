import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QTextEdit

app = QApplication([])
#_______________________________________________

class MyWindow(QWidget):
    layout = QVBoxLayout()

    previous_chat =QTextEdit()
    line_edit = QLineEdit()

    def __init__(self):
        super().__init__()
        self.setWindowTitle('My chat room')
        self.resize(800, 800)

        # UInput
        self.line_edit.setPlaceholderText("Type something and press Enter")
        self.line_edit.returnPressed.connect(self.handle_return_pressed)
        self.line_edit.setFont(QFont("Arial", 16))

        #Chat-log
        self.previous_chat.setReadOnly(True)
        self.previous_chat.setFont(QFont("Arial", 16))

        #Layout
        self.layout.addWidget(self.previous_chat)
        self.layout.addWidget(self.line_edit)
        self.setLayout(self.layout)



    # Handle Input
    def handle_return_pressed(self):
        text = self.line_edit.text()
        print(f"You typed: {text}")
        self.previous_chat.append("\t\t\tU: " + text)
        self.line_edit.clear()



def run_app():
    main_window = MyWindow()
    main_window.show()
    sys.exit(app.exec_())