#!/usr/bin/python3

import os, sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import *
from PyQt5.Qt import *


# Build QML application
if __name__ == "__main__":
    app = QGuiApplication(sys.argv)

    # Create engine - connection to use QML
    engine = QQmlApplicationEngine()

    # Create component factory and load QML script
    component = QQmlComponent(engine)
    component.loadUrl(QUrl("qmlmain.qml"))

    # Create objects from QML
    window = component.create()
    if window:
        window.show()
    else:
        for error in component.errors():
            print(error.toString())

    sys.exit(app.exec_())
