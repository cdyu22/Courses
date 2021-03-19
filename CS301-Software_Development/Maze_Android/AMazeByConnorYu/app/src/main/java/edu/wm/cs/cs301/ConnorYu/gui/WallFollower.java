package edu.wm.cs.cs301.ConnorYu.gui;

import android.util.Log;

import edu.wm.cs.cs301.ConnorYu.generation.Distance;
import edu.wm.cs.cs301.ConnorYu.gui.Robot.Direction;
import edu.wm.cs.cs301.ConnorYu.gui.Robot.Turn;

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
 * <p>
 * The robot doesn't necessarily know about the WallFollower, it just knows that it's
 * getting orders from somewhere that it then sends to the controller to notify the
 * controller of what it's doing (which in turn notifies StatePlaying).
 * <p>
 * <p>
 * Achieves _ coverage
 * Collaborators: Robot (BasicRobot)
 *
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
        Log.v("WallFollwoer","Received command to move");
		if (robot.getBatteryLevel() <= 0)
			((BasicRobot) robot).setWinOrLoss(false);
		if (((BasicRobot) robot).mazeConnection.pause)
		    return true;
        boolean left, front, right;
        robot.getCurrentDirection();
        front = false;
        left = false;
        right = false;
        if (robot.distanceToObstacle(Direction.LEFT) == 0)
            left = true;
        if (robot.distanceToObstacle(Direction.FORWARD) == 0)
            front = true;
        if (robot.distanceToObstacle(Direction.RIGHT) == 0)
            right = true;

        if (!left)
            robot.rotate(Turn.LEFT);
        else if (front && !right)
            robot.rotate(Turn.RIGHT);
        else if (left && front && right)
            robot.rotate(Turn.AROUND);

        if (getEnergyConsumption() <= 0)
            return false;

        try {
            robot.move(1, false);
        } catch (Exception e) {
        }
        return exitReached;
    }
}
