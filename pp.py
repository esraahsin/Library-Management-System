from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
import sys

class ajouter_etudiant (QMainWindow ):
    def __init__(self,numero_inscription,adresse,date_de_naissance,mail,niv,nom,prenom,sectio,telephone) -> None:
        numero_inscription=self.num.text()
        adresse=self.adresse.text()
        date_de_naissance=self.date_de_naissance()
        mail=self.mail.text()
        niv=self.niv.text()
        nom=self.nom.text
        prenom=self.prenom.text()
        section=self.section.text()
        telephone=self.telephone.text()
        loadUi("code\main.ui",self)
        self.actionNew.triggered.connect(aff)
    def aff(self):
        print("new was pressed ")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = code()
    fenetre.show()
    sys.exit(app.exec_())