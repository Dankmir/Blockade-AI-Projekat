from Board import Board

b = Board(11, 14)

b.draw()

b.playTurn('X', 1, 8, 2, 'B', 4, 3)
b.playTurn('X', 1, 2, 1, 'B', 1, 1)

b.draw()


'''
- Postavljanje zidova (da ne mogu da budu tri u nizu, za horizontalne radi, treba za vertikalne)
- Postavljanje zida (onaj slucaj sa discorda sto sam slao)
- Inicializacija table na pocetku (da unosimo parametre)
- Da se pamti broz zidova po igracu
- Da se pamte pocetne pozicija i da se doda provera da li je igrac stigao na pocetnu poziciju protivnika
- Provera da zidovi ne mogu da se postave oko pocetnih polja
- Provera da li igrac ima zidove
'''