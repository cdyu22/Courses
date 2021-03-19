l__tile = float(input("What is the length of a tile's side in inches? "))
l_wall = float(input("What is length of a wall in feet? "))
n_of_tiles = (l_wall*12)//l__tile
remainder = (l_wall*12)%(l__tile)
print("Each row needs "+str(n_of_tiles)+" tiles, with "+str(remainder)+" inches remaining")
