from PySide6.QtCore import QSize
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import QApplication, QWidget, QPushButton
import sys

class Tela(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100,50,600,450)
        self.setWindowTitle("Botôes")
        self.create_button()


    def create_button(self):
        btn=QPushButton(self)
        btn.setText("Clique")
        btn.setGeometry(50,50,180,80)
        btn.setFont(QFont("time",25, QFont.Weight.Bold))
        btn.setStyleSheet("background-color:black; color:white")

        btn.setIcon(QIcon("img/check.png"))
        btn.setIconSize(QSize(50,50))
     





app= QApplication(sys.argv)
janela=Tela()
janela.show()
sys.exit(app.exec())