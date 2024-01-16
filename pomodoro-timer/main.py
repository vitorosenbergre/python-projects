import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import ttk, Style

# Constantes para os intervalos de trabalho e pausa
WORK_TIME = 25 * 60
SHORT_BREAK_TIME = 5 * 60
LONG_BREAK_TIME = 15 * 60


class PomodoroTimer:
    def __init__(self):
        # Configuração da janela principal
        self.root = tk.Tk()
        self.root.geometry("300x250")
        self.root.title("Pomodoro Timer")

        # Estilo da interface gráfica
        # Escolha do tema 'darkly' para um estilo mais escuro
        self.style = Style(theme="darkly")
        self.style.theme_use()

        # Componentes da interface
        self.timer_label = tk.Label(
            self.root, text="", font=("Helvetica", 40), fg="white", bg="#343a40")
        self.timer_label.pack(pady=20)

        self.start_button = ttk.Button(
            self.root, text="Start", command=self.start_timer, style="primary.TButton")
        self.start_button.pack(pady=5)

        self.stop_button = ttk.Button(
            self.root, text="Stop", command=self.stop_timer, style="danger.TButton", state=tk.DISABLED)
        self.stop_button.pack(pady=5)

        # Variáveis de controle do temporizador
        self.work_time, self.break_time = WORK_TIME, SHORT_BREAK_TIME
        self.is_work_time, self.pomodoros_completed, self.is_running = True, 0, False

        # Inicialização da interface gráfica
        self.update_display()
        self.root.mainloop()

    def start_timer(self):
        # Configurações ao iniciar o temporizador
        self.start_button["state"] = tk.DISABLED
        self.stop_button["state"] = tk.NORMAL
        self.is_running = True
        self.update_timer()

    def stop_timer(self):
        # Configurações ao parar o temporizador
        self.start_button["state"] = tk.NORMAL
        self.stop_button["state"] = tk.DISABLED
        self.is_running = False

    def update_timer(self):
        # Atualização do temporizador
        if self.is_running:
            if self.is_work_time:
                # Contagem regressiva durante o tempo de trabalho
                self.work_time -= 1
                if self.work_time == 0:
                    # Mudança para o tempo de pausa após o término do tempo de trabalho
                    self.is_work_time = False
                    self.pomodoros_completed += 1
                    self.break_time = LONG_BREAK_TIME if self.pomodoros_completed % 4 == 0 else SHORT_BREAK_TIME
                    # Exibição de mensagem após cada conjunto de 4 pomodoros
                    messagebox.showinfo(
                        "GREAT JOB!" if self.pomodoros_completed % 4 == 0 else "GOOD JOB!",
                        "TAKE A LONG BREAK AND REST YOUR MIND." if self.pomodoros_completed % 4 == 0 else "TAKE A SHORT BREAK AND REST YOUR LEGS"
                    )
            else:
                # Contagem regressiva durante o tempo de pausa
                self.break_time -= 1
                if self.break_time == 0:
                    # Reinicialização para o próximo ciclo de trabalho
                    self.is_work_time, self.work_time = True, WORK_TIME
                    messagebox.showinfo("WORK TIME", "GET BACK TO WORK!")

            # Atualização do rótulo do temporizador
            minutes, seconds = divmod(
                self.work_time if self.is_work_time else self.break_time, 60)
            self.timer_label.config(
                text="{:02d}:{:02d}".format(minutes, seconds))

            # Agendamento da próxima atualização após 1 segundo
            self.root.after(1000, self.update_timer)

    def update_display(self):
        # Atualização inicial do rótulo do temporizador
        minutes, seconds = divmod(self.work_time, 60)
        self.timer_label.config(text="{:02d}:{:02d}".format(minutes, seconds))


# Instanciando e iniciando o temporizador Pomodoro
pomodoro_timer = PomodoroTimer()
