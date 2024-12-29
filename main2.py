import random
from PyQt6.QtWidgets import*


app = QApplication([])
window = QWidget()
window.resize(500,500)
nadpus = QLabel("Вікторина")
winner_lbl =QLabel("?")
knopka = QPushButton("Визначити переможця")
slider = QSlider()
krugok = QDial()

main_line = QVBoxLayout()
main_line.addWidget(nadpus)
main_line.addWidget(winner_lbl)
main_line.addWidget(knopka)
main_line.addWidget(slider)
main_line.addWidget(krugok)

def winner():
    w=random.randint(1,100)
    winner_lbl.setText(str(w))
knopka.clicked.connect(winner)

window.setLayout(main_line)
window.show()
app.exec()