from Board import Board

b = Board(11, 14)



b.placeWallVertical(7, 9)
b.placeWallVertical(6, 10)
b.placeWallHorizontal(6, 9)
b.placeWallHorizontal(7, 10)

b.draw()

b.movePlayer(1, 1, 3)

b.draw()
