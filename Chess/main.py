import tkinter as tk
from PIL import ImageTk, Image
from ChessMain import *


class WelcomeScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chess Game")

        # Set window size
        self.width = 400
        self.height = 400
        self.geometry("{}x{}".format(self.width, self.height))

        self.create_widgets()

    def create_widgets(self):

        ###

        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)

        # Create the Depth menu
        depth_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Depth", menu=depth_menu)

        # Add options for Depth menu
        depth_options = [1, 2, 3]
        self.depth_var = tk.IntVar()
        self.depth_var.set(depth_options[0])
        for depth in depth_options:
            depth_menu.add_radiobutton(label=f"Depth {depth}", value=depth, variable=self.depth_var)

        # Create the Color menu
        color_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Color", menu=color_menu)

        # Add options for Color menu
        color_options = ["White", "Black"]
        self.color_var = tk.StringVar()
        self.color_var.set(color_options[0])
        for color in color_options:
            color_menu.add_radiobutton(label=color, value=color, variable=self.color_var)
        ###
        canvas = tk.Canvas(self, width=self.width, height=self.height)
        canvas.pack(fill="both", expand=True)

        background_image = Image.open("image2.jpg")
        background_image = background_image.resize((self.width, self.height), Image.ANTIALIAS)
        background_image = ImageTk.PhotoImage(background_image)

        canvas.create_image(0, 0, image=background_image, anchor=tk.NW)
        canvas.image = background_image  # Keep a reference to the image

        label = tk.Label(self, text="Welcome to Chess Game!", font=("Arial", 24), bg="white")
        canvas.create_window(self.width // 2, 40, anchor=tk.CENTER, window=label)

        start_button = tk.Button(self, text="Start", command=self.start_game, width=20, bg="green", fg="white")
        canvas.create_window(self.width // 2, self.height // 2, anchor=tk.CENTER, window=start_button)

        exit_button = tk.Button(self, text="Exit", command=self.quit, width=20, bg="red", fg="white")
        canvas.create_window(self.width // 2, self.height // 2 + 50, anchor=tk.CENTER, window=exit_button)
        # Create the Algorithm menu
        algorithm_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Algorithm", menu=algorithm_menu)

        # Add options for Algorithm menu
        algorithm_options = ["MinMax", "Alpha Beta"]
        self.algorithm_var = tk.StringVar()
        self.algorithm_var.set(algorithm_options[0])
        for algorithm in algorithm_options:
            algorithm_menu.add_radiobutton(label=algorithm, value=algorithm, variable=self.algorithm_var)


    def get_algorithm(self):
        selected_algorithm = self.algorithm_var.get()
        return selected_algorithm

    # to get chosen depth
    def getDepth(self):
        selected_depth=self.depth_var.get()
        return  selected_depth
    # this function to run chess game
    def start_game(self):

        selected_algorithm = self.algorithm_var.get()
        self.destroy()
        Depth = self.getDepth()
        algorithm = self.get_algorithm()
        #print("Depth: ",selected)
        main(Depth,algorithm)  # to run the game

################# hello
if __name__ == "__main__":
    app = WelcomeScreen()
    app.mainloop()
