import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QTextEdit
from connect_chat_bot import chat_with_ai, close_link

class MyWindow(QWidget):
    app = QApplication([])

    layout = QVBoxLayout()

    previous_chat = QTextEdit()
    line_edit = QLineEdit()

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Chat with deepai.org')
        self.resize(1900, 1000)

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



    # Handle Input and give response
    def handle_return_pressed(self):
        input_from_user = self.line_edit.text()
        self.previous_chat.append("\t\t\t\t\t\t\t\t\t\t\t\tUInput: " + input_from_user)
        self.line_edit.clear()

        response_from_ai = chat_with_ai(input_from_user)
        self.previous_chat.append("\nResponse: " + response_from_ai)

def run_app():
    main_window = MyWindow()
    main_window.show()
    main_window.app.exec_()
    close_link()
    sys.exit(0)
