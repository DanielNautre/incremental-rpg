#!/usr/bin/python3.6
# -*- coding: utf8 -*

import sys
import traceback

# Import Graphic Lib
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

# Import widgets
from mainwindow import MainWindow
from game import Game


def main():

    # initiate window
    app = QApplication(sys.argv)
    app.setStyleSheet("")
    w = MainWindow()
    g = Game(w)

    # setup timer for the game tick (1 tick per second)
    timer = QTimer()
    timer.start(1000)
    timer.timeout.connect(g.run_loop)

    # setup timer for the game refresh rate (10fps)
    ui_timer = QTimer()
    ui_timer.start(100)
    ui_timer.timeout.connect(g.refresh_interface)

    w.show()

    # run the main loop
    sys.exit(app.exec_())


if __name__ == '__main__':

    try:
        main()
    except Exception:
        print(traceback.format_exc())

# EOF
