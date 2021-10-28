import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # add a title
        self.setWindowTitle("Hello World! Whats your name")

        # set vertical layout
        self.setLayout(qtw.QVBoxLayout())

        # create a label
        my_label = qtw.QLabel("Hello World!")

        # change font size of label
        my_label.setFont(qtg.QFont('Helvectica', 18))
        self.layout().addWidget(my_label)

        # create an entry box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name_field")
        my_entry.setText("")
        self.layout().addWidget(my_entry)

        # create a button
        my_button = qtw.QPushButton("Press me!",
            clicked = lambda: press_it()  )
        self.layout().addWidget(my_button)

        # show the app
        self.show()

        def  press_it():
            # add name to label
            my_label.setText(f'Hello {my_entry.text()}!')
            # clear the entry box
            my_entry.setText("")

app = qtw.QApplication([])
mw = MainWindow()

# run the app

app.exec_()