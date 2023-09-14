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
        self.aline1=label.alignment() # return o valor do alinhamento
        label.resize(150, 40)# Redefine o tamanho da label
        label.setStyleSheet("background-color: black; color:white")
        label2=QLabel(self)
        label2.setText("Texto 2 no app")

        label2.setStyleSheet("background-color: #6C4473; color:white")






app=QApplication(sys.argv)

janela=Janela()
janela.show()
print(janela.aline1)
sys.exit(app.exec())