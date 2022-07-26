from quiz_brain import QuizBrain
import tkinter as t

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = t.Tk()
        self.window.config(background=THEME_COLOR, padx=20, pady=20)
        self.window.title("Quizzler")
        # Score
        self.score = t.Label()
        self.score.config(text=f"Score: {self.quiz.score}", font=("Arial", 20, "italic"), fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)
        # Buttons
        self.right_button_img = t.PhotoImage(file="images/true.png")
        self.wrong_button_img = t.PhotoImage(file="images/false.png")
        self.right_button = t.Button()
        self.right_button.config(image=self.right_button_img, bg=THEME_COLOR,
                                 activebackground=THEME_COLOR, border=0, command=self.right_button_click)
        self.right_button.grid(column=0, row=2)
        self.wrong_button = t.Button()
        self.wrong_button.config(image=self.wrong_button_img, bg=THEME_COLOR,
                                 activebackground=THEME_COLOR, border=0, command=self.wrong_button_click)
        self.wrong_button.grid(column=1, row=2)
        # Canvas
        self.canvas = t.Canvas(width=300, height=250)
        self.text = self.canvas.create_text((150,125),
                                            width=280,
                                            text="",
                                            font=("Arial", 20, "italic"),
                                            fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.change_text()

        self.window.mainloop()

    def change_text(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text, fill=THEME_COLOR)
            self.score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.text, text="You've reached the end of the quiz.", fill=THEME_COLOR)
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def right_button_click(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong_button_click(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="#60C750")
            self.canvas.itemconfig(self.text, fill="white")
        else:
            self.canvas.config(bg="#F36E6E")
            self.canvas.itemconfig(self.text, fill="white")

        self.window.after(1000, self.change_text)