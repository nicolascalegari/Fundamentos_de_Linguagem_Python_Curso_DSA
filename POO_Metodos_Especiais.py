class Livro:

    def __init__(self, titulo, autor,paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    # Quando usamos print ou str
    def __str__(self):
        return f"'{self.titulo}' por {self.autor}"

    # Quando usamos len() no objeto
    def __len__(self):
        return self.paginas

# Cria o objeto
livro = Livro("O Hobbit", "JRR Tolkien", 330)

type(livro)

# O metodo __str__ é chamado aqui
print(livro)

# o metodo __len)) é chamda aqui
print(f"O livro tem {len(livro)} paginas.")