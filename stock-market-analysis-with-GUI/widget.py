# This Python file uses the following encoding: utf-8
import sys
import time
import webScraping

from PySide6.QtWidgets import QApplication, QWidget, QGraphicsOpacityEffect, QVBoxLayout
from PySide6.QtCore import (QPropertyAnimation, QTimer)
from loading import LoadingAnimation

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

        # Crie uma instância da classe LoadingAnimation
        self.loading_animation = LoadingAnimation()
        # Adicione o widget de loading_animation ao frame self.ui.frame2
        layout = QVBoxLayout(self.ui.frame2)
        layout.addWidget(self.loading_animation)
        self.loading_animation.start_animation()

        self.ui.NextWelcome.clicked.connect(lambda: self.welcomePage())
        self.ui.stocksOptions.clicked.connect(lambda: self.Options("Ações"))
        self.ui.fiisOptions.clicked.connect(lambda: self.Options("Fiis"))
        self.ui.stocksFilters.clicked.connect(lambda: self.nextPage(self.ui.endPage))
        self.ui.fiisFilters.clicked.connect(lambda: self.nextPage(self.ui.endPage))
        self.ui.end.clicked.connect(lambda: self.reset())
        #self.ui.NextWelcome.clicked.connect(lambda: self.nextPage(self.ui.stocksOptions))

    def welcomePage(self):
        global x, xx, path
        x = xx = 0

        path = self.ui.path.text()
        print(path)

        if (self.ui.yes.isChecked() or self.ui.no.isChecked()) and (self.ui.acoes.isChecked() or self.ui.fiis.isChecked()) and (self.ui.path.text()!= ""):
            if self.ui.acoes.isChecked():
                x = "ação"
                if self.ui.no.isChecked():
                    xx = "no"
                    self.nextPage(self.ui.stocksOptionsPage)
                else:
                    xx = "yes"
                    webScraping.web(self, x, xx, path)
                    self.nextPage(self.ui.endPage)

            else:
                x = "fiis"
                if self.ui.no.isChecked():
                    xx = "no"
                    self.nextPage(self.ui.fiisOptionsPage)
                else:
                    xx = "yes"
                    webScraping.web(self, x, xx, path)
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
            self.stockFilters()
        else:
            self.nextPage(self.ui.fiisFiltersPage)

    def stockFilters (self):
        webScraping.web(self, x, xx, path)

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
