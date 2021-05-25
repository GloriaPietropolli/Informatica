"""
- Implementazione della classe Grafi Grafi attraverso le liste di adiacenza
- Implementazione di una funzione che visiti in ampiezza un grafo a partire da una sorgente
"""
from enum import Enum


class Nodo:

    def __init__(self, value, succ):
        self.value = value
        self.succ = succ

class Lista:

    def __init__(self):
        self.testa = None

    def insert(self, value):
        new_node = Nodo(value, self.testa)
        self.testa = new_node

    def __str__(self):
        s = ""
        nodo_corrente = self.testa
        while nodo_corrente is not None:
            s += str(nodo_corrente.value) + " "
            nodo_corrente = nodo_corrente.succ
        return s


class GrafoAdiacenza:
    """
    gli oggetti della classe vengono definiti attraverso :
    - il numero di nodi presenti nel grafo
    - un array di coppie di numeri interi nel range (0, #nodi - 1 ) --> archi del grafo
    """

    def __init__(self, numero_nodi, archi):
        self.numero_nodi = numero_nodi
        # gli archi del grafo vengon inseriti nelle liste di adiacenza
        self.liste = [None] * numero_nodi
        # inseriamo una lista vuota per ogni posizione
        for i in range(0, numero_nodi):
            self.liste[i] = Lista()
        for u, v in archi:
            self.liste[u].insert(v)

    def __str__(self):
        s = ""
        for i, adiacenti in enumerate(self.liste):
            s += "Nodo " + str(i) + " ha adiacenti " + str(adiacenti) + "\n"
        return s

class Coda:

    def __init__(self):
        self.testa = None
        self.coda = None

    def enqueue(self, value):
        """
        aggiungere alla coda (self) un nodo che potrebbe avere ancora vicina di visitare (value)
        :param value: nodo che aggiungo alla coda
        :return: coda modificata
        """
        nuovo_nodo = Nodo(value, None)
        if self.coda is None:  # sto aggiungendo il nodo testa
            self.coda = nuovo_nodo
            self.testa = nuovo_nodo
        else:
            self.coda.succ = nuovo_nodo
            self.coda = nuovo_nodo

    def dequeue(self):
        """
        prendere il primo nodo dalla coda
        assumiamo che la coda non sia vuota (ho aggiunto almeno la testa dell'albero)
        :return:
        """
        value = self.testa.value
        if self.testa.succ is None:
            self.coda = None
        self.testa = self.testa.succ
        return value

    def is_empty(self):
        truth_value = self.testa is None
        return truth_value


class Colore(Enum):
    BIANCO = 0
    GRIGIO = 1
    NERO = 2


def ricerca_ampiezza(G, s):
    """
    ricerca di un ampiezza di un valore all'interno di un grafo
    :param G: grafo
    :param s: nodo sorgente
    :return: distanza tra la radice e il valore
    """
    colore = [None] * G.numero_nodi
    predecessore = [None] * G.numero_nodi
    distanza = [None] * G.numero_nodi
    for i in range(0, G.numero_nodi):
        colore[i] = Colore.BIANCO
    # il nodo sorgente è i primo che visitiamo
    colore[s] = Colore.GRIGIO  # il nodo sorgente assume il colore grigio
    distanza[s] = 0  # il nodo sorgente ha distanza 0 da se stesso
    Q = Coda()
    Q.enqueue(s)  # nella coda dei nodi che potrebbero avere ancora vicini da visitare aggiungo s
    while not Q.is_empty():  # il ciclo continua finche rimangono nodi da visitare
        u = Q.dequeue()  # prendiamo il primo nodo della coda
        nodo_attuale = G.liste[u].testa  # e ne esploriamo tutti i vicini
        while nodo_attuale is not None:
            v = nodo_attuale.value
            if colore[v] == Colore.BIANCO:
                colore[v] = Colore.GRIGIO
                predecessore[v] = u
                distanza[v] = distanza[u] + 1
                Q.enqueue(v)  # accodiamo perchè potrebbe avere vicini bianchi
            nodo_attuale = nodo_attuale.succ
        colore[u] = Colore.NERO # abbiamo fininto di visitare tutti i nodi raggiungibili da u
    return distanza


# IMPLEMENTAZIONE DELLA VISITA IN PROFONDITA'

# stiamo usando variabli locali (non globali) per porprieà come colore, tempo, predecessore..
# Nella implementazione di DFS dobbiamo utilizzare due funzioni distinte e vorremmo che queste variabili si potessero
# leggere da una funzione all'altra

# SOLUZIONE? --> introduciamo una CLASSE in cui raccogliamo queste informazioni

class Parametri:
    def __init__(self, colore, predecessore, t_inizio, t_fine, t):
        self.colore = colore
        self.predecessore = predecessore
        self.t_inizio = t_inizio
        self.t_fine = t_fine
        self.t = t

def ricerca_profondità(G):
    """
    IMplementazione delle routine per la ricerca in profonfità
    :param G: grafo di input
    :return: parametri (oggetto della classe Parametri)
    """
    colore = [None] * G.numero_nodi
    predecessore = [None] * G.numero_nodi
    t_inizio = [None] * G.numero_nodi
    t_fine = [None] * G.numero_nodi
    for i in range(0, G.numero_nodi):
        colore[i] = Colore.BIANCO
    t = 0  # azzeriamo il contatore globale del tempo
    # raccogliamo tutti i parametri in un unico oggetto
    p = Parametri(colore, predecessore, t_inizio, t_fine, t)
    for u in range(0, G.numero_nodi):  # seleziono ogni singolo nodo del grafo e per ogni nodo avvio una procedura
        # che ha il compito di effettuare la visita vera e propria
        DFS_visit(G, u, p)
    return p

def DFS_visit(G, u, p):
    """
    La procedura per la visita si occupa di:
    - colorare opportunamente tutti i vertici visitati a partire da u
    - aggiornare i valori temporali
    - costruire la foresta DFS
    :param G: grafo di input
    :param u: vertice considerato
    :param p: parametri
    """
    p.t += 1
    p.t_inizio[u] = p.t
    p.colore[u] = Colore.GRIGIO
    nodo_corrente = G.liste[u].testa
    # visitiamo ognuno dei nodi adiacenti ad u scorrendo la lista
    while nodo_corrente is not None:
        v = nodo_corrente.value
        if p.colore[v] == Colore.BIANCO:
            p.predecessore[v] = u
            DFS_visit(G, v, p)
        nodo_corrente = nodo_corrente.succ
    p.colore[u] = Colore.NERO
    p.t += 1
    p.t_fine[u] = p.t

