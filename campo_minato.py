"""
ESERCITAZIONE

DEFINIRE UN'INTERFACCIA PER UN GIOCATORE DEL GIOCO 'CAMPO MINATO'
- al giocatore deve essere  permesso di inserire delle mosse
- il gioco deve controllare la validità delle mosse e decretare l'eventuale esito della partita
- il gioco deve essere parametrico rispetto alle dimensioni del campo da gioco e al numero di bombe presenti

REGOLE
il campo da gioco consiste in un campo RETTANGOLARE di celle. Ogni cella viene scoperta cliccando su di essa.
Se una cella contenente una bomba viene cliccata il gioco termina ed il giocatore perde.
Se la cella non contiene una bomba allora
1) o appare un numero che indica la quantità di celle adiacenti (incluse diagonali) che contengono bombe
2) non appare nessun numero --> il gioco ripulisce automaticamente le celle adiacenti a quella vuota (fin quando non
   conterranno un numero)
Il giocatore vince se tutte le celle che non contengono un numero vengono coperte
"""

import random


class CampoMinato():
    def __init__(self, dim_x=8, dim_y=8, n_bombe=5):
        """
        :param dim_x: dimensione orrizzontale del campo di celle
        :param dim_y: dimensione verticale del campo di celle
        :param n_bombe: numero di bombe
        """
        self.dim_x = dim_x
        self.dim_y = dim_y
        self.n_bombe = n_bombe
        self.bombe = set(random.sample(self.tutte_le_celle(), n_bombe))
        self.celle = [[-1] * self.dim_x for i in range(self.dim_y)]  # con -1 indichiamo una cella coperta

    def in_board(self, x, y):
        return 0 <= x < self.dim_x and 0 <= y < self.dim_y

    def tutte_le_celle(self):
        tutti_x = range(self.dim_x)
        tutti_y = range(self.dim_y)
        return [(x, y) for x in tutti_x for y in tutti_y]

    def cella_coperta(self, x, y):
        return self.celle[x][y] == -1

    def numero_celle_coperte(self):
        return len([(x, y) for (x, y) in self.tutte_le_celle() if self.cella_coperta(x, y)])

    def vicini(self, x, y):
        return set([(xx, yy) for yy in (y - 1, y, y + 1) for xx in (x - 1, x, x + 1) if
                    self.in_board(xx, yy) and (xx, yy) != (x, y)])

    def print_board(self):
        print(''),
        for i in range(self.dim_y):
            print(i),
        print('')
        for x in range(self.dim_x):
            print(x),
            for y in range(self.dim_y):
                if self.cella_coperta(x, y):
                    print('#'),
                elif self.celle[x][y] == 0:
                    print(''),
                else:
                    print("%d"%self.celle[x][y]),

    def scopri(self, x, y):
        self.celle[x][y] = len(self.bombe & self.vicini(x, y))
        if not self.celle[x][y]:
            for (xx, yy) in self.vicini(x, y):
                if self.cella_coperta(xx, yy):
                    self.scopri(xx, yy)

    def clicca(self, x, y):
        if (x, y) in self.bombe:
            print('La cella' + str( (x, y) ) + 'è una BOMBA!!!!!')
            return False
        if not self.cella_coperta(x, y):
            print('La cella' + str( (x, y) ) + 'è già stata scoperta...')
            return True
        self.scopri(x, y)
        if self.numero_celle_coperte() == self.n_bombe:
            print('Hai VINTO!!!')
            return False
        return True

    def play(self):
        self.print_board()
        ret = True
        while ret:
            x = input('Inserisci al coordinata x  : ')
            y = input('Inserisci la coordinata y  : ')
            (x, y) = (int(x), int(y))
            ret = self.clicca(x, y)
            self.print_board()

c = CampoMinato()
c.play()