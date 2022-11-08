from tkinter import *
from tkinter import filedialog , messagebox


root = Tk()
root.title('Notes')
root.iconbitmap(r'notes_icon.ico')


text_scroll = Scrollbar(root)
text_scroll.pack(side = RIGHT , fill = Y)

# Menu
my_menu = Menu(root)
root.config(menu = my_menu)


my_text = Text(root , width = 97 , height = 25 , font = ('Times' , 15 , 'normal') , selectbackground = 'gray60' , selectforeground = 'black', undo = True , yscrollcommand = text_scroll.set)
my_text.pack(expand=YES, fill= BOTH, pady = 10 )


text_scroll.config(command = my_text.yview)

	
# Functions
#==================FISRT MENU=========================================
def new_file():
	#checks if there is any word inside so it can save it , if it's not then directly quit
	written_text = my_text.get(1.0 , END)
	if len(written_text) > 1:
		#checks if you would like to save what's inside
		if messagebox.askyesno("Notes", "Do want to save it ?"):
			text_file = filedialog.asksaveasfilename(defaultextension = '.txt' , initialdir = 'C:/Desktop' , title = 'Save File' , filetypes = (('Text Files' , '*.txt') , ('All Files' , '*.*')))
			if text_file:
				text_file = open(text_file , 'w')
				text_file.write(my_text.get(1.0 , END))
				text_file.close()
				my_text.delete('1.0' , END)
				status_bar.config(text = 'New File')
		else:
			my_text.delete('1.0' , END)
			status_bar.config(text = 'New File')
	else:
		my_text.delete('1.0' , END)
		status_bar.config(text = 'New File')

	
def open_file():
	#checks if there is any word inside so it can save it , if it's not then directly quit
	written_text = my_text.get(1.0 , END)
	if len(written_text) > 1:
		#checks if you would like to save what's inside
		if messagebox.askyesno("Notes", "Do want to save it ?"):
			text_file = filedialog.asksaveasfilename(defaultextension = '.txt' , initialdir = 'C:/Desktop' , title = 'Save File' , filetypes = (('Text Files' , '*.txt') , ('All Files' , '*.*')))
			if text_file:
				text_file = open(text_file , 'w')
				text_file.write(my_text.get(1.0 , END))
				text_file.close()
				
				my_text.delete('1.0' , END)
				text_file = filedialog.askopenfilename(initialdir = 'C:/Desktop', title = 'Open file' , filetypes = (('Text Files', '*.txt') , ('All Files' , '*.*')))
				name = text_file
				status_bar.config(text = name)
				
				text_file = open(text_file, 'r')
				stuff = text_file.read()
				my_text.insert(END , stuff)
				text_file.close()
		else:
			my_text.delete('1.0' , END)
			text_file = filedialog.askopenfilename(initialdir = 'C:/Desktop', title = 'Open file' , filetypes = (('Text Files', '*.txt') , ('All Files' , '*.*')))
			name = text_file
			status_bar.config(text = name)
		
			text_file = open(text_file, 'r')
			stuff = text_file.read()
			my_text.insert(END , stuff)
			text_file.close()		
	else:
		my_text.delete('1.0' , END)
		text_file = filedialog.askopenfilename(initialdir = 'C:/Desktop', title = 'Open file' , filetypes = (('Text Files', '*.txt') , ('All Files' , '*.*')))
		name = text_file
		status_bar.config(text = name)
	
		text_file = open(text_file, 'r')
		stuff = text_file.read()
		my_text.insert(END , stuff)
		text_file.close()	

	
def save_file():
	text_file = filedialog.asksaveasfilename(defaultextension = '.txt' , initialdir = 'C:/Desktop' , title = 'Save File' , filetypes = (('Text Files' , '*.txt') , ('All Files' , '*.*')))
	if text_file:
		status_bar.config(text = 'File Saved')

		text_file = open(text_file , 'w')
		text_file.write(my_text.get(1.0 , END))
		text_file.close()
	
def word_counter():
	words = my_text.get('1.0' , END)
	words_list = words.split()
	number_of_words = len(words_list)
	status_bar.config(text = '{x} words'.format(x = number_of_words))	
	
	
def close_window():
	#checks if there is any word inside so it can save it , if it's not then directly quit
	written_text = my_text.get(1.0 , END)
	if len(written_text) > 1:
		#checks if you would like to save what's inside
		if messagebox.askyesno("Notes", "Do want to save it ?"):
			text_file = filedialog.asksaveasfilename(defaultextension = '.txt' , initialdir = 'C:/Desktop' , title = 'Save File' , filetypes = (('Text Files' , '*.txt') , ('All Files' , '*.*')))
			if text_file:
				text_file = open(text_file , 'w')
				text_file.write(my_text.get(1.0 , END))
				text_file.close()
				root.destroy()	
		else:
			root.destroy()
	else:
		root.destroy()

root.protocol("WM_DELETE_WINDOW", close_window)
	
	
def exit():
	#checks if there is any word inside so it can save it , if it's not then directly quit
	written_text = my_text.get(1.0 , END)
	if len(written_text) > 1:
		#checks if you would like to save what's inside
		if messagebox.askyesno("Notes", "Do want to save it ?"):
			text_file = filedialog.asksaveasfilename(defaultextension = '.txt' , initialdir = 'C:/Desktop' , title = 'Save File' , filetypes = (('Text Files' , '*.txt') , ('All Files' , '*.*')))
			if text_file:
				text_file = open(text_file , 'w')
				text_file.write(my_text.get(1.0 , END))
				text_file.close()
				root.destroy()	
		else:
			root.destroy()
	else:
		root.destroy()
	
	
#======================SECOND MENU==========================
def cut_text(parameter):
	global selected
	if parameter:
		selected = root.clipboard_get()
	else:
		if my_text.selection_get():
			#select text
			selected = my_text.selection_get()
			# delete text
			my_text.delete('sel.first' , 'sel.last')
			root.clipboard_clear()
			root.clipboard_append(selected)
	
def copy_text(parameter):
	global selected
	# check to see if we used keyboard shortcuts
	if parameter:
		selected = root.clipboard_get()
	
	if my_text.selection_get():
		selected = my_text.selection_get()
		root.clipboard_clear()
		root.clipboard_append(selected)
	
def paste_text(parameter):
	global selected
	if parameter:
		selected = root.clipboard_get()
	else:	
		if selected:
			position = my_text.index(INSERT)
			my_text.insert(position , selected)	
	
# Menu
my_menu = Menu(root)
root.config(menu = my_menu)


# Add file to menu
file_menu = Menu(my_menu , tearoff = False)
my_menu.add_cascade(label = 'File' , menu = file_menu)
file_menu.add_command(label = 'New' , command = new_file)
file_menu.add_command(label = 'Open' , command = open_file)
file_menu.add_command(label = 'Save', command = save_file)
file_menu.add_command(label = 'Count words', command = word_counter)
file_menu.add_separator()
file_menu.add_command(label = 'Exit' , command = exit)
	
# Add edit menu
edit_menu = Menu(my_menu , tearoff = False)
my_menu.add_cascade(label = 'Edit' , menu = edit_menu)
edit_menu.add_command(label = 'Cut' , command = lambda: cut_text(0) , accelerator = '(Ctrl+X)')
edit_menu.add_command(label = 'Copy' , command = lambda: copy_text(0) , accelerator = '(Ctrl+C)')
edit_menu.add_command(label = 'Paste' , command = lambda: paste_text(0) , accelerator = '(Ctrl+V)')
edit_menu.add_separator()
edit_menu.add_command(label = 'Undo' , command = my_text.edit_undo , accelerator = '(Ctrl+Z)')
edit_menu.add_command(label = 'Redo', command = my_text.edit_redo , accelerator = '(Ctrl+Y)')
	
	
# Add status bar
status_bar = Label(root , text = 'Ready  ', anchor = E )
status_bar.pack(fill = X , side = BOTTOM )
	
	
# edit bidings
root.bind('<Control-x>', cut_text)
root.bind('<Control-c>', copy_text)
root.bind('<Control-v>', paste_text)




root.mainloop()