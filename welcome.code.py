import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget ,QMainWindow
from PyQt5.QtGui import QPixmap
import sqlite3

class main(QMainWindow) :
    def __init__(self) :
        super(main, self).__init__()
        loadUi("welcome.ui",self)
        self.actionNew.triggered.connect(self.ajouteretudiant)
    def ajouteretudiant(self):
        ajoutetudiant=ajout_etudiant_widget()
        widget.addWidget(ajoutetudiant)
        widget.setCurrentWidget(ajoutetudiant)
class ajout_etudiant_widget(QWidget):
    def __init__(self) :
        super(ajout_etudiant_widget,self).__init__()
        loadUi("etudiant_widget.ui",self)


        
         
    


        
# main
app = QApplication(sys.argv)
mainwindow = main()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1200)
widget.setFixedWidth(800)
widget.show()
app.exec_()
