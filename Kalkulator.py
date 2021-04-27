
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QHBoxLayout

class Kalkulator(QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.lista = []
        self.interfejs()

    def interfejs(self):

        #pola tekstowe
        self.wynik = QLineEdit()
        self.wynik.setReadOnly(True)
        self.operacje = QLineEdit()
        self.operacje.setReadOnly(True)
        
        # przypisanie pól tekstowych do układu tabelarycznego
        uklad = QGridLayout()
        uklad.addWidget(self.wynik, 0, 0)
        uklad.addWidget(self.operacje, 1, 0)

        #przyciski
        przycisk_7 = QPushButton('7', self)
        przycisk_8 = QPushButton('8', self)
        przycisk_9 = QPushButton('9', self)
        przycisk_plus = QPushButton('+', self)
        przycisk_4 = QPushButton('4', self)
        przycisk_5 = QPushButton('5', self)
        przycisk_6 = QPushButton('6', self)
        przycisk_minus = QPushButton('-', self)
        przycisk_1 = QPushButton('1', self)
        przycisk_2 = QPushButton('2', self)
        przycisk_3 = QPushButton('3', self)
        przycisk_mnozenie = QPushButton('*', self)
        przycisk_del = QPushButton('DEL', self)
        przycisk_0 = QPushButton('0', self)
        przycisk_przecinek = QPushButton(',', self)
        przycisk_dzielenie = QPushButton('/', self)

        uklad2 = QGridLayout()
        uklad2.addWidget(przycisk_7, 0, 0)
        uklad2.addWidget(przycisk_8, 0, 1)
        uklad2.addWidget(przycisk_9, 0, 2)
        uklad2.addWidget(przycisk_plus, 0, 3)
        uklad2.addWidget(przycisk_4, 1, 0)
        uklad2.addWidget(przycisk_5, 1, 1)
        uklad2.addWidget(przycisk_6, 1, 2)
        uklad2.addWidget(przycisk_minus, 1, 3)
        uklad2.addWidget(przycisk_1, 2, 0)
        uklad2.addWidget(przycisk_2, 2, 1)
        uklad2.addWidget(przycisk_3, 2, 2)
        uklad2.addWidget(przycisk_mnozenie, 2, 3)
        uklad2.addWidget(przycisk_del, 3, 0)
        uklad2.addWidget(przycisk_0, 3, 1)
        uklad2.addWidget(przycisk_przecinek, 3, 2)
        uklad2.addWidget(przycisk_dzielenie, 3, 3)

        uklad.addLayout(uklad2, 2, 0, 1, 1)

        # przypisanie utworzonego układu do okna
        self.setLayout(uklad)

        przycisk_7.clicked.connect(self.dzialanie)
        przycisk_8.clicked.connect(self.dzialanie)
        przycisk_9.clicked.connect(self.dzialanie)
        przycisk_plus.clicked.connect(self.dzialanie)
        przycisk_4.clicked.connect(self.dzialanie)
        przycisk_5.clicked.connect(self.dzialanie)
        przycisk_6.clicked.connect(self.dzialanie)
        przycisk_minus.clicked.connect(self.dzialanie)
        przycisk_1.clicked.connect(self.dzialanie)
        przycisk_2.clicked.connect(self.dzialanie)
        przycisk_3.clicked.connect(self.dzialanie)
        przycisk_mnozenie.clicked.connect(self.dzialanie)
        przycisk_del.clicked.connect(self.dzialanie)
        przycisk_0.clicked.connect(self.dzialanie)
        przycisk_przecinek.clicked.connect(self.dzialanie)
        przycisk_dzielenie.clicked.connect(self.dzialanie)

        self.resize(300, 200)
        self.setWindowTitle("Kalkulator")
        self.show()

    def dzialanie(self):

        nadawca = self.sender()

        if nadawca.text() == '7':
            self.lista.append(7)
        elif nadawca.text() == '8':
            self.lista.append(8)
        elif nadawca.text() == ('9'):
            self.lista.append(9)
        elif nadawca.text() == ('+'):
            if 

        elif nadawca.text() == 'DEL':
            self.lista = []

        lista_stringow = []
        for i in self.lista:
            lista_stringow.append(str(i))
        self.wynik.setText(''.join(lista_stringow))

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = Kalkulator()
    sys.exit(app.exec_())