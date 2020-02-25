from tkinter import filedialog
from tkinter import *
import hashlib

sha256_hash = hashlib.sha256()

filename = None


def center_window(width=500, height=500):
    # get screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))


def choose_file():
    window.filename = filedialog.askopenfilename(title="Select file")
    file_path = window.filename
    show_path = Label(window, text=file_path)
    show_path.grid(column=0, row=3, sticky="W")


def copy_hash():
    window.clipboard_clear()
    window.clipboard_append(window.file_hash)

    hash_copy_success = Label(window, text="Hash copied!")
    hash_copy_success.grid(column=0, row=8)


def calculate_hash():
    with open(window.filename, "rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
        window.file_hash = sha256_hash.hexdigest()
    computed_hash = Label(window, text=window.file_hash)
    computed_hash.grid(column=0, row=7)

    hash_copy_button = Button(window, text="Copy Hash", command=copy_hash)
    hash_copy_button.grid(column=0, row=8)


window = Tk()
center_window()
window.title("Crypt")

title = Label(window, text="Crypt", font=("Arial Rounded MT Bold", 25))
title.grid(column=0, row=0, sticky="W")

subtitle = Label(window, text="The handy crypto suite", font=("Arial Rounded MT Bold", 15))
subtitle.grid(column=0, row=1, sticky="W")

btn = Button(window, text="Choose File", command=choose_file)
btn.grid(column=0, row=2, sticky="W")

hash_title = Label(window, text="Hash", font=("Arial Rounded MT Bold", 15))
hash_title.grid(column=0, row=4, sticky="W")

hash_text = Label(window, text="A hash is a unique fingerprint of your file. \nIt is used to verify that the file was"
                               " not altered in time or during transmission.\n"
                               "Crypt uses the SHA-256 hashing algorithm.")
hash_text.grid(column=0, row=5, sticky="W")

hash_button = Button(window, text="Hash it", command=calculate_hash)
hash_button.grid(column=0, row=6, sticky="W")

window.mainloop()