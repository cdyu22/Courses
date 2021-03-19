package edu.wm.cs.cs301.ConnorYu.gui;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;

import com.example.amazebyconnoryu.R;

import edu.wm.cs.cs301.ConnorYu.generation.Maze;

import static edu.wm.cs.cs301.ConnorYu.gui.Constants.UserInput;

/**
 * One of the two options that GeneratingActivity can call. This activity/java class is called
 * if the user signals that they want to manually navigate to the exit of the maze themselves. It
 * mainly consists of buttons that serve to navigate the maze and buttons that toggle different
 * things to show up on screen.
 */

public class PlayManuallyActivity extends Activity {
    //Buttons that handle user navigation
    Button left, right, forward, back;

    //Buttons that handle the toggling of different displays on screen
    Button fullMaze, solution, wallToggle;

    /*
    The driver string will track which driver algorithm the user picked. It will always be manual,
    but doing this allows for consistency in the structuring of the flow of information between
    classes. The win boolean tracks whether the user won or not, changing to false if the user
    loses. Note, it's impossible to lose in this state, as the user can explore the maze for a
    theoretically indefinite period of time, the only way they lose is if they quit. So in this
    activity the boolean will always be true, but it's important to pass that in for clarity
    as well in FinishActivity, which will change depending on the boolean that's passed in.
     */
    boolean win = true;
    String driver;

    //The maze reference, the MazePanel that we will draw on, and the reference to StatePlaying,
    //which will allow us to play the game
    Maze maze = null;
    MazePanel mazePanel;
    StatePlaying statePlay;

    int pathLength = 0;
    /**
     * The first method that is called when the activity is created. It sets up the screen, changing
     * what is happening on the android screen. For this class, it sets up and connects a lot of
     * buttons, as well as their respective listeners which impact what happens when the buttons
     * are clicked. For now, the listeners just call a Log.v message and create a toast message,
     * with the exception of the temporary winning button, which moves the activity to
     * the FinishActivity.
     *
     * @param savedInstanceState A bundle object passed into the onCreate method that can carry
     *                           some data.
     */
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.play_manually_activity);

        Log.v(getString(R.string.TAGACT3),"RECEIVED COMMAND TO RETRIEVE STORED MAZE");
        //Retrieve the maze from MazeHolder
        maze = MazeHolder.getData();

        //Link up the MazePanel in PlayManuallyActivity to the mazepanel reference
        mazePanel = findViewById(R.id.panel);

        //Create a new stateplaying that we use to play the game
        statePlay = new StatePlaying();

        //Setting up the references
        statePlay.setMazeConfiguration(maze);
        statePlay.controlManually = this;

        //Start the game
        statePlay.start(mazePanel);

        //Get the driver value, mainly a formality, as it will always be "Manual" in this class.
        driver = getIntent().getExtras().getString(getString(R.string.driverKey));

        //*******************************Handling Navigation Buttons********************************
        //If this button is called, move forward
        forward = findViewById(R.id.forward);
        forward.setOnClickListener(new View.OnClickListener() {
            /**
             * This allows us to do some action whenever we click this button
             * @param view
             */
            public void onClick(View view) {
                Log.v(getString(R.string.TAGACT3), "RECEIVED COMMAND TO MOVE FORWARD");
                statePlay.keyDown(UserInput.Up, 0);
            }
        });

        //If this button is called, move back
        back = findViewById(R.id.back);
        back.setOnClickListener(new View.OnClickListener() {
            public void onClick(View view) {
                Log.v(getString(R.string.TAGACT3), "RECEIVED COMMAND TO MOVE BACK");
                statePlay.keyDown(UserInput.Down, 0);
            }
        });

        //If this button is called, rotate left
        left = findViewById(R.id.left);
        left.setOnClickListener(new View.OnClickListener() {
            public void onClick(View view) {
                Log.v(getString(R.string.TAGACT3), "RECEIVED COMMAND TO TURN LEFT");
                statePlay.keyDown(UserInput.Left, 0);
            }
        });

        //If this button is called, rotate right
        right = findViewById(R.id.right);
        right.setOnClickListener(new View.OnClickListener() {
            /**
             * This allows us to do some action whenever we click this button
             * @param view
             */
            public void onClick(View view) {
                Log.v(getString(R.string.TAGACT3), "RECEIVED COMMAND TO TURN RIGHT");
                statePlay.keyDown(UserInput.Right, 0);
            }
        });


        //*********************************Handling Toggle Buttons**********************************
        //Call to display the maze
        fullMaze = findViewById(R.id.fullMaze);
        fullMaze.setOnClickListener(new View.OnClickListener() {
            /**
             * This allows us to do some action whenever we click this button
             * @param view
             */
            public void onClick(View view) {
                Log.v(getString(R.string.TAGACT3), "RECEIVED COMMAND TO SHOW THE FULL MAZE");
                statePlay.keyDown(UserInput.ToggleFullMap, 0);
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
                Log.v(getString(R.string.TAGACT3), "RECEIVED COMMAND TO SHOW MAZE SOLUTION");
                statePlay.keyDown(UserInput.ToggleSolution, 0);
            }
        });

        ////Call to display the walls
        wallToggle = findViewById(R.id.toggleWalls);
        wallToggle.setOnClickListener(new View.OnClickListener() {
            /**
             * This allows us to do some action whenever we click this button
             * @param view
             */
            public void onClick(View view) {
                Log.v(getString(R.string.TAGACT3), "RECEIVED COMMAND TO TOGGLE WALL VISIBILITY");
                statePlay.keyDown(UserInput.ToggleLocalMap, 0);
            }
        });

    }

    /**
     * The method that will be called to move from this activity/java class to FinishActivity. For
     * now, it will simply be triggered by the shortcut button. In project 5, it will only be called
     * in this activity if we get to the end.
     */
    public void moveToWin() {
        Log.v(getString(R.string.TAGACT3),"RECEIVED COMMAND TO MOVE TO FINISHACTIVITY");
        Intent intent = new Intent(this, FinishActivity.class);

        //Storing the driver, which lets FinishActivity know if it should remove certain TextViews.
        intent.putExtra(getString(R.string.driverKey), driver);

        //Stores whether the user won the game or not.
        intent.putExtra(getString(R.string.winKey), win);

        //Placing pathLength into finishactivity
        intent.putExtra(getString(R.string.pathKey), pathLength);
        startActivity(intent);
        finish();
    }

    /**
     * Method called if we hit the back button that sets StatePlaying to null, and we lose the
     * reference to the game, and garbage collection removes everything
     */
    @Override
    public void onBackPressed() {
        statePlay = null;

        finish();
        super.onBackPressed();
    }
}
