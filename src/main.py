from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout, QHBoxLayout, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
import sys
import os

sys.path.append('../ui')
from messageBox import show_error_message, show_normal_message
from download import download_image
from process import run_cpp


class MyDialog(QDialog):
	def __init__(self):
		super().__init__()
		ui_file = "../ui/window.ui"
		loadUi(ui_file, self)
		self.set_default_images()
		self.init_ui()
		self.image_path = None
		self.emoji_path = None
		self.cout = None
	
	def init_ui(self):		
		self.save_button.clicked.connect(self.save)
		self.generate_button.clicked.connect(self.generate)
		self.browse_image_button.clicked.connect(self.browse_image)
		self.browse_emoji_button.clicked.connect(self.browse_emoji)
		self.download_button.clicked.connect(self.dowload_image_and_emoji)

	def set_default_images(self):
		original_image_path = "../images/default_original_image.png"
		res_image_path = "../images/default_result_image.png"
		original_image = QPixmap(original_image_path)
		res_image = QPixmap(res_image_path)
		self.original_image.setPixmap(original_image)
		self.res_image.setPixmap(res_image)

	def save(self):
		print("Save button")
		if self.cout is None:
			show_error_message("   ","No generated image to save")
			return
		options = QFileDialog.Options()
		options |= QFileDialog.ShowDirsOnly
        
		dest_file_path, _ = QFileDialog.getSaveFileName(self, "Choose Destination Directory and Filename", "", "Images (*.png *.jpg *.bmp);;All Files (*)", options=options)

		if dest_file_path:
			try:
				os.rename(self.cout, dest_file_path)
				print(f"File moved successfully to: {destination_path}")
			except Exception as e:
				print(f"Failed to move file. Error: {e}")
		else:
			print("No destination file name selected.")

		
	def generate(self):
		print("Generate button")
		if self.image_path is None:
			show_error_message("Empty image", "Please browse image")
			return
		if self.emoji_path is None:
			show_error_message("Empty emoji", "Please browse emoji")
			return
		self.cout, cerr = run_cpp(self.image_path, self.emoji_path)
		if cerr is not None:
			show_error_message("Unconvertable image", "Unable to convert image")
			return
		print("stdout: [", self.cout, "]")
		print("stderr: [", cerr, "]")
		self.show_image(self.res_image, self.cout)
	
	def browse_image(self):
		print("Image button")
		options = QFileDialog.Options()
		options |= QFileDialog.ReadOnly
		self.image_path, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif);;All Files (*)", options=options)
		self.show_image(self.original_image, self.image_path)
		print("browsing ", self.image_path)

	def browse_emoji(self):
		print("Emoji button")
		options = QFileDialog.Options()
		options |= QFileDialog.ReadOnly
		self.emoji_path, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif);;All Files (*)", options=options)
		print("browsing ", self.emoji_path)

	def show_image(self, location, image_path):
		if image_path:
			pixmap = QPixmap(image_path)
			location.setPixmap(pixmap.scaled(550, 630))

	def dowload_image_and_emoji(self):
		image_url = self.image_description.text()
		emoji_url = self.emoji_description.text()
		image_name = self.image_name.text()
		emoji_name = self.emoji_name.text()
		if image_url != "" and  image_name != "":
			try:
				download_image(image_url, image_name)
				show_normal_message("Image downloaded successfully")
			except:
				show_error_message("Invalid URL", "No image was found")
				return
		elif image_url == "" and image_name == "":
			pass
		elif image_url == "":
			show_error_message("Empty URL", "Please provide image's URL")
			return
		else:
			show_error_message("Empty name", "Please provide image's name")
			return

		if emoji_url != "" and  emoji_name != "":
			try:
				download_image(emoji_url, emoji_name)
				show_normal_message("Emoji downloaded successfully")
			except:
				show_error_message("Invalid URL", "No emoji was found")
				return
		elif emoji_url == "" and emoji_name == "":
			pass
		elif emoji_url == "":
			show_error_message("Empty URL", "Please provide emoji's URL")
			return
		else:
			show_error_message("Empty name", "Please provide emoji's name")
			return
		
		self.image_description.clear()
		self.emoji_description.clear()
		self.image_name.clear()
		self.emoji_name.clear()

	def show_normal_message(self, message):
		message_box = QMessageBox()
		message_box.setIcon(QMessageBox.Information)
		message_box.setWindowTitle("    ")
		message_box.setText(message)
		message_box.setStandardButtons(QMessageBox.Ok)
		message_box.exec_()

def run_ui():
	app = QApplication(sys.argv)
	dialog = MyDialog()
	dialog.setWindowTitle("Dialog")
	
	dialog.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	run_ui()

