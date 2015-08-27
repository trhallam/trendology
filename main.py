#!/usr/bin/python3
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

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
import qt.trendologyGUI as tGUI

# initiate window
class trendologyMain(QMainWindow):
    def __init__(self, parent=None):
        super(trendologyMain, self).__init__(parent)

        self.ui = tGUI.trendologyGUI()

        self.ui.setupUi(self)
'''
    @pyqtSlot(int)
    def on_inputSpinBox1_valueChanged(self, value):
        self.ui.outputWidget.setText(str(value + self.ui.inputSpinBox2.value()))

    @pyqtSlot(int)
    def on_inputSpinBox2_valueChanged(self, value):
        self.ui.outputWidget.setText(str(value + self.ui.inputSpinBox1.value()))
'''

# Main Application        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    trendapp = trendologyMain()
    trendapp.show()
    sys.exit(app.exec_())  