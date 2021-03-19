package gui;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

import generation.Distance;

/**
 * This class serves to test the Wizard class, which implements the RobotDriver interface.
 * It tests whether the robot is working, and whether it can get to the end. 
 * 
 * @author Connor Yu
 */
public class WizardTest {
	//Objects that we use to test the Wizard
	BasicRobot roboTest;
	ControllerStub fakeController;
	String file = "test/data/input.xml";
	
	Wizard wizard; 
	
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
		wizard = new Wizard(); 
		
		wizard.setRobot(roboTest); 
		fakeController.setRobotAndDriver(roboTest, wizard);
		
		//Overrides default battery level if told to (2000)
		wizard.batteryLevel = batteryLevel;
		
		fakeController.switchFromTitleToGenerating(file); 
		
	}
	
	/**
	 * Ran after every test, it makes all of the objects null and returns
	 * the battery level back to what it is by default.
	 */
	private void controllerTearDown() {
		roboTest = null;
		wizard = null;
		fakeController = null;
		
		//Resets it back to 2000.
		batteryLevel = 2000;
	}
	
	////////////////////////////////////////////////////////////////////////////
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
	 * When utilizing the wizard, it should be able to get to the exit after using 1400 power, so in
	 * this test we set it to 1000, and it should fail.
	 * @throws Exception if drive 2 exit fails
	 */
	@Test
	void testWizardFails() throws Exception {
		batteryLevel = 1000;
		
		controllerSetUp();
		
		wizard.drive2Exit();

		assertFalse(fakeController.completed);
		
		controllerTearDown();
	}
	
	/**
	 * Following the above test, we want to make sure that it is working and can get to the exit.
	 * It takes around 1400~ batteryLevel to get the robot to the exit in the maze, so we set
	 * the battery level to 2000 to be safe, and then we let it drive to the exit. We check if the
	 * maze was completed, and make sure that it was.
	 * @throws Exception
	 */
	@Test
	void testWizardSucceeds() throws Exception {
		controllerSetUp();
		
		wizard.drive2Exit();
		
		assertTrue(fakeController.completed);
		
		controllerTearDown();
	}
	
	/**
	 * Very important test for the wizard. It looks at the distance matrix to see how far away
	 * the initial position is from the exit. Then, after driving to the exit it asks the robot
	 * how far it's walked (counting with the odometer). They should be the same, signifying that 
	 * it took the most optimal route (or one of the most optimal routes, as there are multiple
	 * when there are rooms).
	 * @throws Exception
	 */
	@Test
	void testWizardSteps() throws Exception {
		controllerSetUp();
		
		Distance distMatrix;
		distMatrix = fakeController.mazeConfig.getMazedists();
		
		int initialDistancetoExit = distMatrix.getDistanceValue(4, 0);
		
		wizard.drive2Exit();
		
		int distanceTraveled = wizard.getPathLength();
		
		assertEquals(initialDistancetoExit, distanceTraveled);
		
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
		
		wizard.drive2Exit();
		
		//This means it was not able to get to the exit.
		assertFalse(wizard.exitReached);
		
		//Though the battery was at -1, we changed it to represent 0, as 
		//having negative energy should not be possible for a battery.
		assertEquals(fakeController.battery,0);
		
		//We make sure that the controller knows that the robot didn't get
		//to the exit, and we didn't win the game.
		assertFalse(fakeController.winner);
		
		controllerTearDown();
	}
	
	/**
	 * This is a test of the interaction between the wizard and the BasicRobot. We call stop() on
	 * the robot, which changes a variable within the robot. We then let wizard drive to the exit,
	 * but first it checks the stopped variable. It shouldn't have gotten to the exit, and it should have
	 * tried to return to the title. This mimics the user letting the program run, and then hitting escape
	 * to return to the title, we're only interested in it trying to get to the title.
	 * @throws Exception if drive2exit does.
	 */
	@Test
	void testStopped() throws Exception {
		controllerSetUp();
		
		roboTest.stop();
		wizard.drive2Exit();
		
		assertFalse(wizard.exitReached);
		
		//This being true means that switchToTitle was called.
		assertTrue(fakeController.triedtoReturn);
		
		controllerTearDown();
	}
}
