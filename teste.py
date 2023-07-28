import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTableWidget, QTableWidgetItem, QWidget
import pandas as pd

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Exibindo DataFrame no Qt Creator')
        self.setGeometry(100, 100, 800, 600)

        # Exemplo de DataFrame (substitua com o seu DataFrame)
        data = {'Nome': ['João', 'Maria', 'Pedro', 'Ana'],
                'Idade': [25, 30, 22, 27],
                'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba']}
        df = pd.DataFrame(data)

        # Criar a tabela e exibir o DataFrame nela
        self.table = QTableWidget(self)
        self.table.setRowCount(df.shape[0])
        self.table.setColumnCount(df.shape[1])
        self.table.setHorizontalHeaderLabels(df.columns)

        for row in range(df.shape[0]):
            for col in range(df.shape[1]):
                item = QTableWidgetItem(str(df.iat[row, col]))
                self.table.setItem(row, col, item)

        # Criar layout vertical para incorporar a tabela
        layout = QVBoxLayout()
        layout.addWidget(self.table)

        # Widget do Qt que conterá a tabela
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
