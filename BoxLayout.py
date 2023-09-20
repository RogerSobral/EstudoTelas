
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import (QApplication, QWidget, QHBoxLayout,QVBoxLayout,
                               QPushButton, QLineEdit, QLabel)
import sys

class Tela(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(100, 50, 600, 450)
        self.setWindowTitle("Box Layout")
        self.create_widgets()

#Arrumar o código
    def create_widgets(self):
        vbox=QVBoxLayout()

        imagem=QPixmap("img/fundo_tratado_novo.png")
        print(imagem.size())
        label_img=QLabel()
        label_img.setPixmap(imagem)
        label_img.setAlignment(Qt.AlignmentFlag.AlignCenter)


        btn=QPushButton("Entrar")

        login=QLineEdit()
        login.setPlaceholderText("Login")
        #hbox.addWidget(icone)
        vbox.addWidget(label_img)
        vbox.addWidget(login)

        senha=QLineEdit()
        senha.setEchoMode(QLineEdit.EchoMode.Password)
        senha.setPlaceholderText("Senha")

        vbox.addWidget(senha)
        vbox.addWidget(btn)

        self.setLayout(vbox)




app = QApplication(sys.argv)
janela = Tela()
janela.show()
sys.exit(app.exec())