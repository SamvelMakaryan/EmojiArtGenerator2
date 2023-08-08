import sys
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout, QHBoxLayout, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
from download import download_image

class MyDialog(QDialog):
	def __init__(self):
		super().__init__()
		ui_file = "window.ui"
		loadUi(ui_file, self)
		self.set_default_images()
		self.init_ui()
	
	def init_ui(self):		
		self.save_button.clicked.connect(self.save)
		self.generate_button.clicked.connect(self.generate)
		self.browse_image_button.clicked.connect(self.browse_image)
		self.browse_emoji_button.clicked.connect(self.browse_emoji)

	def set_default_images(self):
		original_image_path = "default_original_image.png"
		res_image_path = "default_result_image.png"
		original_image = QPixmap(original_image_path)
		res_image = QPixmap(res_image_path)
		self.original_image.setPixmap(original_image)
		self.res_image.setPixmap(res_image)

	def save(self):
		print("Save button")

	def generate(self):
		print("Generate button")
		image_path = self.image_description.text()
		emoji_path = self.emoji_description.text()

		if image_path == "":
			image_path = self.browse_emoji()
		else:
			try:
				download_image(image_path, "image.png")
			except:
				print("Invalid URL")
				return #add message box

		if emoji_path == "":
			emoji_path = self.browse_emoji()
		else:
			try:
				download_image(emoji_path, "emoji.png")
			except:
				print("Invalid URL")
				return #add message box

		print(image_path)
		print(emoji_path)
		#c++ code

	def browse_image(self):
		print("Image button")
		options = QFileDialog.Options()
		options |= QFileDialog.ReadOnly
		image_path, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif);;All Files (*)", options=options)

		if image_path:
			pixmap = QPixmap(image_path)
			self.original_image.setPixmap(pixmap)
		return image_path
			
	def browse_emoji(self):
		print("Emoji button")
		options = QFileDialog.Options()
		options |= QFileDialog.ReadOnly
		emoji_path, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif);;All Files (*)", options=options)
		return emoji_path

def run_ui():
	app = QApplication(sys.argv)
	dialog = MyDialog()
	dialog.setWindowTitle("Dialog")
	
	dialog.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	run_ui()

