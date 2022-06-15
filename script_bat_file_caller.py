# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 22:39:56 2022
@author: Karan K. Bhat
This script invokes a GUI for calling any windows batch file 
"""

import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon

class Batch_caller (QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Windows Batch File Caller'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 200
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        button=QPushButton('Open Script', self)
        button.setToolTip('Click to open the batch script')
        button.move (50, 150)
        button.clicked.connect(self.launcher)
        
        button1=QPushButton('Kill hub4com', self)
        button1.move (250, 150)
        button1.clicked.connect(self.killer)

    def launcher(self):
        print('Button clicked!')
        filepath="C:/Program Files (x86)/hub4com/hub4com_Runner/serial_monitor.bat"
        p = subprocess.Popen(filepath, shell=True)                     
    
    def killer(self):
        subprocess.call("taskkill /F /im hub4com.exe")
        
if __name__ == '__main__':
    application=QApplication([])
    caller=Batch_caller()
    caller.show()
    sys.exit(application.exec_())