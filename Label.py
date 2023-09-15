from PySide6.QtWidgets import QApplication, QWidget, QLabel
import sys

class Janela(QWidget):
    def __init__(self):
        super(Janela, self).__init__()
        self.setWindowTitle("Estudo de Labels")
        self.setStyleSheet("backgroud-color:#A2A637")
        label = QLabel(self)
        label.setText("Texto no app")
        label.move(20,34) # Move a label

        label.resize(150, 40)# Redefine o tamanho da label
        label.setStyleSheet("background-color: black; color:white")

        label2=QLabel(self)
        label2.setText("TEXTO 2")
        label2.setGeometry(20,0,100,30)
        label2.setMargin(20)
        #label2.hide() Esconde a Label
        #label2.clear() # Limpa o conteudo

        "Propriedades"
        print(label2.text())# devolve o valor
        print(label2.alignment()) # return o valor do alinhamento
        print(label2.hasSelectedText()) # Se ha algum texto selecionado devolve um Bool
        print(label2.indent())
        print(label2.margin()) #Devolve o valor da marge dada ao elemento

        label2.setStyleSheet("background-color: #6C4473; color:white")






app=QApplication(sys.argv)

janela=Janela()
janela.show()

sys.exit(app.exec())