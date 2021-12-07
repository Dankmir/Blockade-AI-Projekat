from Board import Board

b = Board(11, 14)

b.placeWallHorizontal(0, 0)
b.placeWallHorizontal(9, 0)
b.placeWallHorizontal(0, 12)
b.placeWallHorizontal(9, 12)

b.placeWallVertical(1, 1)
b.placeWallVertical(8, 1)
b.placeWallVertical(1, 11)
b.placeWallVertical(8, 11)

b.draw()

b.movePlayer(3, 1, 3)

b.draw()
