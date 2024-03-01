""" Main GUI file for the application. """
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from add_sub_gui import Gui

class MainGui:
    """ Main GUI class. """
    def __init__(self):
        self.root = ttk.Window(title="Gestione iscritti")
        self.style = ttk.Style("darkly")
        self.add_sub_gui = Gui(self)

    def build_gui_widgets(self):
        """ Build the main GUI widgets. """
        b1 = ttk.Button(
            self.root,
            text="Controlla scadenze",
            bootstyle=(INFO, OUTLINE),
        )
        b1.pack(padx=5, pady=10)
        b2 = ttk.Button(
            self.root,
            text="Aggiungi utente",
            bootstyle=(INFO, OUTLINE),
            command=lambda: self.switch_page(self.add_sub_gui)
        )
        b2.pack(padx=5, pady=10)

        b3 = ttk.Button(
            self.root,
            text="Modifica dati utente",
            bootstyle=(INFO, OUTLINE),
        )
        b3.pack(padx=5, pady=10)
        b4 = ttk.Button(
            self.root,
            text="Salva su excel",
            bootstyle=(INFO, OUTLINE),
        )
        b4.pack(padx=5, pady=10)

    def switch_page(self,target_page):
        """ Switch the page. """
        [button.pack_forget() for button in list(self.root.children.values())]
        target_page.build_gui_widgets()

    def run(self):
        """ Run the GUI. """
        self.root.mainloop()

gui = MainGui()
gui.build_gui_widgets()
gui.run()
