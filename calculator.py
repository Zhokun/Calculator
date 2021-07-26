from tkinter import *


class Calculator(Tk):
    def __init__(self):
        Tk.__init__(self)
        # Set window dimension
        self.geometry(f'400x500+'
                      f'{int((self.winfo_screenwidth() / 2) - (400 / 2))}+{int((self.winfo_screenheight() / 2) - (400 / 2))}')
        # Set title
        self.title('Calculator')
        # Set icon
        self.iconphoto(True, PhotoImage(file='Da.png'))

        # Frame for the old calc result
        self.above_result = Frame(self)
        self.above_result.pack()

        # Label for above result
        self.cima = Label(self.above_result, font=('Verdana', 15), width=22,
                          justify='right', )
        self.cima.pack()
        # Frame for the number being typed
        self.below_result = Frame(self)
        self.below_result.pack()

        # Frame for below result
        self.baixo = Label(self.below_result, font=('Verdana', 15), width=22,
                           justify='right', )
        self.baixo.pack()

        # Keyboard Frame
        self.kb_main_frame = Frame(self, )
        self.kb_main_frame.pack()

        # First line frame
        self.first_line = Frame(self.kb_main_frame)
        self.first_line.pack()

        # Buttons first line
        self.b_null = Button(self.first_line, text='C', font=('Verdana', 25), width=3, command=lambda: self.get_values('clear'))
        self.b_null.pack(side=LEFT, padx=2, pady=2)

        self.b_divide = Button(self.first_line, text='/', font=('Verdana', 25), width=3, command=lambda: self.get_values('/'))
        self.b_divide.pack(side=LEFT, padx=2, pady=2)

        self.b_times = Button(self.first_line, text='*', font=('Verdana', 25), width=3, command=lambda : self.get_values('*'))
        self.b_times.pack(side=LEFT, padx=2, pady=2)

        self.b_minus = Button(self.first_line, text='-', font=('Verdana', 25), width=3, command=lambda: self.get_values('-'))
        self.b_minus.pack(side=LEFT, padx=2, pady=2)

        # Second line frame
        self.second_line = Frame(self.kb_main_frame)
        self.second_line.pack()

        # Buttons second line
        self.b_seven = Button(self.second_line, text='7', font=('Verdana', 25), width=3, command=lambda: self.get_values(7))
        self.b_seven.pack(side=LEFT, padx=2, pady=2)

        self.b_eight = Button(self.second_line, text='8', font=('Verdana', 25), width=3, command=lambda: self.get_values(8))
        self.b_eight.pack(side=LEFT, padx=2, pady=2)

        self.b_nine = Button(self.second_line, text='9', font=('Verdana', 25), width=3, command=lambda: self.get_values(9))
        self.b_nine.pack(side=LEFT, padx=2, pady=2)

        self.b_plus = Button(self.second_line, text='+', font=('Verdana', 25), width=3, command=lambda: self.get_values('+'))
        self.b_plus.pack(side=LEFT, padx=2, pady=2)

        # Third line frame
        self.third_line = Frame(self.kb_main_frame)
        self.third_line.pack()

        # Buttons third line
        self.b_four = Button(self.third_line, text='4', font=('Verdana', 25), width=3, command=lambda: self.get_values(4))
        self.b_four.pack(side=LEFT, padx=2, pady=2)

        self.b_five = Button(self.third_line, text='5', font=('Verdana', 25), width=3, command=lambda: self.get_values(5))
        self.b_five.pack(side=LEFT, padx=2, pady=2)

        self.b_six = Button(self.third_line, text='6', font=('Verdana', 25), width=3, command=lambda: self.get_values(6))
        self.b_six.pack(side=LEFT, padx=2, pady=2)

        self.b_dot = Button(self.third_line, text='.', font=('Verdana', 25), width=3, command=lambda: self.get_values('.'))
        self.b_dot.pack(side=LEFT, padx=2, pady=2)
        # Fourth line frame
        self.fourth_line = Frame(self.kb_main_frame)
        self.fourth_line.pack()
        # Buttons fourth line
        self.b_one = Button(self.fourth_line, text='1', font=('Verdana', 25), width=3, command=lambda: self.get_values(1))
        self.b_one.pack(side=LEFT, padx=2, pady=2)

        self.b_two = Button(self.fourth_line, text='2', font=('Verdana', 25), width=3, command=lambda: self.get_values(2))
        self.b_two.pack(side=LEFT, padx=2, pady=2)

        self.b_three = Button(self.fourth_line, text='3', font=('Verdana', 25), width=3, command=lambda: self.get_values(3))
        self.b_three.pack(side=LEFT, padx=2, pady=2)

        self.parentheses = Frame(self.fourth_line,)
        self.parentheses.pack(side=LEFT, padx=2, pady=2)
        self.b_p_right = Button(self.parentheses, text='(', font=('Verdana', 12), width=2, )
        self.b_p_right.pack(side=LEFT, padx=2, pady=2)
        self.b_p_left = Button(self.parentheses, text=')', font=('Verdana', 12), width=2, )
        self.b_p_left.pack(side=LEFT, padx=2, pady=2)
        # Fourth line frame
        self.fifth_line = Frame(self.kb_main_frame)
        self.fifth_line.pack()
        # Buttons fourth line
        self.b_zero = Button(self.fifth_line, text='0', font=('Verdana', 25), width=7, command=lambda: self.get_values(0))
        self.b_zero.pack(side=LEFT, padx=2, pady=2)
        # Button to calculate
        self.b_calculate = Button(self.fifth_line, text='=', font=('Verdana', 25), width=7, command=self.calculate)
        self.b_calculate.pack(side=LEFT, padx=2, pady=2)

        # Save the expression
        self.ex_cima = ''
        self.numeroembaixo = ''

    # Get all the values and concatenate them
    def get_values(self, txt):
        # If button 'C' is pressed, clear the screen


        if txt == 'clear':
            self.ex_cima = ''
            self.numeroembaixo = ''
            self.baixo.config(text='')
            self.cima.config(text='')
        else:
            if txt == '+':
                self.ex_cima += self.numeroembaixo + '+'
                self.cima.config(text=self.ex_cima)
                self.numeroembaixo = ''
                print(self.numeroembaixo)
            elif txt == '-':
                self.ex_cima += self.numeroembaixo + '-'
                self.cima.config(text=self.ex_cima)
                self.numeroembaixo = ''
                print(self.numeroembaixo)
            elif txt == '*':
                self.ex_cima += self.numeroembaixo + '*'
                self.cima.config(text=self.ex_cima)
                self.numeroembaixo = ''
                print(self.numeroembaixo)
            elif txt == '/':
                self.ex_cima += self.numeroembaixo + '/'
                self.cima.config(text=self.ex_cima)
                self.numeroembaixo = ''
                print(self.numeroembaixo)
            else:

                self.numeroembaixo += str(txt)
                self.baixo.config(text=self.numeroembaixo)





    def calculate(self):
        # Calculate using function eval
        result = eval(self.ex_cima + self.numeroembaixo)
        self.ex_cima = str(result)
        self.baixo.config(text=result)
        self.numeroembaixo = ''
        return str(result)


if __name__ == '__main__':
    app = Calculator()
    app.mainloop()
