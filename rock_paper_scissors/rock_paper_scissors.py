from tkinter import *
import random
import tkinter as tk

choices = ["Rock", "Paper", "Scissors"]

player = ""

draws = 0
wins = 0
loses = 0

root = Tk()
root.geometry("500x500")
root.title("Rock-Paper-Scissors")
root.iconbitmap("icon.ico")

canvas = Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
canvas.pack()

background_image = PhotoImage(file="font.png")
canvas.background = background_image
canvas.create_image(0, 0, anchor=NW, image=background_image)





def logic(player, computer):
    global draws, wins, loses

    def delete():
        result.place_forget()

    if player == computer:
        result = tk.Label(root, text="Draw!", font=("Arial", 60), fg="green", bg="red")
        result.place(x=120, y=220)
        root.after(1000, delete)
        draws += 1
    elif (player == "Rock" and computer == "Scissors") or \
            (player == "Paper" and computer == "Rock") or \
            (player == "Scissors" and computer == "Paper"):
        result = tk.Label(root, text="You win!", font=("Arial", 60), fg="green", bg="red")
        result.place(x=120, y=220)
        root.after(1000, delete)

        wins += 1
    else:
        loses += 1
        result = tk.Label(root, text="You Lose!", font=("Arial", 60), fg="green", bg='red')
        result.place(x=120, y=220)
        root.after(1000, delete)


def rock():
    player = "Rock"
    computer_choices = random.choice(choices)
    logic(player, computer_choices)


def paper():
    player = "Paper"
    computer_choices = random.choice(choices)
    logic(player, computer_choices)


def scissors():
    player = "Scissors"
    computer_choices = random.choice(choices)
    logic(player, computer_choices)


rock_button = Button(root, text="Rock", font=("Arial", 30), bg="transparent", fg="black", command=rock)
paper_button = Button(root, text="Paper", font=("Arial", 30), bg="white", fg="black", command=paper)
scissors_button = Button(root, text="Scissors", font=("Arial", 30), bg="white", fg="black", command=scissors)

rock_button.place(x=10, y=400)
paper_button.place(x=350, y=400)
scissors_button.place(x=300, y=10)
scissors_button.place()

label = tk.Label(root, text=f"Wins: {wins}\nLoses: {loses}\nDraws: {draws}", fg="green",
                     font=("Arial", 25))
label.place(x=10, y=10)

rock_button.pack_forget()
root.mainloop()
