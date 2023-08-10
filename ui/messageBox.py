from PyQt5.QtWidgets import QMessageBox, QApplication
import sys

class ResizableMessageBox(QMessageBox):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
	
	def resizeEvent(self, event):
		width = 320
		height = 100
		self.setFixedSize(width, height)
		
		super().resizeEvent(event)

def show_normal_message(message):
	msg_box = ResizableMessageBox()
	msg_box.setIcon(QMessageBox.Information)
	msg_box.setWindowTitle("    ")
	msg_box.setText(message)
	msg_box.setStandardButtons(QMessageBox.Ok)

	msg_box.setStyleSheet("""
        QMessageBox {
            background:qlineargradient(x1:0, y1:1, x2:1, y2:0, stop:0 #D900D9, stop:1 #00E5E5)
        }
        QPushButton {
            background-color: white;
            color: #e647a9;
            border: none;
            padding: 5px 10px;
        }
        QPushButton:hover {
            background-color: #e647e3;
			color: white;
        }
	""")

	msg_box.exec_()

def show_error_message(title, message):
	msg_box = ResizableMessageBox()
	msg_box.setWindowTitle(title)
	msg_box.setText(message)
	msg_box.setIcon(QMessageBox.Warning)

	msg_box.setStyleSheet("""
        QMessageBox {
            background:qlineargradient(x1:0, y1:1, x2:1, y2:0, stop:0 #D900D9, stop:1 #00E5E5)
        }
        QPushButton {
            background-color: white;
            color: #e647a9;
            border: none;
            padding: 5px 10px;
        }
        QPushButton:hover {
            background-color: #e647e3;
			color: white;
        }
	""")

	msg_box.exec_()


