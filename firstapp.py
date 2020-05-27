#!/usr/bin/python3

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


# Create class with basic page, inherits from QWidget
class Page(QWidget):
    # Build out page
    def __init__(self, parent = None):
        # Instantiate parent as well
        super(Page, self).__init__(parent)

        # Create Label
        my_label = QLabel("This is my label")
        # Create Layout
        layout = QVBoxLayout()

        # Add label into layout
        layout.addWidget(my_label)

        # Grid Layout, pass in how many rows and colums
        mainLayout = QGridLayout()
        mainLayout.addLayout(layout, 0, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle("My First Qt App")

# Instantiate app
if __name__ == "__main__":
    # Need to exit app
    import sys

    # Assign var, pas system arguments
    app = QApplication(sys.argv)

    # Create window, show window, execute window function
    window = Page()
    window.show()

    sys.exit(app.exec_())




