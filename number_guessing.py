import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc
import random

class NumberGuess(qtw.QWidget):
    def __init__(self) -> None:
        super().__init__()

        # Window
        self.setWindowTitle("Number Guess")
        self.setLayout(qtw.QGridLayout())

        # Label - Range
        self.label_1 = qtw.QLabel("Number Guess")
        self.label_1.setFont(qtg.QFont("HYRunYuan", 28))

        self.label_2 = qtw.QLabel("Set the range")
        self.label_2.setFont(qtg.QFont("HYRunYuan", 16))

        self.label_3 = qtw.QLabel("Lower Bound")
        self.label_3.setFont(qtg.QFont("HYRunYuan", 12))

        self.label_4 = qtw.QLabel("Upper Bound")
        self.label_4.setFont(qtg.QFont("HYRunYuan", 12))

        # Entry - Range
        self.entry_1 = qtw.QLineEdit()
        self.entry_1.setText("")

        self.entry_2 = qtw.QLineEdit()
        self.entry_2.setText("")

        # Button - Range
        self.button_1 = qtw.QPushButton("Set range", clicked = lambda: self.set_range())

        # Label - Guess
        self.label_5 = qtw.QLabel("Make your Guess")
        self.label_5.setFont(qtg.QFont("HYRunYuan", 16))

        # Entry - Guess
        self.guess_entry_1 = qtw.QLineEdit()
        self.guess_entry_1.setText("")

        # Button - Guess
        self.guess_button_1 = qtw.QPushButton("Guess", clicked = lambda: self.number_guess())

        # Arrangement
        self.layout().addWidget(self.label_1,0,0,1,0, qtc.Qt.AlignCenter)
        self.layout().addWidget(self.label_2,1,0,2,0, qtc.Qt.AlignCenter)
        self.layout().addWidget(self.label_3,3,0, qtc.Qt.AlignLeft)
        self.layout().addWidget(self.entry_1,3,1, qtc.Qt.AlignRight)
        self.layout().addWidget(self.label_4,4,0, qtc.Qt.AlignLeft)
        self.layout().addWidget(self.entry_2,4,1, qtc.Qt.AlignRight)
        self.layout().addWidget(self.button_1,5,0,5,0, qtc.Qt.AlignCenter)

        self.layout().addWidget(self.label_5,10,0,10,0, qtc.Qt.AlignCenter)
        self.layout().addWidget(self.guess_entry_1,20,0,20,0, qtc.Qt.AlignCenter)
        self.layout().addWidget(self.guess_button_1,40,0,40,0, qtc.Qt.AlignCenter)


        self.show()

    def set_range(self):
        if self.entry_1.text().isdigit() and self.entry_2.text().isdigit():
            self.upper_bound = int(self.entry_2.text())
            self.lower_bound = int(self.entry_1.text())
            self.random_number = random.randint(self.lower_bound, self.upper_bound)
        else:
            self.label_2.setText("Please Enter Integer")

    def number_guess(self):
        try:
            if self.entry_1.text().isdigit() and self.entry_2.text().isdigit():
                if self.guess_entry_1.text().isdigit() is True:
                    if int(self.guess_entry_1.text()) > self.upper_bound or int(self.guess_entry_1.text()) < self.lower_bound:
                        self.label_5.setText("WITHIN THE RANGE!!!")
                    elif self.random_number > int(self.guess_entry_1.text()):
                        self.label_5.setText("Too Small")
                    elif self.random_number < int(self.guess_entry_1.text()):
                        self.label_5.setText("Too Large")
                    elif self.random_number == int(self.guess_entry_1.text()):
                        self.label_5.setText("Congrats your Guess is Right")
                        self.entry_1.setText("")
                        self.entry_2.setText("")
                        self.guess_entry_1.setText("")
                elif self.guess_entry_1.text().isdigit() is False:
                    self.label_5.setText("Enter Your Guess")
            else:
                self.label_5.setText("Set Range First")
        except:
            self.label_5.setText("Set Range First")


app = qtw.QApplication([])
mw = NumberGuess()

app.exec_()
