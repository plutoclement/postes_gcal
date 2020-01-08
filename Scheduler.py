# coding: utf8
# @author Clement Jany
# @date 2017 - all rights reserved

from PyQt5 import QtWidgets
from  gui import Ui_Form
import sys
import datetime
import calendar
import json

import gcal



class Scheduler(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.mygui = Ui_Form()
        self.mygui.setupUi(self)
        
        self.Week=0
        self.Year = 0
        self.Mygcal = gcal.gcal()
        self.postes = {} 
        self.haschanged = 0
        self.weekdays = []
        
        
        self.initialize()

        
        
        
    def bind_radio(self):
        for i in self.weekdays:
            for j in self.postes:
                #print(type(i),type(j))
                eval('self.mygui.radioButton_'+i+'_'+j+'.clicked.connect(self.changed)')
                
    def changed(self,arg):
        self.haschanged = 1
        
    def MondayoftheWeek(self,year, week):
        d = datetime.date(year,1,1)
        if(d.weekday()>3):
            d = d+datetime.timedelta(7-d.weekday())
        else:
            d = d - datetime.timedelta(d.weekday())
        dlt = datetime.timedelta(days = (week-1)*7)
        return d + dlt


    def initialize(self):
        self.weekdays = ["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
        self.get_postes()    
        print(self.postes)
        self.thisWeek()
        self.mygui.pushButton_4.clicked.connect(self.nextWeek)
        self.mygui.pushButton_5.clicked.connect(self.prevWeek)
        self.mygui.pushButton.clicked.connect(self.thisWeek)        
        self.mygui.pushButton_enregistrer.clicked.connect(self.saveWeekcal)
        self.mygui.pushButton_quitter.clicked.connect(self.close)
        self.bind_radio()

    def get_postes(self):
        with open('postes.txt', 'r') as file:
            self.postes = json.load(file)        
            
    def setWeek(self):
        
        # Create datetime for each day
        self.lundi = self.MondayoftheWeek(self.Year,self.Week)
        self.mardi = self.lundi + datetime.timedelta(days=1)
        self.mercredi = self.lundi + datetime.timedelta(days=2)
        self.jeudi = self.lundi + datetime.timedelta(days=3)
        self.vendredi = self.lundi + datetime.timedelta(days=4)
        self.samedi = self.lundi + datetime.timedelta(days=5)
        self.dimanche = self.lundi + datetime.timedelta(days=6)
        
        # Get week number
        actualWeek = self.lundi.isocalendar()[1]
        self.mygui.label_semaine.setText("Semaine "+str(actualWeek))

        # actualize dates on the gui
        self.mygui.label_lundi.setText(self.lundi.strftime("%d %b %Y"))
        self.mygui.label_mardi.setText(self.mardi.strftime("%d %b %Y"))
        self.mygui.label_mercredi.setText(self.mercredi.strftime("%d %b %Y"))
        self.mygui.label_jeudi.setText(self.jeudi.strftime("%d %b %Y"))
        self.mygui.label_vendredi.setText(self.vendredi.strftime("%d %b %Y"))
        self.mygui.label_samedi.setText(self.samedi.strftime("%d %b %Y"))
        self.mygui.label_dimanche.setText(self.dimanche.strftime("%d %b %Y"))
        
        # load gcalendar
        self.loadWeekcal()
        
        #print(monday.isoformat())
        #print(self.Mygcal.read(monday))
        
    def nextWeek(self):
        self.Week += 1
        self.setWeek()
        
    def prevWeek(self):
        self.Week -= 1
        self.setWeek()    
    
    def thisWeek(self):
        now = datetime.datetime.now()
        self.Year = now.isocalendar()[0]
        self.Week = now.isocalendar()[1]
        
        self.setWeek()    
        
    def gcal_event(self,day,poste):
        dstart = eval('self.'+day)
        
        if poste == "nuit":
            dstop = dstart++ datetime.timedelta(days=1)
        else :
            dstop = dstart
        print(poste)
        if poste != "repos":
            gcal_event = {
                'summary': self.postes[poste]["nom"],
              'location': '',
              'description': 'Dernière modification :'+datetime.datetime.now().strftime("%d/%m/%y"),
              'start': {
                  'dateTime': dstart.isoformat()+'T'+self.postes[poste]["heure_debut"]+':00+01:00',
                'timeZone': 'Europe/Paris',
                },
              'end': {
                  'dateTime': dstop.isoformat()+'T'+self.postes[poste]["heure_fin"]+':00+01:00',
                'timeZone': 'Europe/Paris',
                },
            }
        else:
            gcal_event = 0
        return gcal_event     
    
    
    def loadWeekcal(self):
        for i in self.weekdays:
            poste = self.Mygcal.read(eval('self.'+i))
            if poste != 0:
                print(i,poste.lower())
                eval('self.mygui.radioButton_'+i+'_'+poste.lower()+'.setChecked(True)')
            else:
                eval('self.mygui.radioButton_'+i+'_repos.setChecked(True)')
            
    def saveWeekcal(self):
        
        for i in self.weekdays:
            self.Mygcal.delete_event(eval('self.'+i))
            for j in self.postes:
                if eval('self.mygui.radioButton_'+i+'_'+j+'.isChecked()'):
                    self.Mygcal.create_event(self.gcal_event(i,j))
                    print(self.gcal_event(i,j))
        self.haschanged = 0
        
    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the window?',
                                                 QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
    
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
            print('Window closed')
        else:
            event.ignore()    
            
app = QtWidgets.QApplication([])    
application = Scheduler()
application.show()
sys.exit(app.exec())
