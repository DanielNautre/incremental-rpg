#!/usr/bin/python3.6
# -*- coding: utf8 -*

from PyQt5.QtWidgets import QMainWindow, QStatusBar


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setGeometry(50, 50, 1024, 600)
        self.setWindowTitle('Incremental RPG')

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
