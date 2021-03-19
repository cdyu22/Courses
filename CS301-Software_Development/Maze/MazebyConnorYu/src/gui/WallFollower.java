package gui;

import generation.Distance;
import gui.Robot.Direction;
import gui.Robot.Turn;

/**
 * This serves as the object that guides the robot towards the exit, though in this
 * case it does it in a very inefficient way. The RobotDriver asks the robot about 
 * its surroundings and its state, and based off of that tells it what to do. In this
 * case, it tells the robot to hug the left wall until it reaches the exit. It also 
 * checks the robot's battery level, and if it is below zero, it knows to terminate 
 * the program. It also has other checks to see if the program has terminated, and 
 * depending on that information, it can send data to the controller to modify its
 * current states. If the driver is running, then SimpleKeyListener is not allowed
 * to take any user inputs apart from returning to the title screen (ESC key). 
 * 
 * The robot doesn't necessarily know about the WallFollower, it just knows that it's
 * getting orders from somewhere that it then sends to the controller to notify the 
 * controller of what it's doing (which in turn notifies StatePlaying).
 * 
 * 
 * Achieves _ coverage
 * Collaborators: Robot (BasicRobot)
 * @author Connor Yu
 */
public class WallFollower implements RobotDriver {
	
	//The reference to the robot
	Robot robot;
	
	//The maze's height and width, stored with setDimensions which is run in the controller
	int mazeWidth;
	int mazeHeight;
	
	boolean exitReached;
	
	//Can be overwritten, but allows us to set a default batteryLevel.
	float batteryLevel = 2000;
	
	//Not used in this implementation
	Distance distanceMatrix;

	///////////////////////////Set Methods///////////////////////////
	@Override
	public void setRobot(Robot r) {
		//Gives the WallFollower a connection to the robot
		robot = r;
	}

	@Override
	public void setDimensions(int width, int height) {
		mazeWidth = width;
		mazeHeight = height;
	}
	
	@Override
	public void setDistance(Distance distance) {
		//Not used in WallFollower, but stores the distanceMatrix.
		distanceMatrix = distance;
	}
	
	///////////////////////////Get Methods///////////////////////////

	@Override
	public float getEnergyConsumption() {
		//Asks the robot what its battery level is
		return robot.getBatteryLevel();
	}

	@Override
	public int getPathLength() {
		//Asks the robot how far it has gone
		return robot.getOdometerReading();
	}


	///////////////////////////Drives Robot to Exit///////////////////////////
	
	//Called by controller to signal WallFollower to start working
	@Override
	public boolean drive2Exit() throws Exception {
		//Setting battery level
		robot.setBatteryLevel(batteryLevel); 
		
		//Boolean variables to keep track of surrounding WallBoards
		boolean left, front, right;
		
		//Will loop until one of the break conditions occurs
		while (!doneChecker()) {
			
			//Updates the direction that we're in
			robot.getCurrentDirection();
			
			//Initially set to false, meaning there are no WallBoards in that direction
			front = false;
			left = false;
			right = false;
			
			//We tell the robot to check its surroundings, and if there are WallBoards we update the variables
			if (robot.distanceToObstacle(Direction.LEFT) == 0)
				left = true;
			if (robot.distanceToObstacle(Direction.FORWARD) == 0)
				front = true;
			if (robot.distanceToObstacle(Direction.RIGHT) == 0)
				right = true; 

			//We tell the robot to rotate depending on its surroundings
			//If there is no left WallBoard it turns left
			if (!left) 
				robot.rotate(Turn.LEFT);
			//If there is a front WallBoard but no right WallBoard it turns right
			else if(front && !right)
				robot.rotate(Turn.RIGHT);
			//If it is surrounded by WallBoards it turns around
			else if (left && front && right)
				robot.rotate(Turn.AROUND);
			
			//Checks energy consumption, if it's less than 0 it doesn't move and continues the loop
			//for the checker to flag that it ran out of power
			if (getEnergyConsumption() <= 0)
				continue;
			
			/*
			 * If it has energy then it moves forward, should never run into a situation when it's facing a
			 * wall and tries to move. Surround in try/catch block so that if we move out of bounds, we continue
			 * at which point the checker flags that we're done.
			 */
			try {
			robot.move(1, false);
			} catch(Exception e) {
				continue;
			}
		}
		//This will have been changed to some value depending on how we exited the maze
		return exitReached;
	}
	
	
	/**
	 * Drive to Exit helper method, checks conditions that signify that the robot is done
	 * at the beginning of every loop. The three stop conditions all lead to use handling
	 * the program in different ways, so the method runs those necessary steps and returns 
	 * true. Meaning the driver stops moving and we switch the controller's state.
	 * @return true if the robot is done, false otherwise
	 */
	private boolean doneChecker() {
		
		/* Checks stopped, which is a variable the controller flips to true if the player hits escape.
		 * It flips the variable back to false, sets the controller back to the title screen, and 
		 * concludes that we were not able to finish, setting exitReached to false, meaning drive2exit
		 * returns false
		 */
		if (((BasicRobot) robot).stopped) {
			((BasicRobot) robot).stopped = false;
			((BasicRobot) robot).mazeConnection.switchToTitle();
			exitReached = false;
			return true;
		}
		
		/*
		 * Checks if the energy level is at or below 0. If it is, we set exitReached to false, as we didn't
		 * reach the exit, and we run setWinOrLoss, which gives the controller information that StateWinning will pull 
		 * from, telling it what to display, whether we win or lost and what the battery level looked like at the end, 
		 * and then we switch the controller to StateWinning,
		 */
		if (getEnergyConsumption() <= 0){
		  ((BasicRobot) robot).setWinOrLoss(false);
		  ((BasicRobot) robot).mazeConnection.switchFromPlayingToWinning(0);
		  exitReached = false;
		  return true;
		}
		
		/*
		 * At the start of every loop, we call getCurrentPosition, because it updates where we are in the maze.
		 * It changes completed to true if we're out of bounds, meaning we've won and exited the maze. If we
		 * catch that exception, we set exitReached to true, so drive2exit returns true, and we setWinOrLoss to 
		 * true, so drive2exit returns true and tells the robot to give information to the controller that 
		 * StateWinning will pull from, and then we switch the controller's state from playing to winning.
		 */
		try {
			robot.getCurrentPosition();
		} catch (Exception e) {
			e.printStackTrace();
		}
		if (((BasicRobot) robot).completed) {
			((BasicRobot) robot).setWinOrLoss(true);
			((BasicRobot) robot).mazeConnection.switchFromPlayingToWinning(0);
			((BasicRobot) robot).completed = false;
			exitReached = true;
			return true;
		}
		
		//If none of the checks are true, we return false
		return false;
	}
	
}
