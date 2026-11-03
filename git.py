import tkinter as tk


class CalculadoraApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry("320x500")
        self.resizable(False, False)
        self.configure(bg="#f2f2f2")

        self.expression = ""

        self.display_var = tk.StringVar()
        self.display = tk.Entry(
            self,
            textvariable=self.display_var,
            font=("Arial", 28, "bold"),
            justify="right",
            bg="#ffffff",
            fg="#222222",
            bd=0,
            relief="flat",
        )
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=12, pady=(12, 8))

        self.grid_rowconfigure(0, weight=1)
        for i in range(1, 6):
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

        botoes = [
            ("C", 1, 0, "clear"),
            ("⌫", 1, 1, "backspace"),
            ("%", 1, 2, "percent"),
            ("/", 1, 3, "operator"),
            ("7", 2, 0, "number"),
            ("8", 2, 1, "number"),
            ("9", 2, 2, "number"),
            ("*", 2, 3, "operator"),
            ("4", 3, 0, "number"),
            ("5", 3, 1, "number"),
            ("6", 3, 2, "number"),
            ("-", 3, 3, "operator"),
            ("1", 4, 0, "number"),
            ("2", 4, 1, "number"),
            ("3", 4, 2, "number"),
            ("+", 4, 3, "operator"),
            ("0", 5, 0, "number", 2),
            (".", 5, 2, "number"),
            ("=", 5, 3, "calculate"),
        ]

        for botao in botoes:
            if len(botao) == 4:
                texto, linha, coluna, tipo = botao
                columnspan = 1
            else:
                texto, linha, coluna, tipo, columnspan = botao

            btn = tk.Button(
                self,
                text=texto,
                font=("Arial", 20, "bold"),
                fg="#222222",
                bg="#ffffff" if tipo == "number" else "#f0f0f0",
                activebackground="#d9d9d9",
                relief="flat",
                bd=0,
                command=lambda valor=texto, acao=tipo: self.on_click(valor, acao),
            )
            btn.grid(row=linha, column=coluna, columnspan=columnspan, sticky="nsew", padx=4, pady=4)

    def on_click(self, valor, tipo):
        if tipo == "number":
            self.add_number(valor)
        elif tipo == "operator":
            self.add_operator(valor)
        elif tipo == "clear":
            self.clear()
        elif tipo == "backspace":
            self.backspace()
        elif tipo == "percent":
            self.percent()
        elif tipo == "calculate":
            self.calculate()

    def add_number(self, valor):
        self.expression += str(valor)
        self.display_var.set(self.expression)

    def add_operator(self, valor):
        if not self.expression:
            return
        last_char = self.expression[-1]
        if last_char in "+-*/":
            return
        self.expression += valor
        self.display_var.set(self.expression)

    def clear(self):
        self.expression = ""
        self.display_var.set("")

    def backspace(self):
        self.expression = self.expression[:-1]
        self.display_var.set(self.expression)

    def percent(self):
        if not self.expression:
            return
        try:
            resultado = eval(self.expression, {"__builtins__": None}, {}) / 100
            self.expression = str(resultado)
            self.display_var.set(self.expression)
        except Exception:
            self.expression = ""
            self.display_var.set("Erro")

    def calculate(self):
        if not self.expression:
            return
        try:
            resultado = eval(self.expression, {"__builtins__": None}, {})
            self.expression = str(resultado)
            self.display_var.set(self.expression)
        except Exception:
            self.expression = ""
            self.display_var.set("Erro")


if __name__ == "__main__":
    app = CalculadoraApp()
    app.mainloop()
