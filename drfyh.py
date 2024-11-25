from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import Qt

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Rendre la fenêtre transparente
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def paintEvent(self, event):
        painter = QPainter(self)

        # Dessiner un rectangle semi-transparent
        brush = QBrush(QColor(255, 255, 255, 128))
        painter.setBrush(brush)
        painter.drawRect(0, 0, self.width(), self.height())

if __name__ == '__main__':
    app = QApplication([])
    widget = MyWidget()
    widget.resize(400, 300)
    widget.show()
    app.exec_()
