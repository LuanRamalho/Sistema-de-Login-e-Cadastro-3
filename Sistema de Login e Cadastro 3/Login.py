import tkinter as tk
from tkinter import messagebox
import json
import os

# Nome do arquivo JSON para armazenar os dados
DATA_FILE = "users.json"

# Função para carregar os dados do arquivo JSON
def load_users():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {}

# Função para salvar os dados no arquivo JSON
def save_users():
    with open(DATA_FILE, "w") as file:
        json.dump(users, file, indent=4)

# Inicializar o banco de dados de usuários
users = load_users()

# Função para realizar o login
def login():
    username = entry_login.get()
    password = entry_password.get()
    if username in users and users[username] == password:
        messagebox.showinfo("Login", "Usuário Cadastrado!")
    else:
        messagebox.showerror("Erro", "Login ou Senha incorreto!")

# Função para abrir a tela de cadastro
def open_register():
    login_window.withdraw()
    register_window.deiconify()

# Função para cadastrar um novo usuário
def register():
    username = register_login.get()
    password = register_password.get()
    confirm_password = register_confirm_password.get()
    if username in users:
        messagebox.showerror("Erro", "Usuário já cadastrado!")
    elif password != confirm_password:
        messagebox.showerror("Erro", "As senhas não coincidem!")
    else:
        users[username] = password
        save_users()  # Salvar os dados no arquivo JSON
        messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")
        register_window.withdraw()
        login_window.deiconify()

# Função para abrir a tela de recuperação de senha
def open_forgot_password():
    login_window.withdraw()
    forgot_password_window.deiconify()

# Função para recuperar a senha
def recover_password():
    username = forgot_password_login.get()
    if username in users:
        messagebox.showinfo("Recuperar Senha", f"A senha do usuário {username} é: {users[username]}")
    else:
        messagebox.showerror("Erro", "Login inexistente!")

# Função para criar hiperlinks
def create_hyperlink(parent, text, command, bg_color):
    label = tk.Label(parent, text=text, font=("Arial", 10), bg=bg_color, fg="blue", cursor="hand2")
    label.bind("<Button-1>", lambda e: command())
    label.pack()
    return label

# Janela de Login
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("400x300")
login_window.configure(bg="#ADD8E6")

tk.Label(login_window, text="Login", font=("Arial", 16), bg="#ADD8E6").pack(pady=10)
entry_login = tk.Entry(login_window, font=("Arial", 14))
entry_login.pack(pady=5)

tk.Label(login_window, text="Senha", font=("Arial", 16), bg="#ADD8E6").pack(pady=10)
entry_password = tk.Entry(login_window, font=("Arial", 14), show="*")
entry_password.pack(pady=5)

tk.Button(login_window, text="Logar", font=("Arial", 14), command=login, bg="#32CD32", fg="white").pack(pady=10)

create_hyperlink(login_window, "Esqueceu sua senha?", open_forgot_password, "#ADD8E6")
create_hyperlink(login_window, "Não tem login? Cadastre-se", open_register, "#ADD8E6")

# Janela de Cadastro
register_window = tk.Toplevel(login_window)
register_window.title("Cadastro")
register_window.geometry("400x300")
register_window.configure(bg="#FFD700")
register_window.withdraw()

tk.Label(register_window, text="Cadastro", font=("Arial", 16), bg="#FFD700").pack(pady=10)
register_login = tk.Entry(register_window, font=("Arial", 14))
register_login.pack(pady=5)

register_password = tk.Entry(register_window, font=("Arial", 14), show="*")
register_password.pack(pady=5)

register_confirm_password = tk.Entry(register_window, font=("Arial", 14), show="*")
register_confirm_password.pack(pady=5)

tk.Button(register_window, text="Cadastrar", font=("Arial", 14), command=register, bg="#32CD32", fg="white").pack(pady=10)

# Janela de Recuperação de Senha
forgot_password_window = tk.Toplevel(login_window)
forgot_password_window.title("Recuperar Senha")
forgot_password_window.geometry("400x300")
forgot_password_window.configure(bg="#FF6347")
forgot_password_window.withdraw()

tk.Label(forgot_password_window, text="Recuperar Senha", font=("Arial", 16), bg="#FF6347").pack(pady=10)
forgot_password_login = tk.Entry(forgot_password_window, font=("Arial", 14))
forgot_password_login.pack(pady=5)

tk.Button(forgot_password_window, text="Recuperar", font=("Arial", 14), command=recover_password, bg="#32CD32", fg="white").pack(pady=10)

# Iniciar a aplicação
login_window.mainloop()
