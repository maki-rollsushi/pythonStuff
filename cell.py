from tkinter import Button


class Cell:
    def __init__(self, isMine = False):
        self.isMine = isMine
        self.cell_btn_obj = None

    def create_btn(self, location):
        btn = Button(
            location,
            text = 'Text'
        )
        self.create_btn = btn


