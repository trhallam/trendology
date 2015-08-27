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

from qt.mainGUI import *
from lib import trendologyIO as tIO


class trendologyGUI(Ui_Trendology):

#Redfine setupUi with additional linkages etc.
    def setupUi(self, parent=None):
        super(trendologyGUI, self).setupUi(parent)
        #menu connections
        self.actionLoad_File.triggered.connect(self.openFile)
    
# items from me
    def __init__(self):
        self.wellModel = QtGui.QStandardItemModel()
        self.formModel = QtGui.QStandardItemModel()
        #self.dataModel = QtGui.QStandardItemModel()
      
    def setWells(self, wells):
        '''
        set wells in the well list
        '''
        for well in wells:
            item=QtGui.QStandardItem(well)
            item.setCheckable(True)
            item.setCheckState(QtCore.Qt.Checked)
            self.wellModel.appendRow(item)
            
        self.listViewWells.setModel(self.wellModel)
    
    def setFormations(self, formations):
        '''
        set formations in the formation list
        '''
        #remove duplicates
        shortForms=list(set(formations))
        #add to list
        for form in shortForms:
            item=QtGui.QStandardItem(form)
            item.setCheckable(True)
            item.setCheckState(QtCore.Qt.Checked)
            self.formModel.appendRow(item)
            
        self.listViewFormations.setModel(self.formModel)
      
    def setData(self):
        '''
        set data into the data table tab
        '''
        self.tableWidget.setColumnCount(self.numCol)
        self.tableWidget.setRowCount(self.numRow+2)
        #self.tableWidget.setItem(2,2,QtWidgets.QTableWidgetItem("Help"))
        
        for row in range(self.numRow):
            for col in range(self.numCol):
                self.tableWidget.setItem(row,col,\
                    QtWidgets.QTableWidgetItem(self.data[row][col]))
        #self.tableWidget.setModel(self.dataModel)
        
        '''
        headers = [
            QtWidgets.QTableWidgetItem(field)
            for field in self.dataHeaders
        ]
        self.dataModel.appendRow(headers)
        '''
    
    def openFile(self):
        # QT Open File Dialog from Menu
        openDlg=QtWidgets.QWidget()
        self.fileName=QtWidgets.QFileDialog.getOpenFileName(openDlg, 'Open File')
        #read file
        self.dataHeaders,self.dataUnits,self.data=tIO.loadCSV("example_data\wells.csv")
        self.numRow=len(self.data)
        self.numCol=len(self.data[0])
        self.dataWells=[]
        self.dataFormations=[]
        for row in range(0,self.numRow):
            self.dataWells.append(self.data[row][0])
            self.dataFormations.append(self.data[row][1])

        #for col in range(0,numCol):
            
        #display data
        self.setWells(self.dataWells)
        self.setFormations(self.dataFormations)
        self.setData()

