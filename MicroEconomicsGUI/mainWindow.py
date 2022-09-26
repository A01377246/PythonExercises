from Question import Question
import tkinter as tk
from PIL import ImageTk,Image 
import pygame

class App(tk.Tk): #Inherits from the tk object

    def __init__(self):
        super().__init__()

        self.title('My Awesome App')
        #self.geometry('300x300')
        
        pygame.mixer.init()
        pygame.mixer.music.load("./MicroEconomicsGui/resources/audio/a.mp3")
        pygame.mixer.music.play(loops = -1)


def main():

    firstQuestion = Question(1, "Complete the following phrase: Trying to make the mother of all Omelettes here, Jack", 
    {"A": "Pass me the sauce", "B": "Can't fret over every egg", "C":"Nano machines, son"}, "C")

    print(f'Question {firstQuestion.questionNumber}')
    print(f'{firstQuestion.question}')
    for key, value in firstQuestion.optionDictionary.items():
        print(f'{key}) {value}')

    app = App()
    app.mainloop()
main()