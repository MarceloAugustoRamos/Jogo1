import tkinter as tk

# Criação da janela principal
root = tk.Tk()
root.title("Ecos do Abismo")
root.geometry("1024x768")
root.attributes('-fullscreen', True)
root.bind("<Escape>", lambda _: root.attributes('-fullscreen', False))

# Variável para rastrear o tema
is_dark_theme = False  # Iniciar com o tema claro
theme_button = None  # Inicializar a variável global

# Cores para os temas
light_theme = {"bg": "#f0f0f0", "fg": "#000000", "button_bg": "#e0e0e0", "button_fg": "#000000"}
dark_theme = {"bg": "#1e1e1e", "fg": "#ffffff", "button_bg": "#333333", "button_fg": "#ffffff"}

# Função para aplicar o tema
def apply_theme(theme):
    root.config(bg=theme["bg"])
    for widget in root.winfo_children():
        if isinstance(widget, tk.Button):
            widget.config(bg=theme["button_bg"], fg=theme["button_fg"], activebackground=theme["button_bg"], activeforeground=theme["button_fg"])
        else:
            widget.config(bg=theme["bg"], fg=theme["fg"])

# Função para alternar entre tema claro e escuro
def toggle_theme():
    global is_dark_theme
    if is_dark_theme:
        apply_theme(light_theme)
        theme_button.config(text="Tema Escuro")
        is_dark_theme = False
    else:
        apply_theme(dark_theme)
        theme_button.config(text="Tema Claro")
        is_dark_theme = True

# Função para exibir diferentes telas
def show_screen(screen_name):
    for widget in root.winfo_children():
        widget.destroy()
    if screen_name == "inicio":
        show_inicio()
    elif screen_name == "explorar":
        show_explorar()
    elif screen_name == "configuracoes":
        show_configuracoes()

# Tela inicial
def show_inicio():
    title = tk.Label(root, text="Ecos do Abismo", font=("Arial", 24))
    title.pack(pady=20)

    subtitle = tk.Label(root, text="Bem-vindo, Buzeira. Escolha seu destino.", font=("Arial", 14))
    subtitle.pack(pady=10)

    explorar_button = tk.Button(root, text="Explorar Masmorra", command=lambda: show_screen("explorar"))
    explorar_button.pack(pady=10)

    configuracoes_button = tk.Button(root, text="Configurações", command=lambda: show_screen("configuracoes"))
    configuracoes_button.pack(pady=10)

    sair_button = tk.Button(root, text="Sair", command=root.quit)
    sair_button.pack(pady=10)

    apply_theme(dark_theme if is_dark_theme else light_theme)

# Tela de configurações
def show_configuracoes():
    global theme_button  # Declarar como global para ser acessada em outras funções
    title = tk.Label(root, text="Configurações", font=("Arial", 24))
    title.pack(pady=20)

    theme_button = tk.Button(root, text="Tema Claro" if is_dark_theme else "Tema Escuro", command=toggle_theme)
    theme_button.pack(pady=10)

    voltar_button = tk.Button(root, text="Voltar", command=lambda: show_screen("inicio"))
    voltar_button.pack(pady=10)

    apply_theme(dark_theme if is_dark_theme else light_theme)

# Tela de explorar masmorras
def show_explorar():
    title = tk.Label(root, text="Explorar Masmorra", font=("Arial", 24))
    title.pack(pady=20)

    description = tk.Label(root, text="Iniciar aventura!", font=("Arial", 14))
    description.pack(pady=10)

    masmorrateste_button = tk.Button(root, text="Masmorra: Catedral Profanada", command=start_game)
    masmorrateste_button.pack(pady=10)

    voltar_button = tk.Button(root, text="Voltar", command=lambda: show_screen("inicio"))
    voltar_button.pack(pady=10)

    apply_theme(dark_theme if is_dark_theme else light_theme)

# Função para iniciar o jogo
def start_game():
    for widget in root.winfo_children():
        widget.destroy()
    title = tk.Label(root, text="Iniciando Aventura", font=("Arial", 14))
    title.pack(pady=20)

    # Equipamento inicial
    espada = 3
    pocao = 1
    vida = True
    chave = 0

    # Variáveis das salas na primeira parte da masmorra
    tranca3 = True  # Tranca da porta vermelha na sala 3
    prim3 = True  # Primeira vez na sala 3 (para pegar a chave)
    prim4 = True  # Primeira vez na sala 4 (para pegar a poção)
    prim6 = True  # Primeira vez na sala 6 (para pegar a chave)
    skl5 = True  # Esqueleto na sala 5 não derrotado
    sala7 = False  # Jogador chegou na sala 7

    # Por enquanto, apenas um botão para voltar
    voltar_button = tk.Button(root, text="Voltar", command=lambda: show_screen("explorar"))
    voltar_button.pack(pady=10)

# Inicializar a tela inicial e iniciar o loop principal
show_inicio()

root.mainloop()


