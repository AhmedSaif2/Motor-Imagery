import tkinter as tk
from tkinter import *
from tkinter import filedialog
import pandas as pd
import predict

# Creating tkinter window
window = Tk()
window.title('EEG Motor Imagery')
window.geometry('500x500')

label = Label(window, text="Select a CSV file to upload")
label.pack()

up_arrow = tk.PhotoImage(file='up_arrow.png')
down_arrow = tk.PhotoImage(file='down_arrow.png')
left_arrow = tk.PhotoImage(file='left_arrow.png')
right_arrow = tk.PhotoImage(file='right_arrow.png')

up_arrow_label = tk.Label(window, image=up_arrow, bd=0)
down_arrow_label = tk.Label(window, image=down_arrow, bd=0)
left_arrow_label = tk.Label(window, image=left_arrow, bd=0)
right_arrow_label = tk.Label(window, image=right_arrow, bd=0)

up_arrow_label.place(x=225, y=100)
down_arrow_label.place(x=225, y=400)
left_arrow_label.place(x=50, y=240)
right_arrow_label.place(x=400, y=240)

def update_arrows():
    prediction=predict.predict_movement()
    if prediction == 'foot':
        initial_color = up_arrow_label.cget('bg')
        up_arrow_label.config(bg='green')
        up_arrow_label.after(2000, lambda: up_arrow_label.config(bg=initial_color))
    elif prediction == "tongue":
        initial_color = down_arrow_label.cget('bg')
        down_arrow_label.config(bg='green')
        down_arrow_label.after(2000, lambda: down_arrow_label.config(bg=initial_color))
    elif prediction == "left":
        initial_color = left_arrow_label.cget('bg')
        left_arrow_label.config(bg='green')
        left_arrow_label.after(2000, lambda: left_arrow_label.config(bg=initial_color))
    elif prediction == "right":
        initial_color = right_arrow_label.cget('bg')
        right_arrow_label.config(bg='green')
        right_arrow_label.after(2000, lambda: right_arrow_label.config(bg=initial_color))


def browseFiles():
    file_path = filedialog.askopenfilename(initialdir="/", title="Select a CSV File",
                                           filetypes=(("CSV files", "*.csv*"), ("all files", "*.*")))
    label.configure(text="File selected: " + file_path)
    data = pd.read_csv(file_path)
    print(data)

uploadButton = Button(window, text="Browse Files", command=browseFiles)
uploadButton.pack()
predict_button = Button(window, text='Predict', command=update_arrows)
predict_button.place(x=225, y=250)

window.mainloop()