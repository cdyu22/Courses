package generation;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import generation.Order.Builder;


class MazeFactoryTest {
	private MazeContainer mazeHolder;
	private Floorplan floorPlan;
	private MazeFactory mazeMaker;
	private OrderStub fakeOrder;
	
	//The parameters for the order, to test other scenarios just change these.
	private Order.Builder builderTest = Builder.Kruskal;
	private boolean perfect = false;
	private int skillLevel = 9;
	
	
	////////////////////////////////////////Private Helper Methods////////////////////////////////
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
		fakeOrder.setBuilder( builderTest );
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
	
	///////////////////////////////////Attribute Tests/////////////////////////////////////
	/**
	 * Goes through all of the cells and makes sure that all of them have been visited.
	 * They should all have been visited, and the test fails if one is detected that has not. We can
	 * tell if they have been visited by looking at their walls. If they have four walls they haven't
	 * been visited, as no walls have been town down and it's inaccessible, if at least one wall is
	 * torn down then it has been visited.
	 */
	@Test
	void testVisit() {
		mazeSetUp();
		
		Wallboard WallCounter = new Wallboard( 0, 0, CardinalDirection.North );
		//Scans through all of the cells in floorPlan
		for ( int i = 0; i < mazeHolder.getWidth(); i++ ) 
			for ( int j=0; j < mazeHolder.getHeight(); j++ ) {
				int counter = 0;
				for (CardinalDirection cd : CardinalDirection.values()) {
					WallCounter.setLocationDirection( i, j, cd );
					//Counts how many wallboards every cell has
					if (floorPlan.hasWall( i, j, cd )){
						counter++;
					}
				}
				//For all of the cells, asserts it doesn't have four wallboards
				assertNotEquals( 4, counter );
			}
		
		mazeReset();
	}
	
	/**
	 * Fairly simple test. MazeContainer stores the start position, so we scan through the 
	 * borders, similar to ExitTest, and we find the cell that has the exit. We make sure
	 * they are not the same. At the minimum, they should be at least 1 cells away, just to ensure the StartPoint 
	 * isn't the EndPoint, though this will be a boring game. Fails if the starting cell is the ending cell. 
	 * Will catch silly errors.
	 */
	@Test
	void testStart() {
		mazeSetUp();
		
		int[] startPoint = new int[ 2 ];
		int[] endPoint = new int[ 2 ];
		//Stores starting position
		startPoint = mazeHolder.getStartingPosition();
		
		//Scans through all of the cells and checks if they're an Exit point.
		for ( int i = 0; i < mazeHolder.getWidth() ; i++ ) 
			for ( int j=0; j < mazeHolder.getHeight(); j++ ) 
				if ( floorPlan.isExitPosition( i, j ) ) {
					endPoint[ 0 ] = i;
					endPoint[ 1 ] = j;
				}
		assertNotEquals( startPoint, endPoint );
		
		mazeReset();
		
	}
	
	/**
	 * After declaring the order variables, (skill, builder, perfect) create the maze
	 * and then test to make sure that none of those variables were changed. Fails if they are
	 * different.
	 */
	@Test
	void testSetGet() {
		mazeSetUp();
		
		//Maze is setup, checking to make sure nothing in the order changes
		assertEquals( skillLevel, fakeOrder.getSkillLevel() );
		assertEquals( builderTest, fakeOrder.getBuilder() );
		assertEquals( perfect, fakeOrder.isPerfect() );	
		
		mazeReset();
		
	}
	
	/**
	 * Checks to see if it's possible to exit the grid.
	 * To do this, we scan through all of the outside wall boards
	 * and test isExitPosition. Take the width and height of the 
	 * maze to ensure we only test the borders of the maze and not 
	 * the inner cells. Fails if there's no exit.
	 */
	@Test
	void testExit() {
		mazeSetUp();
		
		int counter = 0;
		for ( int i = 0; i < mazeHolder.getWidth(); i++ ) 
			for ( int j = 0; j < mazeHolder.getHeight(); j++ ) 
				if ( floorPlan.isExitPosition( i, j ) ) 
					//Increment if there's an exit position
					counter++;
		//Check to make sure that the counter is no longer zero.
		assertNotEquals( counter, 0 );
		
		mazeReset();
	}
	
	/**
	 * Check to see if the maze only has ONE exit. Previous test ensures
	 * we have an exit, but it's a problem if we have multiple. Separation of tests
	 * let us know if what we do is correct. 
	 * Create a counter variable and loop through all of the cells, testing isExitPosition
	 * for all of them. Non-border cells shouldn't have exits, but could catch mistakes.
	 * We also take the width and height to know how far to loop. If the counter at the end
	 * of the loop is not 1, test fails.
	 */
	@Test
	void testOneExit() {
		mazeSetUp();
		
		int counter = 0;
		for ( int i = 0; i < mazeHolder.getWidth(); i++ ) 
			for ( int j=0; j < mazeHolder.getHeight(); j++ ) 
				if ( floorPlan.isExitPosition( i, j ) )
					//Increment if there's an exit position
					counter++;		
		//Check to make sure that there's only one exit
		assertEquals( counter, 1 );
	
		mazeReset();
	}
	//////////////////////////////Room and Pathway Tests//////////////////////////
	
	/**
	 * Checks to see if you can reach the exit. Note that this also means that
	 * every cell can access the exit. To do this, we look at MazeContainer's MazeDist
	 * matrix and check all of the values in there and make sure they're less than infinity,
	 * or the total amount of nodes (if perfect). 
	 */
	@Test
	void testExitReachable() {
		mazeSetUp();
		
		//Records the amount of nodes in the entire maze, upper bound of path length to the exit.
		int totalNodes = mazeHolder.getWidth() * mazeHolder.getHeight();
		Distance distMatrix;
		distMatrix = mazeHolder.getMazedists();
		for ( int i = 0; i < mazeHolder.getWidth(); i++ ) 
			for ( int j = 0; j < mazeHolder.getHeight(); j++ ) 
				//For every cell, assert the distance value is less than total nodes
				assertTrue( distMatrix.getDistanceValue( i, j ) <= totalNodes);
		
		mazeReset();
	}

	/**
	 * Similar to PathwayWidthTest. Scan through all of the cells in the FloorPlan and 
	 * count the amount of cells that have 3 walls, if they do then they're classified
	 * as dead ends. There should be more than 0 dead-ends. Fails if there are 0 dead-ends.
	 * Fails if any of the dead-ends are found to be in rooms. 
	 */
	@Test
	void testDeadEnd() {
		mazeSetUp();
		
		//The counter for the amount of dead-ends
		int counter = 0;
		
		Wallboard wallboard = new Wallboard( 0, 0, CardinalDirection.North );
		for ( int i = 0; i < mazeHolder.getWidth(); i++ ) 
			for ( int j = 0; j < mazeHolder.getHeight(); j++ ) {
				
				//The counter for the amount of WallBoards in every cell
				int wallCounter = 0;
				for ( CardinalDirection cd : CardinalDirection.values() ) {
					wallboard.setLocationDirection( i, j, cd );
					if (floorPlan.hasWall( i, j, cd ))
						wallCounter++;
					
					//If there are three WallBoards, its a dead end, increment dead-end counter.
					if (wallCounter == 3)
						counter++;
				}
			}
		assertTrue( 0 < counter );
		
		mazeReset();
	}
	
	/**
	 * Similar to PathwayWidthTest. Want to check to see if all of the cells in rooms
	 * have zero to two walls, never having 3. Scan through all of the cells in the 
	 * FloorPlan. If the cell is in a room, test to see if it has between 0 and 2 walls. 
	 * If it does not, then it fails. This is because the only cells that have 
	 * 0/1 walls should be in rooms. Should specifically make sure the maze isn't perfect.
	 */
	@Test
	void testZerotoTwo() {
		mazeMaker = new MazeFactory( true );
		fakeOrder = new OrderStub();
		
		fakeOrder.setSkillLevel( skillLevel );
		fakeOrder.setBuilder( builderTest );
		fakeOrder.setPerfect( false );
		
		mazeMaker.order( fakeOrder );
		mazeMaker.waitTillDelivered();
		mazeHolder = fakeOrder.mazeDeliver();
		floorPlan = mazeHolder.getFloorplan();
		
		Wallboard wallboard = new Wallboard( 0, 0, CardinalDirection.North );
		for ( int i = 0; i < mazeHolder.getWidth(); i++ ) 
			for ( int j = 0; j < mazeHolder.getHeight(); j++ ) {
				//Only counts the amount of WallBoards if the cell is in a room
				if ( floorPlan.isInRoom( i, j ) ) {
					int wallCounter = 0;
					for ( CardinalDirection cd : CardinalDirection.values() ) {
						wallboard.setLocationDirection( i, j, cd );
						if (floorPlan.hasWall( i, j, cd )){
							wallCounter++;
						}
					}
					assertTrue( 0 <= wallCounter && wallCounter <= 2 );
				}
			}
		
		mazeReset();
	}
	
	///////////////////////////////////Perfect Variable Tests/////////////////////////////////
	
	/**
	 * In this maze there are three possible states cells can be in. They can be in rooms,
	 * they can be a pathway, or they can be a dead-end. This tests makes sure that if the cell
	 * is in a dead-end, that being that it has 3 walls, then it cannot be in a room. 
	 */
	@Test
	void testRoom() {
		mazeMaker = new MazeFactory( true );
		fakeOrder = new OrderStub();
		
		fakeOrder.setSkillLevel( skillLevel );
		fakeOrder.setBuilder( builderTest );
		fakeOrder.setPerfect( false );
		
		mazeMaker.order( fakeOrder );
		mazeMaker.waitTillDelivered();
		mazeHolder = fakeOrder.mazeDeliver();
		floorPlan = mazeHolder.getFloorplan();
		
		Wallboard wallboard = new Wallboard( 0, 0, CardinalDirection.North );
		for ( int i = 0; i < mazeHolder.getWidth(); i++ ) 
			for ( int j = 0; j < mazeHolder.getHeight(); j++ ) {
					
				//Counts the amount of walls every cell has
				int wallCounter = 0;
				for ( CardinalDirection cd : CardinalDirection.values() ) {
					wallboard.setLocationDirection( i, j, cd );
					if (floorPlan.hasWall( i, j, cd )){
						wallCounter++;
					}		
				}
				//If it has three, check to make sure it's not in a room
				if ( wallCounter == 3 )
					assertFalse( floorPlan.isInRoom( i, j ) );
			}
		
		mazeReset();
	}
	
	/**
	 * We tell the builder that the maze is perfect, meaning that there are no rooms.
	 * After that, we go through all of the cells and check if they are in rooms. If any
	 * of them are, the test fails. After this, if both testRoom and testNoRoom run correctly,
	 * we know that the perfect aspect works correctly.
	 */
	@Test
	void testNoRooms() {
		mazeMaker = new MazeFactory( true );
		fakeOrder = new OrderStub();
		
		fakeOrder.setSkillLevel( skillLevel );
		fakeOrder.setBuilder( builderTest );
		fakeOrder.setPerfect( true ); //Set it to be perfect, so no rooms
		
		mazeMaker.order( fakeOrder );
		mazeMaker.waitTillDelivered();
		mazeHolder = fakeOrder.mazeDeliver();
		floorPlan = mazeHolder.getFloorplan();
		
		for ( int i = 0; i < mazeHolder.getWidth(); i++ ) 
			for ( int j=0; j < mazeHolder.getHeight(); j++ ) 
				//Checks that no cells are in a room
				assertFalse( floorPlan.isInRoom( i, j ) );
		mazeReset();
	}
	
	//////////////////////////////Square and Rectangle test/////////////////////////////////
	
	/**
	 * Tests the generation of a maze that is a square. Looks at the distance matrix
	 * to make sure that all of the nodes can access the exit, which is one of the fundamental
	 * criteria for a maze. Set the skill level to 10, which creates a 70 by 70 maze.
	 */
	@Test
	void testSquareMaze(){
		mazeMaker = new MazeFactory( true );
		fakeOrder = new OrderStub();
		
		//Only aspect we ensure is that skill level is set to 11, ensuring it's dimensions
		//lead to a square
		fakeOrder.setSkillLevel( 10 );
		fakeOrder.setBuilder( builderTest );
		fakeOrder.setPerfect( perfect );
		
		mazeMaker.order( fakeOrder );
		mazeMaker.waitTillDelivered();
		mazeHolder = fakeOrder.mazeDeliver();
		
		//Checks to make sure that it's solvable
		int totalNodes = mazeHolder.getWidth() * mazeHolder.getHeight();
		Distance distMatrix;
		distMatrix = mazeHolder.getMazedists();
		for ( int i = 0; i < mazeHolder.getWidth(); i++ ) 
			for ( int j = 0; j < mazeHolder.getHeight(); j++ ) 
				assertTrue( distMatrix.getDistanceValue( i, j ) <= totalNodes);
		
		mazeReset();
	}
	
	/**
	 * Tests the generation of a maze that is a rectangle. Looks at the distance matrix
	 * to make sure that all of the nodes can access the exit, which is one of the fundamental
	 * criteria for a maze. Set the skill level to 11, which creates a 80 by 75 maze. If
	 * both this and testSquareMaze run correctly, we can infer that the dimensions of the maze
	 * will not impact the functionality of the maze builder, and we can test different skill 
	 * levels without worrying if differing x/y dimensions will cause issues.
	 */
	@Test
	void testRectangleMaze(){
		mazeMaker = new MazeFactory( true );
		fakeOrder = new OrderStub();
		
		//Only aspect we ensure is that skill level is set to 11, ensuring it's dimensions
		//lead to a rectangle
		fakeOrder.setSkillLevel( 11 );
		fakeOrder.setBuilder( builderTest );
		fakeOrder.setPerfect( perfect );
		
		mazeMaker.order( fakeOrder );
		mazeMaker.waitTillDelivered();
		mazeHolder = fakeOrder.mazeDeliver();
		
		//Checks to make sure that it's solvable
		int totalNodes = mazeHolder.getWidth() * mazeHolder.getHeight();
		Distance distMatrix;
		distMatrix = mazeHolder.getMazedists();
		for ( int i = 0; i < mazeHolder.getWidth(); i++ ) 
			for ( int j = 0; j < mazeHolder.getHeight(); j++ ) 
				assertTrue( distMatrix.getDistanceValue( i, j ) <= totalNodes);
		
		
		mazeReset();
	}
	
	//////////////////////////////////Skill Configuration Tests////////////////////////////////////
	/**
	 * This test exists outside of the given parameters, just makes sure that the 
	 * maze can be solvable if it is set to a low skill level. We test this by making
	 * sure that the distance to an exit for every cell has a lower bound of all of 
	 * the nodes in the matrix.
	 */
	@Test
	void testLowSkill() {
		mazeSetUp();
		mazeMaker = new MazeFactory( true );
		fakeOrder = new OrderStub();
		
		fakeOrder.setSkillLevel( 2 );
		fakeOrder.setBuilder( builderTest );
		fakeOrder.setPerfect( true );
			
		mazeMaker.order( fakeOrder );
		mazeMaker.waitTillDelivered();
		mazeHolder = fakeOrder.mazeDeliver();
		floorPlan = mazeHolder.getFloorplan();
		
		int totalNodes = mazeHolder.getWidth() * mazeHolder.getHeight();
		Distance distMatrix;
		distMatrix = mazeHolder.getMazedists();
		for ( int i = 0; i < mazeHolder.getWidth(); i++ ) 
			for ( int j = 0; j < mazeHolder.getHeight(); j++ ) 
				assertTrue( distMatrix.getDistanceValue( i, j ) <= totalNodes);
		
		mazeReset();
	}
	
	/**
	 * This test exists outside of the given parameters, just makes sure that the 
	 * maze can be solvable if it is set to a medium skill level. We test this by making
	 * sure that the distance to an exit for every cell has a lower bound of all of 
	 * the nodes in the matrix.
	 */
	@Test
	void testMediumSkill() {
		mazeSetUp();
		mazeMaker = new MazeFactory( true );
		fakeOrder = new OrderStub();
		
		fakeOrder.setSkillLevel( 8 );
		fakeOrder.setBuilder( builderTest );
		fakeOrder.setPerfect( true );
			
		mazeMaker.order( fakeOrder );
		mazeMaker.waitTillDelivered();
		mazeHolder = fakeOrder.mazeDeliver();
		floorPlan = mazeHolder.getFloorplan();
		
		int totalNodes = mazeHolder.getWidth() * mazeHolder.getHeight();
		Distance distMatrix;
		distMatrix = mazeHolder.getMazedists();
		for ( int i = 0; i < mazeHolder.getWidth(); i++ ) 
			for ( int j = 0; j < mazeHolder.getHeight(); j++ ) 
				assertTrue( distMatrix.getDistanceValue( i, j ) <= totalNodes);
		
		mazeReset();
	}
	
	/**
	 * This test exists outside of the given parameters, just makes sure that the 
	 * maze can be solvable if it is set to the highest skill level. We test this by making
	 * sure that the distance to an exit for every cell has a lower bound of all of 
	 * the nodes in the matrix. After this, if all of the tests concerning skill run correctly,
	 * we can reasonably infer that the maze can generate at any skill level.
	 */
	@Test
	void testHighSkill() {
		mazeSetUp();
		mazeMaker = new MazeFactory( true );
		fakeOrder = new OrderStub();
		
		fakeOrder.setSkillLevel( 15 );
		fakeOrder.setBuilder( builderTest );
		fakeOrder.setPerfect( true );
			
		mazeMaker.order( fakeOrder );
		mazeMaker.waitTillDelivered();
		mazeHolder = fakeOrder.mazeDeliver();
		floorPlan = mazeHolder.getFloorplan();
		
		int totalNodes = mazeHolder.getWidth() * mazeHolder.getHeight();
		Distance distMatrix;
		distMatrix = mazeHolder.getMazedists();
		for ( int i = 0; i < mazeHolder.getWidth(); i++ ) 
			for ( int j = 0; j < mazeHolder.getHeight(); j++ ) 
				assertTrue( distMatrix.getDistanceValue( i, j ) <= totalNodes);
		
		mazeReset();
	}
	
	/////////////////////////////Seed or Determinism Tests/////////////////////////
	
	/**
	 * Create a maze and store the FloorPlan. Then, reset order and MazeFactory
	 * and create the same maze given the same criteria, then test the FloorPlans
	 * to make sure that they're the same. If they are not, the test fails. Makes sure
	 * that MazeFactory is using deterministic correctly.
	 */
	@Test
	void testSeed() {
		//Creates a maze and then stores the floorPlan (use floorPlan as it has
		//an .equals method, so can't compare, say, MazeContainers)
		MazeFactory mazeMaker = new MazeFactory( true );
		OrderStub fakeOrder = new OrderStub();
		OrderStub equivalent = new OrderStub();
		
		fakeOrder.setSkillLevel( skillLevel );
		fakeOrder.setBuilder( builderTest );
		fakeOrder.setPerfect( perfect );
		
		mazeMaker.order( fakeOrder );
		mazeMaker.waitTillDelivered();
		
		Floorplan floorPlan1 = fakeOrder.mazeDeliver().getFloorplan();
		//After storing it, reset everything
		mazeReset();
		
		//Recreate the maze with the same aspects
		equivalent.setSkillLevel( skillLevel );
		equivalent.setBuilder( builderTest );
		equivalent.setPerfect( perfect );
		
		mazeMaker.order( equivalent );
		mazeMaker.waitTillDelivered();
		
		Floorplan floorPlan2 = equivalent.mazeDeliver().getFloorplan();
		assertEquals( floorPlan1, floorPlan2 );
	}
	
	/**
	 * Create a maze and store the FloorPlan. Then, reset order and MazeFactory
	 * and create a maze with the same criteria, then test the FloorPlans
	 * to make sure that they're not the same. If they are, the test fails. Makes sure
	 * that MazeFactory is using deterministic correctly.
	 */
	@Test
	void testNoSeed() {
		//Creates a maze and then stores the floorPlan (use floorPlan as it has
		//an .equals method)
		MazeFactory mazeMaker = new MazeFactory();
		OrderStub fakeOrder = new OrderStub();
		OrderStub equivalent = new OrderStub();
		
		fakeOrder.setSkillLevel( skillLevel );
		fakeOrder.setBuilder( builderTest );
		fakeOrder.setPerfect( perfect );
		
		mazeMaker.order( fakeOrder );
		mazeMaker.waitTillDelivered();
		
		Floorplan floorPlan1 = fakeOrder.mazeDeliver().getFloorplan();
		//After storing it, reset everything
		mazeReset();
		
		//Recreate the maze with the same aspects
		equivalent.setSkillLevel( skillLevel );
		equivalent.setBuilder( builderTest );
		equivalent.setPerfect( perfect );
		
		mazeMaker.order( equivalent );
		mazeMaker.waitTillDelivered();
		
		Floorplan floorPlan2 = equivalent.mazeDeliver().getFloorplan();
		assertNotEquals( floorPlan1, floorPlan2 );
	}
	
}
