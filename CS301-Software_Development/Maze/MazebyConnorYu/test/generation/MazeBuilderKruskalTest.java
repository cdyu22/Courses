package generation;

import static org.junit.jupiter.api.Assertions.*;

import java.util.Random;

import org.junit.jupiter.api.Test;

import generation.Order.Builder;

//To allow us to test the private methods

class MazeBuilderKruskalTest {
	private MazeContainer mazeHolder;
	private Floorplan floorPlan;
	private MazeFactory mazeMaker;
	private OrderStub fakeOrder;
	
	//The parameters for the order, to test other scenarios just change these.
	private int skillLevel = 9;
	private boolean perfect = true;
	
	//////////////////////////////////////Private Helper Methods/////////////////////////////////////
	/**
	 * Sets up the maze. Creates a MazeFactory object and an OrderStub object. Tells the order the skill 
	 * level, the builder, and whether the Maze should be perfect or not. Once it's returned, we can easily
	 * tweak those aspects of the order in the individual methods, and if we want to change the 
	 * skill/builder/perfect status for all of the methods, just need to change one line.
	 */
	private void mazeSetUp() {
		mazeMaker = new MazeFactory( true );
		fakeOrder = new OrderStub();
		
		fakeOrder.setSkillLevel( skillLevel );
		fakeOrder.setBuilder( Builder.Kruskal );
		fakeOrder.setPerfect( perfect );
		
		mazeMaker.order( fakeOrder );
		mazeMaker.waitTillDelivered();
		mazeHolder = fakeOrder.mazeDeliver();
		floorPlan = mazeHolder.getFloorplan();
	}
	
	/**
	 * Ran after every test. The MazeFactory resets automatically, so all we need to do is reset the OrderStub,
	 * the MazeContainer and the FloorPlan.
	 */
	private void mazeReset() {
		fakeOrder = null;
		floorPlan = null;
		mazeHolder = null;
	}
	
	////////////////////////////////////////Attribute Tests/////////////////////////////////////////
	
	/**
	 * Redundant, as similar test in MazeFactoryTest.java, but will specifically test it for Kruskal.
	 * Makes sure that after construction, order is still Kruskal. 
	 */
	@Test
	void testKruskalBuilder() {
		mazeSetUp();
		
		//After test is built, checks the attributes of the order to make sure nothing is changed.
		assertEquals( skillLevel, fakeOrder.getSkillLevel() );
		assertEquals( Builder.Kruskal, fakeOrder.getBuilder() );
		assertEquals( perfect, fakeOrder.isPerfect() );	
		
		mazeReset();
	}
	
	/**
	 * Scan through all of the borders and find the exit position. Find the distance between
	 * the start and the exit position, they should not be the same cell. Fails if they 
	 * are in the same cell.
	 */
	@Test
	void testStartExit() {
		mazeSetUp();
		
		int[] startPoint = new int[ 2 ];
		int[] endPoint = new int[ 2 ];
		startPoint = mazeHolder.getStartingPosition();
		
		for ( int i = 0; i < mazeHolder.getWidth(); i++ ) 
			for ( int j = 0; j < mazeHolder.getHeight(); j++ ) 
				if ( floorPlan.isExitPosition( i, j ) ) {
					endPoint[ 0 ] = i;
					endPoint[ 1 ] = j;
				}
		//After finding EndPoint, we make sure that the startpoint and endpoint aren't the same
		assertNotEquals( startPoint, endPoint );
		
		mazeReset();
	}
	
	@Test
	void testRandom() {
		mazeSetUp();
		
		int north = 0;
		int south = 0;
		int east = 0;
		int west = 0;
		
		for ( int i = 0; i < mazeHolder.getWidth(); i++ ) 
			for ( int j = 0; j < mazeHolder.getHeight(); j++ ) 
				for (CardinalDirection cd : CardinalDirection.values())
					if (floorPlan.hasNoWall(i, j, cd)) {
						if (cd == CardinalDirection.North)
							north++;
						if (cd == CardinalDirection.South)
							south++;
						if (cd == CardinalDirection.East)
							east++;
						if (cd == CardinalDirection.West)
							west++;
					}
				
		assertTrue( 0 < north);
		assertTrue( 0 < south);
		assertTrue( 0 < east);
		assertTrue( 0 < west);
		mazeReset();
	}
	
	/////////////////////////////////Minimum Spanning Tree Tests///////////////////////////////
	
	/**
	 * Ensuring that the maze is perfect, we count the amount of WallBoards every cell
	 * DOESN'T have. Due to it being a minimum spanning tree, it should have n - 1 lack of walls.
	 * Fails if it doesn't. Placed in this test due to possible Eller's implementation. A maze
	 * can be correct and not a minimum spanning tree.
	 */
	@Test
	void testminSpanningTree() {
		mazeSetUp();
		
		CardinalDirection cd;
		int counter = 0;
		Wallboard wallboard = new Wallboard( 0, 0, CardinalDirection.North );
		//For all of the cells in the floorboard, we count the amount of walls
		//that aren't there.
		for ( int i = 0; i < mazeHolder.getWidth(); i++ ) 
			for ( int j = 0; j < mazeHolder.getHeight(); j++ ) {
				
				//Only go through east and south, as if we counted north and west
				//we would double count all of the walls that aren't there.
				cd = CardinalDirection.East;
				wallboard.setLocationDirection( i, j, cd );
				if ( floorPlan.hasNoWall( i, j, cd ) )
					counter++;
				
				cd = CardinalDirection.South;
				wallboard.setLocationDirection( i, j, cd );
				if (floorPlan.hasNoWall( i, j, cd )){
					counter++;
				}	
				
			}
		//Assert that it's a minimum spanning tree in that it has (total nodes - 1) connections
		//(which in this scenario are torn down walls)
		assertEquals( counter, mazeHolder.getWidth() * mazeHolder.getHeight() - 1 );
		
		mazeReset();	
	}
	
	/**
	 * One of the attributes of minimum spanning trees is that if you take away one edge,
	 * it is no longer a spanning tree and isn't fully connected, as it has the minimum amount
	 * of edges as possible. This tests whether that is true. We find a WallBoard that has been
	 * torn down. We then add it to the FloorPlan, and recompute distances. This should always 
	 * throw an AssertionError, as if the maze is set up correctly, there are cells that cannot
	 * reach the exit, as removing one edge cuts them off from the pathway to the exit. 
	 */
	@Test
	void testAddOneWall() {
		mazeSetUp();
		
		boolean fails = false;
		Random random = new Random();
		
		//Setting up a search for a random WallBoard that has been torn down.
		int WidthRandom = random.nextInt(mazeHolder.getWidth()); 
		int HeightRandom = random.nextInt(mazeHolder.getHeight());
		CardinalDirection TearDownDirection = CardinalDirection.North;
		TearDownDirection = TearDownDirection.randomDirection();
		
		//Will loop until we find a WallBoard that has been torn down.
		while (!floorPlan.hasNoWall(WidthRandom, HeightRandom, TearDownDirection)) {
			WidthRandom = random.nextInt(mazeHolder.getWidth());
			HeightRandom = random.nextInt(mazeHolder.getHeight());
			TearDownDirection = TearDownDirection.randomDirection();
		}
		
		//We found the WallBoard, now we add it back to the FloorPlan, and get a distance matrix
		//from the MazeHolder. This should have all previous distance calculations.
		Wallboard wallboard = new Wallboard( WidthRandom, HeightRandom, TearDownDirection );
		floorPlan.addWallboard(wallboard, true);
		Distance distMatrix = mazeHolder.getMazedists();

		//We rerun it, calculating distances for all of the cells.
		try {
			distMatrix.computeDistances(floorPlan);
		}
		//Should always give an AssertionError, as now certain cells aren't connected
		//to the overall maze.
		catch(AssertionError e) {
			fails = true;
		}
		
		assertTrue(fails);
		
		mazeReset();
	}
	
	////////////////////////////////////Perfect Variable Test/////////////////////////////////
	
	/**
	 * Set the maze to be not perfect, and the skill level to two, so there should be rooms.
	 * Then, scan through all of the cells in the FloorPlan and test if they're in a room,
	 * will exit if one cell is found, will fail if none found. Will only work with later implementation
	 * that includes the generation of rooms.
	 */
	@Test
	void testRoom() {
		mazeMaker = new MazeFactory( true );
		fakeOrder = new OrderStub();
		
		fakeOrder.setSkillLevel( 2 );
		fakeOrder.setBuilder( Builder.Kruskal );
		fakeOrder.setPerfect( false );
		
		boolean room = false;
		
		mazeMaker.order( fakeOrder );
		mazeMaker.waitTillDelivered();
		mazeHolder = fakeOrder.mazeDeliver();
		floorPlan = mazeHolder.getFloorplan();
		
		//Scans all cells in WallBoard, sets room boolean variable to
		//true if there is a cell in a room
		for ( int i = 0; i < mazeHolder.getWidth(); i++ ) 
			for ( int j = 0; j < mazeHolder.getHeight(); j++ ) 
				if ( floorPlan.isInRoom( i, j ) )
					room = true;
			
		assertTrue( room );
		
		mazeReset();
	}
	
	/**
	 * Set the maze to be perfect. Then, scan through all of the cells in the 
	 * FloorPlan and test if any of them are in a room, will fail if none cell 
	 * in a room is found.
	 */
	@Test
	void testNoRoom() {
		mazeMaker = new MazeFactory( true );
		fakeOrder = new OrderStub();
		
		fakeOrder.setSkillLevel( skillLevel );
		fakeOrder.setBuilder( Builder.Kruskal );
		fakeOrder.setPerfect( true );
		
		boolean room = false;
		
		mazeMaker.order( fakeOrder );
		mazeMaker.waitTillDelivered();
		mazeHolder = fakeOrder.mazeDeliver();
		floorPlan = mazeHolder.getFloorplan();
		
		for ( int i = 0; i < mazeHolder.getWidth(); i++ ) 
			for ( int j = 0; j < mazeHolder.getHeight(); j++ ) 
				if ( floorPlan.isInRoom( i, j ) )
					room = true;
			
		//Similar to testRoom, it sets room to true if there is a room,
		//but here we want it to be false, as we set there to be no rooms
		assertFalse( room );
		
		mazeReset();
	}
	
	/////////////////////////////Seed or Determinism Tests/////////////////////////////
	
	/**
	 * Similar to the seed test in MazeFactoryTest, but this specifically checks 
	 * Kruskal's algorithm. Creates a maze and FloorPlan, stores the FloorPlan,
	 * creates another one with identical parameters and makes sure they're equal,
	 * as we make sure the generation is deterministic given the seed.
	 */
	@Test
	void testDeterminism() {
		MazeFactory mazeMaker = new MazeFactory( true );
		OrderStub fakeOrder = new OrderStub();
		OrderStub equivalent = new OrderStub();
		
		fakeOrder.setSkillLevel( skillLevel );
		fakeOrder.setBuilder( Builder.Kruskal );
		fakeOrder.setPerfect( perfect );
		
		mazeMaker.order( fakeOrder );
		mazeMaker.waitTillDelivered();
		
		Floorplan floorPlan = fakeOrder.mazeDeliver().getFloorplan();
		mazeReset();
		
		equivalent.setSkillLevel( skillLevel );
		equivalent.setBuilder( Builder.Kruskal );
		equivalent.setPerfect( perfect );
		
		mazeMaker.order( equivalent );
		mazeMaker.waitTillDelivered();
		
		Floorplan floorPlan2 = equivalent.mazeDeliver().getFloorplan();
		assertEquals( floorPlan, floorPlan2 );
		
		mazeReset();
	}
	
	/**
	 * The opposite of the DeterminismTest. We need to make sure that unless it's specifically 
	 * asked for, then all generated mazes should be different, or random. We won't pass in a 
	 * boolean so the default constructor should run, meaning that it won't use any previous
	 * seed when generating the maze.
	 */
	@Test
	void testnonDeterminism() {
		MazeFactory mazeMaker = new MazeFactory();
		OrderStub fakeOrder = new OrderStub();
		OrderStub equivalent = new OrderStub();
		
		fakeOrder.setSkillLevel( skillLevel );
		fakeOrder.setBuilder( Builder.Kruskal );
		fakeOrder.setPerfect( perfect );
		
		mazeMaker.order( fakeOrder );
		mazeMaker.waitTillDelivered();
		
		Floorplan floorPlan = fakeOrder.mazeDeliver().getFloorplan();
		mazeReset();
		
		equivalent.setSkillLevel( skillLevel );
		equivalent.setBuilder( Builder.Kruskal );
		equivalent.setPerfect( perfect );
		
		mazeMaker.order( equivalent );
		mazeMaker.waitTillDelivered();
		
		Floorplan floorPlan2 = equivalent.mazeDeliver().getFloorplan();
		assertNotEquals( floorPlan, floorPlan2 );
		
		mazeReset();
	}
	
	/////////////////////////CheckAllSame Private Method Tests////////////////////////////////
	
	/**
	 * Had to use a stand in, using almost the exact same code of the CheckAllSame method
	 * from MazeBuilderKruskal. We create a new array that has all different variables, and
	 * the method should return false if everything is working correctly. 
	 */
	@Test
	void testCheckAllSameFalse() {
		mazeSetUp();
		boolean allSame = true;
		int[][] cells = new int[ mazeHolder.getWidth() ][ mazeHolder.getHeight() ];
		int counter = 0;
		for ( int wFill = 0; wFill < mazeHolder.getWidth(); wFill++ ) 
			for ( int hFill = 0; hFill < mazeHolder.getHeight(); hFill++ ) {
				cells[ wFill ][ hFill ] = counter;
				counter++;
			}
		
		int val = cells[ 0 ][ 0 ];
		for ( int l = 0; l < mazeHolder.getWidth(); l++ )
			for ( int i = 0; i < mazeHolder.getHeight(); i++ )
				//If any value is found to be different, the test fails.
				if ( cells[ l ][ i ] != val )
					allSame = false;
		
		assertFalse(allSame);
		
		mazeReset();
	}
	
	/**
	 * Had to use a stand in, using almost the exact same code of the CheckAllSame method
	 * from MazeBuilderKruskal. We create a new array that has all the same variables, and
	 * the method should return true if everything is working correctly. If this and 
	 * testCheckkAllSameFalse pass, then we know that it correctly ends the program when
	 * all of the cells in the FloorPlan are of the same type.
	 */
	@Test
	void testCheckAllSameTrue() {
		mazeSetUp();
		boolean allSame = true;
		int[][] cells = new int[ mazeHolder.getWidth() ][ mazeHolder.getHeight() ];
		int counter = 0;
		for ( int wFill = 0; wFill < mazeHolder.getWidth(); wFill++ ) 
			for ( int hFill = 0; hFill < mazeHolder.getHeight(); hFill++ ) 
				cells[ wFill ][ hFill ] = counter;
				// No counter++
			
		int val = cells[ 0 ][ 0 ];
		for ( int l = 0; l < mazeHolder.getWidth(); l++ )
			for ( int i = 0; i < mazeHolder.getHeight(); i++ )
				//If any value is found to be different, the test fails.
				if ( cells[ l ][ i ] != val )
					allSame = false;
		
		assertTrue(allSame);
		
		mazeReset();
	}
	
}
