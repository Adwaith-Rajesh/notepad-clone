from tkinter import *
from tkinter.font import Font


class Notepad(Tk):
    def __init__(self, *args, **kwargs):
        super(Notepad, self).__init__(*args, **kwargs)

        self.title("Notepad -Clone Adwaith-Rajesh")
        self.geometry("700x500+100+50")

        self.setup_menu_bar()

    def setup_menu_bar(self):
        """ This method will make all the required menu bar """

        # variable for the check button
        self.is_status_bar_checked = IntVar(self)
        self.is_status_bar_checked.set(1)

        # initializing the menu object
        self.menu = Menu(self)
        self.config(menu=self.menu)

        # the file menu
        self.file_menu = Menu(self.menu, tearoff=False)
        self.file_menu.add_command(label="New")
        self.file_menu.add_command(label="New Window")
        self.file_menu.add_command(label="Open")
        self.file_menu.add_command(label="Save")
        self.file_menu.add_command(label="Save As")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.quit)

        # The edit menu
        self.edit_menu = Menu(self.menu, tearoff=False)
        self.edit_menu.add_command(label="Cut")
        self.edit_menu.add_command(label="Copy")
        self.edit_menu.add_command(label="Paste")
        self.edit_menu.add_command(label="Delete")
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Select All")

        # The format menu
        self.format_menu = Menu(self.menu, tearoff=False)
        self.format_menu.add_command(label="Font")

        # view menu
        self.view_menu = Menu(self.menu, tearoff=False)
        self.view_menu.add_checkbutton(
            label="Status Bar",
            onvalue=1,
            offvalue=0,
            variable=self.is_status_bar_checked,
        )

        # The help menu
        self.help_menu = Menu(self.menu, tearoff=False)
        self.help_menu.add_command(label="About Notepad Clone")

        # add the all the sub menu to the main menu bar
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.menu.add_cascade(label="Format", menu=self.format_menu)
        self.menu.add_cascade(label="View", menu=self.view_menu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)

        # Call the setup_ui method
        self.setup_ui()

    def setup_ui(self):
        """Set up the main UI stuff"""

        # The font
        self.default_text_area_font = Font(family="Lucida Console",
                                           size=10,
                                           weight=NORMAL)

        self.text_frame = Frame(self)
        self.text_frame.pack(side=TOP,
                             anchor=W,
                             fill=BOTH,
                             expand=True,
                             pady=(0, 10))

        self.text_area = Text(self.text_frame,
                              wrap=NONE,
                              font=self.default_text_area_font)
        self.text_area.pack(expand=True, fill=BOTH, side=LEFT)

        self.y_scroll = Scrollbar(self.text_frame,
                                  command=self.text_area.yview)
        self.y_scroll.pack(side=RIGHT, fill=Y)

        self.x_scroll = Scrollbar(self,
                                  orient=HORIZONTAL,
                                  command=self.text_area.xview)
        self.x_scroll.pack(side=BOTTOM, fill=X, anchor=W)
        self.text_area.config(yscrollcommand=self.y_scroll.set,
                              xscrollcommand=self.x_scroll)

    # def test(self):
    #     print(self.is_status_bar_checked.get())


if __name__ == "__main__":
    pad = Notepad()
    pad.mainloop()