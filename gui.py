import tkinter as tk
from tkinter import Text, filedialog, Menu


class FileChooserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LC Pdf Converter")
        self.selected_file = None
        self.saved_file = None

        # Pasek menu
        menu_bar = Menu(self.root)
        self.root.config(menu=menu_bar)

        # Dodanie menu "File"
        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # dodanie convert menu
        convert_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Convert", menu=convert_menu)

        # dodanie menu display
        display_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Display", menu=display_menu)

        # Opcje w menu "File"
        file_menu.add_command(label="Open File", command=self.open_file)
        file_menu.add_command(label="Save File", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        # opcje w menu "Display"
        display_menu.add_command(label="Display results", command=self.open_file)

        # text field
        text_field = Text(self.root, width=78, height=20)
        text_field.pack(pady=10)


    def open_file(self):
        self.selected_file = filedialog.askopenfilename(
            title="Select a file",
            filetypes=(("PDF Files", "*.pdf"),("Txt Files", "*.txt"), ("All Files", "*.*"))
        )
        if self.selected_file:
            print(f"Selected file: {self.selected_file}")

    def save_file(self):
        self.saved_file = filedialog.asksaveasfilename(
            title="Save file as",
            defaultextension=".pdf",
            filetypes=(("PDF Files", "*.pdf"), ("All Files", "*.*"))
        )
        if self.saved_file:
            print(f"File will be saved as: {self.saved_file}")
    
    def show_result():
        
        pass


# Uruchomienie aplikacji
root = tk.Tk()
root.geometry("800x600")
app = FileChooserApp(root)

root.mainloop()
