import subprocess

def run_cpp(image_path, emoji_path, size):
	binary_path = './build/EmojiArt'  
	command_line_arguments = [image_path, emoji_path, str(size)]  
	cout = None
	cerr = None	
	try:
		result = subprocess.run([binary_path] + command_line_arguments, capture_output=True, text=True, check=True)
		cout = result.stdout
	except subprocess.CalledProcessError as e:
		cerr = e.stderr
	return (cout, cerr)

