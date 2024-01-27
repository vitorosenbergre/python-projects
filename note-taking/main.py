import tkinter as tk
from tkinter import ttk, messagebox
import json
from ttkbootstrap import Style

# Creating the main window
root = tk.Tk()
root.title("Notes")
root.geometry("500x500")
style = Style(theme='journal')
style = ttk.Style()

# Tab bold font
style.configure("TNotebook.Tab", font=("TkDefaultFont", 14, "bold"))

# Notebook for the notes
notebook = ttk.Notebook(root, style="TNotebook")

# Load saved notes
notes = {}
try:
    with open("notes.json", "r") as f:
        notes = json.load(f)
except FileNotFoundError:
    pass

# Notebook to hold the notes
notebook = ttk.Notebook(root)
notebook.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Functions to add a new note


def add_note():
    # New tab for the note
    note_frame = ttk.Frame(notebook, padding=10)
    notebook.add(note_frame, text="New Note")

    # Widgets for the title and content of the note
    title_label = ttk.Label(note_frame, text="Title:")
    title_label.grid(row=0, column=0, padx=10, pady=10, sticky="W")

    title_entry = ttk.Entry(note_frame, width=30)  # Adjust the width
    title_entry.grid(row=0, column=1, padx=10, pady=10)

    content_label = ttk.Label(note_frame, text="Content:")
    content_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    content_entry = tk.Text(note_frame, width=30,
                            height=10)  # Adjust the width
    content_entry.grid(row=1, column=1, padx=10, pady=10)

    # Create a function to save the note
    def save_note():
        # title and content of the note
        title = title_entry.get()
        content = content_entry.get("1.0", tk.END)

        # Notes to the dictionary
        notes[title] = content.strip()

        # Save the notes dictionary to the file
        with open("notes.json", "w") as f:
            json.dump(notes, f)

        # Add Note to the notebook
        note_content = tk.Text(notebook, width=40, height=10)
        note_content.insert(tk.END, content)
        notebook.forget(notebook.select())
        notebook.add(note_content, text=title)

    # Note save button
    save_button = ttk.Button(note_frame, text="Save",
                             command=save_note, style="save.TButton")
    save_button.grid(row=2, column=1, padx=10, pady=10)


def load_notes():
    try:
        with open("notes.json", "r") as f:
            notes = json.load(f)

        for title, content in notes.items():
            note_content = tk.Text(notebook, width=40, height=10)
            note_content.insert(tk.END, content)
            notebook.add(note_content, text=title)
    except FileNotFoundError:
        # file doesn't exist
        pass


# Load notes at the start of the app
load_notes()

# Delete notes


# Delete notes
def delete_note():
    # Get the current tab index
    current_tab = notebook.index(notebook.select())

    # Title of note to be deleted
    note_title = notebook.tab(current_tab, "text")

    if note_title in notes:  # Check if the note title exists in the dictionary
        # Show a confirmation dialog
        confirm = messagebox.askyesno(
            "Delete Note", f"Are you sure you want to delete {note_title}?")

        if confirm:
            # Remove from the notebook
            notebook.forget(current_tab)

            # Remove from the notes dictionary
            # Use dict.pop(key, None) to avoid KeyError if key is not present
            notes.pop(note_title, None)

            # Save the notes dictionary to the file
            with open("notes.json", "w") as f:
                json.dump(notes, f)


# Load icon files
new_icon = tk.PhotoImage(file="icons/new_icon.png")
delete_icon = tk.PhotoImage(file="icons/delete_icon.png")

# Assuming you have ttkbootstrap installed, you can use the existing 'info.TButton' and 'primary.TButton' styles
style = Style(theme='journal')

# Extend the existing styles or create new ones
style.configure("new_note_button.TButton", foreground='black',
                background='#FFFFFF')  # Black text, white background
style.configure("delete_button.TButton", foreground='black',
                background='#FFFFFF')  # Black text, white background
style.configure("save.TButton", foreground='black',
                background='#FFFFFF')  # Black text, white background

# Buttons for the main frame with centered icons
new_button = ttk.Button(root, text="New Note", command=add_note,
                        image=new_icon, compound=tk.LEFT, style="new_note_button.TButton")
new_button.pack(side=tk.LEFT, padx=10, pady=10)

delete_button = ttk.Button(root, text="Delete", command=delete_note,
                           image=delete_icon, compound=tk.LEFT, style="delete_button.TButton")
delete_button.pack(side=tk.LEFT, padx=10, pady=10)

root.mainloop()