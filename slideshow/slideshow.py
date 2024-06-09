from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Slideshow")
#root.iconbitmap('.ico')

my_img0 = ImageTk.PhotoImage(Image.open("D:/OneDrive/py/tkinter/slideshow/img/2022 professional.jpeg"))
my_img1 = ImageTk.PhotoImage(Image.open("D:/OneDrive/py/tkinter/slideshow/img/andrew.jpeg"))
my_img2 = ImageTk.PhotoImage(Image.open("D:/OneDrive/py/tkinter/slideshow/img/gingerbread.jpeg"))
my_img3 = ImageTk.PhotoImage(Image.open("D:/OneDrive/py/tkinter/slideshow/img/train.jpeg"))

image_list = [my_img0, my_img1, my_img2, my_img3]

status = Label(root, text="Image "+ str(1) +" of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image=my_img0)
my_label.grid(row=0, column=0, columnspan=3) #3 column span to span back, exit, forward buttons

def forward(image_number):
	global my_label
	global button_forward
	global button_back
	global status

	status.grid_forget()
	status = Label(root, text="Image "+ str(image_number) +" of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

	my_label.grid_forget()
	my_label = Label(image=image_list[image_number-1])

	button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
	button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

	if image_number == 4:
		button_forward = Button(root, text=">>", state=DISABLED)

	my_label.grid(row=0, column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_forward.grid(row=1, column=2)
	status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def back(image_number):
	global my_label
	global button_forward
	global button_back
	global status

	status.grid_forget()
	status = Label(root, text="Image "+ str(image_number) +" of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

	my_label.grid_forget()
	my_label = Label(image=image_list[image_number-1])
	button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
	button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

	if image_number == 1:
		button_back = Button(root, text="<<", state=DISABLED)

	my_label.grid(row=0, column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_forward.grid(row=1, column=2)
	status.grid(row=2, column=0, columnspan=3, sticky=W+E)


button_back = Button(root, text="<<", state=DISABLED) #last photo
button_exit = Button(root, text="QUIT", command=root.quit) #exit program
button_forward = Button(root, text=">>", command=lambda: forward(2)) #next photo

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()