# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QGraphicsOpacityEffect
from PySide6.QtCore import (QPropertyAnimation, QTimer)

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.ui.frame.hide()

        self.ui.NextWelcome.clicked.connect(lambda: self.welcomePage())
        self.ui.stocksOptions.clicked.connect(lambda: self.Options("Ações"))
        self.ui.fiisOptions.clicked.connect(lambda: self.Options("Fiis"))
        self.ui.stocksFilters.clicked.connect(lambda: self.nextPage(self.ui.endPage))
        self.ui.fiisFilters.clicked.connect(lambda: self.nextPage(self.ui.endPage))
        self.ui.end.clicked.connect(lambda: self.reset())
        #self.ui.NextWelcome.clicked.connect(lambda: self.nextPage(self.ui.stocksOptions))

    def welcomePage(self):
        if (self.ui.yes.isChecked() or self.ui.no.isChecked()) and (self.ui.acoes.isChecked() or self.ui.fiis.isChecked()) and (self.ui.path.text()!= ""):
            if self.ui.acoes.isChecked():
                if self.ui.no.isChecked():
                    self.nextPage(self.ui.stocksOptionsPage)
                else:
                    exec(open('webScraping.py').read())
                    self.nextPage(self.ui.endPage)
            else:
                if self.ui.no.isChecked():
                    self.nextPage(self.ui.fiisOptionsPage)
                else:
                    self.nextPage(self.ui.endPage)
        else:
            self.ui.frame.show()
            timer = QTimer(self)
            timer.timeout.connect(lambda: self.ui.frame.hide())
            timer.start(2000)

    def Options(self, type):
        if type == "Ações":
            indicadores = ["DY", "PL", "PVP", "MargemEbit", "Margem", "P_EBIT", "P_Cap", "Divida_Pat", "ROE", "ROA", "ROIC", "PatAti", "PasAti", "CAGRR", "CAGRL", "Liquidez", "PEG", "Valor"]
        else:
            indicadores = ["Fiis_DY", "Fiis_DY3", "Fiis_DY_CAGR", "Fiis_Liquidez", "Fiis_PVP", "Fiis_VacF", "Fiis_VacF_2", "Fiis_Valor"]

        for indicador in indicadores:
            checkbox = getattr(self.ui, indicador)
            widget = getattr(self.ui, f"f{indicador}")
            if not checkbox.isChecked():
                widget.hide()

        if type == "Ações":
            self.nextPage(self.ui.stocksFiltersPage)
        else:
            self.nextPage(self.ui.fiisFiltersPage)

    def reset(self):
        indicadores = ["DY", "PL", "PVP", "MargemEbit", "Margem", "P_EBIT", "P_Cap", "Divida_Pat", "ROE", "ROA", "ROIC", "PatAti", "PasAti", "CAGRR", "CAGRL", "Liquidez", "PEG", "Valor", "Fiis_DY", "Fiis_DY3", "Fiis_DY_CAGR", "Fiis_Liquidez", "Fiis_PVP", "Fiis_VacF", "Fiis_VacF_2", "Fiis_Valor"]
        welcome_checkBox = ["yes", "no", "fiis", "acoes"]

        for indicador in indicadores:
            checkbox = getattr(self.ui, indicador)
            checkbox.setChecked(False)

        for indicador in indicadores:
            widget = getattr(self.ui, f"f{indicador}")
            widget.show()

        for value in welcome_checkBox:
            options = getattr(self.ui, value)
            options.setAutoExclusive(False)
            options.setChecked(False)

        for value in welcome_checkBox:
            options = getattr(self.ui, value)
            options.setAutoExclusive(True)

        self.ui.path.setText("")
        self.nextPage(self.ui.welcomePage)


    def nextPage(self, page):
        self.ui.stackedWidget.setCurrentWidget(page)
        fadeIn = QGraphicsOpacityEffect(page)
        self.animation = QPropertyAnimation(fadeIn, b"opacity")
        page.setGraphicsEffect(fadeIn)
        self.animation.setDuration(500)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
