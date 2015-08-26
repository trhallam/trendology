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

import csv

"""
Attempt 1: Loading csv data.
"""

def loadWells(file):
    '''
    Well names should be defined in the first column of the file.
    '''
    with open(file) as csvfile:
        wellReader = csv.reader(csvfile, delimiter=',')
        wells=[]
        for row in wellReader:
            wells.append(row[0])
    return wells