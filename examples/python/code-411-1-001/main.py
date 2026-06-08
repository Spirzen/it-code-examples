
import tkinter as tk

from tkinter import ttk, messagebox, filedialog, scrolledtext
from datetime import datetime

class DesktopAppDemo:
    def __init__(self, root):
        self.root = root
        self.root.title("Демонстрация десктопного интерфейса")
        self.root.geometry("900x600")

        # --- 1. Меню (Menu) ---
        menubar = tk.Menu(root)
        root.config(menu=menubar)

        # Пункт Файл
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Файл", menu=file_menu)
        file_menu.add_command(label="Открыть...", command=self.open_file)
        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=root.quit)

        # Пункт Правка
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Правка", menu=edit_menu)
        edit_menu.add_command(label="Копировать", accelerator="Ctrl+C")
        edit_menu.add_command(label="Вставить", accelerator="Ctrl+V")

        # Пункт Справка
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Справка", menu=help_menu)
        help_menu.add_command(label="О программе", command=self.show_about)

        # --- 2. Панель инструментов (Toolbar) ---
        toolbar = tk.Frame(root, bd=1, relief=tk.RAISED)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        btn_new = tk.Button(toolbar, text="📄 Новый", command=self.new_action)
        btn_new.pack(side=tk.LEFT, padx=2, pady=2)

        btn_save = tk.Button(toolbar, text="💾 Сохранить", command=self.save_action)
        btn_save.pack(side=tk.LEFT, padx=2, pady=2)

        btn_print = tk.Button(toolbar, text="🖨️ Печать", command=self.print_action)
        btn_print.pack(side=tk.LEFT, padx=2, pady=2)

        # --- 3. Вкладки (Tabs) ---
        tab_control = ttk.Notebook(root)
        tab_control.pack(expand=1, fill="both")

        # Вкладка 1: Элементы ввода
        tab_input = ttk.Frame(tab_control)
        tab_control.add(tab_input, text='Ввод данных')
        self.create_input_tab(tab_input)

        # Вкладка 2: Списки и таблицы
        tab_lists = ttk.Frame(tab_control)
        tab_control.add(tab_lists, text='Списки и Таблицы')
        self.create_list_tab(tab_lists)

        # Вкладка 3: Индикаторы и статус
        tab_status = ttk.Frame(tab_control)
        tab_control.add(tab_status, text='Статус и Прогресс')
        self.create_status_tab(tab_status)

        # --- 4. Строка состояния (Status Bar) ---
        self.status_var = tk.StringVar()
        self.status_var.set("Готов к работе")
        statusbar = tk.Label(root, textvariable=self.status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        statusbar.pack(side=tk.BOTTOM, fill=tk.X)

        # Контекстное меню для основного окна
        self.context_menu = tk.Menu(root, tearoff=0)
        self.context_menu.add_command(label="Обновить данные", command=self.refresh_data)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Настройки", command=self.show_settings)
        
        root.bind("<Button-3>", self.show_context_menu)

    def create_input_tab(self, parent):
        # Label и TextBox
        frame_top = tk.Frame(parent, padx=10, pady=10)
        frame_top.pack(fill=tk.X)

        lbl_name = tk.Label(frame_top, text="Имя пользователя:")
        lbl_name.grid(row=0, column=0, sticky=tk.W, pady=5)

        self.entry_name = tk.Entry(frame_top, width=40)
        self.entry_name.grid(row=0, column=1, pady=5, padx=5)
        self.entry_name.insert(0, "Введите имя...")
        self.entry_name.bind("<FocusIn>", lambda e: self.on_entry_focus(e, "Введите имя..."))
        self.entry_name.bind("<FocusOut>", lambda e: self.on_entry_focus_out(e, "Введите имя..."))

        # ComboBox
        lbl_role = tk.Label(frame_top, text="Роль:")
        lbl_role.grid(row=1, column=0, sticky=tk.W, pady=5)

        roles = ["Администратор", "Редактор", "Наблюдатель", "Гость"]
        self.combo_role = ttk.Combobox(frame_top, values=roles, state="readonly", width=37)
        self.combo_role.current(0)
        self.combo_role.grid(row=1, column=1, pady=5, padx=5)
        self.combo_role.bind("<<ComboboxSelected>>", self.on_combo_select)

        # Checkbox
        self.check_agree = tk.BooleanVar()
        chk_agree = tk.Checkbutton(frame_top, text="Я согласен с условиями обработки данных", variable=self.check_agree, command=self.on_checkbox_change)
        chk_agree.grid(row=2, column=0, columnspan=2, sticky=tk.W, pady=10)

        # Кнопка действия
        btn_submit = tk.Button(frame_top, text="Отправить форму", command=self.submit_form, bg="#dddddd")
        btn_submit.grid(row=3, column=0, columnspan=2, pady=10)

        # Многострочное поле (ScrolledText как аналог TextBox с прокруткой)
        lbl_desc = tk.Label(parent, text="Комментарий:", anchor=tk.W)
        lbl_desc.pack(fill=tk.X, padx=10, pady=(10, 0))
        
        self.txt_comment = scrolledtext.ScrolledText(parent, height=8)
        self.txt_comment.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    def create_list_tab(self, parent):
        # Поле поиска
        search_frame = tk.Frame(parent, padx=10, pady=5)
        search_frame.pack(fill=tk.X)
        
        lbl_search = tk.Label(search_frame, text="Поиск:")
        lbl_search.pack(side=tk.LEFT)
        
        self.entry_search = tk.Entry(search_frame)
        self.entry_search.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        self.entry_search.bind("<KeyRelease>", self.filter_list)

        # ListBox
        list_frame = tk.Frame(parent, padx=10, pady=5)
        list_frame.pack(fill=tk.BOTH, expand=True)

        self.listbox = tk.Listbox(list_frame)
        scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.listbox.yview)
        self.listbox.configure(yscrollcommand=scrollbar.set)

        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Заполнение списка данными
        sample_data = [f"Элемент данных {i}" for i in range(1, 51)]
        for item in sample_data:
            self.listbox.insert(tk.END, item)

        self.listbox.bind('<<ListboxSelect>>', self.on_list_select)

    def create_status_tab(self, parent):
        frame = tk.Frame(parent, padx=20, pady=20)
        frame.pack(fill=tk.BOTH, expand=True)

        lbl_progress = tk.Label(frame, text="Прогресс операции:")
        lbl_progress.pack(anchor=tk.W, pady=5)

        self.progress_bar = ttk.Progressbar(frame, orient=tk.HORIZONTAL, length=400, mode='determinate')
        self.progress_bar.pack(pady=10)

        btn_start = tk.Button(frame, text="Запустить процесс", command=self.start_process)
        btn_start.pack(pady=5)

        lbl_info = tk.Label(frame, text="Статус процесса: Ожидание", fg="blue")
        lbl_info.pack(pady=20)
        self.lbl_process_status = lbl_info

    # --- Обработчики событий (Event Handlers) ---

    def on_entry_focus(self, event, placeholder):
        if self.entry_name.get() == placeholder:
            self.entry_name.delete(0, tk.END)
            self.entry_name.config(fg="black")

    def on_entry_focus_out(self, event, placeholder):
        if not self.entry_name.get():
            self.entry_name.insert(0, placeholder)
            self.entry_name.config(fg="grey")

    def on_combo_select(self, event):
        selected = self.combo_role.get()
        self.status_var.set(f"Выбрана роль: {selected}")

    def on_checkbox_change(self):
        state = "принято" if self.check_agree.get() else "не принято"
        self.status_var.set(f"Согласие: {state}")

    def on_list_select(self, event):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            value = self.listbox.get(index)
            self.status_var.set(f"Выбран элемент #{index}: {value}")

    def filter_list(self, event):
        query = self.entry_search.get().lower()
        self.listbox.delete(0, tk.END)
        sample_data = [f"Элемент данных {i}" for i in range(1, 51)]
        for item in sample_data:
            if query in item.lower():
                self.listbox.insert(tk.END, item)

    def submit_form(self):
        name = self.entry_name.get()
        role = self.combo_role.get()
        comment = self.txt_comment.get("1.0", tk.END).strip()
        
        if name == "Введите имя..." or not name:
            messagebox.showwarning("Ошибка", "Пожалуйста, введите имя.")
            return

        msg = f"Форма отправлена!\nИмя: {name}\nРоль: {role}\nКомментарий: {comment[:20]}..."
        messagebox.showinfo("Успех", msg)
        self.status_var.set("Форма успешно отправлена")

    def start_process(self):
        self.lbl_process_status.config(text="Статус процесса: Выполняется...", fg="orange")
        self.progress_bar['value'] = 0
        self.run_progress(0)

    def run_progress(self, value):
        if value <= 100:
            self.progress_bar['value'] = value
            self.lbl_process_status.config(text=f"Статус процесса: {value}%")
            self.root.after(50, self.run_progress, value + 2)
        else:
            self.lbl_process_status.config(text="Статус процесса: Завершено", fg="green")
            self.status_var.set("Операция завершена")
            messagebox.showinfo("Готово", "Процесс завершен на 100%")

    def refresh_data(self):
        self.status_var.set("Данные обновлены")
        messagebox.showinfo("Обновление", "Списки и данные перезагружены.")

    def show_context_menu(self, event):
        try:
            self.context_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.context_menu.grab_release()

    def show_settings(self):
        messagebox.showinfo("Настройки", "Здесь могли бы быть настройки приложения.")

    def show_about(self):
        messagebox.showinfo("О программе", "Демонстрационное приложение\nВерсия 1.0\nИспользует Tkinter")

    def open_file(self):
        filename = filedialog.askopenfilename(title="Открыть файл", filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")])
        if filename:
            self.status_var.set(f"Открыт файл: {filename}")

    def new_action(self):
        self.status_var.set("Создание нового документа...")
    
    def save_action(self):
        self.status_var.set("Сохранение изменений...")
        messagebox.showinfo("Сохранение", "Данные сохранены (эмуляция).")

    def print_action(self):
        self.status_var.set("Отправка на печать...")

# --- Основной цикл (Main Loop) ---
if __name__ == "__main__":
    root = tk.Tk()
    app = DesktopAppDemo(root)
    # Запуск цикла обработки событий
    root.mainloop()
