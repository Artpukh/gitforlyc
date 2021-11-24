import sys
from circ import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from random import randint


class Yellow_Circle(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.paint = False
        self.push.clicked.connect(self.run)

    def run(self):
        self.paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp):
        x, y = randint(0, 600), randint(0, 400)
        diam = randint(0, 300)
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        qp.drawEllipse(x, y, diam, diam)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Yellow_Circle()
    ex.show()
    sys.exit(app.exec())
