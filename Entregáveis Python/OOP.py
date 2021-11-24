# Entregavel - Python OOP
l_times = []

class Time:
    l_ordenada = []

    # SG = saldo de gols, V = vitorias, E = empates, D = derrotas
    def __init__(self, nome, SG, V, E, D ):
        self.nome = nome 
        self.SG = SG
        self.V = V
        self.E = E
        self.D = D
        self.pontos = 3*V + E
        l_times.append(self)
    
    def __repr__(self):
        txt = f'\n{self.nome} | V:{self.V} | E:{self.E} | D:{self.D} | SG:{self.SG} '
        return txt
    
    def __add__(self, t2):
        return self.pontos + t2.pontos
    def __sub__(self, t2):
        return self.pontos - t2.pontos
    
    @classmethod
    def ordenarTimes(cls):
        l_ordenada = []
        l_copia = l_times.copy()
        while l_copia: # lista nao vazia
            pts = 0 
            sg = 0
            for time in l_copia:
                if time.pontos > pts:
                    melhor = time
                    sg = time.SG
                    pts = time.pontos
                if time.pontos == pts:
                    if time.SG >= sg:
                        sg = time.SG
                        pts = time.pontos
                        melhor = time
                    else:
                        pass
                else:
                    pass
            l_ordenada.append(melhor)
            l_copia.remove(melhor)
        return l_ordenada

# Objetos de exemplo, tirados da tabela do brasileirao serie A
palmeras = Time("Palmeras", 12, 18, 4, 12)               
atletico = Time("Atletico Mineiro", 31, 23, 5, 5)
flamengo = Time("Flamengo", 35, 20, 6, 7)
corinthians = Time("Corinthians", 5, 14, 11, 9)

# Testes de print
print(f'TABELA: \n {Time.ordenarTimes()}')
print(f'\nPontos do Flamengo: {flamengo.pontos}')
print(f'Pontos do Palmeras: {palmeras.pontos}')
print(f'Diferença: {flamengo-palmeras}')
print(f'Soma: {flamengo+palmeras}')