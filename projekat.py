from Board import Board

b = Board(11, 14)

b.placeWallVertical(7, 10)
b.placeWallVertical(6, 9)
b.placeWallHorizontal(7, 9)
b.placeWallHorizontal(5, 10)

b.draw()

b.movePlayer(1, 1, 3)
b.movePlayer(4, 1, 3)
b.movePlayer(7, 1, 3)
# b.movePlayer(7, 1, 3)
# b.movePlayer(9, 1, 3)
# b.movePlayer(3, 1, 3)

# b.movePlayer(1, 2, 3)
# b.movePlayer(7, 2, 3)
# b.movePlayer(9, 2, 3)
# b.movePlayer(3, 2, 3)

b.draw()
