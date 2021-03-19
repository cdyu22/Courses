package edu.wm.cs.cs301.ConnorYu.gui;

import android.util.Log;

import edu.wm.cs.cs301.ConnorYu.generation.Distance;
import edu.wm.cs.cs301.ConnorYu.gui.Robot.Direction;
import edu.wm.cs.cs301.ConnorYu.gui.Robot.Turn;

/**
 * This serves as another implementation of the RobotDriver interface. Instead of just
 * sticking to the left wall, the wizard checks the robots surrounding, and as it has
 * access to the distance matrix, it's able to tell the robot where to go based on
 * which of the spots have a lower value in the distance matrix. This is much more
 * efficient than WallFollower, but mainly because it knows exactly where to go. It
 * has a lot of the same functionality as WallFollower, but there are a few changes to
 * ensure that it drives correctly and looks towards the exit when it's at the cell
 * that is the exit point.
 * <p>
 * Collaborators: Robot (BasicRobot)
 *
 * @author Connor Yu
 */
public class Wizard implements RobotDriver {

    //The reference to the robot
    Robot robot;

    //The maze's height and width, stored with setDimensions which is run in the controller
    int mazeWidth;
    int mazeHeight;

    //Can be overwritten, but allows us to set a default batteryLevel.
    float batteryLevel = 2000;

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

    @Override
    public boolean drive2Exit() throws Exception {
        Log.v("BasicRobot","Received command to move");
        if (robot.getBatteryLevel() <= 0)
             ((BasicRobot) robot).setWinOrLoss(false);
        Direction step = null;

        //These are true if there's a wall in that direction
        boolean left, right, front, back;

        int lowest = 100000;//Maximum possible total nodes is 72,000 at level 15

        robot.getCurrentPosition();
        robot.getCurrentDirection();

        //Initially set to assume there is no wall
        front = false;
        left = false;
        right = false;
        back = false;

        //If a wall is detected we set it to true
        if (robot.distanceToObstacle(Direction.LEFT) == 0)
            left = true;
        if (robot.distanceToObstacle(Direction.FORWARD) == 0)
            front = true;
        if (robot.distanceToObstacle(Direction.RIGHT) == 0)
            right = true;
        if (robot.distanceToObstacle(Direction.BACKWARD) == 0)
            back = true;

        //Initialize a 2-cell array to hold x and y coordinates for the spot we're checking
        int[] spot = new int[2];

        //ONLY DO ANY OF THESE IF THERE ISN'T A WALL IN THAT DIRECTION
        if (!front) {
            spot[0] = ((BasicRobot) robot).getSpot(Direction.FORWARD)[0];
            spot[1] = ((BasicRobot) robot).getSpot(Direction.FORWARD)[1];
            //If it's a valid spot, and the distance of that spot is lower than the current lowest value, we
            //reassign lowest and set step (which is the direction we'll step, to left, do the same for all directions.
            if (((BasicRobot) robot).mazeConnection.maze.isValidPosition(spot[0], spot[1]) &&
                    distanceMatrix.getDistanceValue(spot[0], spot[1]) < lowest) {
                lowest = distanceMatrix.getDistanceValue(spot[0], spot[1]);
                step = Direction.FORWARD;
            }
        }
        if (!back) {
            spot[0] = ((BasicRobot) robot).getSpot(Direction.BACKWARD)[0];
            spot[1] = ((BasicRobot) robot).getSpot(Direction.BACKWARD)[1];
            if (((BasicRobot) robot).mazeConnection.maze.isValidPosition(spot[0], spot[1]) &&
                    distanceMatrix.getDistanceValue(spot[0], spot[1]) < lowest) {
                lowest = distanceMatrix.getDistanceValue(spot[0], spot[1]);
                step = Direction.BACKWARD;
            }
        }
        if (!left) {
            spot[0] = ((BasicRobot) robot).getSpot(Direction.LEFT)[0];
            spot[1] = ((BasicRobot) robot).getSpot(Direction.LEFT)[1];
            if (((BasicRobot) robot).mazeConnection.maze.isValidPosition(spot[0], spot[1]) &&
                    distanceMatrix.getDistanceValue(spot[0], spot[1]) < lowest) {
                lowest = distanceMatrix.getDistanceValue(spot[0], spot[1]);
                step = Direction.LEFT;
            }
        }
        if (!right) {
            spot[0] = ((BasicRobot) robot).getSpot(Direction.RIGHT)[0];
            spot[1] = ((BasicRobot) robot).getSpot(Direction.RIGHT)[1];
            if (((BasicRobot) robot).mazeConnection.maze.isValidPosition(spot[0], spot[1]) &&
                    distanceMatrix.getDistanceValue(spot[0], spot[1]) < lowest) {
                lowest = distanceMatrix.getDistanceValue(spot[0], spot[1]);
                step = Direction.RIGHT;
            }
        }

		if (robot.isAtExit()) {
			//If there isn't a wall to the left, and the spot gives an x index of -10, we know that's the way
			//to the exit.
			if (0 < robot.distanceToObstacle(Direction.LEFT) &&
					((BasicRobot) robot).getSpot(Direction.LEFT)[0] == -10) {
				robot.rotate(Turn.LEFT);
			}
			//If there isn't a wall to the right, and the spot gives an x index of -10, we know that's the way
			//to the exit.
			else if (0 < robot.distanceToObstacle(Direction.RIGHT) &&
					((BasicRobot) robot).getSpot(Direction.RIGHT)[0] == -10) {
				robot.rotate(Turn.RIGHT);
			}
			robot.move(1, false);

			((BasicRobot) robot).setWinOrLoss(true);
			((BasicRobot) robot).completed = false;
			return true;
		}

        //Depending on what step was set to, we rotated
        if (step == Direction.LEFT)
            robot.rotate(Turn.LEFT);

        else if (step == Direction.RIGHT)
            robot.rotate(Turn.RIGHT);

        else if (step == Direction.FORWARD) {
        } else if (step == Direction.BACKWARD)
            robot.rotate(Turn.AROUND);


        //If it has energy then it moves forward, should never run into a situation when it's facing a
        //wall and tries to move. Surround in try/catch block so that if we move out of bounds, we continue
        //at which point the checker flags that we're done.
        try {
            robot.move(1, false);
        } catch (Exception e) {
            //continue;
        }

        return true;
    }
}
