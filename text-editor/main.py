import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfile


def open_file(window, text_edit):
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])

    if not filepath:
        return

    text_edit.delete(1.0, tk.END)
    with open(filepath, "r") as f:
        content = f.read()
        text_edit.insert(tk.END, content)

    window.title(f"Open File: {filepath}")


def save_file(window, text_edit):
    file = asksaveasfile(defaultextension=".txt", filetypes=[
                         ("Text Files", "*.txt")])

    if not file:
        return

    filepath = file.name

    with open(filepath, "w") as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)

    window.title(f"Saved File: {filepath}")


def main():
    window = tk.Tk()
    window.title("Text Editor")

    text_edit = tk.Text(window, font=("Arial", 12), wrap=tk.WORD)
    text_edit.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    save_button = tk.Button(frame, text="Save", command=lambda: save_file(
        window, text_edit), width=15, height=2)
    open_button = tk.Button(frame, text="Open", command=lambda: open_file(
        window, text_edit), width=15, height=2)

    save_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    open_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
    frame.grid(row=0, column=0, sticky="ns", padx=10, pady=10)

    window.rowconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)

    window.bind("<Control-s>", lambda x: save_file(window, text_edit))
    window.bind("<Control-o>", lambda x: open_file(window, text_edit))

    window.mainloop()


if __name__ == "__main__":
    main()
