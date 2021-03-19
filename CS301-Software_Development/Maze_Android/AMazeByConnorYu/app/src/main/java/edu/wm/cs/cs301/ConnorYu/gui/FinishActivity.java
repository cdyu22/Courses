package edu.wm.cs.cs301.ConnorYu.gui;

import android.app.Activity;
import android.media.MediaPlayer;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import com.example.amazebyconnoryu.R;

/**
 * The class that is used when the user is done with either of the two playing activities. They
 * call this class/activity, which utilizes text boxes (TextView) to display what happened during
 * their exploration of the maze, including whether they got to the end, and other stats if the
 * user decided to have a robot explore the maze. The only button that shows up on this screen is
 * a button that returns the state to the title screen (AMazeActivity), at which point the user
 * can start a new maze.
 */
public class FinishActivity extends Activity {
    //The widgets that we will use, with a button that returns us to the title screen and
    //TextViews that display data on what happened while the user played and explored the maze.
    Button returnToTitle;
    TextView pathResult, batteryResult, winorloss;

    //Data that will be unpacked from the intent, the boolean win tells us whether the user/robot
    //navigated to the exit or not, and the driver string tells us what type of driver was used,
    //or if the user navigated to the exit themselves.
    boolean win = true;
    String driver;

    //Integers that track the pathLength and the battery level. They will only be pulled from the
    //intent if FinishActivity detects it came from PlayAnimationActivity (driver isn't manual).
    //If they are still -10 once data has been retrieved, we set some TextViews to gone.
    int pathLength = -10;
    int battery = -10;

    /**
     * The method that sets up the screen, changing what is happening on the android screen.
     * For this class, it sets up and connects TextView widgets and one button widget. Depending on
     * the data that it pulls out, it may try to pull out the pathLength and Battery level, setting
     * the TextViews that display those results if they aren't pulled out. The only interactive part
     * of this activity is the button that returns the user to the title. Apart from that, it simply
     * serves as an end to the maze, displaying data to the user.
     *
     * @param savedInstanceState A bundle object passed into the onCreate method that can carry
     *                           some data.
     */
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.finish_activity);

        //Retrieving data from the intent that was used to start FinishActivity. No matter the
        //circumstances, it will always be passed what driver was used, and whether the user/robot
        //won or not (navigated to the exit).
        driver = getIntent().getExtras().getString(getString(R.string.driverKey));
        win = getIntent().getExtras().getBoolean(getString(R.string.winKey));
        pathLength = getIntent().getExtras().getInt(getString(R.string.pathKey));

        //If a robot was used (meaning driver doesn't equal Manual, we also retrieve the pathLength
        //and the final energy level.
        if (!driver.equals("Manual"))
            battery = getIntent().getExtras().getInt(getString(R.string.energyKey));

        //***********************************Handling TextViews*************************************
        //Matching up the variables to their respective widgets in finish_activity.xml
        winorloss = findViewById(R.id.WinOrLose);
        pathResult = findViewById(R.id.pathlengthResult);
        batteryResult = findViewById(R.id.energyResult);

        //We set up the TextViews, the reason why we initially set pathLength and battery to -10 was
        //so that this was possible if the user manually drove through the maze.
        pathResult.setText(getString(R.string.totalSteps) + pathLength);
        batteryResult.setText(getString(R.string.finalEnergy) + battery);

        //If battery is -10, meaning the user navigated through the maze, we set the visbility
        //of the two TextViews to GONE.
        if (battery == -10)
            batteryResult.setVisibility(View.GONE);

        //stopService(new Intent(this, BackGroundMusic.class));

        //Depending on whether the user won or not, we display YOU WIN! or YOU LOSE.
        if (win) {
            winorloss.setBackground(getDrawable(R.drawable.winner));
            final MediaPlayer mp = MediaPlayer.create(this, R.raw.win);
            mp.start();
            Log.v(getString(R.string.TAGACT5), "RECEIVED COMMAND TO PLAY WINNING SOUND");
        } else {
            winorloss.setBackground(getDrawable(R.drawable.loser));
            final MediaPlayer mp = MediaPlayer.create(this, R.raw.lose);
            mp.start();
            Log.v(getString(R.string.TAGACT2), "RECEIVED COMMAND TO PLAY LOSING SOUND");
        }


        //************************************Handling Buttons**************************************
        //The button, serving as the only interactive widget in this activity. Pushing the button
        //returns the user to the title screen.
        returnToTitle = findViewById(R.id.returnToTitle);
        returnToTitle.setOnClickListener(new View.OnClickListener() {
            /**
             * This allows us to do some action whenever we click this button
             * @param view
             */
            public void onClick(View view) {
                Log.v(getString(R.string.TAGACT5), "RECEIVED COMMAND TO RETURN TO THE TITLE SCREEN");
                finish();
            }
        });
    }
}

