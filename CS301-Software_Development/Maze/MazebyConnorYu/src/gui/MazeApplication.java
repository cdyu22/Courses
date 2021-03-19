/**
 * 
 */
package gui;

import generation.Order;

import java.awt.event.KeyListener;
import java.io.File;

import javax.swing.JFrame;


/**
 * This class is a wrapper class to startup the Maze game as a Java application
 * 
 * This code is refactored code from Maze.java by Paul Falstad, www.falstad.com, Copyright (C) 1998, all rights reserved
 * Paul Falstad granted permission to modify and use code for teaching purposes.
 * Refactored by Peter Kemper
 * 
 * TODO: use logger for output instead of Sys.out
 */
public class MazeApplication extends JFrame {

	// not used, just to make the compiler, static code checker happy
	private static final long serialVersionUID = 1L;

	/**
	 * Constructor
	 */
	public MazeApplication() {
		init(null);
	}

	/**
	 * Constructor that loads a maze from a given file or uses a particular method to generate a maze
	 * @param parameter can identify a generation method (Prim, Kruskal, Eller)
     * or a filename that stores an already generated maze that is then loaded, or can be null
	 */
	public MazeApplication(String[] parameter) {
		init(parameter);
	}

	/**
	 * Instantiates a controller with settings according to the given parameter.
	 * @param parameter can identify a generation method (Prim, Kruskal, Eller)
	 * or a filename that contains a generated maze that is then loaded,
	 * or can be null
	 * @return the newly instantiated and configured controller
	 */
	Controller createController(String[] parameter) {
		Controller result = new Controller() ;
		String parser;
		int i = 0;
		
		if (parameter == null) {
			System.out.println("No parameters detected, will generate default maze.");
			return result;
		}
		//Track which commands have been passed in
		boolean dRan = false;
		boolean gRan = false;
		boolean fRan = false;

		
		while (i < parameter.length) {
			parser = parameter[i];

			//Assume that if we detect a '-', the next item in the sequence is correct.
			if (parser.equals("-g")){
				gRan = true;
				i++;
				parser = parameter[i];
				
				//If a file has already been specified and it's valid, we don't let the program set a builder
				if (fRan) {
					System.out.println("Maze File already specified, cannot set builder");
					i++;
					continue;
				}
				
				if ("Prim".equalsIgnoreCase(parser)){
					System.out.println("MazeApplication: generating random maze with Prim's algorithm.");
					result.setBuilder(Order.Builder.Prim);
				}

				else if ("Kruskal".equalsIgnoreCase(parser)){
					System.out.println("MazeApplication: generating random maze with Kruskal's algorithm.");
					result.setBuilder(Order.Builder.Kruskal);
				}

				else if ("Eller".equalsIgnoreCase(parser)){
					throw new RuntimeException("Don't know anybody named Eller ...");
				}

				else
					System.out.println("MazeApplication: unknown parameter value: " + parameter + " ignored, operating in default mode.");
			}

			if (parser.contains("-d")){
				i++;
				dRan = true;
				parser = parameter[i];

				//At this point, initialize robot and driver, and set up all connections,
				//so connecting controller and robot, connecting driver to robot, and connecting
				//controller to robot.
				if ("WallFollower".equalsIgnoreCase(parser)){
					System.out.println("MazeApplication: initializing WallFollower robot.");
					BasicRobot robot1 = new BasicRobot();
					WallFollower robotDriver = new WallFollower();
					robotDriver.setRobot(robot1);
					result.setRobotAndDriver(robot1,robotDriver);
				}

				else if ("Wizard".equalsIgnoreCase(parser)){
					System.out.println("MazeApplication: initializing Wizard robot.");
					BasicRobot robot1 = new BasicRobot();
					Wizard robotDriver = new Wizard();
					robotDriver.setRobot(robot1);
					result.setRobotAndDriver(robot1,robotDriver);
				}
			}

			if (parser.contains("-f")){
				i++;
				parser = parameter[i];
				File f = new File(parser) ;
				if (f.exists() && f.canRead()){
					System.out.println("MazeApplication: loading maze from file: " + parameter);
					result.setFileName(parser);
					fRan = true;
					//If builder has been set, we set the builder to null and ignore it.
					//Only overwrites it if we can read the maze.
					if(gRan) {
						gRan = false;
						result.setBuilder(null);
						System.out.println("Builder ignored");
					}
				}
				else
					System.out.println("Cannot read file.");
			}
			i++;
		}
		if (!dRan)
			System.out.println("No driver algorithm chosen, player must navigate to exit.");
		if (!gRan && !fRan)
			System.out.println("No builder algorithm chosen, operating in default mode.");
		return result;
	}


	/**
	 * Initializes some internals and puts the game on display.
	 * @param parameter can identify a generation method (Prim, Kruskal, Eller)
     * or a filename that contains a generated maze that is then loaded, or can be null
	 */
	private void init(String[] parameter) {
	    // instantiate a game controller and add it to the JFrame
	    Controller controller = createController(parameter);
		add(controller.getPanel()) ;
		// instantiate a key listener that feeds keyboard input into the controller
		// and add it to the JFrame
		KeyListener kl = new SimpleKeyListener(this, controller) ;
		addKeyListener(kl) ;
		// set the frame to a fixed size for its width and height and put it on display
		setSize(Constants.VIEW_WIDTH, Constants.VIEW_HEIGHT+22) ;
		setVisible(true) ;
		// focus should be on the JFrame of the MazeApplication and not on the maze panel
		// such that the SimpleKeyListener kl is used
		setFocusable(true) ;
		// start the game, hand over control to the game controller
		controller.start();
	}
	
	/**
	 * Main method to launch Maze game as a java application.
	 * The application can be operated in three ways. 
	 * 1) The intended normal operation is to provide no parameters
	 * and the maze will be generated by a randomized DFS algorithm (default). 
	 * 2) If a filename is given that contains a maze stored in xml format. 
	 * The maze will be loaded from that file. 
	 * This option is useful during development to test with a particular maze.
	 * 3) A predefined constant string is given to select a maze
	 * generation algorithm, currently supported is "Prim".
	 * @param args is optional, first string can be a fixed constant like Prim or
	 * the name of a file that stores a maze in XML format
	 */
	public static void main(String[] args) {
	    JFrame app = null ; 
	    if (0 < args.length) {
	    	app = new MazeApplication(args);
	    }
		if (args.length == 0)
			app = new MazeApplication() ;
		app.repaint() ;
	}

}
