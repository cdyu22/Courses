package edu.wm.cs.cs301.ConnorYu.gui;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ProgressBar;
import android.widget.TextView;

import com.example.amazebyconnoryu.R;

import edu.wm.cs.cs301.ConnorYu.generation.Maze;


/**
 * One of the two options that GeneratingActivity can call. This activity/java class is called
 * if the user signals that they want a robot, either WallFollower or Wizard, to navigate to the
 * exit of the maze. It mainly consists of buttons that toggle different things to show up on screen
 */
public class PlayAnimationActivity extends Activity {
    //Buttons that handle the toggling of different displays on screen
    Button fullMaze, solution, wallToggle;

    //The robot and driver that will navigate to the exit
    Robot robot1;
    RobotDriver robotDriver;

    //Fields that track the internal status of the activity.
    /*
    The driver string will track which driver algorithm the user picked, either WallFollower or
    Wizard. The win boolean tracks whether the user won or not, changing to false if the user
    loses. It will only ever be switched to false if the robot runs out of energy and can no longer
    move due to having no battery left.
     */
    boolean winner = true;
    String driver;

    /*
    pathLength tracks how many steps the robot has taken, and battery tracks how much energy
    the robot has left. In project 5, the progressBar energyLeft will reflect how much energy
    has been used.
     */
    int pathLength = 0;
    int battery = 2000;
    ProgressBar energyLeft;
    TextView pathTracker, energyTracker;

    /*
   A boolean pause tracks whether the user wants the robot paused or playing. It starts false, as
   the robot starts walking to the exit. The button togglePause, when selected, changes the pause
   boolean to true, and if it's true it changes to false. Depending on the state, it also changes
   the background of the button.
    */
    Button togglePause;
    Boolean pause = false;

    //The maze reference, the MazePanel that we will draw on, and the reference to StatePlaying,
    //which will allow us to play the game
    public static Maze maze = null;
    MazePanel mazePanel;
    StatePlaying statePlay;

    //The thread that will be used to drive to the exit
    Thread Driving = null;

    /**
     * The first method that is called when the activity is created. It sets up the screen, changing
     * what is happening on the android screen. For this class, it sets up and connects buttons that
     * toggle different things to show up on screen, as well as their respective listeners. For now,
     * the listeners just call a Log.v message and create a toast message, with the exception of the
     * temporary winning button, which moves the activity to the FinishActivity.
     * @param savedInstanceState A bundle object passed into the onCreate method that can carry
     *                           some data.
     */
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.play_animation_layout);

        //Getting the driver that was packed into the algorithm, lets us know to either use
        //the WallFollower or Wizard algorithm.
        driver = getIntent().getExtras().getString(getString(R.string.driverKey));

        Log.v(getString(R.string.TAGACT4),"RECEIVED COMMAND TO RETRIEVE STORED MAZE");
        //Retrieving the maze from MazeHolder
        maze = MazeHolder.getData();

        //Link up the MazePanel in PlayManuallyActivity to the mazepanel reference
        mazePanel = findViewById(R.id.panel);

        //Create a new stateplaying that we use to play the game
        statePlay = new StatePlaying();

        //Setting up the references
        statePlay.setMazeConfiguration(maze);
        statePlay.controlAnimation = this;

        //Start the game
        statePlay.start(mazePanel);

        //Create the robot and driver, set up the references so robot points to this, driver points
        //to robot
        robot1 = new BasicRobot();
        //Creates the driver depending on the driver string that was passed in
        if (driver.equals("WallFollower"))
            robotDriver = new WallFollower();
        else if (driver.equals("Wizard"))
            robotDriver = new Wizard();
        robotDriver.setRobot(robot1);
        robotDriver.setDistance(maze.getMazedists());//Setting up distance matrix for wizard
        robotDriver.setDimensions(maze.getWidth(), maze.getHeight());
        robot1.setMaze(this);

        //***********************************Handling TextViews*************************************
        //they will be updated to show the increase in path length and the decrease
        //in the robot's energy.
        pathTracker = findViewById(R.id.pathTracker);
        pathTracker.setText(getString(R.string.pathLength) + pathLength);

        energyTracker = findViewById(R.id.energyTracker);
        energyTracker.setText(getString(R.string.energyLeft) + battery);


        //***********************************Handling ProgressBar***********************************
        energyLeft = findViewById(R.id.energyRemaining);
        //Sets up the reference to the progressbar, will match with the battery's level
        energyLeft.setMax(2000);

        //************************************Handling Buttons**************************************
        togglePause = findViewById(R.id.pauseButton);
        togglePause.setOnClickListener(new View.OnClickListener() {
            /**
             * This allows us to do some action whenever we click this button
             * @param view
             */
            public void onClick(View view) {
                //If pause is detected to be true, the game is paused, and the user is signaling
                //they want it to resume. So we set pause to false and change the background of
                //the button.
                if (pause) {
                    pause = false;
                    togglePause.setBackground(getDrawable(R.drawable.resume));
                    Log.v(getString(R.string.TAGACT4),
                            "RECEIVED COMMAND TO RESUME ROBOT DRIVER");
                }
                //If pause is false, the game is playing and the user wants it to pause. So we
                //set pause to true and change the background of the button.
                else {
                    pause = true;
                    togglePause.setBackground(getDrawable(R.drawable.pause));
                    Log.v(getString(R.string.TAGACT4),
                            "RECEIVED COMMAND TO PAUSE ROBOT DRIVER");
                }
            }
        });

        //Call to display the maze
        fullMaze = findViewById(R.id.fullMaze);
        fullMaze.setOnClickListener(new View.OnClickListener() {
            /**
             * This allows us to do some action whenever we click this button
             * @param view
             */
            public void onClick(View view) {
                Log.v(getString(R.string.TAGACT4), "RECEIVED COMMAND TO SHOW THE FULL MAZE");
                statePlay.keyDown(Constants.UserInput.ToggleFullMap, 0);
            }
        });

        //Call to display the solution
        solution = findViewById(R.id.solution);
        solution.setOnClickListener(new View.OnClickListener() {
            /**
             * This allows us to do some action whenever we click this button
             * @param view
             */
            public void onClick(View view) {
                Log.v(getString(R.string.TAGACT4), "RECEIVED COMMAND TO SHOW THE MAZE SOLUTION");
                statePlay.keyDown(Constants.UserInput.ToggleSolution, 0);
            }
        });

        //Call to toggle the display of the walls
        wallToggle = findViewById(R.id.toggleWalls);
        wallToggle.setOnClickListener(new View.OnClickListener() {
            /**
             * This allows us to do some action whenever we click this button
             * @param view
             */
            public void onClick(View view) {
                Log.v(getString(R.string.TAGACT4), "RECEIVED COMMAND TO TOGGLE WALLS");
                statePlay.keyDown(Constants.UserInput.ToggleLocalMap, 0);
            }
        });

        //The handler that will delay the thread after every step
        final Handler handler = new Handler();
        //Set the battery level to be 2000
        robot1.setBatteryLevel(2000);
        //Create the driving thread
        Driving = new Thread(new Runnable() {
            /**
             * What we call when we want the thread to run
             */
            public void run() {
                try {
                        robotDriver.drive2Exit();//Take a step
                        handler.postDelayed(this, 500);//Wait half a second

                        //Then update variables
                        pathLength = robot1.getOdometerReading();
                        battery = (int) robot1.getBatteryLevel();

                        //Then update textviews/progressbar
                        pathTracker.setText(getString(R.string.pathLength) + pathLength);
                        energyTracker.setText(getString(R.string.energyLeft) + battery);
                        energyLeft.setProgress(battery);
                } catch (Throwable e) { }
            }
        });
        Driving.start();//Then start the thread
    }

    /**
     * The method that will be called to move from this activity/java class to FinishActivity. For
     * now, it will simply be triggered by the shortcut button. In project 5, it will only be called
     * in this activity if the robot manages to get to the end. Compared to PlayManuallyActivity, it
     * also packs in additional variables pathLength and battery, as those are unique to this
     * class. FinishActivity will know to only pull those variables out if it detects the user
     * selected a robot algorithm to attempt to move to the exit
     */
    public void moveToWin() {
        Log.v(getString(R.string.TAGACT4),"RECEIVED COMMAND TO RETRIEVE STORED MAZE");
        //Setting everything that could be running in the background to null
        if (Driving != null)
            Driving.interrupt();
        robot1 = null;
        robotDriver = null;

        Intent intent = new Intent(this, FinishActivity.class);

        //Place the pathLength and battery into the intent/bundle. FinishActivity will only pull it
        //out if they detect that this activity, and not PlayManuallyActivity, was called.
        intent.putExtra(getString(R.string.pathKey), pathLength);

        //If battery level is less than 0, will change it to zero, as battery power can't be negative
        if (battery < 0)
            battery = 0;
        intent.putExtra(getString(R.string.energyKey), battery);

        //Same as PlayManuallyActivity, it stores what driver was used and whether the user/robot
        //won or not.
        intent.putExtra(getString(R.string.driverKey), driver);
        intent.putExtra(getString(R.string.winKey), winner);

        startActivity(intent);
        finish();
    }

    /**
     * In the case that the user hits the back button midway through, we need to interrupt the
     * thread, as it is running in the background
     */
    @Override
    public void onBackPressed() {
        if (Driving != null)
            Driving.interrupt();

        finish();
        super.onBackPressed();
    }
}
