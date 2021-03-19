package edu.wm.cs.cs301.ConnorYu.gui;

import edu.wm.cs.cs301.ConnorYu.generation.CardinalDirection;
import edu.wm.cs.cs301.ConnorYu.generation.Floorplan;
import edu.wm.cs.cs301.ConnorYu.gui.Constants.UserInput;

/**
 * This is the BasicRobot that implements the robot interface. It has a connection
 * to the controller and the RobotDriver has a connection to it. The robot is able to
 * look at its surroundings by storing and checking the FloorPlan through its controller
 * connection. Then, the RobotDriver tells it what to do based off of that information.
 * It then does as it was commanded by telling the controller what it is doing, with the
 * controller passing along that information to StatePlaying (or StateWinning, if the
 * RobotDriver terminates for a variety of reasons). It also stores a variety of information,
 * such as its current position and which direction it's looking at, as well as how far
 * it has walked, and how much battery it has left.
 *
 * The robot serves as the way the RobotDriver interacts with the maze, moving around
 * and telling the RobotDriver what its surroundings look like, and the RobotDriver acts
 * based off of that information. Serves as the connecting point between the RobotDriver
 * and Controller. The Controller then serves as the connecter between the robot,
 * MazeApplication, and the various States (StatePlaying, StateWinning, etc.)
 *
 * Note: the BasicRobot is using FloorPlan, but it's not listed as a collaborator
 * because it's not changing anything in the FloorPlan, it's simply reading its data.
 *
 * Collaborators: Controller and RobotDriver(WallFollower or Wizard)
 * @author Connor Yu
 */
public class BasicRobot implements Robot {
	Floorplan layout;
	StatePlaying mazeConnection;

	//Storing position and direction.
	int[] currentSpace = new int[2];
	CardinalDirection currentDirection;

	int odometer = 0;
	float battery;

	//Controller sets this to true if it wants driver to stop.
	boolean stopped = false;

	boolean completed = false;

	@Override
	public void setMaze(StatePlaying controller) {
		//Not only sets a connection between the robot and controller, but stores the floorplan.
		layout = controller.getMazeConfiguration().getFloorplan();
		mazeConnection = controller;
	}


	///////////////////////////////////////////Private Helper Methods///////////////////////////////////////////
	/**
	 * The controller will call this if the driver is running and the player hits escape, returning the controller
	 * to the title. It starts with disallowing key presses if the controller has a driver that's running. The only
	 * exception is if the player hits escape, in which case, the controller signals the robot to run stop(). The
	 * driver checks to see if stopped is true, and if it is, it sets it back to false and exits the drive2exit
	 * method, and tells the controller to return to the title.
	 */
	public void stop() {
		stopped = true;
	}

	/**
	 * This is called by the driver on the robot. It says whether the robot reached the end or not. If it does, it
	 * changes controller tracker variables that StateWinning uses, both to display if the robot won or not, and also
	 * what the ending battery level was.
	 * @param win Whether the robot reached the end or not.
	 */
	public void setWinOrLoss(boolean win) {
		if (win)
			mazeConnection.winner = true;
		else
			mazeConnection.winner = false;

		if (battery < 0) //If it loses, makes sure we can't have negative battery.
			battery = 0;
		mazeConnection.battery = (int) battery;
		mazeConnection.pathLength = getOdometerReading();
	}

	/**
	 * This method exists solely to help support the wizard's operations. The wizard calls this method
	 * to get the x and y coordinates on the FloorPlan to spots that are adjacent to the robot using
	 * its relative directions. It only calls this if the robot checks that there are no walls surrounding
	 * it, this point is important, because it lets the wizard know which way to turn once we get to the exit.
	 * @param direction The direction of the spot that we want to get
	 * @return The x and y coordinates in a 2-cell array x coordinate being in 0, y in 1. returns [-10, -10]
	 * if it is an invalid spot, which signals that that is the way to the exit, as the only time it would be
	 * an invalid spot is if there's no wall leading to an invalid spot.
	 */
	public int[] getSpot(Direction direction) {
		//Set up the array we'll usually return.
		int[] positionTracker = new int[2];
		positionTracker[0] = currentSpace[0];
		positionTracker[1] = currentSpace[1];

		//Convert the direction to a cardinal direction.
		CardinalDirection look;
		look = currentDirection;
		if (direction == Direction.BACKWARD)
			look = look.oppositeDirection();
		if (direction == Direction.LEFT)
			look = look.rotateClockwise();
		if (direction == Direction.RIGHT)
			look = look.rotateClockwise().rotateClockwise().rotateClockwise();

		//Based off of the cardinal direction we increment or decrement either the x or y coordinate
		if(mazeConnection.getMazeConfiguration().isValidPosition(positionTracker[0], positionTracker[1])) {
			if (look == CardinalDirection.North)
				positionTracker[1]--;

			if (look == CardinalDirection.South)
				positionTracker[1]++;

			if (look == CardinalDirection.West)
				positionTracker[0]--;

			if (look == CardinalDirection.East)
				positionTracker[0]++;
		}

		/*
		 * If the position that we're checking is not a valid position, which is only possible if we call
		 * that doesn't have a wall leading to an invalid position (only the exit) then we return an
		 * array of value [-10,-10]. The checker that sees if we're done looks specifically for an array
		 * of that type and then rotates in the direction that leads to [-10, -10] and moves forward, to
		 * simulate leaving the maze.
		 */
		if(!mazeConnection.getMazeConfiguration().isValidPosition(positionTracker[0], positionTracker[1])) {
			int[] exit = new int[2];
			exit[0] = -10;
			exit[1] = -10;
			return exit;
		}

		//In most cases, however, we just return the array with coordinates that we incremented/decremented.
		return positionTracker;

	}

	//////////////////////////Position tracking methods//////////////////////////

	@Override
	public int[] getCurrentPosition() throws Exception {
		//Uses controller to get current position from state playing and store it.
		currentSpace = mazeConnection.getCurrentPosition();

		//If it's out of bounds either in the x or y position, it's complete, so set completed to true.
		if (currentSpace[0] < 0 || mazeConnection.getMazeConfiguration().getWidth() <= currentSpace[0] ||
			currentSpace[1] < 0 || mazeConnection.getMazeConfiguration().getHeight() <= currentSpace[1]) {
			completed = true;
			throw new Exception();
		}


		return currentSpace;
	}

	@Override
	public CardinalDirection getCurrentDirection() {
		//Stores current direction
		currentDirection = mazeConnection.getCurrentDirection();
		return currentDirection;
	}

	@Override
	public boolean isAtExit() {
		//Checks current position in FloorPlan to see if it's at the exit.
		if (layout.isExitPosition(currentSpace[0], currentSpace[1]))
			return true;
		return false;
	}

	//////////////////////////General Running method algorithms//////////////////////////
	@Override
	public boolean canSeeThroughTheExitIntoEternity(Direction direction) throws UnsupportedOperationException {
		//Never throws exception, as specified by instructor. Always has sensor.

		//Create a variable that can check what's happening at a given position
		int[] positionTracker = new int[2];
		positionTracker[0] = currentSpace[0];
		positionTracker[1] = currentSpace[1];

		//Converting currentDirection to the direction we're looking in
		CardinalDirection look;
		look = currentDirection;
		if (direction == Direction.BACKWARD)
			look = look.oppositeDirection();
		if (direction == Direction.LEFT)
			look = look.rotateClockwise();
		if (direction == Direction.RIGHT)
			look = look.rotateClockwise().rotateClockwise().rotateClockwise();

		battery--;//BATTERY

		//If we're at the exit position then everywhere we look should lead to the exit position
		if(layout.isExitPosition(positionTracker[0], positionTracker[1]))
			return true;

		if(layout.hasNoWall(positionTracker[0], positionTracker[1], CardinalDirection.East))
			System.out.println("wall");

		//If the spot we're looking at is a valid position and isn't blocked by a wall, we keep on looking until
		//we run into a wall, or if the spot we're looking at is the exit position.
		while (mazeConnection.getMazeConfiguration().isValidPosition(positionTracker[0], positionTracker[1]) &&
			layout.hasNoWall(positionTracker[0], positionTracker[1], look)) {
			System.out.println("X Variable: " + positionTracker[0] + ", Y Variable: " + positionTracker[1]);

			if (look == CardinalDirection.North)
				positionTracker[1]--;

			if (look == CardinalDirection.South)
				positionTracker[1]++;

			if (look == CardinalDirection.West)
				positionTracker[0]--;

			if (look == CardinalDirection.East)
				positionTracker[0]++;

			if(layout.isExitPosition(positionTracker[0], positionTracker[1]))
				return true;
		}
		return false;
	}

	@Override
	public boolean isInsideRoom() throws UnsupportedOperationException {
		//Never throws exception, as specified by instructor. Always has sensor.

		//Can easily check if the robot is inside a room by comparing the current spot to the FloorPlan
		if (layout.isInRoom(currentSpace[0], currentSpace[1]))
			return true;
		return false;
	}

	@Override
	public boolean hasStopped() {
		//With out algorithm, we turn if we're facing a wall, so we should never have a wall in front of us when we move forward
		if (layout.hasWall(currentSpace[0], currentSpace[1], currentDirection))
			return true;

		//If the battery level is less than 0, the robot has to have stopped
		if (battery <= 0)
			return true;
		return false;
	}

	@Override
	public int distanceToObstacle(Direction direction) throws UnsupportedOperationException {
		//Never throws exception, as specified by instructor. Always has sensor.

		//Create a counter that keeps track of open spaces
		int distanceCounter = 0;

		//Create an integer array that can test a spot to see if there's a wall
		int[] positionTracker = new int[2];
		positionTracker[0] = currentSpace[0];
		positionTracker[1] = currentSpace[1];

		//Create a variable that we can use to track where we're looking by combining currentDirection and
		//the direction we're told to look in
		CardinalDirection look;
		look = currentDirection;
		if (direction == Direction.BACKWARD)
			look = look.oppositeDirection();
		if (direction == Direction.LEFT)
			look = look.rotateClockwise();
		if (direction == Direction.RIGHT)
			look = look.rotateClockwise().rotateClockwise().rotateClockwise();

		//While we're looking at a valid spot, and that spot isn't blocked by a wall, move the variable that's
		//checking the spaces further in the direction that we're looking towards.
		while (mazeConnection.getMazeConfiguration().isValidPosition(positionTracker[0], positionTracker[1]) &&
			layout.hasNoWall(positionTracker[0], positionTracker[1], look)) {

			distanceCounter++;
			if (look == CardinalDirection.North)
				positionTracker[1]--;

			if (look == CardinalDirection.South)
				positionTracker[1]++;

			if (look == CardinalDirection.West)
				positionTracker[0]--;

			if (look == CardinalDirection.East)
				positionTracker[0]++;
		}
		battery--;//BATTERY
		return distanceCounter;
	}


	///////////////////////////////Movement Methods///////////////////////////////

	@Override
	public void rotate(Turn turn) {
		if (turn == Turn.LEFT) {
			//Subtracts from battery level
			if (battery < getEnergyForFullRotation()/4)
				return;
			battery = battery - (getEnergyForFullRotation()/4);//BATTERY
			//Then tells the controller to tell StatePlaying to turn left
			mazeConnection.keyDown(UserInput.Left, 0);
		}
		else if (turn == Turn.RIGHT) {
			if (battery < getEnergyForFullRotation()/4)
				return;
			battery = battery - (getEnergyForFullRotation()/4);//BATTERY
			mazeConnection.keyDown(UserInput.Right, 0);
		}
		else if (turn == Turn.AROUND) {
			//Requires twice as much energy to turn around
			if (battery < getEnergyForFullRotation()/2)
				return;
			battery = battery - (getEnergyForFullRotation()/2);//BATTERY
			//Can substitute turning around with two right turns
			mazeConnection.keyDown(UserInput.Right, 0);
			mazeConnection.keyDown(UserInput.Right, 0);
		}
		//Updates current direction so we know where we're facing.
		getCurrentDirection();
	}

	@Override
	public void move(int distance, boolean manual) {
		while (0 < distance) {
			//Doesn't allow us to move forward if hasStopped returns true
			if (hasStopped())
				break;
			battery = battery - (getEnergyForStepForward());//BATTERY
			mazeConnection.keyDown(UserInput.Up, 0);
			odometer++;
			distance--;
		}
		//After the move, we get the current position we're in to keep track of where we are
		try {
			getCurrentPosition();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	@Override
	public void jump() throws Exception {
		try{
			//We try jumping, throwing an exception if it fails, then update where we are with current position.
			mazeConnection.keyDown(UserInput.Jump, 0);
			odometer++;
			battery = battery - (getEnergyForStepForward());//BATTERY
			getCurrentPosition();
		} catch(Exception e){
			throw new Exception();
		}
	}

	//////////////////////////////// BATTERY////////////////////////////////
	@Override
	public void setBatteryLevel(float level) {
		battery = level;
	}

	@Override
	public float getBatteryLevel() {
		//In this implementation, robot keeps track of its battery level
		return battery;
	}

	@Override
	public float getEnergyForStepForward() {
		return 4;
	}

	@Override
	public float getEnergyForFullRotation() {
		return 12;
	}

	///////////////////////////////////ODOMETER////////////////////////////
	@Override
	public int getOdometerReading() {
		return odometer;
	}

	@Override
	public void resetOdometer() {
		odometer = 0;
	}

	///////////////////////////////Sensor Methods///////////////////////////////
	@Override
	public boolean hasRoomSensor() {
		return true;
	}

	@Override
	public boolean hasOperationalSensor(Direction direction) {
		return true;
	}
}
