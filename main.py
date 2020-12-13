from tkinter import *
from tkinter.font import Font
from tkinter.messagebox import *
from tkinter.filedialog import askopenfilename


class Notepad(Tk):
    def __init__(self, *args, **kwargs):
        super(Notepad, self).__init__(*args, **kwargs)

        self.file_name_opened = "*untitled.txt"

        self.title(f"{self.file_name_opened} Notepad -Clone Adwaith-Rajesh")
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
        self.file_menu.add_command(
            label="New", command=lambda: self.menu_commands("file", "new"))
        self.file_menu.add_command(
            label="New Window",
            command=lambda: self.menu_commands("file", "new-w"))
        self.file_menu.add_command(
            label="Open", command=lambda: self.menu_commands("file", "open"))
        self.file_menu.add_command(
            label="Save", command=lambda: self.menu_commands("file", "save"))
        self.file_menu.add_command(
            label="Save As",
            command=lambda: self.menu_commands("file", "save-as"))
        self.file_menu.add_separator()
        self.file_menu.add_command(
            label="Exit", command=lambda: self.menu_commands("file", "exit"))

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

        # load all the binding

        self.note_bindings()

    def note_bindings(self):
        self.bind_all("<Control-q>", self.exit_notepad)
        self.bind_all("<Control-s>", self.exit_notepad)
        self.bind_all("<Control-Shift-S>", self.exit_notepad)
        self.bind_all("<Control-o>", self.exit_notepad)
        self.bind_all("<Control-n>", self.exit_notepad)
        self.bind_all("<Control-Shift-N>", self.exit_notepad)
        self.bind_all("<Control-q>", self.exit_notepad)

    def menu_commands(self, main_, sub_):
        print("in menu commands")
        commands = {
            "file": {
                "new": lambda: self.new_options(0),
                "new-w": "",
                "open": "",
                "save": "",
                "save-as": "",
                "exit": ""
            },
            "edit": {"cut", "copy", "paste", "delete", "select-all"},
        }

        print(main_, sub_, commands[main_][sub_])
        commands[main_][sub_]()

    def new_options(self, _i: int):
        print("New option", _i)
        # _i = 0 => open new file
        # _i = 1 => open a new window

        if _i == 0:
            file_name = askopenfilename()
            with open(file_name, "r") as f:
                contents = f.read()
                self.text_area.delete(0.0, END)
                self.text_area.insert(0.0, contents)
                # TODO: change the title
                # TODO: Ask the user to save before changing the file
        if _i == 1: ...

    def save_options(self, _i: int):
        pass

    def edit_options(self, _i: int):
        pass

    def exit_notepad(self, event):
        self.quit()

    def test(self):
        print(self.is_status_bar_checked.get())


if __name__ == "__main__":
    pad = Notepad()
    pad.mainloop()