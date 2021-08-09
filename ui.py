import time
from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

#  this is called every time we create a new object from this class
# create the buttons and layout here
# make these widgets a property of the class
# ex: self.window vs just window



    def __init__(self, quiz_brain: QuizBrain):
        # pass in the quiz_brain object from the main.py
        # create a property called quiz to hold this object
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.minsize(width=340, height=340)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0")
        self.score_label.config(padx=2, pady=2, fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.config(bg="white")
        font_tuple=("Arial", 20, "italic")
        self.question_text=self.canvas.create_text(
            150, 125,
            width=280,
            text="",
            font=font_tuple)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_image = PhotoImage(file="./images/true.png")
        false_image = PhotoImage(file="./images/false.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.check_true)
        self.true_button.config(pady=20, padx=20)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.check_false)
        self.false_button.config(pady=20, padx=20)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        #  change canvas background back to white
        self.canvas.config(bg="white")
        # check if there are questions remaining
        if self.quiz.still_has_questions():
            # uses quiz brain to get next question from the random list from the api
            q_text = self.quiz.next_question()
            # next, update the canvas with this text
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text,
                text=f"You have reached the end of the quiz")
        # disable the buttons since the quiz is over
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def check_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg = "green")
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg = "red")
            self.window.after(1000, self.get_next_question)
