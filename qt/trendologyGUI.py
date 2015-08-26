# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 20:06:21 2015

@author: Antony Hallam

This file is part of Trendology.

    Trendology is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Trendology is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Trendology.  If not, see <http://www.gnu.org/licenses/>.
"""

"""
This Library contains the necessary classes to handle loading and saving of
data from the trendology package.
"""

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Trendology(object):

    
    
    def setupUi(self, Trendology):
        Trendology.setObjectName("Trendology")
        Trendology.resize(1024, 768)
        Trendology.setMinimumSize(QtCore.QSize(1024, 768))
        self.centralwidget = QtWidgets.QWidget(Trendology)
        self.centralwidget.setObjectName("centralwidget")
        self.listViewWells = QtWidgets.QListView(self.centralwidget)
        self.listViewWells.setGeometry(QtCore.QRect(30, 30, 211, 711))
        self.listViewWells.setMouseTracking(False)
        self.listViewWells.setWindowTitle("Wells")
        self.listViewWells.setObjectName("listViewWells")
        #Trendology.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Trendology)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        #Trendology.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Trendology)
        self.statusbar.setObjectName("statusbar")
        #Trendology.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(Trendology)
        self.actionExit.setObjectName("actionExit")
        self.actionLoad_File = QtWidgets.QAction(Trendology)
        self.actionLoad_File.setObjectName("actionLoad_File")
        self.actionSave_Project = QtWidgets.QAction(Trendology)
        self.actionSave_Project.setObjectName("actionSave_Project")
        self.menuFile.addSeparator()
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionLoad_File)
        self.menuFile.addAction(self.actionSave_Project)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

# items from me
        self.wellModel = QtGui.QStandardItemModel()    


        self.retranslateUi(Trendology)
        QtCore.QMetaObject.connectSlotsByName(Trendology)

    def retranslateUi(self, Trendology):
        _translate = QtCore.QCoreApplication.translate
        Trendology.setWindowTitle(_translate("Trendology", "MainWindow"))
        self.menuFile.setTitle(_translate("Trendology", "File"))
        self.menuEdit.setTitle(_translate("Trendology", "Edit"))
        self.menuView.setTitle(_translate("Trendology", "View"))
        self.menuSettings.setTitle(_translate("Trendology", "Settings"))
        self.menuHelp.setTitle(_translate("Trendology", "Help"))
        self.actionExit.setText(_translate("Trendology", "Exit"))
        self.actionLoad_File.setText(_translate("Trendology", "Load File"))
        self.actionSave_Project.setText(_translate("Trendology", "Save Project"))
        
    def setWells(self, wells):
        '''
        set wells in the well list
        '''
        for well in wells:
            item=QtGui.QStandardItem(well)
            item.setCheckable(True)
            self.wellModel.appendRow(item)
            
        self.listViewWells.setModel(self.wellModel)
       

