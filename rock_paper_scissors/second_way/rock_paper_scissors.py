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
root.configure(bg="white")


def reset():
    global draws, wins, loses
    draws, wins, loses = 0, 0, 0
    label.configure(text=f"Wins: {wins}\nLoses: {loses}\nDraws: {draws}")


def logic(player, computer):
    global draws, wins, loses

    def delete():
        result.place_forget()

    if player == computer:
        result = tk.Label(root, text=f"Draw!\nComputer: {computer}", font=("Arial", 30), fg="black", bg="blue")
        result.place(x=120, y=220)
        root.after(1000, delete)
        draws += 1
    elif (player == "Rock" and computer == "Scissors") or \
            (player == "Paper" and computer == "Rock") or \
            (player == "Scissors" and computer == "Paper"):
        result = tk.Label(root, text=f"You win!\nComputer: {computer}", font=("Arial", 30), fg="black", bg="green")
        result.place(x=120, y=220)
        root.after(1500, delete)

        wins += 1
    else:
        loses += 1
        result = tk.Label(root, text=f"You Lose!\nComputer: {computer}", font=("Arial", 30), fg="black", bg='red')
        result.place(x=120, y=220)
        root.after(1500, delete)
    label.configure(text=f"Wins: {wins}\nLoses: {loses}\nDraws: {draws}")


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

rock_photo = PhotoImage(file="rock.png")
paper_photo = PhotoImage(file="paper.png")
scissors_photo = PhotoImage(file="scissors.png")
reset_photo = PhotoImage(file="reset.png").subsample(4,4)

rock_button = Button(root, command=rock, image=rock_photo)
paper_button = Button(root, image=paper_photo, command=paper)
scissors_button = Button(root, image=scissors_photo, command=scissors)
reset_button = Button(root, image=reset_photo, command=reset)

rock_button.place(x=10, y=250)
paper_button.place(x=250, y=270)
scissors_button.place(x=240, y=1)
reset_button.place(x=20, y=130)

label = tk.Label(root, text=f"Wins: {wins}\nLoses: {loses}\nDraws: {draws}", fg="green",
                 font=("Arial", 25))
label.place(x=10, y=10)

rock_button.pack_forget()
root.mainloop()
