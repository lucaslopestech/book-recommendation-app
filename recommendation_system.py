import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox

# Catálogo de livros com gêneros
catalogo_livros = {
    'livro': [
        'Orgulho e Preconceito', 'Duna', 'O Senhor dos Anéis',
        'O Assassinato no Expresso Oriente', 'O Silêncio dos Inocentes',
        'A Ilha do Tesouro', 'Os Miseráveis', '1984',
        'Sapiens: Uma Breve História da Humanidade', 'O Guardador de Rebanhos'
    ],
    'autor': [
        'Jane Austen', 'Frank Herbert', 'J.R.R. Tolkien',
        'Agatha Christie', 'Thomas Harris',
        'Robert Louis Stevenson', 'Victor Hugo', 'George Orwell',
        'Yuval Noah Harari', 'Alberto Caeiro (Fernando Pessoa)'
    ],
    'genero': [
        'Romance', 'Ficção Científica', 'Fantasia',
        'Mistério', 'Suspense', 'Aventura',
        'Histórico', 'Distopia', 'Não Ficção', 'Poesia'
    ]
}
catalogo_df = pd.DataFrame(catalogo_livros)

# Criar a interface gráfica
class RecomendacaoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Recomendação de Livros")
        
        # Nome do usuário
        self.label_nome = tk.Label(root, text="Digite seu nome:")
        self.label_nome.pack(pady=5)
        self.entry_nome = tk.Entry(root)
        self.entry_nome.pack(pady=5)
        
        # Escolha do gênero
        self.label_genero = tk.Label(root, text="Escolha um gênero:")
        self.label_genero.pack(pady=5)
        self.genero_var = tk.StringVar()
        self.combobox_genero = ttk.Combobox(root, textvariable=self.genero_var)
        self.combobox_genero['values'] = list(catalogo_df['genero'].unique())
        self.combobox_genero.pack(pady=5)
        
        # Botão de recomendação
        self.botao_recomendar = tk.Button(root, text="Obter Recomendações", command=self.obter_recomendacoes)
        self.botao_recomendar.pack(pady=20)
        
        # Área de resultados
        self.text_resultado = tk.Text(root, height=10, width=50)
        self.text_resultado.pack(pady=10)
        
    def obter_recomendacoes(self):
        nome_usuario = self.entry_nome.get()
        genero_escolhido = self.genero_var.get()
        
        if nome_usuario and genero_escolhido:
            self.text_resultado.delete(1.0, tk.END)
            # Filtrando o DataFrame corretamente pelo gênero escolhido
            livro_recomendado = catalogo_df[catalogo_df['genero'] == genero_escolhido]
            if not livro_recomendado.empty:
                livro, autor = livro_recomendado.iloc[0][['livro', 'autor']]  # Seleciona o primeiro livro do gênero escolhido
                self.text_resultado.insert(tk.END, f"Livro recomendado para {nome_usuario} no gênero {genero_escolhido}:\n")
                self.text_resultado.insert(tk.END, f"{livro} - {autor}\n")
            else:
                self.text_resultado.insert(tk.END, f"Desculpe, não há livros disponíveis no gênero {genero_escolhido}.")
        else:
            messagebox.showwarning("Entrada inválida", "Por favor, preencha todos os campos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = RecomendacaoGUI(root)
    root.mainloop()
