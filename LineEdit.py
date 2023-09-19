from PySide6.QtCore import QSize
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit
import sys


class Tela(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 50, 600, 450)
        self.setWindowTitle("LineEdit")
        self.setMaximumSize(600,450)
        self.setMinimumSize(200,150)

        self.creat_line_edit()

    def creat_line_edit(self):
        line_edit=QLineEdit(self)
        line_edit.setFont(QFont("Sanserif",15))
        line_edit.setPlaceholderText("Digite a sua senha")
        line_edit.setEchoMode(QLineEdit.EchoMode.Password)








app= QApplication(sys.argv)
janela=Tela()
janela.show()
sys.exit(app.exec())