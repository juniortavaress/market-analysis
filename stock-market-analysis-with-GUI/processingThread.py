from PySide6.QtCore import QObject, Signal
import webScraping

class WebScrapingWorker(QObject):
    finished = Signal()

    def __init__(self, widget, x, xx, path, value):
        super().__init__()
        self.widget = widget
        self.x = x
        self.xx = xx
        self.path = path
        self.value = value

    def run(self):
        webScraping.web(self.widget, self.x, self.xx, self.path, self.value)
        self.finished.emit()
