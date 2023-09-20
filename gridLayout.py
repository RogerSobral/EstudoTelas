
from PySide6.QtWidgets import (QApplication, QWidget, QGridLayout,
                               QPushButton, QLabel)
import sys

class Tela(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(100, 50, 600, 450)
        self.setWindowTitle("Box Layout")

        self.create_widgets()

    def create_widgets(self):
        btn=QPushButton("Mudar o Texto")
        btn_voltar=QPushButton("Voltar o Texto")

        self.texto_inicial="Esse é o texto inicial"
        self.lb_mensagem=QLabel(self.texto_inicial)
        btn.clicked.connect(self.cliked_label)
        btn_voltar.clicked.connect(self.cliked_back)


#O Grid trabalha por posições dos widget:
#|0,0 | 0,1 | 0,2 |
#|1,0 | 1,1 | 1,2 |
#|2,0 | 2,1 | 2,2 |
#|3,0 | 3,1 | 3,2 |

        grid=QGridLayout()
        grid.addWidget(btn,0,0)
        grid.addWidget(btn_voltar,1,0)
        grid.addWidget(self.lb_mensagem,0,1)

        self.setLayout(grid)

    #metodo para mudar o texto da label
    def cliked_label(self):
        self.lb_mensagem.setText("O texto Mudou!")


    def cliked_back(self):
        self.lb_mensagem.setText(self.texto_inicial)




app = QApplication(sys.argv)
janela = Tela()
janela.show()
sys.exit(app.exec())