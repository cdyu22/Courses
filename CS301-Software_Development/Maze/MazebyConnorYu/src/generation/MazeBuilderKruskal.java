package generation;

public class MazeBuilderKruskal extends MazeBuilder implements Runnable {
	public MazeBuilderKruskal() {
		super();
		System.out.println("MazeBuilderKruskal uses Kruskal's algorithm to generate maze.");
	}
	public MazeBuilderKruskal( boolean det ) {
		super( det );
		System.out.println("MazeBuilderKruskal uses Kruskal's algorithm to generate maze.");
	}
	
	/**
	* The only method that needs to be overridden from MazeBuilder. When we implement rooms,
	* we just need to make a few tweaks. The general idea behind it is that all we really need 
	* to represent the maze is a two-dimensional array. The array will originally have all of 
	* its cells be a unique value. We then, with the maze and FloorPlan itself, pick a random 
	* cell and random direction that combined point to a WallBoard, and we see if we can remove 
	* it. If we can, we get the cell  on the other side of the wall and see if in the constructed 
	* two-dimensional array they are the same value. If they are, we just try another cell and 
	* direction, if they aren't, we tear down the wall, and change all of the values in the cells 
	* in the two-dimensional array that have the neighbors value to the value of the original 
	* randomly chosen cell, and we do this until all of the cells in the two-dimensional array have 
	* the same value. When implementing rooms, all we need to do, as rooms as placed in before the 
	* pathways are generated, is make sure that all of the cells in a room have the same number in 
	* the two dimensional array, so there aren't two adjacent doors in a room.
	*/
	@Override
	protected void generatePathways() {
		/*
		Generate a 2-dimensional array, with the first array being the width (x)
		of the maze, and the inner, second array representing the height (y) of the maze.
		We then fill that up with with values, with the first, (0,0) cell having 0,
		(0,1) having the integer 1, and so on and so forth.
		*/
		int WidthRandom; 
		int HeightRandom; 
		int WidthNeighbor; 
		int HeightNeighbor;
		int[][] cells = new int[ width ][ height ];
		CardinalDirection TearDownDirection = CardinalDirection.North;
		
		//Filling cells to all have different values, starting at 0
		int counter = 0;
		for ( int wFill = 0; wFill < width; wFill++ ) 
			for ( int hFill = 0; hFill < height; hFill++ ) {
				cells[ wFill ][ hFill ] = counter;
				counter++;
			}
		
		/*
		At the very beginning, before we implement rooms for Kruskal, we override MazeBuilder's
		generateRooms() to always return 0. Once the algorithm works for the original, we need to
		treat the rooms as one cell. We can do this by looping through at the beginning of the
		two-dimensional array construction, and if no WallBoards detected at that point, then give
		them the same number.
		*/
		if ( !order.isPerfect() ) {
			Wallboard wallboard = new Wallboard( 0, 0, TearDownDirection );
			//Scans through all cells in the FloorPlan
			for ( int xSearch = 0; xSearch < width; xSearch++ ) 
				for ( int ySearch = 0; ySearch < height; ySearch++ ) 
					for ( CardinalDirection cd : CardinalDirection.values() ) {
						wallboard.setLocationDirection( xSearch, ySearch, cd );
						//If they don't have a wall already, they're in a room
						if ( floorplan.hasNoWall( xSearch, ySearch, cd ) ) 
						{
							WidthRandom = wallboard.getNeighborX();
							HeightRandom = wallboard.getNeighborY();
							//So make sure they have the same value in cells
							cells[ WidthRandom ][ HeightRandom ] = cells[ xSearch ][ ySearch ];
						}
					}
		}
		
		/*
		We then run a loop. We pick a random cell and a random direction, We then look at the 
		WallBoard that cell is pointing to with its direction, and see if we can tear it down. 
		If we can't, we start the loop again. 
		*/
		while ( !checkAllSame( cells ) ) {
			//Random cell and direction generation
			WidthRandom = random.nextIntWithinInterval( 0, width - 1 );
			HeightRandom = random.nextIntWithinInterval( 0, height - 1 );
			TearDownDirection = TearDownDirection.randomDirection();
			
			//Only continue if you can tear down the WallBoard
			Wallboard wallboard = new Wallboard( WidthRandom, HeightRandom, TearDownDirection );
			if ( !floorplan.canTearDown( wallboard ) )
				continue;

			/*
			If it is possible to tear it down, we get the (x,y) coordinates of the cell that our original 
			cell is pointing towards. We check if the values in the two-dimensional array are the same. 
			If they are,then nothing happens. If they're different, we delete the WallBoard, set the value
			of the neighboring cell to that of the original cell, and loop through the two-dimensional array,
			checking to see if all of the values in the two-dimensional array are the same, if they are,then 
			every cell is in the same set. And we end the loop.
			*/
			WidthNeighbor = wallboard.getNeighborX();
			HeightNeighbor = wallboard.getNeighborY();
		
			//If they have the same value they're already of the same set, start loop again
			if ( cells[ WidthRandom ][ HeightRandom ] == cells[ WidthNeighbor ][ HeightNeighbor ] ) 
				continue;
			floorplan.deleteWallboard( wallboard );
			
			int NewValue = cells[ WidthRandom ][ HeightRandom ];
			int WillReplace = cells[ WidthNeighbor ][ HeightNeighbor ];
			for ( int xSearch = 0; xSearch < width; xSearch++ ) 
				for ( int ySearch = 0; ySearch < height; ySearch++ ) 
					if ( cells[ xSearch ][ ySearch ] == WillReplace )
						cells[ xSearch ][ ySearch ] = NewValue;
		}
	}
	
	/**
	* We run this after every loop, it contains the condition for exiting the program. We take the
	* first value and scan through all of the possible values, if they are all the same, then it returns
	* true, and we exit MazeBuilderKruskal. If we run into a different value, they can't all be the same,
	* so we return false, and the while loop that tears down WallBoards continues.
	* @param visited: Will pass in cells, the two-dimensional array, which we will scan through.
	* @return boolean: true if all of them are the same type, false if they are not.
	*/
	private boolean checkAllSame(int[][] visited) {
		//Take value at first cell
		int val = visited[ 0 ][ 0 ];
		for ( int l = 0; l < width; l++ )
			for ( int i = 0; i < height; i++ )
				//If any value is found to be different, the test fails.
				if ( visited[ l ][ i ] != val )
					return false;
		return true;
	}
			
}