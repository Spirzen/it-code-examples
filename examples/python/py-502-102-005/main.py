
import socket
import threading
import tkinter as tk

from tkinter import scrolledtext, messagebox, simpledialog

class ChatClientGUI:
    def __init__(self, host='127.0.0.1', port=5555):
        self.host = host
        self.port = port
        self.client_socket = None
        self.nickname = None
        self.running = False
        
        # Создаём главное окно
        self.root = tk.Tk()
        self.root.title("Мессенджер")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # Настройка стилей
        self.setup_ui()
        
        # Подключаемся к серверу
        self.connect_to_server()
        
    def setup_ui(self):
        """Настройка интерфейса"""
        # Верхняя панель с информацией
        self.top_frame = tk.Frame(self.root, bg='gray', height=40)
        self.top_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.status_label = tk.Label(
            self.top_frame, 
            text="Не подключён", 
            bg='gray', 
            fg='white',
            font=('Arial', 10)
        )
        self.status_label.pack(side=tk.LEFT, padx=10)
        
        # Кнопки управления
        self.disconnect_btn = tk.Button(
            self.top_frame,
            text="Отключиться",
            command=self.disconnect,
            bg='red',
            fg='white'
        )
        self.disconnect_btn.pack(side=tk.RIGHT, padx=5)
        
        # Область отображения сообщений
        self.chat_area = scrolledtext.ScrolledText(
            self.root,
            wrap=tk.WORD,
            font=('Arial', 11),
            bg='white',
            fg='black'
        )
        self.chat_area.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Нижняя панель для ввода сообщений
        self.bottom_frame = tk.Frame(self.root)
        self.bottom_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Поле ввода сообщения
        self.message_entry = tk.Entry(
            self.bottom_frame,
            font=('Arial', 11),
            state='disabled'
        )
        self.message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        self.message_entry.bind('<Return>', self.send_message_event)
        
        # Кнопка отправки
        self.send_button = tk.Button(
            self.bottom_frame,
            text="Отправить",
            command=self.send_message,
            state='disabled',
            bg='#4CAF50',
            fg='white',
            width=10
        )
        self.send_button.pack(side=tk.RIGHT)
        
        # Меню
        self.setup_menu()
        
    def setup_menu(self):
        """Настройка меню"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # Меню "Файл"
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Файл", menu=file_menu)
        file_menu.add_command(label="Подключиться заново", command=self.reconnect)
        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=self.on_closing)
        
        # Меню "Справка"
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Справка", menu=help_menu)
        help_menu.add_command(label="О программе", command=self.show_about)
        help_menu.add_command(label="Команды", command=self.show_commands)
        
    def connect_to_server(self):
        """Подключение к серверу"""
        try:
            # Запрашиваем ник
            self.nickname = simpledialog.askstring(
                "Никнейм",
                "Введите ваш никнейм:",
                parent=self.root
            )
            
            if not self.nickname:
                self.root.quit()
                return
            
            # Подключаемся к серверу
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((self.host, self.port))
            
            # Получаем запрос на ввод ника
            initial = self.client_socket.recv(1024).decode('utf-8')
            if initial == "NICK":
                self.client_socket.send(self.nickname.encode('utf-8'))
            
            # Обновляем интерфейс
            self.status_label.config(text=f"Подключён как: {self.nickname}")
            self.message_entry.config(state='normal')
            self.send_button.config(state='normal')
            self.disconnect_btn.config(text="Отключиться")
            
            # Запускаем поток для приёма сообщений
            self.running = True
            receive_thread = threading.Thread(target=self.receive_messages, daemon=True)
            receive_thread.start()
            
            # Добавляем сообщение о подключении
            self.add_message("Система", f"Вы подключились к серверу как {self.nickname}")
            
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось подключиться к серверу:\n{str(e)}")
            self.root.quit()
    
    def receive_messages(self):
        """Получение сообщений от сервера"""
        while self.running:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message:
                    # Разбираем сообщение для форматирования
                    if ": " in message and not message.startswith("Система"):
                        # Обычное сообщение от пользователя
                        parts = message.split(": ", 1)
                        if len(parts) == 2:
                            self.add_message(parts[0], parts[1])
                        else:
                            self.add_message("Сообщение", message)
                    else:
                        # Системное сообщение
                        self.add_message("Система", message)
                else:
                    break
            except OSError:
                if self.running:
                    self.add_message("Система", "Соединение с сервером потеряно")
                    self.disconnect()
                break
    
    def send_message(self):
        """Отправка сообщения"""
        message = self.message_entry.get().strip()
        if message and self.client_socket:
            try:
                if message == '/quit':
                    self.disconnect()
                else:
                    self.client_socket.send(message.encode('utf-8'))
                    self.message_entry.delete(0, tk.END)
            except OSError:
                self.add_message("Система", "Ошибка при отправке сообщения")
                self.disconnect()
    
    def send_message_event(self, event):
        """Обработчик события Enter"""
        self.send_message()
    
    def add_message(self, sender, message):
        """Добавление сообщения в чат"""
        self.chat_area.config(state='normal')
        
        # Форматируем сообщение
        if sender == "Система":
            self.chat_area.insert(tk.END, f"\n🔔 {message}\n", "Система")
            self.chat_area.tag_config("Система", foreground="red", font=('Arial', 9, 'italic'))
        else:
            self.chat_area.insert(tk.END, f"\n{sender}: ", "sender")
            self.chat_area.insert(tk.END, f"{message}\n", "message")
            self.chat_area.tag_config("sender", foreground="blue", font=('Arial', 10, 'bold'))
            self.chat_area.tag_config("message", foreground="black", font=('Arial', 10))
        
        self.chat_area.see(tk.END)
        self.chat_area.config(state='disabled')
    
    def disconnect(self):
        """Отключение от сервера"""
        self.running = False
        if self.client_socket:
            try:
                self.client_socket.close()
            except OSError:
                pass
            self.client_socket = None
        
        self.status_label.config(text="Отключён")
        self.message_entry.config(state='disabled')
        self.send_button.config(state='disabled')
        self.disconnect_btn.config(text="Подключиться", command=self.reconnect)
        self.add_message("Система", "Вы отключились от сервера")
    
    def reconnect(self):
        """Переподключение к серверу"""
        if self.client_socket:
            self.disconnect()
        self.connect_to_server()
    
    def show_about(self):
        """Показать информацию о программе"""
        about_text = """Мессенджер с графическим интерфейсом

Версия: 1.0
Язык: Python + tkinter
Функции:
• Поддержка множества пользователей
• Системные уведомления
• Отключение/подключение
• Команды: /quit

Для работы требуется сервер (server.py)"""
        messagebox.showinfo("О программе", about_text)
    
    def show_commands(self):
        """Показать доступные команды"""
        commands_text = """Доступные команды:

/quit - Выход из чата (отключение)

Примечание:
Для приватных сообщений нужна доработка сервера."""
        messagebox.showinfo("Команды", commands_text)
    
    def on_closing(self):
        """Обработка закрытия окна"""
        self.running = False
        if self.client_socket:
            try:
                self.client_socket.close()
            except OSError:
                pass
        self.root.destroy()
    
    def run(self):
        """Запуск приложения"""
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

if __name__ == "__main__":
    app = ChatClientGUI()
    app.run()
