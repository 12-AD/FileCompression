import tkinter as tk
from tkinter import filedialog
import lzma

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.file_label = tk.Label(self, text="Select a file:")
        self.file_label.pack()
        self.file_entry = tk.Entry(self)
        self.file_entry.pack()

        self.browse_button = tk.Button(self, text="Browse", command=self.browse_file)
        self.browse_button.pack()

        self.compress_button = tk.Button(self, text="Compress", command=self.compress_file)
        self.compress_button.pack()

        self.decompress_button = tk.Button(self, text="Decompress", command=self.decompress_file)
        self.decompress_button.pack()

    def browse_file(self):
        filename = filedialog.askopenfilename()
        if filename:
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, filename)

    def compress_file(self):
        filename = self.file_entry.get()
        if filename:
            try:
                save_filename = filedialog.asksaveasfilename(defaultextension='.Abd')
                if save_filename:
                    with open(filename, 'rb') as f_in:
                        with lzma.open(save_filename, 'wb') as f_out:
                            f_out.write(f_in.read())
                    tk.messagebox.showinfo("Success", "File compressed successfully!")
            except Exception as e:
                tk.messagebox.showerror("Error", str(e))

    def decompress_file(self):
        filename = self.file_entry.get()
        if filename and filename.endswith('.Abd'):
            try:
                with lzma.open(filename, 'rb') as f_in:
                    save_filename = filedialog.asksaveasfilename(defaultextension='')
                    if save_filename:
                        with open(save_filename, 'wb') as f_out:
                            f_out.write(f_in.read())
                        tk.messagebox.showinfo("Success", "File decompressed successfully!")
            except Exception as e:
                tk.messagebox.showerror("Error", str(e))
        else:
            tk.messagebox.showerror("Error", "Invalid file type!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
