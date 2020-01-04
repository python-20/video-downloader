# ! Warning ! This is just a mockup for the GUI using tkinter, we will most likely use something else later on
# "PREPARE YOUR EYES, THIS MAY BE MESSY, I AM NOT LIABLE FOR LOSS OF EYESIGHT OR LOSS OF BRAIN CELLS" - Ryan S
import tkinter as tk
from tkinter.filedialog import askopenfilename


def gui():
    root = tk.Tk()
    root.title = "Youtube Downloader"  # The title of the youtube downloader

    filename = ''  # Default filename, add prom

    def run_gui():
        v1 = url_input.get()  # Gets URL
        v2 = filetype_var.get()  # Gets file type, might remove if we can't find an API which handles it
        v3 = playlist_var.get()  # Gets 0 if not a playlist, 1 if playlist as an integer
        v4 = filename  # Gets the path to save your document
        print(v1, v2, v3, v4)

    def reset_inputs():
        pass

    def get_filename():
        nonlocal filename
        filename = askopenfilename()

    # ~~~~ URL ~~~~~~~~~~~~
    url_label = tk.Label(root, text="Enter the URL of the video:")
    url_label.grid(row=1, column=1)

    url_input = tk.Entry(root)
    url_input.grid(row=1, column=2)

    # ~~~~ File type ~~~~~~~
    filetype_label = tk.Label(root, text="Enter the file type you want:")
    filetype_label.grid(row=2, column=1)

    filetype_input_list = [".mp4", ".mp3", ".placeholder3", ".placeholder4"]
    # Index of list is the default value in the dropdown menu
    filetype_var = tk.StringVar(root)
    filetype_var.set(filetype_input_list[0])

    filetype_input = tk.OptionMenu(root, filetype_var, *filetype_input_list)
    filetype_input.grid(row=2, column=2)

    # X ~~~~~~ Playlist Toggler ~~~~~~~ X Not a good idea with tkinter, ignore
    # playlist_input = tk.Scale(root, label="Playlist?", from_=0, to=1, orient=tk.HORIZONTAL)
    # playlist_input.grid(row=3, column=2)

    # ~~~~~ Playlist Checkbox ~~~~~~~~~~
    filetype_label = tk.Label(root, text="Playlist?")
    filetype_label.grid(row=3, column=1)

    playlist_var = tk.IntVar()
    playlist_input = tk.Checkbutton(root, variable=playlist_var)
    playlist_input.grid(row=3, column=2)

    # ~~~~~~~ File ~~~~~~~~~~~~~~~~
    filelocation_label = tk.Label(root, text="Open file location: ")
    filelocation_label.grid(row=4, column=1)

    filelocation_input = tk.Button(root, text="FILE", command=lambda: get_filename())
    filelocation_input.grid(row=4, column=2)

    # ~~~~~~ Buttons ~~~~~~~~~~~~~~
    run_button = tk.Button(root, text="Run", command=lambda: run_gui())
    run_button.grid(row=5, column=1)

    reset_button = tk.Button(root, text="Reset", command=lambda: reset_inputs())
    reset_button.grid(row=5, column=2)

    reset_inputs()

    root.mainloop()


if __name__ == "__main__":
    gui()  # Will only run_gui if it is the source file (not importing)
