from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.font import Font
from tkinter.messagebox import *
from tkinter.filedialog import askopenfile, askopenfilename, asksaveasfilename


class Notepad(Tk):
    def __init__(self, *args, **kwargs):
        super(Notepad, self).__init__(*args, **kwargs)

        self.file_name_opened = "untitled"
        self.file_select = False

        self.geometry("700x500+100+50")

        self.add_title()
        self.setup_menu_bar()

    def add_title(self):
        self.title(f"{self.file_name_opened} Notepad -Clone Adwaith-Rajesh")

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
                              font=self.default_text_area_font,
                              undo=True,
                              maxundo=-1,
                              autoseparators=True)
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
        self.bind_all("<Control-s>", lambda x: self.save_options(0))
        self.bind_all("<Control-Shift-S>", lambda x: self.save_options(1))
        self.bind_all("<Control-o>", lambda x: self.open_option())
        self.bind_all("<Control-n>", lambda X: self.new_options(0))
        self.bind_all("<Control-Shift-N>", lambda x: self.new_options(1))

    def menu_commands(self, main_, sub_):
        commands = {
            "file": {
                "new": lambda: self.new_options(0),
                "new-w": lambda: self.new_options(1),
                "open": self.open_option,
                "save": lambda: self.save_options(0),
                "save-as": "",
                "exit": ""
            },
        }
        commands[main_][sub_]()

    def new_options(self, _i: int):
        # _i = 0 => open new file
        # _i = 1 => open a new window

        if _i == 0:
            if self.text_area.edit_modified():
                ans = askyesnocancel("Save",
                                     "Would you like to save the file ?")
                if ans:
                    self.save_options(1)
                    self.file_name_opened = "untitled"
                    self.add_title()
                    self.text_area.delete(0.0, END)
                    self.text_area.edit_modified(False)

                else:
                    pass

        if _i == 1:
            # The new window option
            Notepad().mainloop()

    def save_options(self, _i: int):
        # _i = 0 => if self.file_select then directly opens the file and writes
        # _i = 1 => asks the user for the filename and then saves

        if _i == 0:
            print("SAVED")
            if self.text_area.edit_modified() and "." in self.file_name_opened:
                with open(self.file_name_opened, "w") as f:
                    f.write(self.text_area.get(0.0, END))
                    self.text_area.edit_modified(False)

            else:
                self.save_options(1)

        if _i == 1:
            # The save as option
            filename = asksaveasfilename(initialfile=self.file_name_opened,
                                         title="Save As",
                                         defaultextension=".txt",
                                         filetypes=(("All Files", "."), ))

            if filename:
                with open(filename, "w") as f:
                    f.write(self.text_area.get(0.0, END))
                self.file_name_opened = filename
                self.add_title()
                self.text_area.edit_modified(False)

    def open_option(self):
        if self.text_area.edit_modified():
            ans = askyesnocancel(title="Save File",
                                 message="Do you like to save the file")
            if ans:
                filename = asksaveasfilename(initialfile=self.file_name_opened)

                if filename:
                    with open(filename, "w") as f:
                        f.write(self.text_area.get(0.0, END))
                        self.open_read()

        else:
            self.open_read()

    def open_read(self):
        open_file = askopenfile(title="Open")
        if open_file:
            with open(open_file.name, "r") as f:
                self.text_area.delete(0.0, END)
                self.text_area.insert(0.0, f.read())
                self.text_area.edit_modified(False)
                self.file_name_opened = open_file

    def exit_notepad(self, event):
        self.quit()


if __name__ == "__main__":
    pad = Notepad()
    pad.mainloop()