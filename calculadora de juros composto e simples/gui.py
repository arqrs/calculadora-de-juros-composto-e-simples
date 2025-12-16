import tkinter as tk
from tkinter import ttk, messagebox
import math


def juros_simples(capital, taxa_percent, tempo):
    taxa = taxa_percent / 100.0
    return capital * (1 + taxa * tempo)


def juros_compostos(capital, taxa_percent, tempo, comp_per_year=1):
    taxa = taxa_percent / 100.0
    n = comp_per_year
    return capital * ((1 + taxa / n) ** (n * tempo))


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Calculadora de Juros')
        self.geometry('420x360')
        self.resizable(False, False)
        pad = 10

        frm = ttk.Frame(self, padding=pad)
        frm.pack(fill='both', expand=True)

        ttk.Label(frm, text='Capital inicial:').grid(column=0, row=0, sticky='w')
        self.capital = tk.StringVar()
        ttk.Entry(frm, textvariable=self.capital).grid(column=1, row=0)

        ttk.Label(frm, text='Taxa anual (%):').grid(column=0, row=1, sticky='w')
        self.taxa = tk.StringVar()
        ttk.Entry(frm, textvariable=self.taxa).grid(column=1, row=1)

        ttk.Label(frm, text='Tempo (anos):').grid(column=0, row=2, sticky='w')
        self.tempo = tk.StringVar()
        ttk.Entry(frm, textvariable=self.tempo).grid(column=1, row=2)

        self.modo = tk.StringVar(value='composto')
        ttk.Radiobutton(frm, text='Composto', variable=self.modo, value='composto', command=self._on_modo).grid(column=0, row=3)
        ttk.Radiobutton(frm, text='Simples', variable=self.modo, value='simples', command=self._on_modo).grid(column=1, row=3)

        ttk.Label(frm, text='Compostos por ano:').grid(column=0, row=4, sticky='w')
        self.periodos = tk.IntVar(value=1)
        self.spin = ttk.Spinbox(frm, from_=1, to=365, textvariable=self.periodos, width=6)
        self.spin.grid(column=1, row=4, sticky='w')

        btn_calc = ttk.Button(frm, text='Calcular', command=self.calcular)
        btn_calc.grid(column=0, row=5, pady=12)
        btn_clear = ttk.Button(frm, text='Limpar', command=self.limpar)
        btn_clear.grid(column=1, row=5, pady=12)

        sep = ttk.Separator(frm, orient='horizontal')
        sep.grid(column=0, row=6, columnspan=2, sticky='ew', pady=8)

        self.result = tk.Text(frm, height=6, width=48, state='disabled', wrap='word')
        self.result.grid(column=0, row=7, columnspan=2)

    def _on_modo(self):
        if self.modo.get() == 'simples':
            self.spin.state(['disabled'])
        else:
            self.spin.state(['!disabled'])

    def validar(self):
        try:
            C = float(self.capital.get())
            if C < 0:
                raise ValueError('capital negativo')
        except Exception:
            messagebox.showerror('Erro', 'Capital inválido')
            return None
        try:
            i = float(self.taxa.get())
            if i < 0:
                raise ValueError('taxa negativa')
        except Exception:
            messagebox.showerror('Erro', 'Taxa inválida')
            return None
        try:
            t = float(self.tempo.get())
            if t <= 0:
                raise ValueError('tempo inválido')
        except Exception:
            messagebox.showerror('Erro', 'Tempo inválido')
            return None
        return C, i, t

    def calcular(self):
        vals = self.validar()
        if not vals:
            return
        C, i, t = vals
        if self.modo.get() == 'simples':
            mont = juros_simples(C, i, t)
            tipo = 'Juros Simples'
        else:
            mont = juros_compostos(C, i, t, self.periodos.get())
            tipo = 'Juros Compostos'
        juros = mont - C
        out = f"{tipo}\nCapital inicial: R$ {C:,.2f}\nTaxa anual: {i}%\nTempo: {t} anos\n"
        if self.modo.get() != 'simples':
            out += f"Compostos por ano: {self.periodos.get()}\n"
        out += f"Montante: R$ {mont:,.2f}\nJuros: R$ {juros:,.2f}\n"
        self.result.config(state='normal')
        self.result.delete('1.0', 'end')
        self.result.insert('end', out)
        self.result.config(state='disabled')

    def limpar(self):
        self.capital.set('')
        self.taxa.set('')
        self.tempo.set('')
        self.periodos.set(1)
        self.result.config(state='normal')
        self.result.delete('1.0', 'end')
        self.result.config(state='disabled')


if __name__ == '__main__':
    app = App()
    app.mainloop()
