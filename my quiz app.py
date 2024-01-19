import tkinter as tk
from tkinter import messagebox
import random
from tkinter import Tk, Label, Button, StringVar, IntVar, Entry, messagebox ,simpledialog
from questions.Questions import question

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Game")
        self.master.geometry("600x400")

        self.total_rupees = 0
        self.player_name = ""

        self.rupees_list = [1 * (2 ** i) for i in range(158)]
        self.selected_questions = []

        self.current_question_index = 0

        self.label_question = Label(self.master, text="", wraplength=500, justify="center")
        self.label_question.pack(pady=20)
        
        self.label_name = Label(self.master, text="Muhammad Hasnat Rasool", anchor="e", font=("Arial", 20), fg="green")
        self.label_name.place(relx=1, rely=1, anchor="se")

        self.radio_var = IntVar()
        self.radio_var.set(-1)

        self.radio_buttons = []
        for i in range(4):
            radio_button = Button(self.master, text="", command=lambda i=i: self.answer_selected(i))
            radio_button.pack(pady=5)
            self.radio_buttons.append(radio_button)

        self.button_next = Button(self.master, text="Next Question", command=self.next_question)
        self.button_next.pack(pady=10)

        self.button_skip = Button(self.master, text="Skip Question", command=self.skip_question)
        self.button_skip.pack(pady=10)

        self.button_restart = Button(self.master, text="Restart", command=self.restart_quiz)
        self.button_restart.pack(pady=10)

        self.label_rupees = Label(self.master, text="Total Prize Money: Rs. 0")
        self.label_rupees.pack(pady=10)

        self.show_name_entry()

    def show_name_entry(self):
        self.player_name = simpledialog.askstring("Input", "Enter your name:")
        self.master.title(f"Welcome, {self.player_name}!")

        num_questions = simpledialog.askinteger("Input", "Enter the number of questions you want to answer:",
                                                minvalue=1, maxvalue=len(question))
        # self.selected_questions = question[:num_questions]
        self.selected_questions = random.sample(question, num_questions)

        self.show_question()

    def show_question(self):
        if self.current_question_index < len(self.selected_questions):
            question, options, _ = self.selected_questions[self.current_question_index]

            self.label_question.config(
                text=f"Question {self.current_question_index + 1} - RS.{self.rupees_list[self.current_question_index]}\n\n{question}")

            for i in range(4):
                self.radio_buttons[i].config(text=options[i])

            self.button_next.config(state="disabled")
        else:
            self.show_result()

    def answer_selected(self, selected_answer):
        self.radio_var.set(selected_answer)
        self.button_next.config(state="normal")

    def next_question(self):
        selected_answer = self.radio_var.get()

        if selected_answer == -1:
            messagebox.showwarning("Warning", "Please select an answer.")
            return

        _, _, correct_answer = self.selected_questions[self.current_question_index]

        if selected_answer == correct_answer:
            print("Your answer is correct congratulations !")
            self.total_rupees += self.rupees_list[self.current_question_index]

        self.current_question_index += 1
        self.update_rupees_label()
        # messagebox.showinfo("Question answered", f"Congratulations,\nYour  score is Rs. {self.total_rupees}")
        if self.current_question_index < len(self.selected_questions):
            self.show_question()
        else:
            self.show_result()

    def skip_question(self):
        self.current_question_index += 1
        self.update_rupees_label()
        if self.current_question_index < len(self.selected_questions):
            self.show_question()
        else:
            self.show_result()

    def restart_quiz(self):
        self.current_question_index = 0
        self.total_rupees = 0
        self.update_rupees_label()
        self.show_question()

    def show_result(self):
        messagebox.showinfo("Quiz Completed",
                            f"Congratulations, {self.player_name}!\nYour final score is Rs. {self.total_rupees}")
        self.save_game()
        self.master.destroy()

    def update_rupees_label(self):
        self.label_rupees.config(text=f"Total Prize Money: Rs. {self.total_rupees}")

    def save_game(self):
        with open("game_records.txt", "a") as file:
            file.write(f"Player: {self.player_name}, Total Prize Money: Rs.{self.total_rupees}\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
   
# code written by hasnat , 
# more ideas sounds for correct and background+ next questions
# single window for all name + questions + show question .
# clear answers format.
# categories