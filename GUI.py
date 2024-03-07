import tkinter as tk
from tkinter import *
import predict

# Creating tkinter window
window = Tk()
window.title('EEG Motor Imagery')
window.geometry('500x500')

up_arrow = tk.PhotoImage(file='Images/up_arrow.png')
down_arrow = tk.PhotoImage(file='Images/down_arrow.png')
left_arrow = tk.PhotoImage(file='Images/left_arrow.png')
right_arrow = tk.PhotoImage(file='Images/right_arrow.png')

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

predict_button = Button(window, text='Predict', command=update_arrows)
predict_button.place(x=225, y=250)

window.mainloop()