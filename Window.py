import tkinter as tk
import threading


class ProcessWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Process Window")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.text_var = tk.StringVar()
        self.text_var.set("Initializing...")

        self.label = tk.Label(
            root, textvariable=self.text_var, font=("Helvetica", 12))
        self.label.pack(padx=20, pady=20)

    def set_text(self, new_text):
        self.text_var.set(new_text)

    def on_closing(self):
        self.root.destroy()


def some_function():
    process_window.set_text("Updating status from some_function...")
    # Rest of your code


def another_function():
    process_window.set_text("Updating status from another_function...")
    # Rest of your code


if __name__ == "__main__":
    root = tk.Tk()
    process_window = ProcessWindow(root)

    calculation_thread = threading.Thread(target=some_function)
    calculation_thread.start()

    another_thread = threading.Thread(target=another_function)
    another_thread.start()

    root.mainloop()
