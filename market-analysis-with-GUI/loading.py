from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import QTimer, Qt, QPointF
from PySide6.QtGui import QPainter, QColor, QBrush

class LoadingAnimation(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(100, 100)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_loading)
        self.angle = 0
        self.balls = []

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)

        # Configurações das bolinhas
        self.num_balls = 8
        self.ball_radius = 15
        self.ball_sizes = [4, 5, 6, 7, 8, 9, 10, 11]
        self.ball_opacities = [20, 60, 100, 140, 180, 220, 240, 255]

    def update_loading(self):
        self.angle += 30
        if self.angle >= 360:
            self.angle = 0
        self.create_ball_positions()
        self.update()

    def create_ball_positions(self):
        # Limpa a lista de posições das bolinhas
        self.balls.clear()

        # Calcula as posições das bolinhas em círculo com diferentes tamanhos e opacidades
        for i in range(self.num_balls):
            angle = self.angle + (360 / self.num_balls) * i
            x = self.width() / 2 + 40 * qCos(angle)
            y = self.height() / 2 + 40 * qSin(angle)
            size = self.ball_sizes[i % self.num_balls]
            opacity = self.ball_opacities[i % self.num_balls]
            self.balls.append((QPointF(x, y), size, opacity))

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Desenha as bolinhas com diferentes tamanhos e opacidades
        for ball in self.balls:
            x, y = ball[0].x(), ball[0].y()
            size = ball[1]
            opacity = ball[2]
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(69, 118, 178, opacity))
            painter.drawEllipse(x - size / 2, y - size / 2, size, size)

    def start_animation(self):
        self.create_ball_positions()
        self.timer.start(100)
        self.show()

    def stop_animation(self):
        self.timer.stop()
        self.hide()

def qSin(angle):
    from math import sin, pi
    return sin(angle * pi / 180)

def qCos(angle):
    from math import cos, pi
    return cos(angle * pi / 180)
