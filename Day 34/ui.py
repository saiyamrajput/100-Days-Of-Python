# import statements
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    """Creates window, buttons, and label (Interface for the User)"""
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # creating window
        self.window = Tk()
        self.window.title("Quizz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # creating score label
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR,
                                 font=("Cambria", 15, "bold"))
        self.score_label.grid(column=1, row=0)

        # creating canvas
        self.canvas = Canvas(width=300, height=250, highlightthickness=0,
                             bg="white")
        self.canvas_text = self.canvas.create_text(150, 125, text="Hello",
                                                   width=280,
                                                   fill="black",
                                                   font=("Cambria", 20,
                                                         "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # creating buttons
        self.true_button_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=self.true_button_image,
                                  command=self.answer_is_true,
                                  text="True", fg="green", compound="top",
                                  font=("Cambria", 15, "bold"),
                                  highlightthickness=0, bg=THEME_COLOR)
        self.true_button.grid(column=0, row=2)

        self.false_button_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=self.false_button_image,
                                   command=self.answer_is_false,
                                   text="False", fg="red", compound="top",
                                   font=("Cambria", 15, "bold"),
                                   highlightthickness=0, bg=THEME_COLOR)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """Generates a new question"""

        # keeping screen background white when quiz ended or new question is
        #   displayed
        self.canvas.config(bg="white")
        # checking if there are any questions left or not
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=question)

            # enabling true and false button
            self.true_button.config(state="normal")
            self.false_button.config(state="normal")
        else:
            self.canvas.itemconfig(self.canvas_text, text="You have reached the"
                                                          " end of the Quiz.")

            # disabling true and false button
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_is_true(self):
        """This method checks if the answer given by user is true or not"""
        answer = self.quiz.check_answer("true")
        self.check_answer(answer)

    def answer_is_false(self):
        """This method checks if the answer given by user is false or not"""
        answer = self.quiz.check_answer("false")
        self.check_answer(answer)

    def flash_canvas(self, color, count, next_color):
        """Flashes the canvas background color Twice"""
        if count > 0:
            self.canvas.config(bg=color)
            new_color = "white" if color == next_color else next_color
            self.window.after(200, self.flash_canvas, new_color, count - 1,
                              next_color)
        else:
            self.canvas.config(bg=color)

    def check_answer(self, answer):
        """Checks the user answer and displays if user is right or wrong"""
        if answer:
            color = "green"
        else:
            color = "red"

        # disabling true and false button
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

        self.flash_canvas(color, 4, color)
        self.window.after(2000, self.get_next_question)
