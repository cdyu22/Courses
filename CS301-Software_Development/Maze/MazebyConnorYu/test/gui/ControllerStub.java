package gui;

import generation.CardinalDirection;
import generation.Maze;
import gui.Constants.UserInput;
import gui.Robot.Turn;

/**
 * This class serves solely for testing. Serving as a stand-in for the controller via inheritance,
 * it is utilized in our test classes. 
 * 
 * The biggest change is that we do not allow a panel. While it is possible to just turn off the 
 * graphics, this can also be accomplished by passing in null to all of the state change methods 
 * (switchFromXtoY). We do not allow StateTitle or StateWinning. Though there are variables we use 
 * to check to see if those methods that switch to those states are called.
 * 
 * @author Connor Yu
 */
public class ControllerStub extends Controller {

	//Tracks if any method tries to return the class to the title
	boolean triedtoReturn = false;
	
	//Tracks the completed robot variable, which is the WallFollower telling
	//the robot if it got to the end or not.
	boolean completed = false;
	
	//This variable is always set to true, as when it is, SimpleKeyListener
	//doesn't allow any user inputs, and we never want it during testing.
	boolean running = true;

	//Where we store our maze
	Maze mazeConfig;
	
	//Variables that affect our maze, the battery level and where it's facing.
	float batteryLevel = 2000;
	int xPlaced = 4; 
	int yPlaced = 0;
	Turn turning = null;
	
	//Only allow StateGenerating and StatePlaying.
	public ControllerStub() {
		states = new State[2];
		states[0] = new StateGenerating();
		states[1] = new StatePlaying();
	}

	//We'll be using this method in our testing, as we don't test
	//random mazes, we only test pre-generated mazes.
    public void switchFromTitleToGenerating(String filename) {
        currentState = states[0];
        currentState.setFileName(filename);
        currentState.start(this, null);
    }

    /*
     * Called at the end of the generating state. This had to be changed quite 
     * a bit to suit our testing purposes.
     */
    public void switchFromGeneratingToPlaying(Maze config) {
    	//Set the current position, if we don't change xPlaced and yPlaced, it should default to (4,0).
    	if (config.isValidPosition(xPlaced, yPlaced))
    		config.setStartingPosition(xPlaced, yPlaced);
    	
    	//Storing a reference to the Maze/MazeContainer
    	mazeConfig = config;
  
        currentState = states[1];
        currentState.setMazeConfiguration(config);
        currentState.start(this, null);
        
        //Setting up the robot.
        driver.setDimensions(config.getWidth(), config.getHeight());
        robot.setBatteryLevel(batteryLevel);
        robot.setMaze(this);
        
        //Getting the currentdirection and position
        robot.getCurrentDirection();
        try {
			robot.getCurrentPosition();
		} catch (Exception e) {
			e.printStackTrace();
		}
        
        //Turning if it is specified that it should
        if (turning != null)  
        	robot.rotate(turning);
        driver.setDistance(config.getMazedists());
    }

    //Storing whether the robot got to the end or not
    public void switchFromPlayingToWinning(int pathLength) {
    	if (((BasicRobot) robot).completed)
    		completed = true;
    	}
    
    //We don't allow any inputs to get through, but we need this method
    //for communication between the robot and StatePlaying through the controller.
    public boolean keyDown(UserInput key, int value) {
    	if (key == UserInput.ReturnToTitle) {
    		return true;
    	}
        return currentState.keyDown(key, value);
    }

    public Maze getMazeConfiguration() {
        return mazeConfig;
    }
    
    //Had to modify this, as we changed StatePlaying from states[2] to states[1]
    @Override
    public int[] getCurrentPosition() {
        return ((StatePlaying)states[1]).getCurrentPosition();
    }
    
    @Override
    public CardinalDirection getCurrentDirection() {
        return ((StatePlaying)states[1]).getCurrentDirection();
    }
    
    //If this is called, we make sure that we remember that it was called
    @Override
    public void switchToTitle() {
    	triedtoReturn = true;
    	}
}