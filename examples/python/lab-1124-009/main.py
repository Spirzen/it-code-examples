import tkinter as tk

root = tk.Tk()
root.title("Заметки")
root.geometry("400x300")

frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text = tk.Text(frame, wrap=tk.WORD, yscrollcommand=scrollbar.set)
text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=text.yview)

text.insert("1.0", "Черновик заметки..\nВторая строка.")

root.mainloop()
