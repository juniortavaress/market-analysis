
import get as gi

from PySide6.QtWidgets import QApplication, QWidget, QGraphicsOpacityEffect, QVBoxLayout
from PySide6.QtCore import (QPropertyAnimation, QTimer, QThread)
from loading import LoadingAnimation
from processingThread import WebScrapingWorker



#class Get_Information():
#    def __init__(self):
#        super(Get_Information, self).__init__()


def animation(self):
    self.loading_animation = LoadingAnimation()
    layout = QVBoxLayout(self.ui.frame2)
    layout.addWidget(self.loading_animation)
    self.loading_animation.start_animation()

def changePageAnimation(self):
    self.ui.frame_13.hide()
    self.ui.frame2.show()
    self.nextPage(self.ui.loadingAndErrorPage)

def welcomePage(self):
    global x, xx, path, variaveis
    variaveis = 0
    is_acoes_checked = self.ui.acoes.isChecked()
    is_yes_checked = self.ui.yes.isChecked()
    path = self.ui.path.text()

    if (self.ui.yes.isChecked() or self.ui.no.isChecked()) and (self.ui.acoes.isChecked() or self.ui.fiis.isChecked()) and (self.ui.path.text()!= ""):
        x = "ação" if is_acoes_checked else "fiis"
        xx = "yes" if is_yes_checked else "no"

        if is_acoes_checked and not is_yes_checked:
            self.nextPage(self.ui.stocksOptionsPage)
        elif is_acoes_checked and is_yes_checked:
            self.processing()
        elif not is_acoes_checked and not is_yes_checked:
            self.nextPage(self.ui.fiisOptionsPage)
        else:
            self.processing()
    else:
        self.ui.frame.show()
        timer = QTimer(self)
        timer.timeout.connect(lambda: self.ui.frame.hide())
        timer.start(2000)

def processing(self):
    self.changePageAnimation()
    self.worker = WebScrapingWorker(self, x, xx, path, variaveis)
    #self.worker.finished.connect(self.showEndPage)
    self.worker.finished_with_argument.connect(self.nextStep)

    # Finalize o thread existente antes de criar um novo
    if self.thread and self.thread.isRunning():
        self.thread.quit()
        self.thread.wait()

    self.thread = QThread()
    self.worker.moveToThread(self.thread)
    self.thread.started.connect(self.worker.run)
    self.thread.finished.connect(self.thread.quit)
    self.thread.finished.connect(self.worker.deleteLater)
    self.thread.finished.connect(self.thread.deleteLater)
    self.thread.start()

def nextStep(self, error):
    print(error)
    if error == "no error":
        self.nextPage(self.ui.endPage)
    else:
        self.ui.frame2.hide()
        self.ui.frame_13.show()
        self.nextPage(self.ui.loadingAndErrorPage)


def Options(self, type):
    if self.ui.acoes.isChecked():
        page = self.ui.stocksFiltersPage
        indicadores = ["DY", "PL", "PVP", "MargemEbit", "Margem", "P_EBIT", "P_Cap", "Divida_Pat", "ROE", "ROA", "ROIC", "PatAti", "PasAti", "CAGRR", "CAGRL", "Liquidez", "PEG", "Valor"]
    else:
        page = self.ui.fiisFiltersPage
        indicadores = ["Fiis_DY", "Fiis_Cotas", "Fiis_DY_CAGR", "Fiis_Liquidez", "Fiis_PVP", "Fiis_Dividendo", "Fiis_CAGR", "Fiis_Valor"]

    for indicador in indicadores:
        checkbox = getattr(self.ui, indicador)
        widget = getattr(self.ui, f"f{indicador}")
        if not checkbox.isChecked():
            widget.hide()

    self.nextPage(page)


def Filters (self):
    global variaveis
    if self.ui.acoes.isChecked():
        indicadores = ["DY", "PL", "PVP", "MargemEbit", "Margem", "P_EBIT", "P_Cap", "Divida_Pat", "ROE", "ROA", "ROIC", "PatAti", "PasAti", "CAGRR", "CAGRL", "Liquidez", "PEG", "Valor"]
    else:
        indicadores = ["Fiis_DY", "Fiis_Cotas", "Fiis_DY_CAGR", "Fiis_Liquidez", "Fiis_PVP", "Fiis_Dividendo", "Fiis_CAGR", "Fiis_Valor"]

    variaveis = np.full((len(indicadores), 3), None)
    for i, indicador in enumerate(indicadores):
        minValue = getattr(self.ui, f"min_{indicador}").text().replace(",", ".")
        maxValue = getattr(self.ui, f"max_{indicador}").text().replace(",", ".")
        variaveis[i] = [indicador, minValue, maxValue]

    self.processing()

def reset(self):
    indicadores = ["DY", "PL", "PVP", "MargemEbit", "Margem", "P_EBIT", "P_Cap", "Divida_Pat", "ROE", "ROA", "ROIC", "PatAti", "PasAti", "CAGRR", "CAGRL", "Liquidez", "PEG", "Valor", "Fiis_DY", "Fiis_Cotas", "Fiis_DY_CAGR", "Fiis_Liquidez", "Fiis_PVP", "Fiis_Dividendo", "Fiis_CAGR", "Fiis_Valor"]
    welcome_checkBox = ["yes", "no", "fiis", "acoes"]

    for indicador in indicadores:
        checkbox = getattr(self.ui, indicador)
        checkbox.setChecked(False)
        widget = getattr(self.ui, f"f{indicador}")
        widget.show()
        value_min = getattr(self.ui, f"min_{indicador}")
        value_min.setText('')
        value_max = getattr(self.ui, f"max_{indicador}")
        value_max.setText('')

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
