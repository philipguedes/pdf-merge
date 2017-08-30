from tkinter import *
from views.main_window import Application


def main():
    # Creating empty window with a title
    root = Tk()
    root.title("Bizu do Gafa")

    # Getting the screen infos
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    geometry = '{}x{}+{}+{}'.format(700, 400, width//4, height//4)
    root.geometry(geometry)

    # Initializing the app
    Application(root)
    root.mainloop()


if __name__ == '__main__':
    main()
