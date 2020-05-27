import sys, math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


# Create button class for button press actions --> method to call on click
class Button:
    def __init__(self, text, results):
        # Create button, create objects
        self.b = QPushButton(str(text))
        self.text = text
        self.results = results
        # Connect button to event handler, each button has own method,
        # Can not pass variable in method, need to use lambda
        self.b.clicked.connect(lambda: self.handleInput(self.text))

    # Need to pass variable
    def handleInput(self, v):
        # Evaluate results of entered text, show result
        if v == "=":
            res = eval(self.results.text())
            self.results.setText(str(res))
        elif v == "AC":
            self.results.setText("")
        elif v == "√":
            # Convert value to float set value to input
            value = float(self.results.text())
            self.results.setText(str(math.sqrt(value)))
        elif v == "DEL":
            # Get current value and set to current value minus last character
            current_value = self.results.text()
            self.results.setText(current_value[:-1])
        else:
            # Get text of input when button pressed
            current_value = self.results.text()
            new_value = current_value + str(v)
            self.results.setText(new_value)


# Create Widget
class Application(QWidget):
    # Initialize, inherit, set window title, show app
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.CreateApp()

    def CreateApp(self):
        # Create grid layout with space for results
        grid = QGridLayout()
        results = QLineEdit()

        # Create list of button in order we want to see
        buttons = ["AC", "√", "DEL", "/",
                   7, 8, 9, "*",
                   4, 5, 6, "-",
                   1, 2, 3, "+",
                   0, ".", "="]

        # Add results line
        grid.addWidget(results, 0, 0, 1, 4)

        # Starting point for grid row/col
        row = 1
        col = 0

        # Add buttons to grid
        for button in buttons:
            # Start new row after 3 buttons
            if col > 3:
                col = 0
                row += 1

            # Set button to grid, add button there (pass button text and input area)
            button_obj = Button(button, results)

            # Make 0 button take 2 col
            if button == 0:
                grid.addWidget(button_obj.b, row, col, 1, 2)
                # Restart col position after longer button
                col += 1
            else:
                grid.addWidget(button_obj.b, row, col, 1, 1)

            # Increase row and col, based on how many used
            col += 1

        self.setLayout(grid)

        self.show()


# Application open, run, close
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Application()
    sys.exit(app.exec())
