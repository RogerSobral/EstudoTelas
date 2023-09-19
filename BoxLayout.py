from PySide6.QtCore import QSize
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import (QApplication, QWidget, QHBoxLayout,QVBoxLayout,
                               QPushButton, QLineEdit, QLabel)
import sys

class Tela(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(100, 50, 600, 450)
        self.setWindowTitle("Box Layout")
        self.setMaximumSize(600,450)
        self.setMinimumSize(200,150)
        self.create_widgets()

#Arrumar o código
    def create_widgets(self):
        vbox=QVBoxLayout()

        hbox=QHBoxLayout()

        btn=QPushButton("Entrar")
     #   icone=QLabel()
     #   icon=QPixmap("img/icone2.png")

      #  icone.setPixmap(icon)

        login=QLineEdit()
        login.setPlaceholderText("Login")
        #hbox.addWidget(icone)
        hbox.addWidget(login)

        senha=QLineEdit()
        senha.setEchoMode(QLineEdit.EchoMode.Password)
        senha.setPlaceholderText("Senha")
        vbox.addItem(hbox)
        vbox.addWidget(senha)

        hbox.addWidget(btn)
        self.setLayout(hbox)




app = QApplication(sys.argv)
janela = Tela()
janela.show()
sys.exit(app.exec())