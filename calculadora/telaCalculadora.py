import typing

from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap, QPainter, QColor
from PyQt6.QtWidgets import (QApplication, QWidget, QHBoxLayout,
                             QVBoxLayout,QLabel, QLineEdit, QPushButton)
import sys



class JanelaLogin(QWidget):

    formatacao_botao="""
    QPushButton{
     background-color:#BF459F;
        height:30px;
        border-radius: 10px;
        padding: 2px 4px;
        margin:15px
    }
    
    QPushButton:hover{
     background-color:#F23D7F;
        height:30px;
        border-radius: 10px;
        padding: 2px 4px;
    }
    """

    fortacao_input="""QLineEdit{
        background-color:#BF459F;
        width: 180px;
        height:30px;
        border-radius: 10px;
        padding: 2px 4px;
       
       }
       
       QLineEdit:focus {
        color: rgb(127, 0, 63);
        selection-color: white;   
        border-radius: 10px;
        padding: 2px 4px;
       
       }

    QLineEdit:edit-focus {
       color: rgb(127, 0, 63);
       selection-color: white;  
       border-radius: 10px;
       padding: 2px 4px;
      
}
        """
    def __init__(self):
        super(JanelaLogin, self).__init__()
        self.setWindowTitle("Login")
        self.setMaximumSize(450,500)
        self.setMinimumSize(450,500)
        self.widget_padrao()
        self.setStyleSheet("""
        background-color:#080C26;
        color:#FFFFFF;
        
        """)



    def widget_padrao(self):
        fonte_texto=QFont("roboto",14,weight=600)
        fonte_btn = QFont("roboto", 18, weight=800)
        font_input=QFont("roboto",14,weight=300)

        #Imagem topo
        imagem=QPixmap("img/calculadora.png")

        label_img=QLabel()
        label_img.setPixmap(imagem)
        label_img.setAlignment(Qt.AlignmentFlag.AlignCenter)


        #Linha 1
        linha1=QHBoxLayout()
        img_nome= QPixmap("img/nome.png")
        icon_nome=QLabel()
        icon_nome.setPixmap(img_nome)
        nome=QLabel()
        nome.setText("Nome")
        nome.setMargin(23)
        nome.setFont(fonte_texto)

        linha1.addWidget(icon_nome)
        linha1.addWidget(nome)
        self.input_nome=QLineEdit()
        self.input_nome.setStyleSheet(JanelaLogin.fortacao_input)
        self.input_nome.setFont(font_input)


        linha1.addWidget(self.input_nome)


        #Linha 2
        senha=QLabel("Senha")
        senha.setFont(fonte_texto)
        senha.setMargin(22)

        img_senha = QPixmap("img/trancar.png")
        icon_senha = QLabel()
        icon_senha.setPixmap(img_senha)

        self.input_senha=QLineEdit()
        self.input_senha.setStyleSheet(JanelaLogin.fortacao_input)
        self.input_senha.setFont(font_input)

        linha2=QHBoxLayout()
        linha2.addWidget(icon_senha)
        linha2.addWidget(senha)
        linha2.addWidget(self.input_senha)


        #Criando o Botão
        btn_entrar=QPushButton()
        btn_entrar.setText("Entrar")
        btn_entrar.setFont(fonte_btn)

        btn_entrar.setStyleSheet(JanelaLogin.formatacao_botao)
        btn_entrar.clicked.connect(self.chamarCalculadora)
        #Add elementos ao layout principal
        corpo=QVBoxLayout()
        corpo.addWidget(label_img)
        corpo.addItem(linha1)
        corpo.addItem(linha2)
        corpo.addWidget(btn_entrar)

        self.setLayout(corpo)

    def chamarCalculadora(self):

        nome=self.input_nome.text()
        senha=self.input_senha.text()
        if nome in ["carlos", "maria"] and senha == "123":
            print("Entrou no sistema")





class JanelaCalculadora(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")
        self.setMaximumSize(500,600)


app=QApplication(sys.argv)
tela=JanelaLogin()
tela.show()
sys.exit(app.exec())