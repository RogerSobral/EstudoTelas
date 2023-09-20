from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QFont, QPixmap, QIcon
from PySide6.QtWidgets import (QApplication, QWidget, QHBoxLayout,QVBoxLayout,
                               QPushButton, QLineEdit, QLabel, QRadioButton)

import sys

class Tela(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(100, 50, 400, 150)
        self.setWindowTitle("Box Layout")
        self.create_widgets()
        self.setMaximumSize(400,150)

    def create_widgets(self):
        facebook=QRadioButton("Facebook")
        facebook.setIcon(QIcon("img/logos/Facebook.png"))
        instagram = QRadioButton("Instagram")
        instagram.setIcon(QIcon("img/logos/instagram.png"))
        whatsApp = QRadioButton("WhatsApp")
        whatsApp.setIcon(QIcon("img/logos/whats.png"))
        self.label = QLabel("Escolha sua rede Social:")

        facebook.toggled.connect(self.radio_button_selected)
        instagram.toggled.connect(self.radio_button_selected)
        whatsApp.toggled.connect(self.radio_button_selected)

        vbox=QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(facebook)
        vbox.addWidget(instagram)
        vbox.addWidget(whatsApp)
        self.setLayout(vbox)

    def radio_button_selected(self):
        #
        radio_select=self.sender()

        if radio_select.isChecked():
            self.label.setText(f"A rede Social escolhida foi {radio_select.text()}")




app = QApplication(sys.argv)
janela = Tela()
janela.show()
sys.exit(app.exec())