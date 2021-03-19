package gui;

import org.junit.jupiter.api.Test;

import generation.CardinalDirection;
import gui.Robot.Direction;
import gui.Robot.Turn;

import static org.junit.jupiter.api.Assertions.*;

/**
 * This class serves to test the WallFollower class, which implements the RobotDriver interface.
 * It tests whether the robot is working, and whether it can get to the end. It also tests 
 * interactions between the robot and the WallFollower, such as testing cases when both should terminate.
 * 
 * @author Connor Yu
 */
public class WallFollowerTest {
	//Objects that we use to test the WallFollower
	BasicRobot roboTest;
	ControllerStub fakeController;
	String file = "test/data/input.xml";
	
	WallFollower wallFlower; 
	
	//We only test a change in the battery level.
	float batteryLevel = 2000;
	
	/////////////////////////Private Helper Methods/////////////////////////
	
	/**
	 * Ran before every test. This sets up the controller, robot and WallFollower.
	 * It sets the battery level of the robot through the WallFollower and then starts
	 * the test.
	 */
	private void controllerSetUp() {
		fakeController = new ControllerStub();
		
		roboTest = new BasicRobot();
		wallFlower = new WallFollower(); 
		
		wallFlower.setRobot(roboTest); 
		fakeController.setRobotAndDriver(roboTest, wallFlower);
		
		//Overrides default battery level (2000)
		wallFlower.batteryLevel = batteryLevel;
		
		fakeController.switchFromTitleToGenerating(file); 
		
	}
	
	/**
	 * Ran after every test, it makes all of the objects null and returns
	 * the battery level back to what it is by default.
	 */
	private void controllerTearDown() {
		roboTest = null;
		wallFlower = null;
		fakeController = null;
		
		//Resets it back to 2000.
		batteryLevel = 2000;
	}

	//////////////////////////////////////////////////////////////////////////
	
	/**
	 * A rehashing of the BasicRobot test, when we simply test if the initial position is what it should be.
	 * @throws Exception through getCurrentPosition if it's invalid.
	 */
	@Test
	void testInitialPosition() throws Exception {
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
	 * By default, the maze that we pass to it is configured such that it does not get to the end.
	 * We then check if it was completed, and it should say that it was not.
	 * @throws Exception if drive 2 exit fails
	 */
	@Test
	void testWallFollowerFails() throws Exception {
		controllerSetUp();
		
		wallFlower.drive2Exit();
		/*
		int[] currentPosition = roboTest.getCurrentPosition();
		System.out.println("Final X: " + currentPosition[0] + " Final Y: " + currentPosition[1]);
		*/
		assertFalse(fakeController.completed);
		
		controllerTearDown();
	}
	
	/**
	 * Following the above test, we want to make sure that it is working and can get to the exit.
	 * It takes around 2350~ batteryLevel to get the robot to the exit in the maze, so we set
	 * the battery level to 3000 to be safe, and then we let it drive to the exit. We check if the
	 * maze was completed, and make sure that it was.
	 * @throws Exception if drive 2 exit fails
	 */
	@Test
	void testWallFollowerSucceeds() throws Exception {
		batteryLevel = 3000;
		controllerSetUp();
		
		wallFlower.drive2Exit();
		
		assertTrue(fakeController.completed);
		
		controllerTearDown();
	}
	
	/**
	 * This is a test of the interaction between the WallFollower and the BasicRobot. We call stop() on
	 * the robot, which changes a variable within the robot. We then let WallFollower drive to the exit,
	 * but first it checks the stopped variable. It shouldn't have gotten to the exit, and it should have
	 * tried to return to the title. This mimics the user letting the program run, and then hitting escape
	 * to return to the title, we're only interested in it trying to get to the title.
	 * @throws Exception if drive2exit does.
	 */
	@Test
	void testStopped() throws Exception {
		controllerSetUp();
		
		roboTest.stop();
		wallFlower.drive2Exit();
		
		assertFalse(wallFlower.exitReached);
		
		//This being true means that switchToTitle was called.
		assertTrue(fakeController.triedtoReturn);
		
		controllerTearDown();
	}
	
	/**
	 * In this test, we want to check a few things. We set the battery level to -1 and then try to drive
	 * it to the exit. It should immediately quit, then we check a few variables to make sure it's 
	 * implemented correctly.
	 * @throws Exception if drive2exit does.
	 */
	@Test
	void testBatteryLevelTooLow() throws Exception {
		batteryLevel = -1;
		controllerSetUp();
		
		wallFlower.drive2Exit();
		
		//This means it was not able to get to the exit.
		assertFalse(wallFlower.exitReached);
		
		//Though the battery was at -1, we changed it to represent 0, as 
		//having negative energy should not be possible for a battery.
		assertEquals(fakeController.battery,0);
		
		//We make sure that the controller knows that the robot didn't get
		//to the exit, and we didn't win the game.
		assertFalse(fakeController.winner);
		
		controllerTearDown();
	}
	
}
