import sys 
import test
import re
import csv
from datetime import date
from PyQt5.QtCore import Qt


from PyQt5.uic import loadUi
from PyQt5 import QtWidgets ,QtCore , QtGui
from PyQt5.QtWidgets import  QApplication, QWidget ,QMainWindow 
from datetime import datetime


etudiant={}
livre={}
emprunt={}

class main(QMainWindow) :
    def __init__(self) :

        super(main, self).__init__()
        loadUi("welcome.ui",self)
        self.modifier.clicked.connect(self.close)
        self.actionNew.triggered.connect(self.ajouteretudiant)
        self.actionEnregistrement_fichier_ETUDIANTS.triggered.connect(self.enregistrement_etudiants)
        self.Recuperation_fichier_etudiant.triggered.connect(self.recuperation_etudiant)
        self.action_supprimer_etudiant_donnee.triggered.connect(self.supprimer_etudiant)
        self.actionSuppression_des_tudiants_d_une_section_donn_e.triggered.connect(self.supprimer_etudiant_section)
        self.actionSuppression_des_tudiants_d_un_niveau_donn.triggered.connect(self.supprimer_etudiant_niveau)
        self.actionSuppression_des_tudiants_d_une_section_et_un_niveau.triggered.connect(self.supprimer_etudiant_niveau_section)
        self.actionT_l_phone.triggered.connect(self.modifier_telephone)
        self.actionmail.triggered.connect(self.modifier_mail)
        self.actionAdresse.triggered.connect(self.modifier_adresse)
        self.action1_Contenu_du_dictionnaire_tudiants.triggered.connect(self.afficher_etudiants)
        self.action2_Recherche_par_num_ro_inscription.triggered.connect(self.afficher_num)
        self.action3_Recherche_par_section.triggered.connect(self.afficher_section)
        self.action5_Rcherche_par_niveau.triggered.connect(self.afficher_niveau)
        self.action4_Recheche_par_section_et_niveau.triggered.connect(self.afficher_section_niveau)
        self.actionEnregistrement_fichier_LIVRES.triggered.connect(self.enregistrement_livres)
        self.actionR_cuperation_fichier_LIVRE.triggered.connect(self.recuperation_livres)
        self.actionAjouter_un_nouvel_livre.triggered.connect(self.ajout_livre)
        self.action1_Contenu_du_dictionnaire_LIVRE.triggered.connect(self.afficher_livres)
        self.actionSuppression_livre_donn.triggered.connect(self.supprimer_livre)
        self.actionSuppression_livres_d_un_auteur_donn.triggered.connect(self.supprimer_livre_auteur)
        self.actionSuppression_livres_d_une_ann_e_donn_e.triggered.connect(self.supprimer_livre_annee)
        self.actionModifier_nombre_d_exemplaires_d_un_livre.triggered.connect(self.modifier_nbre_exmp)
        self.action2_Recherche_par_R_f_rence.triggered.connect(self.recherche_ref)
        self.action3_Recherche_par_titre.triggered.connect(self.recherche_titre)
        self.action_Recherche_par_annee.triggered.connect(self.recherche_annee)
        self.action5_Recherche_livres_d_un_auteur_donn.triggered.connect(self.recherche_auteur)
        self.action6_Recherche_et_affichage_des_livres_par_ordre_alphab_tique.triggered.connect(self.affichage_tri)
        self.actionEnregistrement_fichier_EMPRUNTS.triggered.connect(self.Enregistrement_fichier_EMPRUNTS)
        self.actionR_cuperation_fichier_EMPRUNTS.triggered.connect(self.recuperation_emprunt)
        self.actionAjouter_un_nouvel_emprunt.triggered.connect(self.ajouter_emprunt)
        self.actionRetour_d_un_emprunt.triggered.connect(self.retour_emprunt)
        self.menuRecherche_et_Affichage_3.triggered.connect(self.affichage_emprunt)
        self.actionSupprimer_d_un_emprunt.triggered.connect(self.supprimer_emprunt)
        self.actionDate_emprunt.triggered.connect(self.modifier_date_emprunt)
        self.actionDate_retour.triggered.connect(self.modifier_date_retour)
        self.actionRecherche_emprunts_par_tudiant.triggered.connect(self.recherche_emprunt_par__etudiant)
        self.actionRecherche_livres_emprunt_s_une_date_donn_e.triggered.connect(self.recherche_par_date_emprunt)
        self.actionRecherche_livres_retourn_s_une_date_donn_e.triggered.connect(self.recherche_par_date_retour)
        self.actionRecherce_livres_entre_deux_dates_donn_es.triggered.connect(self.recherche_entre_deux_dates_emprunts)
        self.actionRecherche_livres_retourn_s_entre_deux_dates_donn_es.triggered.connect(self.recherche_entre_deux_dates_retour)
    def ajouteretudiant(self):
        ajoutetudiant=ajout_etudiant_widget()
        
        widget.addWidget(ajoutetudiant)
        widget.setCurrentWidget(ajoutetudiant)
        
       
    def supprimer_etudiant(self):
        supprimeretudiant=ajout_supprimer_etudiant_widget()
        widget.addWidget(supprimeretudiant)
        widget.setCurrentWidget(supprimeretudiant)
    def supprimer_etudiant_section(self) :
        supprimeretudiant_section=ajout_supprimer_section_etudiant_widget()
        widget.addWidget(supprimeretudiant_section)
        widget.setCurrentWidget(supprimeretudiant_section)
    def supprimer_etudiant_niveau(self):
        supprimeretudiant_niv=ajout_supprimer_niv_etudiant_widget()
        widget.addWidget(supprimeretudiant_niv)
        widget.setCurrentWidget(supprimeretudiant_niv)
    def supprimer_etudiant_niveau_section(self) :
        supprimeretudiant_niveau_section=ajout_supprimer_niv_section_etudiant_widget()
        widget.addWidget(supprimeretudiant_niveau_section)
        widget.setCurrentWidget(supprimeretudiant_niveau_section)
    def modifier_telephone (self):
        modifiertel=ajout_modifier_tel_widget()
        widget.addWidget(modifiertel)
        widget.setCurrentWidget(modifiertel)
    def modifier_mail (self) :
        modifiermail=ajout_modifier_mail_widget()
        widget.addWidget(modifiermail)
        widget.setCurrentWidget(modifiermail)
    def modifier_adresse(self):
        modifieradresse=ajout_modifier_adresse()
        widget.addWidget(modifieradresse)
        widget.setCurrentWidget(modifieradresse)
    def afficher_etudiants(self) :
        afficherdic=ajout_afficher_dic_etudiants_widget()
        widget.addWidget(afficherdic)
        widget.setCurrentWidget(afficherdic)
    def afficher_num(self) :
        affichernum=ajout_afficher_num_widget()
        widget.addWidget(affichernum)
        widget.setCurrentWidget(affichernum)
    def afficher_section(self) :
        affichersection=ajout_afficher_section_widget()
        widget.addWidget(affichersection)
        widget.setCurrentWidget(affichersection)
    def afficher_section_niveau(self) :
        affichersectionniv=ajout_afficher_section_niveau_widget()
        widget.addWidget(affichersectionniv)
        widget.setCurrentWidget(affichersectionniv)
    def afficher_niveau(self) :
        afficherniv=ajout_afficher_niveau_widget()
        widget.addWidget(afficherniv)
        widget.setCurrentWidget(afficherniv)
    def ajout_livre(self) :
        ajoutlivre=ajout_livre_widget()
        widget.addWidget(ajoutlivre)
        widget.setCurrentWidget(ajoutlivre)
    def afficher_livres(self) :
        afficherlivre=ajout_afficher_livres_widget()
        widget.addWidget(afficherlivre)
        widget.setCurrentWidget(afficherlivre)
    def supprimer_livre(self) :
        supprimerlivre=ajout_supprimer_livre_widget()
        widget.addWidget(supprimerlivre)
        widget.setCurrentWidget(supprimerlivre)
    def supprimer_livre_auteur(self) :
        supprimerauteurs=ajout_supprimer_livre_auteur_widget()
        widget.addWidget(supprimerauteurs)
        widget.setCurrentWidget(supprimerauteurs)
    def supprimer_livre_annee(self) :
        supprimerlivre=ajout_supprimer_livre_annee_widget()
        widget.addWidget(supprimerlivre)
        widget.setCurrentWidget(supprimerlivre)
    def modifier_nbre_exmp(self) :
        modifier=ajout_modifier_nbre_d_exemplaires_widget()
        widget.addWidget(modifier)
        widget.setCurrentWidget(modifier)
    def recherche_ref(self) :
        recherche=ajout_recherche_ref_widget()
        widget.addWidget(recherche)
        widget.setCurrentWidget(recherche)
    def recherche_titre(self) :
        recherchetitre=ajout_recherche_titre_widget()
        widget.addWidget(recherchetitre)
        widget.setCurrentWidget(recherchetitre)
    def recherche_annee(self) :
        rechercheannee=ajout_recherche_annee_widget()
        widget.addWidget(rechercheannee)
        widget.setCurrentWidget(rechercheannee)
    def recherche_auteur(self) :
        rechercheauteur=ajout_recherche_auteur_widget()
        widget.addWidget(rechercheauteur)
        widget.setCurrentWidget(rechercheauteur)
    def affichage_tri(self) :
        affichage=ajout_affichage_widget()
        widget.addWidget(affichage)
        widget.setCurrentWidget(affichage)
    def ajouter_emprunt(self) :
        ajouter=ajout_emprunt_widget()
        widget.addWidget(ajouter)
        widget.setCurrentWidget(ajouter)
    def retour_emprunt(self) :
        retour=retour_widget()
        widget.addWidget(retour)
        widget.setCurrentWidget(retour)
    def affichage_emprunt (self) :
        affichage=affichage_dic_emprunt_widget()
        widget.addWidget(affichage)
        widget.setCurrentWidget(affichage)
    def supprimer_emprunt(self) :
        supprimer=supprimer_emprunt_widget()
        widget.addWidget(supprimer)
        widget.setCurrentWidget(supprimer)
    def modifier_date_emprunt(self) :
        modifier=modifier_date_d_emprunt_widget()
        widget.addWidget(modifier)
        widget.setCurrentWidget(modifier)
    def modifier_date_retour (self) :
        modifier=modifier_date_de_retour_widget()
        widget.addWidget(modifier)
        widget.setCurrentWidget(modifier)
    def recherche_emprunt_par__etudiant(self) :
        recherche=recherche_emprunt_par_etudiant()
        widget.addWidget(recherche)
        widget.setCurrentWidget(recherche)
    def recherche_par_date_emprunt (self) :
        recherche=recherche_emprunt_par_date()
        widget.addWidget(recherche)
        widget.setCurrentWidget(recherche)
    def recherche_par_date_retour (self) :
        recherche=recherche_emprunt_par_date_retour()
        widget.addWidget(recherche)
        widget.setCurrentWidget(recherche)
    def recherche_entre_deux_dates_emprunts(self) :
        recherche=recherche_entre_deux_dates_emprunts_widget()
        widget.addWidget(recherche)
        widget.setCurrentWidget(recherche)
    def recherche_entre_deux_dates_retour(self) :
        recherche=recherche_entre_deux_dates_retours_widget()
        widget.addWidget(recherche)
        widget.setCurrentWidget(recherche)
#--------------------Enregistrement et récupération des données -------------------------------
    def enregistrement_etudiants(self):
        with open("Base_etudiant.csv",'w',newline="") as file :
            
            writer=csv.writer(file,delimiter=';')
            for cle,val in etudiant.items():
                ch=[cle]+val
                writer.writerow(ch)

        msge = QtWidgets.QMessageBox()
        msge.setWindowTitle("")
        msge.setText("Fichier ETUDIANTS est enregistré ")
        msge.setIcon(QtWidgets.QMessageBox.Information)
        x= msge.exec_()   

                
    def recuperation_etudiant(self) :
        with open('Base_etudiant.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            for row in csv_reader:
               etudiant[row[0]]=row[1:]
        msge = QtWidgets.QMessageBox()
        msge.setWindowTitle("")
        msge.setText("Fichier ETUDIANTS est récupéré")
        msge.setIcon(QtWidgets.QMessageBox.Information)
        x= msge.exec_() 
        return etudiant
              

    def enregistrement_livres(self) :
        with open ("base_LIVRES.csv","w",newline="") as file :
            writer=csv.writer(file,delimiter=';')
            for cle,val in livre.items():
                ch=[cle]+val
                writer.writerow(ch)
                
        msge = QtWidgets.QMessageBox()
        msge.setWindowTitle("")
        msge.setText("Fichier LIVRES est enregistré ")
        msge.setIcon(QtWidgets.QMessageBox.Information)
        x= msge.exec_()   
    def recuperation_livres (self) :
        
        with open("base_LIVRES.csv","r") as file :
            csv_reader = csv.reader(file, delimiter=';')
            for row in csv_reader:
               livre[row[0]]=row[1:]
        msge = QtWidgets.QMessageBox()
        msge.setWindowTitle("")
        msge.setText("Fichier LIVRES est récupéré")
        msge.setIcon(QtWidgets.QMessageBox.Information)
        x= msge.exec_()    
        return livre           
    def Enregistrement_fichier_EMPRUNTS(self) :
        with open ("Base_EMPRUNTS.csv","w",newline="") as f :
            
            writer=csv.writer(f,delimiter=';')

            for cle,val in emprunt.items():
                ch=[cle]+val
                writer.writerow(ch)
                
        msge = QtWidgets.QMessageBox()
        msge.setWindowTitle("")
        msge.setText("Fichier EMPRUNTS est enregistré ")
        msge.setIcon(QtWidgets.QMessageBox.Information)
        x= msge.exec_()   
    def recuperation_emprunt(self) :
        with open("Base_EMPRUNTS.csv","r") as file :
            csv_reader = csv.reader(file, delimiter=';')
            for row in csv_reader:
               emprunt[row[0]]=row[1:]
        msge = QtWidgets.QMessageBox()
        msge.setWindowTitle("")
        msge.setText("Fichier EMPRUNTS est récupéré")
        msge.setIcon(QtWidgets.QMessageBox.Information)
        x= msge.exec_() 
        return emprunt        
#-------------------------Ajout d'un étudiant------------------------------------------


class ajout_etudiant_widget(QWidget):
    def __init__(self) :
        super(ajout_etudiant_widget,self).__init__()
        loadUi("etudiant_widget.ui",self)
        
        self.annuler.clicked.connect(self.Return)
        self.ajouter.clicked.connect(self.Ajouter)
    def Return(self):
        widget.setCurrentIndex(0)
    
    def Ajouter(self):
         num=self.num.text()
         ok=True
       
         for key in etudiant.keys():
            if key==num :
                ok=False
                break 
         if not (num):
                self.numerreur.setText("Saisissez le numéro de l'inscription  !")
         elif not (num.isdigit()):
                self.numerreur.setText("Faux numéro d'inscription")
                self.num.clear()
         else :
                 self.numerreur.setText("")
         numresultat=self.numerreur.text()
         nom=self.nom.text()
         if not (nom):
            self.nomerreur.setText("Saisissez le nom de l'étudiant")
         elif not (nom.isalpha()):
            self.nomerreur.setText("Faux nom")
            self.nom.clear()
         elif  not  ok:
            self.numerreur.setText("Cet etudiant existe déjà")
         else :
            self.nomerreur.setText("")
         nomresultat=self.nomerreur.text()
         prenom=self.prenom.text()
         if not (prenom):
            self.prenomerreur.setText("Saisissez le prénom de l'étudiant ")
         elif not (prenom.isalpha()):
            self.prenomerreur.setText("Faux prénom")
            self.prenom.clear()
         else :
            self.prenomerreur.setText("")
         prenomresultat=self.prenomerreur.text()
         Date=self.date.text()
         today=date.today()
         if int(Date[6:10])>today.year or  int(Date[3:5])>today.month:
            self.dateerreur.setText("Faux date ")
            self.date.clear()
         else :
            self.dateerreur.setText("")
         dateresultat=self.dateerreur.text()
         niveau=self.niv.text()
         if not niveau :
            self.niverreur.setText("Saisissez le niveau de l'étudiant ")
         elif not (niveau.isdigit()):
            self.niverreur.setText("Faux section")
            self.niv.clear()
         else :
            self.niverreur.setText("")
         nivresultat=self.niverreur.text()
         adresse=self.adresse.text()
         if not adresse :
            self.adresseerreur.setText("Saisissez une adresse  ")
         else :
            self.adresseerreur.setText("")
         adresseresultat=self.adresseerreur.text()
         mail=self.mail.text()
         forme=r'\b[A-Za-z0-9._%+-]+@[A-Aa-z0-9.-]+\.[A-Z|a-z]{2,}\b'
         if not(re.fullmatch(forme,mail)):
            self.mailerreur.setText("Faux adresse Email")
            self.mail.clear()
         elif not mail :
            self.mailerreur.setText("Saisissez une adresse e-mail   ")
         else :
            self.mailerreur.setText("")
         mailresultat=self.mailerreur.text()
         tel=self.telephone.text()
         if not tel :
            self.telephoneerreur.setText("Saisissez un numéro du telephone ")
         elif not len(tel)==8 :
            self.telephoneerreur.setText("Faux numéro")
            self.telephone.clear()
         else :
            self.telephoneerreur.setText("")
         telresultat=self.telephoneerreur.text()
         section=self.section.text()
         if not section :
            self.sectionerreur.setText("Saisissez une section")
         elif not section.isalpha() :
            self.section.clear()
            self.sectionerreur.setText("Faux section")
         else :
            self.sectionerreur.setText("")
         sectionresultat=self.sectionerreur.text()
         if (sectionresultat==nivresultat==numresultat==nomresultat==nivresultat==adresseresultat==prenomresultat==telresultat==mailresultat==dateresultat and ok) :
            ls=[nom,prenom,Date,niveau,section,adresse,mail,tel]
            etudiant[num]=ls
            print(etudiant)
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("")
            msge.setText("Etudiant est ajouté avec succés !")
            msge.setIcon(QtWidgets.QMessageBox.Information)
            x= msge.exec_()     
        
         else :
          msge = QtWidgets.QMessageBox()
          msge.setWindowTitle("")
          msge.setText("Vérifier vos données !")
          msge.setIcon(QtWidgets.QMessageBox.Critical)
          x= msge.exec_()     
 #--------------------------Supprimer un etudiant-------------------------------------------------------
class ajout_supprimer_etudiant_widget(QWidget):
    def __init__(self) :
        super(ajout_supprimer_etudiant_widget,self).__init__()
        loadUi("supprimer_etudiant.ui",self)
        self.annuler.clicked.connect(self.Return)
        self.supprimer.clicked.connect(self.Supprimer)
    def Return(self) :
        widget.setCurrentIndex(0)

    def Supprimer(self) :
        test=False
        num=self.num.text()
        if not etudiant :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Dictionnaire est vide !")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()

        elif not num :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Saisissez un numéro d'inscription !")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()

        elif not num.isdigit():
            self.num.clear()
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Faux numéro !")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()

        else :
            
            for key in etudiant.keys() :
                if num==key :
                    test=True
                    etudiant.pop(key)
                    break
            if test==False :
                    msge = QtWidgets.QMessageBox()
                    msge.setWindowTitle("ERREUR")
                    msge.setText("Cet étudiant n'existe pas !")
                    msge.setIcon(QtWidgets.QMessageBox.Critical)
                    x= msge.exec_()  
                    
            if test==True :
                    msge = QtWidgets.QMessageBox()
                    msge.setWindowTitle("SUCCES")
                    msge.setText("Cet étudiant est supprimé avec succés !")
                    msge.setIcon(QtWidgets.QMessageBox.Information)
                    x = msge.exec_()


#-----------------------supprimer des etudiants d'une section donnée----------------------------------------
class ajout_supprimer_section_etudiant_widget(QWidget) :
    def __init__(self) :
        super(ajout_supprimer_section_etudiant_widget,self).__init__()
        loadUi("supprimer etudiant section.ui ",self)
        self.annuler.clicked.connect(self.Return)
        self.supprimer.clicked.connect(self.Supprimer)
    def Return (self):
            widget.setCurrentIndex(0)
    def Supprimer(self) :
            section=self.section.text()
            if not etudiant :
                    msge = QtWidgets.QMessageBox()
                    msge.setWindowTitle("ERREUR")
                    msge.setText("Dictionnaire est vide  !")
                    msge.setIcon(QtWidgets.QMessageBox.Critical)
                    x= msge.exec_()
            elif not section :
                    msge = QtWidgets.QMessageBox()
                    msge.setWindowTitle("ERREUR")
                    msge.setText("Saisissez une section à supprimer !")
                    msge.setIcon(QtWidgets.QMessageBox.Critical)
                    x= msge.exec_()             
            elif not section.isalpha() :
                    msge = QtWidgets.QMessageBox()
                    msge.setWindowTitle("ERREUR")
                    msge.setText("Faux section !")
                    msge.setIcon(QtWidgets.QMessageBox.Critical)
                    x= msge.exec_()
            else :
                l=[]
                for key in etudiant.keys():
                    if section==etudiant[key][4] :
                        l.append(key)
                if l :
                    for i in l:
                        etudiant.pop(i)
    
                    msge = QtWidgets.QMessageBox()
                    msge.setWindowTitle("SUCCES")
                    msge.setText("Les etudiants de section  "+section+"  sont supprimés avec succés")
                    msge.setIcon(QtWidgets.QMessageBox.Information)
                    x= msge.exec_()
                else :
                    msge = QtWidgets.QMessageBox()
                    msge.setWindowTitle("ERREUR")
                    msge.setText(" Section  "+section+"  n'existe pas ")
                    msge.setIcon(QtWidgets.QMessageBox.Critical)
                    x= msge.exec_()
#----------------------------Supprimer des étudiants d'un niveau donné-------------------------------------                   
class ajout_supprimer_niv_etudiant_widget(QWidget) :
    def __init__(self):
        super(ajout_supprimer_niv_etudiant_widget,self).__init__()   
        loadUi("supprimer etudiant niveau.ui",self)
        self.annuler.clicked.connect(self.Return)
        self.supprimer.clicked.connect(self.Supprimer)
    def Return(self)  :
        widget.setCurrentIndex(0)
    def Supprimer(self) :
        niv=self.niv.text()
        
        if not etudiant :
                    msge = QtWidgets.QMessageBox()
                    msge.setWindowTitle("ERREUR")
                    msge.setText("Dictionnaire est vide  !")
                    msge.setIcon(QtWidgets.QMessageBox.Critical)
                    x= msge.exec_()
        elif not niv :
                    msge = QtWidgets.QMessageBox()
                    msge.setWindowTitle("ERREUR")
                    msge.setText("Saisissiez un niveau à supprimer !")
                    msge.setIcon(QtWidgets.QMessageBox.Critical)
                    x= msge.exec_()             
        elif not niv.isdigit() :
                    msge = QtWidgets.QMessageBox()
                    msge.setWindowTitle("ERREUR")
                    msge.setText("Faux  niveau !")
                    msge.setIcon(QtWidgets.QMessageBox.Critical)
                    x= msge.exec_()
        else :
                l=[]
                for key in etudiant.keys():
                    if niv==etudiant[key][3] :
                        l.append(key)
                if l :
                    for i in l:
                        etudiant.pop(i)
    
                    msge = QtWidgets.QMessageBox()
                    msge.setWindowTitle("SUCCES")
                    msge.setText("Les etudiants de niveau  "+niv+"  sont supprimés avec succés")
                    msge.setIcon(QtWidgets.QMessageBox.Information)
                    x= msge.exec_()
                else :
                    msge = QtWidgets.QMessageBox()
                    msge.setWindowTitle("ERREUR")
                    msge.setText(" Niveau  "+niv+"  n'existe pas ")
                    msge.setIcon(QtWidgets.QMessageBox.Critical)
                    x= msge.exec_()
#----------------------------------Supprimer des étudiants d'un niveau et une section donnés-----------------------------
class ajout_supprimer_niv_section_etudiant_widget(QWidget) :
    def __init__(self) :
        super(ajout_supprimer_niv_section_etudiant_widget,self).__init__()
        loadUi("supprimer etudiant section niveau.ui",self)
        self.annuler.clicked.connect(self.Return)
        self.supprimer.clicked.connect(self.Supprimer)
    def Return(self) :
        widget.setCurrentIndex(0)
    def Supprimer(self) :
        niv=self.niv.text()
        section=self.section.text()
        if not etudiant :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Dictionnaire est vide !")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()
        elif etudiant :
            if not niv :
                self.niverreur.setText("Saisissiez un niveau")
            elif not niv.isdigit():
                self.niverreur.setText("Faux niveau")
                self.niv.clear()
            else :
                self.niverreur.setText("")
            nivresultat=self.niverreur.text()
            if  section=="" and etudiant:
                self.sectionerreur.setText("Saisissiez une section")
        
            elif not section.isalpha() and etudiant and section:
                self.sectionerreur.setText("Faux section")
                self.section.clear()
            else :
                self.sectionerreur.setText("")
            sectionresultat=self.sectionerreur.text()
            test=False
            for key in etudiant.keys():
                if niv==etudiant[key][3] and section==etudiant[key][4] and sectionresultat=="":
                    test=True
           
            if not test and not sectionresultat and not nivresultat :
                msge = QtWidgets.QMessageBox()
                msge.setWindowTitle("ERREUR")
                msge.setText(" Niveau  "+niv+" de section  "+section+"  n'existe pas ")
                msge.setIcon(QtWidgets.QMessageBox.Critical)
                x= msge.exec_()
            elif test and  sectionresultat=="" and  nivresultat=="" :
                l= []
                for key in etudiant.keys() :
                    if niv==etudiant[key][3] and section==etudiant[key][4] :
                        l.append(key)
                for i in l: 
                    etudiant.pop(i)
                msge = QtWidgets.QMessageBox()
                msge.setWindowTitle("SUCCES")
                msge.setText("Les étudiants de section "+section+"  et de  niveau  "+niv+"  sont supprimés avec succés")
                msge.setIcon(QtWidgets.QMessageBox.Information)
                x= msge.exec_()
        else :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText(" Vérifier vos données ")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()   
#----------------------------------Modifier un numero telephone d'un étudiant ---------------------------------
class ajout_modifier_tel_widget(QWidget) :
    def __init__(self) :
            super(ajout_modifier_tel_widget,self).__init__()
            loadUi("modifier_etudiant_telephone.ui",self)
            self.annuler.clicked.connect(self.Return)
            self.modifier.clicked.connect(self.Modifier)
    def Return(self) :
            widget.setCurrentIndex(0)
    def Modifier(self ) :
        num=self.num.text()
        tel=self.tel.text()
        if not etudiant :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Dictionnaire est vide !")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()
        elif etudiant :
         if not num :
            self.numerreur.setText("Saisissez le numero d'inscription")
         elif not num.isdigit() :
            self.numerreur.setText("Faux numero d'inscription")
            self.num.clear()
         else :
            self.numerreur.setText("")
         numresultat=self.numerreur.text()
         test=False
         for key in etudiant.keys() :
             if key==num :
                 test=True
                 break
         if test==False :
             self.numerreur.setText("Cet étudiant n'existe pas !")
             
         if not tel :
            self.telerreur.setText("Saisissez un numéro de téléphone ")
         elif not (tel.isdigit() and len(tel)==8):
            self.telerreur.setText("Faux numéro téléphone")
            self.tel.clear()
         else :
            self.telerreur.setText("")
         telresultat=self.telerreur.text()
         test=False
         if numresultat=="" and telresultat=="" :
            for key in etudiant.keys() :
                if num==key :
                    test=True
                    etudiant[key][7]=tel
                    break
            if test :
                msge = QtWidgets.QMessageBox()
                msge.setWindowTitle("SUCCES")
                msge.setText("Numéro téléphone est modifié avec succés")
                msge.setIcon(QtWidgets.QMessageBox.Information)
                x= msge.exec_()
            else :
                self.numerreur.setText("Etudiant n'existe pas ")
                
        if  etudiant and (numresultat or telresultat ):
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText(" Vérifier vos données ")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()
#-------------------Modifer e-mail d'un etudiant donné-------------------------------
class ajout_modifier_mail_widget (QWidget) :
    def __init__(self) :
        super(ajout_modifier_mail_widget,self).__init__()
        loadUi("modifier mail.ui",self)
        self.annuler.clicked.connect(self.Return)
        self.modifier.clicked.connect(self.Modifier)
    def Return (self):
        widget.setCurrentIndex(0)
    def Modifier (self) :
        num=self.num.text()
        mail=self.mail.text()
        if not etudiant :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Dictionnaire est vide !")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()
        else :
         if not num :
            self.numerreur.setText("Saisissiez un numéro d'inscription ")
         elif not num.isdigit() :
            self.numerreur.setText("Faux numéro d'inscription" )
            self.num.clear()
         else :
            self.numerreur.setText("")
         numresultat=self.numerreur.text()
         forme=r'\b[A-Za-z0-9._%+-]+@[A-Aa-z0-9.-]+\.[A-Z|a-z]{2,}\b'

         if not mail :
            self.mailerreur.setText("Saisissiez un e-mail ")
         elif  not(re.fullmatch(forme,mail)):
            self.mailerreur.setText("Faux e-mail")
            self.mail.clear()
         else :
            self.mailerreur.setText("")
            
         test=False
         mailresultat=self.mailerreur.text()
         if mailresultat=="" and numresultat=="":
            for key in etudiant.keys() :
                if num==key :
                    test=True 
                    etudiant[key][6]=mail
                    break
            if test==True :
                msge = QtWidgets.QMessageBox()
                msge.setWindowTitle("SUCCES")
                msge.setText("E-mail est modifié avec succés")
                msge.setIcon(QtWidgets.QMessageBox.Information)
                x= msge.exec_()  
            else :
                self.numerreur.setText("Cet étudiant n'existe pas ")

        if etudiant and (numresultat or mailresultat) :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Vérifier vos données")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()


#-----------------------------Modifier l'adresse d'un étudiant donné--------------------
class ajout_modifier_adresse(QWidget) :
    def __init__(self) :
        super(ajout_modifier_adresse,self).__init__()
        loadUi("modifier adresse.ui",self)
        self.annuler.clicked.connect(self.Return)
        self.modifier.clicked.connect(self.Modifier)
    def Return (self) :
            widget.setCurrentIndex(0)
    def Modifier (self) :
            num=self.num.text()
            adresse=self.adresse.text()
            if not etudiant :
                msge = QtWidgets.QMessageBox()
                msge.setWindowTitle("ERREUR")
                msge.setText("Dictionnaire est vide !")
                msge.setIcon(QtWidgets.QMessageBox.Critical)
                x= msge.exec_()
            else:
             if not num :
                self.numerreur.setText("Saisissiez un numéro d'inscription ")
             elif not num.isdigit() :
                self.numerreur.setText("Faux numéro d'inscription" )
                self.num.clear()
             else :
                self.numerreur.setText("")
             numresultat=self.numerreur.text()
             if not adresse :
                self.adresseerreur.setText("Saisissiez une adresse")
             else :
                self.adresseerreur.setText('')
             adresseresultat=self.adresseerreur.text()
             test=False
             if  numresultat=="" and adresseresultat=="" :
                for key in etudiant.keys() :
                    if num==key :
                        test=True 
                        etudiant[key][5]=adresse 
                        break 
                if test==True :
                    msge = QtWidgets.QMessageBox()
                    msge.setWindowTitle("SUCCES")
                    msge.setText("Adresse  est modifiée avec succés")
                    msge.setIcon(QtWidgets.QMessageBox.Information)
                    x= msge.exec_()  
                elif not test :
                    self.numerreur.setText("Cet étudiant n'existe pas ")
             if not(numresultat=="" and adresseresultat=="") and etudiant :
                msge = QtWidgets.QMessageBox()
                msge.setWindowTitle("ERREUR")
                msge.setText("Vérifier vos donnés")
                msge.setIcon(QtWidgets.QMessageBox.Critical)
                x= msge.exec_()    


#--------------------------Afficher le dictionnaire étudiant-------------------------------
class ajout_afficher_dic_etudiants_widget(QWidget) :
    def __init__(self) :
        super(ajout_afficher_dic_etudiants_widget,self).__init__()
        loadUi("dictionnaire_etudiant.ui",self)
        self.afficher()
        self.annuler.clicked.connect(self.Return)
    def Return(self):
        widget.setCurrentIndex(0)

    def afficher(self):
        self.tableWidget.setRowCount(len(etudiant))
        if etudiant=={}:
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText(" ")
            msge.setInformativeText(" Dictionnaire vide!")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()
        
        row = 0
        print(etudiant)
        for key in etudiant.keys():

                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(key))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(etudiant[key][0]))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(etudiant[key][1]))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(etudiant[key][2]))
                self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(etudiant[key][3]))
                self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(etudiant[key][4]))
                self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(etudiant[key][5]))
                self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(etudiant[key][6]))
                self.tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(etudiant[key][7]))

                row = row + 1

#-------------------------Recherche avec Numéro d'inscription-------------------------------------
class ajout_afficher_num_widget(QWidget) :
    def __init__(self) :
        super(ajout_afficher_num_widget,self).__init__()
        loadUi("afficher_num.ui",self)
        self.annuler.clicked.connect(self.Return)
        self.recherche.clicked.connect(self.Recherche)
    def Return(self) :
        widget.setCurrentIndex(0)
    def Recherche(self) :
        num=self.num.text()
        if etudiant=={} :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Dictionnaire est vide ")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()    
        elif not num :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Saisissiez un Numéro ID")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()    
        elif not num.isdigit() :
            self.num.clear()
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Faux numéro ID")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()    
        else :
            test=False
            for key in etudiant.keys() :
                if num==key :
                    test=True
                    self.tableWidget.setRowCount(1)
                    self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(key))
                    self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(etudiant[key][0]))
                    self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(etudiant[key][1]))
                    self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem(etudiant[key][2]))
                    self.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem(etudiant[key][3]))
                    self.tableWidget.setItem(0, 5, QtWidgets.QTableWidgetItem(etudiant[key][4]))
                    self.tableWidget.setItem(0, 6, QtWidgets.QTableWidgetItem(etudiant[key][5]))
                    self.tableWidget.setItem(0, 7, QtWidgets.QTableWidgetItem(etudiant[key][6]))
                    self.tableWidget.setItem(0, 8, QtWidgets.QTableWidgetItem(etudiant[key][7]))
                    break 
            if not test :
                msge = QtWidgets.QMessageBox()
                msge.setWindowTitle("ERREUR")
                msge.setText("Numéro ID n'existe pas ")
                msge.setIcon(QtWidgets.QMessageBox.Critical)
                x= msge.exec_() 

#--------------------------Recherche par section --------------------------------------------------------
class ajout_afficher_section_widget(QWidget) :
    def __init__(self) :
        super(ajout_afficher_section_widget,self).__init__()
        loadUi("afficher_section.ui",self)
        self.annuler.clicked.connect(self.Return)
        self.recherche.clicked.connect(self.Recherche)
     
    def Return (self) :
        widget.setCurrentIndex(0)
    def Recherche(self) :
        section=self.section.text()
        row=0
        if etudiant=={} :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Dictionnaire est vide ")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()    
        elif not section :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Saisissiez une section ")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()   
        elif not section.isalpha() :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Faux section ")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()   
        else :
            test=False 
            l=[]
            for key in etudiant.keys() :
                if section==etudiant[key][4] :
                    test=True 
                    l.append(key)
            if test==False :
                msge = QtWidgets.QMessageBox()
                msge.setWindowTitle("ERREUR")
                msge.setText("Cette section n'existe pas  ")
                msge.setIcon(QtWidgets.QMessageBox.Critical)
                x= msge.exec_()   
            else :
                for key in etudiant.keys() :
                    if section==etudiant[key][4] :
                        self.tableWidget.setRowCount(len(l))
                        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(key))
                        self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(etudiant[key][0]))
                        self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(etudiant[key][1]))
                        self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(etudiant[key][2]))
                        self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(etudiant[key][3]))
                        self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(etudiant[key][4]))
                        self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(etudiant[key][5]))
                        self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(etudiant[key][6]))
                        self.tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(etudiant[key][7]))
                        row+=1
#--------------------------Recherche par section et niveau -----------------------------------------------

class ajout_afficher_section_niveau_widget(QWidget) :
    def __init__(self) :
        super(ajout_afficher_section_niveau_widget,self).__init__()
        loadUi("afficher_section_niveau.ui",self)
        self.annuler.clicked.connect(self.Return)
        self.recherche.clicked.connect(self.Recherche)
    def Return (self) :
        widget.setCurrentIndex(0)
    def Recherche(self) :
        section=self.section.text()
        niv=self.niv.text()
        row=0
        k=1
        if etudiant=={} :
            k=0
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Dictionnaire est vide ")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()    
        elif not niv :
            self.niverreur.setText("Saisissez le niveau de l'étudiant ")
        elif not (niv.isdigit()):
            self.niverreur.setText("Faux section")
            self.niv.clear()

        else :
            self.niverreur.setText("")
        nivresultat=self.niverreur.text()
        if k:
         if not section  :
            self.sectionerreur.setText("Saisissez une section")
         elif not section.isalpha() :
            self.section.clear()
            self.sectionerreur.setText("Faux section")
         else  :
            self.sectionerreur.setText("")
         sectionresultat=self.sectionerreur.text()
         if sectionresultat and nivresultat :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Vérifier vos données ")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_() 
         elif sectionresultat=="" and nivresultat=="" :
            l=[]
            tests=False
            testn=False 
            for key in etudiant.keys() :
                if section==etudiant[key][4] :
                    tests=True
                if niv==etudiant[key][3] :
                    testn=True
                if section==etudiant[key][4] and niv==etudiant[key][3] :
                    l.append(key) 
            if testn==False :
                msge = QtWidgets.QMessageBox()
                msge.setWindowTitle("ERREUR")
                msge.setText("Ce niveau n'existe pas ")
                msge.setIcon(QtWidgets.QMessageBox.Critical)
                x= msge.exec_() 
            if tests==False :
                msge = QtWidgets.QMessageBox()
                msge.setWindowTitle("ERREUR")
                msge.setText("Cette section n'existe pas ")
                msge.setIcon(QtWidgets.QMessageBox.Critical)
                x= msge.exec_()  
            if tests and testn and sectionresultat=="" and nivresultat=="" :
                for key in etudiant.keys() :
                    if section==etudiant[key][4] and niv==etudiant[key][3] :
                        self.tableWidget.setRowCount(len(l))
                        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(key))
                        self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(etudiant[key][0]))
                        self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(etudiant[key][1]))
                        self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(etudiant[key][2]))
                        self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(etudiant[key][3]))
                        self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(etudiant[key][4]))
                        self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(etudiant[key][5]))
                        self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(etudiant[key][6]))
                        self.tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(etudiant[key][7]))
                        row+=1
            if not l :
                msge = QtWidgets.QMessageBox()
                msge.setWindowTitle("ERREUR")
                msge.setText("Il n'existe pas des étudiants de niveau "+niv+ " et de section "+section)
                msge.setIcon(QtWidgets.QMessageBox.Critical)
                x= msge.exec_()

#----------------------------Recherche par niveau ----------------------------------------
class ajout_afficher_niveau_widget(QWidget) :
    def __init__(self):
        super(ajout_afficher_niveau_widget,self).__init__()
        loadUi("afficher_niv.ui",self)
        self.annuler.clicked.connect(self.Return)
        self.recherche.clicked.connect(self.Recherche)
    def Return(self) :
        widget.setCurrentIndex(0)
    def Recherche(self) :
        niv=self.niv.text()
        row=0
        if etudiant=={} :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Dictionnaire est vide ")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()    
        elif not niv :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Saisissiez un niveau ")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()   
        elif not niv.isdigit() :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Faux Niveau ")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()   
        else :
            test=False 
            l=[]
            for key in etudiant.keys() :
                if niv==etudiant[key][3] :
                    test=True 
                    l.append(key)
            if test==False :
                msge = QtWidgets.QMessageBox()
                msge.setWindowTitle("ERREUR")
                msge.setText("Ce niveau n'existe pas  ")
                msge.setIcon(QtWidgets.QMessageBox.Critical)
                x= msge.exec_()   
            else :
                for key in etudiant.keys() :
                    if niv==etudiant[key][3] :
                        self.tableWidget.setRowCount(len(l))
                        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(key))
                        self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(etudiant[key][0]))
                        self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(etudiant[key][1]))
                        self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(etudiant[key][2]))
                        self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(etudiant[key][3]))
                        self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(etudiant[key][4]))
                        self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(etudiant[key][5]))
                        self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(etudiant[key][6]))
                        self.tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(etudiant[key][7]))
                        row+=1
#----------------------------Ajouter un livre--------------------------------------------
class ajout_livre_widget(QWidget) :
    def __init__(self) :
        super(ajout_livre_widget,self).__init__()
        loadUi("ajout livre.ui",self)
        self.annuler.clicked.connect(self.Return)
        self.ajouter.clicked.connect(self.Ajouter)
    def Return(self) :
        widget.setCurrentIndex(0)
    def Ajouter(self) :
        
       
         ref=self.reference.text()
         test=True
         if not ref :
            self.referreur.setText("Saisissez une référence ")
         elif not ref.isdigit() :
            self.referreur.setText("Faux référence")
         elif (ref!="" and ref.isdigit()) :
            for key in livre.keys() :
                if ref==key :
                    self.referreur.setText("Ce livre existe déjà")
                    test=False
         if test and ref.isdigit() and ref :
            self.referreur.setText("")

         r=self.referreur.text()
         titre=self.titre.text()
         if not titre :
            self.titreerreur.setText("Saisissez un titre")
         else :
             self.titreerreur.setText("")
    
         t=self.titreerreur.text()
         auteur=self.auteur.text()
         if not auteur :
            self.auteurerreur.setText("Saisissez le nom et le prénom de l'auteur")            
        
         else :
            self.auteurerreur.setText("")
         a=self.auteurerreur.text()
         annee=self.annee.text()
         today=date.today()

         if not annee :
            self.anneeerreur.setText("Saisissez année édition")
         elif not int(annee) <= today.year :
            self.anneeerreur.setText("Vérifier l'année édition")
         else :
            self.anneeerreur.setText("")
         an=self.anneeerreur.text()
         nbre=self.nbre.text()
         if not nbre :
            self.nbreerreur.setText("Saisissez le nombre d'exemplaires ")
         elif not nbre.isdigit() :
            self.nbreerreur.setText("Faux numéro")
         else :
            self.nbreerreur.setText("")
         n=self.nbreerreur.text()
         if (n==an==a==t==r=="") :
            l=[titre,auteur,annee,nbre]
            livre[ref]=l
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("SUCCES")
            msge.setText("livre ajouté avec succès ")
            msge.setIcon(QtWidgets.QMessageBox.Information)
            x= msge.exec_()  
         else :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Vérifier vos données ")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()  

#----------------------------Affichage de dictionnaire LIVRES----------------------------

class ajout_afficher_livres_widget(QWidget) :
    def __init__(self) :
        super(ajout_afficher_livres_widget,self).__init__()
        loadUi("afficher dic livre.ui",self)
        self.afficher()
        self.annuler.clicked.connect(self.Return)
    def Return(self) :
        widget.setCurrentIndex(0)
    def afficher(self):
        l=[]
        if livre=={} :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Dictionnaire est vide! ")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_() 
        else : 
            l=[]
            for key in livre.keys() :
                l.append(key)   
            self.tableWidget.setRowCount(len(l))
            row=0
            for key in livre.keys() :
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(key))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(livre[key][0]))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(livre[key][1]))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(livre[key][2]))
                self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(livre[key][3]))
                row+=1

#-----------------------------Suppression d'un livre-------------------------------
class ajout_supprimer_livre_widget(QWidget) :
    def __init__(self) :
        super(ajout_supprimer_livre_widget,self).__init__()
        loadUi("supprimer livre.ui",self)
        self.annuler.clicked.connect(self.Return)
        self.supprimer.clicked.connect(self.Supprimer)
    def Return (self) :
        widget.setCurrentIndex(0)
    def Supprimer(self) :
        ref=self.ref.text()
        if livre=={} :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Dictionnaire est vide! ")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()
        else :
            if not ref :
                msge = QtWidgets.QMessageBox()
                msge.setWindowTitle("ERREUR")
                msge.setText("Saisissiez une Référence ! ")
                msge.setIcon(QtWidgets.QMessageBox.Critical)
                x= msge.exec_()
            elif not ref.isdigit():
                msge = QtWidgets.QMessageBox()
                msge.setWindowTitle("ERREUR")
                msge.setText("Faux Référence ! ")
                msge.setIcon(QtWidgets.QMessageBox.Critical)
                x= msge.exec_()
            else :
              
                l=[]
                for key in livre.keys() :
                    if ref==key :
                        l.append(key)
                        
                        break
                if not l :
                    msge = QtWidgets.QMessageBox()
                    msge.setWindowTitle("ERREUR")
                    msge.setText("Ce livre n'existe pas ! ")
                    msge.setIcon(QtWidgets.QMessageBox.Critical)
                    x= msge.exec_()
                else :
                    livre.pop(l[0])
                    msge = QtWidgets.QMessageBox()
                    msge.setWindowTitle("SUCCES")
                    msge.setText("Livre est supprimé avec succés! ")
                    msge.setIcon(QtWidgets.QMessageBox.Information)
                    x= msge.exec_()
                     
#-----------------------------Suppression des livres d'un auteurs donnés---------------------------
class ajout_supprimer_livre_auteur_widget(QWidget) :
    def __init__(self) :
        super(ajout_supprimer_livre_auteur_widget,self).__init__()
        loadUi("supprimer livre auteur.ui",self)
        self.annuler.clicked.connect(self.Return)
        self.supprimer.clicked.connect(self.Supprimer)
    def Return(self) :
        widget.setCurrentIndex(0)
    def Supprimer(self) :
        auteur=self.auteur.text()
        if livre=={} :
                msge = QtWidgets.QMessageBox()
                msge.setWindowTitle("ERREUR")
                msge.setText("Dictionnaire vide  ! ")
                msge.setIcon(QtWidgets.QMessageBox.Critical)
                x= msge.exec_()
        elif not auteur :
                msge = QtWidgets.QMessageBox()
                msge.setWindowTitle("ERREUR")
                msge.setText("Saisissiez un auteur ! ")
                msge.setIcon(QtWidgets.QMessageBox.Critical)
                x= msge.exec_()
        elif auteur!="" :
                l=[]
                for key in livre.keys() :
                    if auteur==livre[key][1] :
                        print(livre[key][1])
                        l.append(key)
                if not l :
                    msge = QtWidgets.QMessageBox()
                    msge.setWindowTitle("ERREUR")
                    msge.setText("Il n'y a pas de livre qui correspond à  "+auteur+" ! ")
                    msge.setIcon(QtWidgets.QMessageBox.Critical)
                    x= msge.exec_()
                else :
                    for i in l :
                        livre.pop(i)
                    msge = QtWidgets.QMessageBox()
                    msge.setWindowTitle("SUCCES")
                    msge.setText("Les livres sont supprimés avec succés ! ")
                    msge.setIcon(QtWidgets.QMessageBox.Information)
                    x= msge.exec_()
        
#-----------------------------Suppression des livres d'une annee donnee------------------------------------
class ajout_supprimer_livre_annee_widget(QWidget) :
    def __init__(self):
        super(ajout_supprimer_livre_annee_widget,self).__init__()
        loadUi("supprimer livre annee.ui",self)
        self.annuler.clicked.connect(self.Return)
        self.supprimer.clicked.connect(self.Supprimer)
    def Return (self) :
        widget.setCurrentIndex(0)
    def Supprimer(self) :
        annee=self.annee.text()
        if livre=={} :
                msge = QtWidgets.QMessageBox()
                msge.setWindowTitle("ERREUR")
                msge.setText("Dictionnaire vide  ! ")
                msge.setIcon(QtWidgets.QMessageBox.Critical)
                x= msge.exec_()
        elif not annee :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Saissiez l'année!  ")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()
        else :
            today=date.today().year
            if not (int(annee)<=today) :
                msge = QtWidgets.QMessageBox()
                msge.setWindowTitle("ERREUR")
                msge.setText("Faux année ! ")
                msge.setIcon(QtWidgets.QMessageBox.Critical)
                x= msge.exec_()
            else :
                l=[]
                for key in livre.keys() :
                    if annee==livre[key][2] :
                        l.append(key)
                if not l :
                    msge = QtWidgets.QMessageBox()
                    msge.setWindowTitle("ERREUR")
                    msge.setText("Il n'existe pas de livre qui correspond à cette année d'édition   ! ")
                    msge.setIcon(QtWidgets.QMessageBox.Critical)
                    x= msge.exec_()
                else :
                    for i in l :
                        livre.pop(i)
                    msge = QtWidgets.QMessageBox()
                    msge.setWindowTitle("SUCCES")
                    msge.setText("Les livres sont supprimés avec succés  ! ")
                    msge.setIcon(QtWidgets.QMessageBox.Information)
                    x= msge.exec_()
#-----------------------------Modifier le nombre d'exemplaires ---------------------
class ajout_modifier_nbre_d_exemplaires_widget(QWidget) :
    def __init__(self) :
           super(ajout_modifier_nbre_d_exemplaires_widget,self).__init__()
           loadUi("modifier nombre d'exemplaires.ui",self)
           self.annuler.clicked.connect(self.Return)
           self.modifier.clicked.connect(self.Modifier) 
    def Return(self) :
        widget.setCurrentIndex(0)
    def Modifier(self) :
        ref=self.ref.text()
        nb=self.nb.text()
        if livre=={} :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Dictionnaire vide!")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()
        else :
         if not nb :
            self.nberreur.setText("Saisissiez le nombre d'exemplaires")
         elif not nb.isdigit() :
            self.nberreur.setText("Faux nombre !")
            self.nb.clear()
         else :
            self.nberreur.setText("")
         if not ref :
            self.referreur.setText("Saisissiez une référence !")
         elif not ref.isdigit() :
            self.referreur.setText("Faux référence")
            self.ref.clear()
         else :
            self.referreur.setText("")
         n=self.nberreur.text()
         r=self.referreur.text()
         test=False
         if n==r=="" :
            for key in livre.keys() :
                if ref==key :
                    livre[key][3]=nb
                    test=True
         if test==True :
                    msge = QtWidgets.QMessageBox()
                    msge.setWindowTitle("SUCCES")
                    msge.setText("Nombre d'édition est changé avec succés ")
                    msge.setIcon(QtWidgets.QMessageBox.Information)
                    x= msge.exec_() 
         if test==False and ref.isdigit():
            self.referreur.setText("Ce livre n'existe pas ")
         if not ( n==r=="" ):
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Vérifier vos données  ! ")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()
#------------------------------Recherche par Référence -----------------------------------
class ajout_recherche_ref_widget(QWidget) :
    def __init__(self) :
        super(ajout_recherche_ref_widget,self).__init__()
        loadUi("recherche par référence.ui",self)
        self.annuler.clicked.connect(self.Return)
        self.recherche.clicked.connect(self.Recherche)
    def Return(self) :
        widget.setCurrentIndex(0)
    def Recherche(self) :
        ref=self.ref.text()
        if livre=={} :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Dictionnaire vide!")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()
        elif not ref :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Saisissiez une référence !")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_() 
        elif not ref.isdigit() :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Faux référence ! ")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_() 
        else :
            test=False
            for key in livre.keys() :
                if ref==key :
                    self.tableWidget.setRowCount(1)
                    self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(key))
                    self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(livre[key][0]))
                    self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(livre[key][1]))
                    self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem(livre[key][2]))
                    self.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem(livre[key][3]))
                    test=True
                    break
            if test==False :
                    msge = QtWidgets.QMessageBox()
                    msge.setWindowTitle("ERREUR")
                    msge.setText("Référence n'existe pas ! ")
                    msge.setIcon(QtWidgets.QMessageBox.Critical)
                    x= msge.exec_()      

#-------------------------------Recherche par titre ---------------------------------------
class ajout_recherche_titre_widget(QWidget) :
    def __init__(self) :
        super(ajout_recherche_titre_widget,self).__init__()
        loadUi("recherche par titre.ui",self)
        self.annuler.clicked.connect(self.Return)
        self.recherche.clicked.connect(self.Recherche)
    def Return (self) :
        widget.setCurrentIndex(0)
    def Recherche(self) :
        titre=self.titre.text()
        if livre=={} :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Dictionnaire vide!")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()
        elif not titre :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Saisissiez un titre !")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()  
        else :
            test=False
            row=0
            l=[]
            for key in livre.keys() :
                if titre==livre[key][0] :
                    test=True
                    l.append(key)
            if test==False :
                msge = QtWidgets.QMessageBox()
                msge.setWindowTitle("ERREUR")
                msge.setText("Ce livre n'existe pas !")
                msge.setIcon(QtWidgets.QMessageBox.Critical)
                x= msge.exec_() 
            
            else :
                self.tableWidget.setRowCount(len(l))
                for key in livre.keys() :
                    if titre==livre[key][0] :
                        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(key))
                        self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(livre[key][0]))
                        self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(livre[key][1]))
                        self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(livre[key][2]))
                        self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(livre[key][3]))
                        row+=1
            
#--------------------------------Recherche par année d'édition-------------------------------------
class ajout_recherche_annee_widget(QWidget) :
    def __init__(self) :
        super(ajout_recherche_annee_widget,self).__init__()
        loadUi("recherche par annee.ui",self)
        self.annuler.clicked.connect(self.Return)
        self.recherche.clicked.connect(self.Recherche)
    def Return(self) :
        widget.setCurrentIndex(0)
    def Recherche(self) :
        annee=self.annee.text()
        today=date.today().year

        if livre=={} :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Dictionnaire vide!")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()

        elif not annee :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Saisissiez l'année d'édition!")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()
        elif not annee.isdigit() :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Faux année !")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()

        elif  int(annee) >today :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Faux année !")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()
        else :
            l=[]
            for key in livre.keys() :
                if annee==livre[key][2] :
                    l.append(key)
            if not l :
                msge = QtWidgets.QMessageBox()
                msge.setWindowTitle("ERREUR")
                msge.setText("Cette année d'édition n'existe pas !")
                msge.setIcon(QtWidgets.QMessageBox.Critical)
                x= msge.exec_()
            else :
                row=0
                self.tableWidget.setRowCount(len(l))
                for key in livre.keys() :
                    if annee==livre[key][2] :
                        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(key))
                        self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(livre[key][0]))
                        self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(livre[key][1]))
                        self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(livre[key][2]))
                        self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(livre[key][3]))
                        row+=1

#-------------------------------Recherche par auteur donné----------------------------
class ajout_recherche_auteur_widget(QWidget) :
    def __init__(self) :
        super(ajout_recherche_auteur_widget,self).__init__()
        loadUi("recherche par auteur.ui",self)
        self.annuler.clicked.connect(self.Return)
        self.recherche.clicked.connect(self.Recherche)
    def Return(self) :
        widget.setCurrentIndex(0)
    def Recherche(self) :
        auteur=self.auteur.text()
        if livre=={} :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Dictionnaire vide!")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()
        elif not auteur :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Saisissiez le nom et le prénom de l'auteur!")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()
        else :
            test=True
            for i in auteur :
                if not("A"<=i<="Z" or "a"<=i<="z" or i==" " ) :
                    test=False
                    msge = QtWidgets.QMessageBox()
                    msge.setWindowTitle("ERREUR")
                    msge.setText("Faux nom!")
                    msge.setIcon(QtWidgets.QMessageBox.Critical)
                    x= msge.exec_()
                    break
            if test==True:
                    l=[]
                    for key in livre.keys() :
                        if auteur==livre[key][1] :
                            l.append(key)
                    if not l :
                        msge = QtWidgets.QMessageBox()
                        msge.setWindowTitle("ERREUR")
                        msge.setText("Ce nom n'existe pas !")
                        msge.setIcon(QtWidgets.QMessageBox.Critical)
                        x= msge.exec_()
                    else :
                        row=0
                        self.tableWidget.setRowCount(len(l))
                        for key in livre.keys() :
                            if auteur==livre[key][1] :
                                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(key))
                                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(livre[key][0]))
                                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(livre[key][1]))
                                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(livre[key][2]))
                                self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(livre[key][3]))
                                row+=1

#-------------------------------Affichage par tri-------------------------------------------
class ajout_affichage_widget(QWidget) :
    def __init__(self) :
        super(ajout_affichage_widget,self).__init__()
        loadUi("affichage_tri.ui",self)
        self.affichage()
        self.annuler.clicked.connect(self.Return)
    def Return(self) :
        widget.setCurrentIndex(0)
    def affichage(self) :
        if livre=={} :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Dictionnaire vide!")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()
        else :
            l=[]
            titres_tries = sorted([(ref, livre[ref][0]) for ref in livre], key=lambda x: x[1])
            livre_trie = {}
            for ref, titre in titres_tries:
                livre_trie[ref] = livre[ref]
            for key in livre_trie.keys():
                l.append(key)
            row=0
            self.tableWidget.setRowCount(len(l))
            for key in livre_trie.keys() :
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(key))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(livre[key][0]))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(livre[key][1]))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(livre[key][2]))
                self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(livre[key][3]))
                row+=1

#-------------------------------Ajouter un nouvel emprunt--------------------------------
class ajout_emprunt_widget(QWidget) :
    def __init__(self) :
        super(ajout_emprunt_widget,self).__init__()
        loadUi("ajout emprunt.ui",self)
        self.annuler.clicked.connect(self.Return)
        self.ajouter.clicked.connect(self.Ajouter)
    def Return(self) :
        widget.setCurrentIndex(0)
    def Ajouter(self) :
        num=self.num.text()
        if not livre :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Dictionnaire Livre est vide  !")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()
        if not etudiant :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Dictionnaire Etudiant est vide  !")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()
        else:
         if not num :
            self.numerreur.setText("Saisissiez un numéro d'inscription")
         elif not num.isdigit() :
            self.num.clear()
            self.numerreur.setText("Faux numéro d'inscription")
         else :
            test=False
            ok=False
            retour=False
            for key in etudiant.keys() :
                if num==key  :
                    test=True
                    break
            for key in emprunt.keys() :
                if key==num :  
                 ok=True  
                 if emprunt[num][2] :
                    retour=True
                

            if ok ==False :
                retour=True
            if test==False :
                self.numerreur.setText("Cet élève n'existe pas")
            elif retour==False :
                self.numerreur.setText("Cet élève a dejà emprunté un livre ")
            else :
                self.numerreur.setText("")
         n=self.numerreur.text()
         ref=self.ref.text()
         if not ref :
            self.referreur.setText("Saisissiez une référence ")
         elif not ref.isdigit() :
            self.ref.clear()
            self.referreur.setText("Faux référence")
         else :
            test1=False
            for key in livre.keys() :
                if ref==key and int(livre[key][3]) >0 :
                    c=key
                    test1=True
                    break
            if test1==False :
                self.referreur.setText("Ce livre n'existe pas")
            else :
                self.referreur.setText("")
         r=self.referreur.text()
         dat=self.date.text()
         day=date.today().day
         month=date.today().month
         year=date.today().year
         datee = datetime.strptime(dat, "%d/%m/%Y")
         today=str(day)+'/'+str(month)+'/'+str(year)
         datej = datetime.strptime(today, "%d/%m/%Y")
        

        

         if not(datee<=datej) :
            self.dateerreur.setText("Faux date")
         else :
            self.dateerreur.setText("")
         d=self.dateerreur.text()
         dr=None
         if (d==r==n=="") and retour==True :
            livre[c][3]=str(int(livre[c][3])-1)
            emprunt[num]=[ref,dat,dr]
            print(emprunt)
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("SUCCES")
            msge.setText("Emprunt est ajouté avec succès !")
            msge.setIcon(QtWidgets.QMessageBox.Information)
            x= msge.exec_()
         else :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Vérifiez vos données !")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()

#--------------------------------Retour d'emprunt--------------------------------
class retour_widget(QWidget) :
    def __init__(self) :
        super(retour_widget,self).__init__()
        loadUi("retour emprunt.ui",self)
        self.annuler.clicked.connect(self.Return)
        self.ajouter.clicked.connect(self.Ajouter)
    def Return (self) :
        widget.setCurrentIndex(0)
    def Ajouter(self) :
        num=self.num.text()
        if emprunt=={} :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Dictionnaire Emprunt vide!")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()
        if livre=={} :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Dictionnaire Livre vide!")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()

        elif livre and emprunt  :
         if not num :
            self.numerreur.setText("Saisissiez un numéro d'inscription")
         elif not num.isdigit() :
            self.num.clear()
            self.numerreur.setText("Faux numéro d'inscription")
         else :
            test=False
            for key in emprunt.keys() :
                if num==key :
                    test=True
                    break
            if test:
                self.numerreur.setText("")
            elif not test :
                self.numerreur.setText("Emprunt n'existe pas")
            
         n=self.numerreur.text()
         dat=self.date.text()
         day=date.today().day
         month=date.today().month
         year=date.today().year
         datee = datetime.strptime(dat, "%d/%m/%Y")
         today=str(day)+'/'+str(month)+'/'+str(year)
         datej = datetime.strptime(today, "%d/%m/%Y")


         if not(datee<=datej ) :
            self.dateerreur.setText("Faux date")
         else :
            self.dateerreur.setText("")
         d=self.dateerreur.text()
         

         if(n==d=="") :
            for key in emprunt.keys() :
                if num==key  :
                    if  emprunt[key][2]:
                      msge = QtWidgets.QMessageBox()
                      msge.setWindowTitle("ERREUR")
                      msge.setText("Cet étudiant a déjà retourné ce livre le "+emprunt[key][2])
                      msge.setIcon(QtWidgets.QMessageBox.Critical)
                      x= msge.exec_()
                      break
                    else :
                      date_emprunte=datetime.strptime(emprunt[key][1], "%d/%m/%Y")
                      if (datee < date_emprunte) :
                        self.dateerreur.setText("Vérifier votre  date de retour !")
                        d=self.dateerreur.text()
                        break 
                     
                      else :
                        emprunt[key][2]=dat
                        livre[emprunt[key][0]][3]=str(int(livre[emprunt[key][0]][3])+1)
                        msge = QtWidgets.QMessageBox()
                        msge.setWindowTitle("SUCCES")
                        msge.setText("L'opération de retour est effectué avec succés !")
                        msge.setIcon(QtWidgets.QMessageBox.Information)
                        x= msge.exec_()
                        break
                     
                 
         else :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Vérifiez vos données !")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()

#--------------------------Supprimer un emprunt-------------------------------------------
class supprimer_emprunt_widget(QWidget) :
    def __init__(self) :
        super(supprimer_emprunt_widget,self).__init__()
        loadUi("supprimer emprunt.ui",self)
        self.annuler.clicked.connect(self.Return)
        self.supprimer.clicked.connect(self.Supprimer)
    def Return (self) :
        widget.setCurrentIndex(0)
    def Supprimer(self) :
        num=self.num.text()
        if emprunt=={} :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Dictionnaire est vide! ")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()
        else :
            if not num :
                msge = QtWidgets.QMessageBox()
                msge.setWindowTitle("ERREUR")
                msge.setText("Saisissiez un numéro d'inscription ! ")
                msge.setIcon(QtWidgets.QMessageBox.Critical)
                x= msge.exec_()
            elif not num.isdigit():
                self.num.clear()
                msge = QtWidgets.QMessageBox()
                msge.setWindowTitle("ERREUR")
                msge.setText("Faux Numéro d'inscription ! ")
                msge.setIcon(QtWidgets.QMessageBox.Critical)
                x= msge.exec_()
            else :
              
                l=[]
                for key in emprunt.keys() :
                    if num==key :
                        l.append(key)
                        
                        break
                if not l :
                    msge = QtWidgets.QMessageBox()
                    msge.setWindowTitle("ERREUR")
                    msge.setText("Emprunt n'existe pas ! ")
                    msge.setIcon(QtWidgets.QMessageBox.Critical)
                    x= msge.exec_()
                else :
                    emprunt.pop(l[0])
                    msge = QtWidgets.QMessageBox()
                    msge.setWindowTitle("SUCCES")
                    msge.setText("Emprunt est supprimé avec succés! ")
                    msge.setIcon(QtWidgets.QMessageBox.Information)
                    x= msge.exec_()
#--------------------------Modifer la date d'emprunt--------------------------------
class modifier_date_d_emprunt_widget(QWidget) :
    def __init__(self) :
        super(modifier_date_d_emprunt_widget,self).__init__()
        loadUi("modifier date d'emprunt.ui",self)
        self.annuler.clicked.connect(self.Return)
        self.modifier.clicked.connect(self.Modifier)
    def Return(self) :
        widget.setCurrentIndex(0)
    def Modifier(self) :
        num=self.num.text()
        dat=self.date.text()
        if emprunt=={} :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Dictionnaire est vide! ")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()
        else :
         if not (num):
                self.numerreur.setText("Saisissez le numéro de l'inscription  !")
         elif not (num.isdigit()):
                self.numerreur.setText("Faux numéro d'inscription")
                self.num.clear()
         elif num.isdigit() :
            test=False
            for key in emprunt.keys() :
                if num==key :
                    test=True
                    cle=key
                    break
            if test==False :
                self.numerreur.setText("Emprunt n'existe pas")
            else :
                self.numerreur.setText("")
    
         numresultat=self.numerreur.text()
         dat=self.date.text()
         day=date.today().day
         month=date.today().month
         year=date.today().year
         datee = datetime.strptime(dat, "%d/%m/%Y")
         today=str(day)+'/'+str(month)+'/'+str(year)
         datej = datetime.strptime(today, "%d/%m/%Y")
         if numresultat=="" :
          if emprunt[cle][2] :
           dateretour=datetime.strptime(emprunt[cle][2], "%d/%m/%Y")
           if not( datee<=dateretour) :
            self.dateerreur.setText(" la nouvelle date doit etre  avant "+emprunt[cle][2])                
           else :
            self.dateerreur.setText("")
         d=self.dateerreur.text()
         if d==numresultat=="" :
            for key in emprunt.keys() :
                if num==key :
                    emprunt[key][1]=dat
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("SUCCES")
            msge.setText("Date d'emprunt est modifié avec succés !")
            msge.setIcon(QtWidgets.QMessageBox.Information)
            x= msge.exec_()
         else :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Vérifiez vos données !")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()

#---------------------------------Modifier la date de retour-----------------------------------
class modifier_date_de_retour_widget(QWidget) :
    def __init__(self):
        super(modifier_date_de_retour_widget,self).__init__()
        loadUi("modifier date de retour.ui",self)
        self.annuler.clicked.connect(self.Return)
        self.modifier.clicked.connect(self.Modifier)
    def Return (self) :
        widget.setCurrentIndex(0)
    def Modifier(self) :
        num=self.num.text()
        dat=self.date.text()
        if not emprunt :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Dictionnaire est vide! ")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()
        else :
         if not (num):
                self.numerreur.setText("Saisissez le numéro de l'inscription  !")
         elif not (num.isdigit()):
                self.numerreur.setText("Faux numéro d'inscription")
                self.num.clear()
         elif num.isdigit() :
            test=False
            for key in emprunt.keys() :
                if num==key :
                    test=True
                    c=emprunt[key][1]
                    break
            if test==False :
                self.numerreur.setText("Emprunt n'existe pas")
            else :
                self.numerreur.setText("")
    
         numresultat=self.numerreur.text()
         dat=self.date.text()
         day=date.today().day
         month=date.today().month
         year=date.today().year
         datee = datetime.strptime(dat, "%d/%m/%Y")
         today=str(day)+'/'+str(month)+'/'+str(year)
         datej = datetime.strptime(today, "%d/%m/%Y")
         ta,tb =True,True
         if not datee<=datej :
            self.dateerreur.setText("Faux date !")
            tb=False
         if numresultat=="" :
          date_2 = datetime.strptime(c, "%d/%m/%Y")
          if not( datee >=date_2) :
            self.dateerreur.setText("Date de retour doit etre après  "+c)
            ta=False
         if ta and tb :
            self.dateerreur.setText("")
         d=self.dateerreur.text()
         if d==numresultat=="" :
            for key in emprunt.keys() :
                if num==key :
                    emprunt[key][2]=dat
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("SUCCES")
            msge.setText("Date de retour est modifié avec succés !")
            msge.setIcon(QtWidgets.QMessageBox.Information)
            x= msge.exec_()
         else :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Vérifiez vos données !")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()








#---------------------------------Affichage dictionnaire emprunts------------------------------
class affichage_dic_emprunt_widget(QWidget) : 
    def __init__(self) :
        super(affichage_dic_emprunt_widget,self).__init__()
        loadUi("affichage dic emprunt.ui",self)
        self.affichage()
        self.annuler.clicked.connect(self.Return)
    def Return(self) :
        widget.setCurrentIndex(0)
    def affichage(self) :
        if emprunt=={} :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Dictionnaire vide!")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()
            widget.setCurrentIndex(0)
        else :
            l=[]
            row=0

            for key in emprunt.keys() :
                l.append(key)
            self.tableWidget.setRowCount(len(l))
            for key in emprunt.keys() :
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(key))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(emprunt[key][0]))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(emprunt[key][1]))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(emprunt[key][2]))
                row+=1

#----------------------------------Affichage d'emprunt par étudiant---------------------
class recherche_emprunt_par_etudiant(QWidget) :
    def __init__(self) :
        super(recherche_emprunt_par_etudiant,self).__init__()
        loadUi("afficher_emprunt par etudiant.ui",self)
        self.annuler.clicked.connect(self.Return)
        self.recherche.clicked.connect(self.Afficher)
    def Return (self) :
        widget.setCurrentIndex(0)
    def Afficher(self) :
        num=self.num.text()
        if emprunt=={} :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Dictionnaire est vide ")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()    
        elif not num :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Saisissiez un Numéro d'inscription")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()    
        elif not num.isdigit() :
            self.num.clear()
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Faux numéro ")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()    
        else :
            test=False
            for key in emprunt.keys() :
                if num==key :
                    test=True
                    self.tableWidget.setRowCount(1)
                    self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(key))
                    self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(emprunt[key][0]))
                    self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(emprunt[key][1]))
                    self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem(emprunt[key][2]))
                    break 
            if test==False :
                msge = QtWidgets.QMessageBox()
                msge.setWindowTitle("ERREUR")
                msge.setText("Cet étudiant n'existe pas ! ")
                msge.setIcon(QtWidgets.QMessageBox.Critical)
                x= msge.exec_()  

#-----------------------------------Affichage d'emprunt par date----------------------------
class recherche_emprunt_par_date(QWidget) :
    def __init__(self) :
        super(recherche_emprunt_par_date,self).__init__()
        loadUi("afficher_emprunt par date.ui",self)
        self.annuler.clicked.connect(self.Return)
        self.recherche.clicked.connect(self.Recherche)
    def Return (self) :
        widget.setCurrentIndex(0)
    def Recherche (self) :
        dat=self.date.text()
        day=date.today().day
        month=date.today().month
        year=date.today().year
        datee = datetime.strptime(dat, "%d/%m/%Y")
        today=str(day)+'/'+str(month)+'/'+str(year)
        datej = datetime.strptime(today, "%d/%m/%Y")
        if emprunt=={} :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Dictionnaire Emprunt est vide! ")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()
        if  livre=={} :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Dictionnaire Livre est vide! ")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()
        else :
         if not(datee<=datej) :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Faux date ! ")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()
         else :
                l=[]
                for key in emprunt.keys() :
                    occ=True
                    if dat==emprunt[key][1] :
                        if  l==[] :
                            l.append(emprunt[key][0])
                        else :
                            for i in range(len(l)) :
                                if l[i]==emprunt[key][0] :
                                    occ=False
                                    break
                            if occ==True :
                             l.append(emprunt[key][0])

                    
                if not l :
                    self.tableWidget.setRowCount(0)
                    msge = QtWidgets.QMessageBox()
                    msge.setWindowTitle("ERREUR")
                    msge.setText("Il  n'existe pas des livres empruntés à cette date ! ")
                    msge.setIcon(QtWidgets.QMessageBox.Critical)
                    x= msge.exec_()
                else :
                    self.tableWidget.setRowCount(len(l))
                    row=0
                    for i in l :
                            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(i))
                            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(livre[i][0]))
                            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(livre[i][1]))
                            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(livre[i][2]))
                            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(livre[i][3]))
                            row+=1

#(----------------------------------Affichage d'emprunt par date de retour--------------------------------
class recherche_emprunt_par_date_retour(QWidget) :
    def __init__(self):
        super(recherche_emprunt_par_date_retour,self).__init__()
        loadUi("afficher_emprunt par date retour.ui",self)
        self.annuler.clicked.connect(self.Return)
        self.afficher.clicked.connect(self.Recherche)
    def Return(self) :
        widget.setCurrentIndex(0)
    def Recherche(self) :
        if emprunt=={} :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Dictionnaire Emprunt est vide! ")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()
        if livre=={} :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Dictionnaire Livre  est vide! ")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()
        else :
         dat=self.date.text()
         day=date.today().day
         month=date.today().month
         year=date.today().year
         datee = datetime.strptime(dat, "%d/%m/%Y")
         today=str(day)+'/'+str(month)+'/'+str(year)
         datej = datetime.strptime(today, "%d/%m/%Y")
         if not(datee <= datej) :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Faux date ! ")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()
         else :
                l=[]
                for key in emprunt.keys() :
                    occ=True
                    if dat==emprunt[key][2] and emprunt[key][2] :
                        if  l==[] :
                            l.append(emprunt[key][0])
                        else :
                            for i in range(len(l)) :
                                if l[i]==emprunt[key][0] :
                                    occ=False
                                    break
                            if occ==True :
                             l.append(emprunt[key][0])
                    
                if not l :
                    msge = QtWidgets.QMessageBox()
                    msge.setWindowTitle("ERREUR")
                    msge.setText("Il n'existe pas des livres retournés à cette date ! ")
                    msge.setIcon(QtWidgets.QMessageBox.Critical)
                    x= msge.exec_()
                else :
                    self.tableWidget.setRowCount(len(l))
                    row=0
                    for i in l :
                        
                            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(i))
                            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(livre[i][0]))
                            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(livre[i][1]))
                            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(livre[i][2]))
                            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(livre[i][3]))
                            row+=1
 
#---------------Affichage d'emprunt entre deux dates d'emprunts----------------------------
class recherche_entre_deux_dates_emprunts_widget(QWidget) :
    def __init__(self) :
        super(recherche_entre_deux_dates_emprunts_widget,self).__init__()
        loadUi("afficher_emprunt entre deux dates empruntes.ui",self)
        self.annuler.clicked.connect(self.Return)
        self.afficher.clicked.connect(self.Recherche)
    def Return (self) :
        widget.setCurrentIndex(0)
    def Recherche(self) :
        if emprunt=={} :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Dictionnaire Emprunt est vide! ")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()
        if  livre=={} :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Dictionnaire Livre est vide! ")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()
        else :
         dat1=self.date1.text()
         dat2=self.date2.text()
         day=date.today().day
         month=date.today().month
         year=date.today().year
         today=str(day)+'/'+str(month)+'/'+str(year)
         date_1 = datetime.strptime(dat1, "%d/%m/%Y")
         date_2 = datetime.strptime(dat2, "%d/%m/%Y")

         datej = datetime.strptime(today, "%d/%m/%Y")
         if not (date_1<=datej) :
            self.erreur1.setTet("Faux date !")

                       
         else :
            self.erreur1.setText("")
         d1=self.erreur1.text()
        
         if not (date_2>=date_1 and date_2<=datej ) :
            self.erreur2.setText("Faux date")
         else :
            self.erreur2.setText("")
         d2=self.erreur2.text()
         if d2==d1=="" :
            l=[]
            occ=True
            for key in emprunt.keys() :
                    occ=True

                    d = datetime.strptime(emprunt[key][1], "%d/%m/%Y")
                    if date_1<=d<=date_2 :
                            if  l==[] :
                             l.append(emprunt[key][0])
                            else :
                             for i in range(len(l)) :
                                if l[i]==emprunt[key][0] :
                                    occ=False
                                    break
                             if occ==True :
                              l.append(emprunt[key][0])
            if not l :
                    msge = QtWidgets.QMessageBox()
                    msge.setWindowTitle("ERREUR")
                    msge.setText("Il n'existe pas des livres empruntés entre ces deux dates ! ")
                    msge.setIcon(QtWidgets.QMessageBox.Critical)
                    x= msge.exec_()
            else :
                self.tableWidget.setRowCount(len(l))
                row=0
                for i in l :
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(i))
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(livre[i][0]))
                    self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(livre[i][1]))
                    self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(livre[i][2]))
                    self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(livre[i][3]))

                    row+=1
         else :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Vérifiez vos données! ")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()

#-------------------------------Affichage d'emprunt entre deux dates de retour--------------------------------------
class recherche_entre_deux_dates_retours_widget(QWidget) :
    def __init__(self) :
        super(recherche_entre_deux_dates_retours_widget,self).__init__()
        loadUi("afficher_emprunt entre deux dates de retour.ui",self)
        self.annuler.clicked.connect(self.Return)
        self.afficher.clicked.connect(self.Recherche)
    def Return (self) :
        widget.setCurrentIndex(0)
    def Recherche(self) :
        if emprunt=={} :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Dictionnaire Emprunt est vide! ")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()
        if  livre=={} :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Dictionnaire Livre est vide! ")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()
        else :
         dat1=self.date1.text()
         dat2=self.date2.text()
         day=date.today().day
         month=date.today().month
         year=date.today().year
         today=str(day)+'/'+str(month)+'/'+str(year)
         date_1 = datetime.strptime(dat1, "%d/%m/%Y")
         date_2 = datetime.strptime(dat2, "%d/%m/%Y")

         datej = datetime.strptime(today, "%d/%m/%Y")
         if not (date_1<=datej) :
            self.erreur1.setTet("Faux date !")

                       
         else :
            self.erreur1.setText("")
         d1=self.erreur1.text()
        
         if not (date_2>=date_1 and date_2<=datej ) :
            self.erreur2.setText("Faux date")
         else :
            self.erreur2.setText("")
         d2=self.erreur2.text()
         if d2==d1=="" :
            l=[]
            occ=True
            for key in emprunt.keys() :
                if emprunt[key][2]  :
                    d = datetime.strptime(emprunt[key][2], "%d/%m/%Y")
                    if date_1<=d<=date_2 :
                            if  l==[] :
                             l.append(emprunt[key][0])
                            else :
                             for i in range(len(l)) :
                                if l[i]==emprunt[key][0] :
                                    occ=False
                                    break
                             if occ==True :
                              l.append(emprunt[key][0])
            if not l :
                    msge = QtWidgets.QMessageBox()
                    msge.setWindowTitle("ERREUR")
                    msge.setText("Il n'existe pas des livres retournés entre ces deux dates ! ")
                    msge.setIcon(QtWidgets.QMessageBox.Critical)
                    x= msge.exec_()
            else :
                self.tableWidget.setRowCount(len(l))
                row=0
                for i in l :
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(i))
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(livre[i][0]))
                    self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(livre[i][1]))
                    self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(livre[i][2]))
                    self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(livre[i][3]))

                    row+=1
         else :
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("ERREUR")
            msge.setText("Vérifiez vos données! ")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x= msge.exec_()


    

       
app = QApplication(sys.argv)
mainwindow = main()

widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)

widget.setWindowFlags(Qt.FramelessWindowHint)
widget.setAttribute(Qt.WA_TranslucentBackground)
widget.setFixedHeight(700)
widget.setFixedWidth(1000)
widget.show()


msge = QtWidgets.QMessageBox()
msge.setWindowTitle("")
msge.setText("FAITES LA RECUPERATION! ")
msge.setIcon(QtWidgets.QMessageBox.Critical)
x = msge.exec_()
app.exec_()
