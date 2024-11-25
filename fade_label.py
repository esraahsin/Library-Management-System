from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGraphicsOpacityEffect
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QPropertyAnimation

class FadeLabel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Create a QGraphicsOpacityEffect and set it on the widget
        self.opacity_effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.opacity_effect)

        # Create a label and set its alignment to center
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)

        # Add the label to the layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)

    def setText(self, text):
        # Set the text of the label
        self.label.setText(text)

        # Start the opacity animation
        self.opacity_effect.setOpacity(0)
        self.animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.animation.setDuration(2000)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()
