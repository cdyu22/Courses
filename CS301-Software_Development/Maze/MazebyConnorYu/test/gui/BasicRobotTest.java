package gui;

import org.junit.jupiter.api.Test;

import generation.CardinalDirection;
import gui.Robot.Direction;
import gui.Robot.Turn;

import static org.junit.jupiter.api.Assertions.*;

/**
 * This class serves to test the BasicRobot class, which implements the robot interface.
 * It tests all of the methods that have to do with the robot detecting its surroundings,
 * there are a few private helper methods that it doesn't test, because they mainly have
 * to do with the interaction between the RobotDriver and the BasicRobot. 
 * 
 * There are a variety of attributes in the robot that we want to test, so we have variables 
 * x, y, look(a turn variable) and batteryLevel. These will override what happens by default,
 * so we can place the robot wherever we want and test based off of that. The overriding
 * happens in the setup, when the robot, driver, and controller stub are initialized. At
 * the end we then return the variables to their default values and set the robot, driver
 * and controller stub to null.
 * 
 * 
 * PLEASE NOTE: There will by incomplete coverage, when running the test it tests around 73% 
 * of the code. This is by design, as some code is only reachable through the interaction 
 * between the driver and BasicRobot. The code that wasn't accessed will be used in WallFollowerTest
 * and WizardTest.
 * 
 * Collaborators: BasicRobot, ControllerStub
 * @author Connor Yu
 */
public class BasicRobotTest {
	//Objects that we use to test the BasicRobot
	BasicRobot roboTest;
	ControllerStub fakeController;
	String file = "test/data/input.xml";
	WallFollower dummy; // does nothing

	//Variables that we will override if we want to test certain attributes
	int x = 4;
	int y = 0;
	Turn look = null;
	float batteryLevel = 2000;
	
	/////////////////////////Private Helper Methods/////////////////////////
	
	//Ran before every test
	/**
	 * Ran before every test. This sets up the controller, robot and WallFollower.
	 * It then, if we want it to, can overwrite some of the starting variables of the
	 * basicrobot. We can change the starting position, the way it's looking (defaults
	 * east), and the batteryLevel.
	 */
	private void controllerSetUp() {
		fakeController = new ControllerStub();
		
		//Overriding the variables
		//Starting position
		fakeController.xPlaced = x;
		fakeController.yPlaced = y;
		
		//Direction it's turning
		fakeController.turning = look;
		
		//battery level
		fakeController.batteryLevel = batteryLevel;
		
		roboTest = new BasicRobot();
		dummy = new WallFollower();
		
		dummy.setRobot(roboTest); 
		fakeController.setRobotAndDriver(roboTest, dummy);
		
		/*
		 * In this test, we don't care about the title screen or winning screen,
		 * though sometimes we care and track if methods try to get to them. 
		 * However, the majority of the time, we're only concerned with the 
		 * state when it's generating and playing. The program naturally goes
		 * from generating to playing, and we don't allow anything to happen
		 * when it tries to go to StateWinning.
		 */
		fakeController.switchFromTitleToGenerating(file); 
		
	}
	
	/**
	 * Ran after every test. Tears down all of the objects, including the robot, the 
	 * wallfollower, and fakeController. Then resets the variables to their default setting.
	 */
	private void controllerTearDown() {
		roboTest = null;
		dummy = null;
		fakeController = null;
		
		//We return these to their initial values, so they're the default when we run another test
		x = 4;
		y = 0;
		look = null;
		batteryLevel = 2000;
		
	}
	
	//////////////////////////////////SetMaze Tests/////////////////////////////////////
	
	/**
	 * In this, we test to see if a proper connection was made between the maze and the robot.
	 * The robot can only interact with the StatePlaying through the controller, so this is a
	 * very important connection.
	 */
	@Test
	void testMazeConnection() {
		controllerSetUp();
		
		//The attribute mazeConnection serves as the variable that holds a connection to the maze.
		//The controller should be equal to that, as they should be the exact same thing and reside
		//in the same spot in memory.
		assertEquals(fakeController, roboTest.mazeConnection);
		
		controllerTearDown();
	}
	
	/**
	 * We need to make sure that the FloorPlan that the robot is drawing information from is the 
	 * same FloorPlan that the controller holds. If it isn't, the robot can't tell what its 
	 * surroundings look like.
	 */
	@Test
	void testFloorPlanConnection() {
		controllerSetUp();
		
		assertEquals(fakeController.mazeConfig.getFloorplan(), roboTest.layout);
		
		controllerTearDown();
	}
	
	//////////////////////////////////getCurrentPosition Tests/////////////////////////////////////
	
	/**
	 * The default starting position in the maze that we're testing is (4,0). We want to make sure
	 * that the robot starts at the same position, as there could be a miscommunication between the
	 * robot and the controller if the robot starts at the incorrect location.
	 * @throws Exception if getCurrentPosition throws an exception
	 */
	@Test
	void testgetCurrentPosition() throws Exception{
		controllerSetUp();
		
		int[] initialPosition = new int[2];
		initialPosition[0] = 4;
		initialPosition[1] = 0;
		
		int[] currentPosition = roboTest.getCurrentPosition();
		
		assertEquals(initialPosition[0], currentPosition[0]);
		assertEquals(initialPosition[1], currentPosition[1]);
		
		controllerTearDown();
	}
	
	/**
	 * The default maze isn't facing a wall, so it should be able to move forward by default. If
	 * we tell the robot to move manually (not through the driver) it should update its location
	 * after it moves. 
	 * @throws Exception if getCurrentPosition throws an exception
	 */
	@Test
	void testgetCurrentPositionAfterMove() throws Exception{
		controllerSetUp();
		
		int[] purportedPosition = new int[2];
		purportedPosition[0] = 5;
		purportedPosition[1] = 0;
		
		roboTest.move(1, false);
		int[] currentPosition = roboTest.getCurrentPosition();
		
		assertEquals(purportedPosition[0], currentPosition[0]);
		assertEquals(purportedPosition[1], currentPosition[1]);
		
		controllerTearDown();
	}
	
	//////////////////////////////////getCurrentDirection Tests/////////////////////////////////////
	
	/**
	 * In the default maze, the robot always starts looking to the east, though this is also true
	 * of every maze. 
	 */
	@Test
	void testgetCurrentDirection() {
		controllerSetUp();
		
		assertEquals(roboTest.getCurrentDirection(), CardinalDirection.East);
		
		controllerTearDown();
	}
	
	/**
	 * There is a bit of confusion between the CardinalDirections versus what shows
	 * up on screen. They are actually inverted, so CardinalDirection.North is to the
	 * right of CardinalDirection.East, so if we want to visualize a correct representation
	 * of the compass, it should flip north and south. So turning right, should turn us north.
	 */
	@Test
	void testgetCurrentDirectionRight() {
		controllerSetUp();
		
		roboTest.rotate(Turn.RIGHT);
		assertEquals(roboTest.getCurrentDirection(), CardinalDirection.North);
		
		controllerTearDown();
	}
	
	/**
	 * Following the above test, we need to make sure that turning left turns us to 
	 * the south.
	 */
	@Test
	void testgetCurrentDirectionLeft() {
		controllerSetUp();
		
		roboTest.rotate(Turn.LEFT);
		assertEquals(roboTest.getCurrentDirection(), CardinalDirection.South);
		
		controllerTearDown();
	}
	
	/**
	 * Following the two above tests, turning around should turn us to the west,
	 * though this is true no matter the compass, as east is always the opposite
	 * direction of west, and vice versa.
	 */
	@Test
	void testgetCurrentDirectionAround() {
		controllerSetUp();
		
		roboTest.rotate(Turn.AROUND);
		assertEquals(roboTest.getCurrentDirection(), CardinalDirection.West);
		
		controllerTearDown();
	}
	
	/**
	 * Combining move and getCurrentDirection, moving should never change the direction
	 * we're facing. In this test, we move the robot forward, as previously stated that
	 * it is possible to do so, and then we make sure that the robot is still facing 
	 * the east.
	 */
	@Test
	void testgetCurrentDirectionAfterMove() {
		controllerSetUp();
		
		roboTest.move(1, false);
		assertEquals(roboTest.getCurrentDirection(), CardinalDirection.East);
		
		controllerTearDown();
	}
	
	//////////////////////////////////isAtExit Tests/////////////////////////////////////
	
	/**
	 * In this, we want to make sure that the starting position correctly shows up as not
	 * the exit. Good test because it should always be false by default.
	 */
	@Test
	void testStartingPositionExit() {
		controllerSetUp();
		
		assertFalse(roboTest.isAtExit());
		
		controllerTearDown();
	}
	
	/**
	 * In the default maze, the exit resides at (0,3). In the test we place the robot there,
	 * and make sure that isAtExit can tell that we are actually at the exit.
	 */
	@Test
	void testisatExit() {
		x = 0;
		y = 3;
		controllerSetUp();
		
		assertTrue(roboTest.isAtExit());
		
		controllerTearDown();
	}
	
	/**
	 * This follows from the test above. We place the robot right next to the exit, and we
	 * test to make sure it doesn't incorrectly flag that spot as the exit.
	 */
	@Test
	void testisAdjacentToExit() {
		x = 0;
		y = 2;
		controllerSetUp();
		
		assertFalse(roboTest.isAtExit());
		
		controllerTearDown();
	}
	
	//////////////////////////////////Seeing Exit Tests/////////////////////////////////////
	
	/**
	 * by default, it should not be able to see the exit at the starting position. This is a 
	 * sanity check to make sure it doesn't ever incorrectly flag that it can see the exit.
	 */
	@Test
	void testCannotSeeExit() {
		controllerSetUp();
		
		assertFalse(roboTest.canSeeThroughTheExitIntoEternity(Direction.FORWARD));
		
		controllerTearDown();
	} 
	
	
	
	/**
	 * Though this doesn't come up in WallFollower or Wizard, we test to see if the robot
	 * can look in the direction of the exit and identify that it is seeing the exit. We
	 * move the robot to (0,0) and turn towards the exit, it should be able to see the exit.
	 */
	@Test
	void testCanSeeExit() {
		x = 0;
		y = 0;
		look = Turn.LEFT;
		controllerSetUp();
		
		assertTrue(roboTest.canSeeThroughTheExitIntoEternity(Direction.FORWARD));
		
		controllerTearDown();
	} 
	
	/**
	 * Though this doesn't come up in WallFollower or Wizard, we test to see if the robot
	 * can look in the direction of the exit and identify that it is seeing the exit. We
	 * move the robot to (0,0) and look towards the left to see if the exit is there,
	 * (left on the screen would be towards the north). It should be able to see the exit.
	 */
	@Test
	void testCanSeeExitonLeft() {
		x = 0;
		y = 0;
		controllerSetUp();
		
		assertTrue(roboTest.canSeeThroughTheExitIntoEternity(Direction.LEFT));
		
		controllerTearDown();
	} 
	
	/**
	 * In this test, we place the robot at the place adjacent to the exit, but the place has
	 * a wallboard separating it and the exit. It shouldn't be able to see the exit.
	 */
	@Test
	void testSeparatedbyWallboard() {
		x = 1;
		y = 3;
		look = Turn.AROUND;
		controllerSetUp();
		
		assertFalse(roboTest.canSeeThroughTheExitIntoEternity(Direction.FORWARD));
		
		controllerTearDown();
	} 
	
	//////////////////////////////////Inside Room Tests/////////////////////////////////////
	/**
	 * A sanity check, we know that by default the starting position isn't in the room, so
	 * we test its sensor, and it should correctly say that it is not in a room.
	 */
	@Test
	void testifStartingPositionInRoom() {
		controllerSetUp();
	
		assertFalse(roboTest.isInsideRoom());
		
		controllerTearDown();
	}
	
	/**
	 * A place that's in a room is coordinate (17,4). Because we know that, we place the robot
	 * at that spot and ask if it's in a room, and it should correctly say that it is.
	 */
	@Test
	void testInRoom() {
		x = 17;
		y = 4;
		
		controllerSetUp();
	
		assertTrue(roboTest.isInsideRoom());
		
		controllerTearDown();
	}
	
	/**
	 * This spot is directly adjacent to a room. If the sensor is working correctly, then 
	 * despite its proximity, it should still say that the robot is NOT in a room.
	 */
	@Test
	void testIsNotInRoom() {
		x = 17;
		y = 6;
		
		controllerSetUp();
	
		assertFalse(roboTest.isInsideRoom());
		
		controllerTearDown();
	}
	
	//////////////////////////////////hasStopped Tests///////////////////////////////////// 
	
	/**
	 * In this test we test if it can tell if the robot hasStopped or not. One of the flags
	 * for it stopping is if there is a wall in front of it. If there is ever a miscommunication
	 * between the robot and the controller, hasStopped makes sure it doesn't try to move
	 * into a wall. 
	 */
	@Test
	void testWallinFront() {
		look = Turn.AROUND;
		controllerSetUp();
		
		assertTrue(roboTest.hasStopped());
		
		controllerTearDown();
	}
	
	/**
	 * Another flag that hasStopped checks is if the battery level is at 0 or below. If
	 * it is, then it stops the robot, and doesn't allow it to move.
	 */
	@Test
	void testBatteryLevelZero() {
		batteryLevel = 0;
		controllerSetUp();
		
		assertTrue(roboTest.hasStopped());
		
		controllerTearDown();
	}
	
	/**
	 * If hasStopped is working correctly, it should make sure that the robot isn't allowed to
	 * walk into a wall. We tell it to take a step forward, then turn around and take 2 steps.
	 * In the default starting location one step would make it face a wall, and it shouldn't be
	 * allowed to move after it's facing a wall.
	 * @throws Exception
	 */
	@Test
	void testMoveIntoWall() throws Exception {
		x = 5;
		controllerSetUp();
		
		roboTest.move(1, false);
		roboTest.rotate(Turn.AROUND);
		roboTest.move(2, false);
		int[] currentPosition = roboTest.getCurrentPosition();
		assertEquals(currentPosition[0],4);
		assertEquals(currentPosition[1],0);
		
		controllerTearDown();
	}
	
	//////////////////////////////////Distance to Obstacle Tests/////////////////////////////////////
	
	/**
	 * When testing the distance sensor we first try a very simple situation in which the robot is
	 * surrounded by WallBoards on three sides. By default, it should detect that it can move forward
	 * 11 spaces, and can't move anywhere else.
	 */
	@Test
	void testFirstSpace() {
		controllerSetUp();

		assertEquals(roboTest.distanceToObstacle(Direction.FORWARD),11);
		assertEquals(roboTest.distanceToObstacle(Direction.LEFT),0);
		assertEquals(roboTest.distanceToObstacle(Direction.RIGHT),0);
		assertEquals(roboTest.distanceToObstacle(Direction.BACKWARD),0);
		
		controllerTearDown();
	}
	
	/**
	 * Following the above test, if everything is working correctly then turning right will mean
	 * that we can move 11 spots to the left, and all of the other sides of the robot are now surrounded.
	 */
	@Test
	void testRotateRightOneWallBoard() {
		look = Turn.RIGHT;
		controllerSetUp();

		assertEquals(roboTest.distanceToObstacle(Direction.FORWARD),0);
		assertEquals(roboTest.distanceToObstacle(Direction.LEFT),11);
		assertEquals(roboTest.distanceToObstacle(Direction.RIGHT),0);
		assertEquals(roboTest.distanceToObstacle(Direction.BACKWARD),0);
		
		controllerTearDown();
	}
	
	/**
	 * Following the above tests, if everything is working correctly then turning right will mean
	 * that we can move 11 spots to the right, and all of the other sides of the robot are now surrounded.
	 */
	@Test
	void testRotateLeftOneWallBoard() {
		look = Turn.LEFT;
		controllerSetUp();
		
		assertEquals(roboTest.distanceToObstacle(Direction.FORWARD),0);
		assertEquals(roboTest.distanceToObstacle(Direction.LEFT),0);
		assertEquals(roboTest.distanceToObstacle(Direction.RIGHT),11);
		assertEquals(roboTest.distanceToObstacle(Direction.BACKWARD),0);
		
		controllerTearDown();
	}
	
	/**
	 * Following the above tests, if everything is working correctly then turning around will mean
	 * that we can move 11 spots backwards, and all of the other sides of the robot are now surrounded.
	 */
	@Test
	void testRotateTurnAroundOneWallBoard() {
		look = Turn.AROUND;
		controllerSetUp();
		
		assertEquals(roboTest.distanceToObstacle(Direction.FORWARD),0);
		assertEquals(roboTest.distanceToObstacle(Direction.LEFT),0);
		assertEquals(roboTest.distanceToObstacle(Direction.RIGHT),0);
		assertEquals(roboTest.distanceToObstacle(Direction.BACKWARD),11);
		
		controllerTearDown();
	}
	
	/**
	 * After the simple tests above, we test if the robot can track its distance after movement.
	 * Moving the robot one space forward, it now can only move 10 spots forward and 1 spot backwards.
	 */
	@Test
	void testMoveForwardTracker() {
		controllerSetUp();

		roboTest.move(1, false);
		assertEquals(roboTest.distanceToObstacle(Direction.FORWARD),10);
		assertEquals(roboTest.distanceToObstacle(Direction.LEFT),0);
		assertEquals(roboTest.distanceToObstacle(Direction.RIGHT),0);
		assertEquals(roboTest.distanceToObstacle(Direction.BACKWARD),1);
		
		controllerTearDown();
	}
	
	/**
	 * This now becomes a tad bit more complicated. We found a spot in the maze that has 4 different directions.
	 * It should be able to tell the distance to all of these and track any changes in distances towards its relative
	 * sides. 
	 */
	@Test
	void testRoomFourWallBoardsLeft() {
		x = 10;
		y = 6;
		
		controllerSetUp();

		assertEquals(roboTest.distanceToObstacle(Direction.FORWARD),2);
		assertEquals(roboTest.distanceToObstacle(Direction.LEFT),6);
		assertEquals(roboTest.distanceToObstacle(Direction.RIGHT),1);
		assertEquals(roboTest.distanceToObstacle(Direction.BACKWARD),3);
		
		roboTest.rotate(Turn.LEFT);
	
		assertEquals(roboTest.distanceToObstacle(Direction.FORWARD),6);
		assertEquals(roboTest.distanceToObstacle(Direction.LEFT),3);
		assertEquals(roboTest.distanceToObstacle(Direction.RIGHT),2);
		assertEquals(roboTest.distanceToObstacle(Direction.BACKWARD),1);
		
		controllerTearDown();
	}
	
	/**
	 * Following the above test, we place the robot in the same location, but this time we turn it to the right,
	 * and test to see if it can accurately tell the distance to all of the newly changed obstacles/WallBoards.
	 */
	@Test
	void testRoomFourWallBoardsRight() {
		x = 10;
		y = 6;
		
		controllerSetUp();

		assertEquals(roboTest.distanceToObstacle(Direction.FORWARD),2);
		assertEquals(roboTest.distanceToObstacle(Direction.LEFT),6);
		assertEquals(roboTest.distanceToObstacle(Direction.RIGHT),1);
		assertEquals(roboTest.distanceToObstacle(Direction.BACKWARD),3);
		
		roboTest.rotate(Turn.RIGHT);
	
		assertEquals(roboTest.distanceToObstacle(Direction.FORWARD),1);
		assertEquals(roboTest.distanceToObstacle(Direction.LEFT),2);
		assertEquals(roboTest.distanceToObstacle(Direction.RIGHT),3);
		assertEquals(roboTest.distanceToObstacle(Direction.BACKWARD),6);
		
		controllerTearDown();
	}
	
	/**
	 * Following the above tests, we place the robot in the same location, but this time we turn it to around,
	 * and test to see if it can accurately tell the distance to all of the newly changed obstacles/WallBoards.
	 */
	@Test
	void testRoomFourWallBoardsAround() {
		x = 10;
		y = 6;
		
		controllerSetUp();

		assertEquals(roboTest.distanceToObstacle(Direction.FORWARD),2);
		assertEquals(roboTest.distanceToObstacle(Direction.LEFT),6);
		assertEquals(roboTest.distanceToObstacle(Direction.RIGHT),1);
		assertEquals(roboTest.distanceToObstacle(Direction.BACKWARD),3);
		
		roboTest.rotate(Turn.AROUND);
	
		assertEquals(roboTest.distanceToObstacle(Direction.FORWARD),3);
		assertEquals(roboTest.distanceToObstacle(Direction.LEFT),1);
		assertEquals(roboTest.distanceToObstacle(Direction.RIGHT),6);
		assertEquals(roboTest.distanceToObstacle(Direction.BACKWARD),2);
		
		controllerTearDown();
	}

	
	//////////////////////////////////Jump Tests/////////////////////////////////////
	/**
	 * Though our WallFollower and  Wizard will never ask for the robot to jump, we need
	 * to test to make sure that it can if asked. So we place the robot in its default
	 * location. We face it towards the left, facing a WallBoard, but most importantly
	 * a wall that doesn't make up an outside barrier, and tell it to jump, we then
	 * test that it is now in a different location, specifically on the other side of the 
	 * wall.
	 * @throws Exception if the jump is not possible
	 */
	@Test
	void testValidJump() throws Exception{
		look = Turn.LEFT;
		
		controllerSetUp();

		roboTest.jump();
		
		int[] currentPosition = roboTest.getCurrentPosition();

		assertEquals(currentPosition[0],4);
		assertEquals(currentPosition[1],1);
		
		controllerTearDown();
	}
	
	/**
	 * One of the places that we cannot jump is when we are facing a WallBoard that makes
	 * up the outside barrier. If we face a WallBoard that does and try to jump, it should
	 * do nothing.
	 * @throws Exception
	 */
	@Test
	void testInvalidJump() throws Exception{
		look = Turn.RIGHT;
		
		controllerSetUp();

		roboTest.jump();
		
		int[] currentPosition = roboTest.getCurrentPosition();

		//After jumping, we test to make sure it's still in the same location.
		assertEquals(currentPosition[0],4);
		assertEquals(currentPosition[1],0);
		
		controllerTearDown();
	}
	
	//////////////////////////////////Jump Tests/////////////////////////////////////
	/**
	 * Simply sanity test. We should be able to manually set the battery and then have the
	 * robot remember that that value is its current battery level.
	 */
	@Test
	void testSetBattery() {
		controllerSetUp();
		
		roboTest.setBatteryLevel(9001);
		
		assertEquals(roboTest.getBatteryLevel(),9001);
		
		controllerTearDown();
	}
	
	/**
	 * If we don't give it a specific value, then by default the battery should be set by the
	 * controller or driver to be 2000.
	 */
	@Test
	void testBattery(){
		controllerSetUp();

		assertEquals(roboTest.getBatteryLevel(),2000);
		
		controllerTearDown();
	}
	
	/**
	 * Testing to check that if we turn to the left, the battery is correctly reduced by 3.
	 */
	@Test
	void testBatteryLeft(){
		controllerSetUp();

		roboTest.rotate(Turn.LEFT);
		assertEquals(roboTest.getBatteryLevel(),1997);
		
		controllerTearDown();
	}
	
	/**
	 * Testing to check that if we turn to the right, the battery is correctly reduced by 3.
	 */
	@Test
	void testBatteryRight(){
		controllerSetUp();

		roboTest.rotate(Turn.RIGHT);
		assertEquals(roboTest.getBatteryLevel(),1997);
		
		controllerTearDown();
	}
	
	/**
	 * Testing to check that if we turn around, the battery is correctly reduced by 6.
	 */
	@Test
	void testBatteryAround(){
		controllerSetUp();

		roboTest.rotate(Turn.AROUND);
		assertEquals(roboTest.getBatteryLevel(),1994);
		
		controllerTearDown();
	}
	
	/**
	 * Testing to check that if we do a 360 degree turn, the battery is correctly reduced by 12.
	 */
	@Test
	void testBattery360(){
		controllerSetUp();

		roboTest.rotate(Turn.AROUND);
		roboTest.rotate(Turn.AROUND);
		assertEquals(roboTest.getBatteryLevel(),1988);
		
		controllerTearDown();
	}
	
	/**
	 * Testing to check that if we take a step forward, the battery is correctly reduced by 4.
	 */
	@Test
	void testBatteryStepForward(){
		controllerSetUp();

		roboTest.move(1,false);
		assertEquals(roboTest.getBatteryLevel(),1996);
		
		controllerTearDown();
	}
	
	 /**
	  * Testing to check that if we take two steps forward, the battery is correctly reduced by 8.
	  */
	@Test
	void testBatteryTwoStepsForward(){
		controllerSetUp();

		roboTest.move(2,false);
		assertEquals(roboTest.getBatteryLevel(),1992);
		
		controllerTearDown();
	}
	
	/**
	 * Testing to check that if we take a step forward, then turn around and step backward, the
	 * battery is reduced by 14. Note that we do not allow the robot to take a step backward.
	 */
	@Test
	void testBatteryStepForwardThenBack(){
		controllerSetUp();

		roboTest.move(1,false);
		roboTest.rotate(Turn.AROUND);
		roboTest.move(1,false);
		assertEquals(roboTest.getBatteryLevel(),1986);
		
		controllerTearDown();
	}
	
	//////////////////////////////////Jump Tests/////////////////////////////////////
	/**
	 * Sanity check, need to make sure that at the very beginning when nothing has happened,
	 * the odometer should return that it has stepped 0 spots.
	 */
	@Test
	void testOdometer() {
		controllerSetUp();
		
		assertEquals(roboTest.getOdometerReading(),0);
		
		controllerTearDown();
	}
	
	/**
	 * After taking one step, we test to make sure that it records that it has stepped one spot.
	 */
	@Test
	void testOdometerOneStep() {
		controllerSetUp();
		
		roboTest.move(1, false);
		assertEquals(roboTest.getOdometerReading(),1);
		
		controllerTearDown();
	}
	
	/**
	 * After taking one step, and then reseting the odometer, it should correctly display that it
	 * has taken no steps, even though it's position has changed.
	 * @throws Exception if getCurrentPosition fails
	 */
	@Test
	void testOdometerReset() throws Exception {
		controllerSetUp();
		
		roboTest.move(1, false);
		roboTest.resetOdometer();
		assertEquals(roboTest.getOdometerReading(),0);
		
		int[] currentPosition = roboTest.getCurrentPosition();
		assertEquals(currentPosition[0],5);
		assertEquals(currentPosition[1],0);
		
		controllerTearDown();
	}
	
	/**
	 * Odometer should not track the distance from the starting point, so we test that here. If it moves
	 * forward then we turn around and move it back to its original location, it should still show that 
	 * the robot has moved two spaces.
	 */
	@Test
	void testOdometerStepForwardThenBack() {
		controllerSetUp();
		
		roboTest.move(1, false);
		roboTest.rotate(Turn.AROUND);
		roboTest.move(1, false);
		assertEquals(roboTest.getOdometerReading(),2);
		
		controllerTearDown();
	}
}
