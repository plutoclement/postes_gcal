# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\cj\Scheduler_WAndreea\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(432, 333)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        Form.setAutoFillBackground(False)
        self.pushButton_quitter = QtWidgets.QPushButton(Form)
        self.pushButton_quitter.setGeometry(QtCore.QRect(310, 290, 75, 23))
        self.pushButton_quitter.setObjectName("pushButton_quitter")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 10, 243, 46))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_10.addWidget(self.pushButton_5)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_10.addWidget(self.pushButton)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_10.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.label_semaine = QtWidgets.QLabel(self.layoutWidget)
        self.label_semaine.setAlignment(QtCore.Qt.AlignCenter)
        self.label_semaine.setObjectName("label_semaine")
        self.verticalLayout.addWidget(self.label_semaine)
        self.pushButton_enregistrer = QtWidgets.QPushButton(Form)
        self.pushButton_enregistrer.setGeometry(QtCore.QRect(310, 260, 75, 23))
        self.pushButton_enregistrer.setObjectName("pushButton_enregistrer")
        self.pushButton_reset = QtWidgets.QPushButton(Form)
        self.pushButton_reset.setGeometry(QtCore.QRect(230, 260, 75, 23))
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(11, 84, 380, 154))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_lundi = QtWidgets.QLabel(self.layoutWidget1)
        self.label_lundi.setObjectName("label_lundi")
        self.horizontalLayout.addWidget(self.label_lundi)
        self.radioButton_lundi_matin = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton_lundi_matin.setObjectName("radioButton_lundi_matin")
        self.horizontalLayout.addWidget(self.radioButton_lundi_matin)
        self.radioButton_lundi_soir = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton_lundi_soir.setObjectName("radioButton_lundi_soir")
        self.horizontalLayout.addWidget(self.radioButton_lundi_soir)
        self.radioButton_lundi_nuit = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton_lundi_nuit.setObjectName("radioButton_lundi_nuit")
        self.horizontalLayout.addWidget(self.radioButton_lundi_nuit)
        self.radioButton_lundi_repos = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton_lundi_repos.setObjectName("radioButton_lundi_repos")
        self.horizontalLayout.addWidget(self.radioButton_lundi_repos)
        self.layoutWidget2 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        spacerItem1 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.label_mardi = QtWidgets.QLabel(self.layoutWidget2)
        self.label_mardi.setObjectName("label_mardi")
        self.horizontalLayout_8.addWidget(self.label_mardi)
        self.radioButton_mardi_matin = QtWidgets.QRadioButton(self.layoutWidget2)
        self.radioButton_mardi_matin.setObjectName("radioButton_mardi_matin")
        self.horizontalLayout_8.addWidget(self.radioButton_mardi_matin)
        self.radioButton_mardi_soir = QtWidgets.QRadioButton(self.layoutWidget2)
        self.radioButton_mardi_soir.setObjectName("radioButton_mardi_soir")
        self.horizontalLayout_8.addWidget(self.radioButton_mardi_soir)
        self.radioButton_mardi_nuit = QtWidgets.QRadioButton(self.layoutWidget2)
        self.radioButton_mardi_nuit.setObjectName("radioButton_mardi_nuit")
        self.horizontalLayout_8.addWidget(self.radioButton_mardi_nuit)
        self.radioButton_mardi_repos = QtWidgets.QRadioButton(self.layoutWidget2)
        self.radioButton_mardi_repos.setObjectName("radioButton_mardi_repos")
        self.horizontalLayout_8.addWidget(self.radioButton_mardi_repos)
        self.layoutWidget3 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.label_mercredi = QtWidgets.QLabel(self.layoutWidget3)
        self.label_mercredi.setObjectName("label_mercredi")
        self.horizontalLayout_6.addWidget(self.label_mercredi)
        self.radioButton_mercredi_matin = QtWidgets.QRadioButton(self.layoutWidget3)
        self.radioButton_mercredi_matin.setObjectName("radioButton_mercredi_matin")
        self.horizontalLayout_6.addWidget(self.radioButton_mercredi_matin)
        self.radioButton_mercredi_soir = QtWidgets.QRadioButton(self.layoutWidget3)
        self.radioButton_mercredi_soir.setObjectName("radioButton_mercredi_soir")
        self.horizontalLayout_6.addWidget(self.radioButton_mercredi_soir)
        self.radioButton_mercredi_nuit = QtWidgets.QRadioButton(self.layoutWidget3)
        self.radioButton_mercredi_nuit.setObjectName("radioButton_mercredi_nuit")
        self.horizontalLayout_6.addWidget(self.radioButton_mercredi_nuit)
        self.radioButton_mercredi_repos = QtWidgets.QRadioButton(self.layoutWidget3)
        self.radioButton_mercredi_repos.setObjectName("radioButton_mercredi_repos")
        self.horizontalLayout_6.addWidget(self.radioButton_mercredi_repos)
        self.layoutWidget4 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        spacerItem3 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.label_jeudi = QtWidgets.QLabel(self.layoutWidget4)
        self.label_jeudi.setObjectName("label_jeudi")
        self.horizontalLayout_9.addWidget(self.label_jeudi)
        self.radioButton_jeudi_matin = QtWidgets.QRadioButton(self.layoutWidget4)
        self.radioButton_jeudi_matin.setObjectName("radioButton_jeudi_matin")
        self.horizontalLayout_9.addWidget(self.radioButton_jeudi_matin)
        self.radioButton_jeudi_soir = QtWidgets.QRadioButton(self.layoutWidget4)
        self.radioButton_jeudi_soir.setObjectName("radioButton_jeudi_soir")
        self.horizontalLayout_9.addWidget(self.radioButton_jeudi_soir)
        self.radioButton_jeudi_nuit = QtWidgets.QRadioButton(self.layoutWidget4)
        self.radioButton_jeudi_nuit.setObjectName("radioButton_jeudi_nuit")
        self.horizontalLayout_9.addWidget(self.radioButton_jeudi_nuit)
        self.radioButton_jeudi_repos = QtWidgets.QRadioButton(self.layoutWidget4)
        self.radioButton_jeudi_repos.setObjectName("radioButton_jeudi_repos")
        self.horizontalLayout_9.addWidget(self.radioButton_jeudi_repos)
        self.layoutWidget5 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        spacerItem4 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.label_vendredi = QtWidgets.QLabel(self.layoutWidget5)
        self.label_vendredi.setObjectName("label_vendredi")
        self.horizontalLayout_7.addWidget(self.label_vendredi)
        self.radioButton_vendredi_matin = QtWidgets.QRadioButton(self.layoutWidget5)
        self.radioButton_vendredi_matin.setObjectName("radioButton_vendredi_matin")
        self.horizontalLayout_7.addWidget(self.radioButton_vendredi_matin)
        self.radioButton_vendredi_soir = QtWidgets.QRadioButton(self.layoutWidget5)
        self.radioButton_vendredi_soir.setObjectName("radioButton_vendredi_soir")
        self.horizontalLayout_7.addWidget(self.radioButton_vendredi_soir)
        self.radioButton_vendredi_nuit = QtWidgets.QRadioButton(self.layoutWidget5)
        self.radioButton_vendredi_nuit.setObjectName("radioButton_vendredi_nuit")
        self.horizontalLayout_7.addWidget(self.radioButton_vendredi_nuit)
        self.radioButton_vendredi_repos = QtWidgets.QRadioButton(self.layoutWidget5)
        self.radioButton_vendredi_repos.setObjectName("radioButton_vendredi_repos")
        self.horizontalLayout_7.addWidget(self.radioButton_vendredi_repos)
        self.layoutWidget6 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget6)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_11.addWidget(self.label_6)
        spacerItem5 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem5)
        self.label_samedi = QtWidgets.QLabel(self.layoutWidget6)
        self.label_samedi.setObjectName("label_samedi")
        self.horizontalLayout_11.addWidget(self.label_samedi)
        self.radioButton_samedi_matin = QtWidgets.QRadioButton(self.layoutWidget6)
        self.radioButton_samedi_matin.setObjectName("radioButton_samedi_matin")
        self.horizontalLayout_11.addWidget(self.radioButton_samedi_matin)
        self.radioButton_samedi_soir = QtWidgets.QRadioButton(self.layoutWidget6)
        self.radioButton_samedi_soir.setObjectName("radioButton_samedi_soir")
        self.horizontalLayout_11.addWidget(self.radioButton_samedi_soir)
        self.radioButton_samedi_nuit = QtWidgets.QRadioButton(self.layoutWidget6)
        self.radioButton_samedi_nuit.setObjectName("radioButton_samedi_nuit")
        self.horizontalLayout_11.addWidget(self.radioButton_samedi_nuit)
        self.radioButton_samedi_repos = QtWidgets.QRadioButton(self.layoutWidget6)
        self.radioButton_samedi_repos.setObjectName("radioButton_samedi_repos")
        self.horizontalLayout_11.addWidget(self.radioButton_samedi_repos)
        self.layoutWidget7 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget7.setObjectName("layoutWidget7")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.layoutWidget7)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget7)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_12.addWidget(self.label_8)
        spacerItem6 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem6)
        self.label_dimanche = QtWidgets.QLabel(self.layoutWidget7)
        self.label_dimanche.setObjectName("label_dimanche")
        self.horizontalLayout_12.addWidget(self.label_dimanche)
        self.radioButton_dimanche_matin = QtWidgets.QRadioButton(self.layoutWidget7)
        self.radioButton_dimanche_matin.setObjectName("radioButton_dimanche_matin")
        self.horizontalLayout_12.addWidget(self.radioButton_dimanche_matin)
        self.radioButton_dimanche_soir = QtWidgets.QRadioButton(self.layoutWidget7)
        self.radioButton_dimanche_soir.setObjectName("radioButton_dimanche_soir")
        self.horizontalLayout_12.addWidget(self.radioButton_dimanche_soir)
        self.radioButton_dimanche_nuit = QtWidgets.QRadioButton(self.layoutWidget7)
        self.radioButton_dimanche_nuit.setObjectName("radioButton_dimanche_nuit")
        self.horizontalLayout_12.addWidget(self.radioButton_dimanche_nuit)
        self.radioButton_dimanche_repos = QtWidgets.QRadioButton(self.layoutWidget7)
        self.radioButton_dimanche_repos.setObjectName("radioButton_dimanche_repos")
        self.horizontalLayout_12.addWidget(self.radioButton_dimanche_repos)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_quitter.setText(_translate("Form", "Quitter"))
        self.pushButton_5.setText(_translate("Form", "-1"))
        self.pushButton.setText(_translate("Form", "Cette semaine"))
        self.pushButton_4.setText(_translate("Form", "+1"))
        self.label_semaine.setText(_translate("Form", "Semaine 49"))
        self.pushButton_enregistrer.setText(_translate("Form", "Save"))
        self.pushButton_reset.setText(_translate("Form", "Load"))
        self.label.setText(_translate("Form", "Lundi"))
        self.label_lundi.setText(_translate("Form", "2 décembre 2019"))
        self.radioButton_lundi_matin.setText(_translate("Form", "Matin"))
        self.radioButton_lundi_soir.setText(_translate("Form", "Soir"))
        self.radioButton_lundi_nuit.setText(_translate("Form", "Nuit"))
        self.radioButton_lundi_repos.setText(_translate("Form", "Repos"))
        self.label_7.setText(_translate("Form", "Mardi"))
        self.label_mardi.setText(_translate("Form", "3 décembre 2019"))
        self.radioButton_mardi_matin.setText(_translate("Form", "Matin"))
        self.radioButton_mardi_soir.setText(_translate("Form", "Soir"))
        self.radioButton_mardi_nuit.setText(_translate("Form", "Nuit"))
        self.radioButton_mardi_repos.setText(_translate("Form", "Repos"))
        self.label_3.setText(_translate("Form", "Mercredi"))
        self.label_mercredi.setText(_translate("Form", "4 décembre 2019"))
        self.radioButton_mercredi_matin.setText(_translate("Form", "Matin"))
        self.radioButton_mercredi_soir.setText(_translate("Form", "Soir"))
        self.radioButton_mercredi_nuit.setText(_translate("Form", "Nuit"))
        self.radioButton_mercredi_repos.setText(_translate("Form", "Repos"))
        self.label_9.setText(_translate("Form", "Jeudi"))
        self.label_jeudi.setText(_translate("Form", "5 décembre 2019"))
        self.radioButton_jeudi_matin.setText(_translate("Form", "Matin"))
        self.radioButton_jeudi_soir.setText(_translate("Form", "Soir"))
        self.radioButton_jeudi_nuit.setText(_translate("Form", "Nuit"))
        self.radioButton_jeudi_repos.setText(_translate("Form", "Repos"))
        self.label_5.setText(_translate("Form", "Vendredi"))
        self.label_vendredi.setText(_translate("Form", "6 décembre 2019"))
        self.radioButton_vendredi_matin.setText(_translate("Form", "Matin"))
        self.radioButton_vendredi_soir.setText(_translate("Form", "Soir"))
        self.radioButton_vendredi_nuit.setText(_translate("Form", "Nuit"))
        self.radioButton_vendredi_repos.setText(_translate("Form", "Repos"))
        self.label_6.setText(_translate("Form", "Samedi"))
        self.label_samedi.setText(_translate("Form", "7 décembre 2019"))
        self.radioButton_samedi_matin.setText(_translate("Form", "Matin"))
        self.radioButton_samedi_soir.setText(_translate("Form", "Soir"))
        self.radioButton_samedi_nuit.setText(_translate("Form", "Nuit"))
        self.radioButton_samedi_repos.setText(_translate("Form", "Repos"))
        self.label_8.setText(_translate("Form", "Dimanche"))
        self.label_dimanche.setText(_translate("Form", "8 décembre 2019"))
        self.radioButton_dimanche_matin.setText(_translate("Form", "Matin"))
        self.radioButton_dimanche_soir.setText(_translate("Form", "Soir"))
        self.radioButton_dimanche_nuit.setText(_translate("Form", "Nuit"))
        self.radioButton_dimanche_repos.setText(_translate("Form", "Repos"))
