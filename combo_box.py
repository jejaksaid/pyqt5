import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        #add title
        self.setWindowTitle("Hellow World")

        # set vertical layout
        self.setLayout(qtw.QVBoxLayout())

        # create a label
        my_label = qtw.QLabel("Pick Something From The List Below")

        # change the font size of label
        my_label.setFont(qtg.QFont('Helvetica', 18))
        self.layout().addWidget(my_label) 

        # create an combo box
        my_combo = qtw.QComboBox(self)
        # add items to the combo box
        my_combo.addItem("Pepperoni", "Something")
        my_combo.addItem("Cheese", 2)
        my_combo.addItem("Peppers", qtw.QWidget)
        my_combo.addItem("Mushroom")

        # put combobox on the screen
        self.layout().addWidget(my_combo)
        

        # create a button
        my_button = qtw.QPushButton("Press Me", clicked = lambda: press_it())
        self.layout().addWidget(my_button)

        #show the app
        self.show()

        def press_it():
            # add name to label
            my_label.setText(f'You Picked {my_combo.currentText()}!')
            # clear the entry box
app = qtw.QApplication([])
mw = MainWindow()

#run the app
app.exec_()