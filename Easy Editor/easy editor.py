from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QListWidget
from PyQt5.QtCore import Qt

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Easy Editor")


text = QLabel("Картинка")
papka_btn = QPushButton("Папка")
l_btn = QPushButton("Вліво")
r_btn = QPushButton("Вправо")
mir_btn = QPushButton("Дзеркало")
cb_btn = QPushButton("Ч\Б")
riz_btn = QPushButton("Різкість")
my_list = QListWidget()


horizont_line = QHBoxLayout()
first_v_line = QVBoxLayout()
second_v_line = QVBoxLayout()
buttons_line = QHBoxLayout()

first_v_line.addWidget(papka_btn)
first_v_line.addWidget(my_list)
second_v_line.addWidget(text)

buttons_line.addWidget(l_btn)
buttons_line.addWidget(r_btn)
buttons_line.addWidget(mir_btn)
buttons_line.addWidget(cb_btn)
buttons_line.addWidget(riz_btn)
second_v_line.addLayout(buttons_line, 80)


horizont_line.addLayout(first_v_line, 20)
horizont_line.addLayout(second_v_line, 80)

main_win.setLayout(horizont_line)

main_win.show()
app.exec()