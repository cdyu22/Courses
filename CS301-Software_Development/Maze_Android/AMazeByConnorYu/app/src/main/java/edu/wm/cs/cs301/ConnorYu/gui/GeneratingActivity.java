package edu.wm.cs.cs301.ConnorYu.gui;

import android.app.Activity;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.util.Log;
import android.widget.ProgressBar;

import edu.wm.cs.cs301.ConnorYu.generation.Factory;
import edu.wm.cs.cs301.ConnorYu.generation.Maze;
import edu.wm.cs.cs301.ConnorYu.generation.MazeFactory;
import edu.wm.cs.cs301.ConnorYu.generation.Order;

import com.example.amazebyconnoryu.R;

import java.util.Random;

/**
 * The activity that is always run after the AMazeActivity. This serves to let the phone generate
 * or load the maze, which is required before the user can actually start playing the game. It
 * runs a background thread to constantly check how much of the maze is generated, and then
 * depending on the message, it will update the progress bar to show how much of the generation
 * or loading is complete.
 */
public class GeneratingActivity extends Activity implements Order{
    //Progressbar that tracks how far through the generation process we are
    ProgressBar progress;

    //Variables we use to store the maze's variables
    String driver, builder;
    int level;
    boolean newMaze;
    int seed;

    //The thread that will run in the background, initialized to null so we can tell if the thread
    //has started or not in the method onBackPressed.
    Thread background = null;

    /**
     * The first method that is run when AMazeActivity calls the class activity to start. It sets
     * up the screen, changing what is happening on the android screen, and connects the widgets
     * that appear on screen to this class's variables.
     * @param savedInstanceState A bundle object passed into the onCreate method that can carry
     *                           some data.
     */
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.generate_activity);

        //Linking up the ProgressBar that shows up on the screen to the progress variable.
        progress = findViewById(R.id.generatingBar);

        /*
        Retrieving the data from the intent that was passed in from AMazeActivity. It will always
        contain the maze builder algorithm, whether we use a robot or not, and the skill level that
        was selected, though in the future the builder will be ignored if we load a maze.
         */
        Bundle extras = getIntent().getExtras();
        builder = extras.getString(getString(R.string.builderKey));
        driver = extras.getString(getString(R.string.driverKey));
        level = extras.getInt(getString(R.string.skillKey));
        newMaze = extras.getBoolean(getString(R.string.generationKey));
    }


    //Working with Handlers and ProgressBars source: https://stackoverflow.com/questions/18317098
    //**************************************Handling Handler//**************************************
    Handler mailMan;
    {
        mailMan = new Handler() {
            /**
             * To give the progressBar some way to know how to handle messages
             * @param msg
             */
            @Override
            public void handleMessage(Message msg) {
                progress.setProgress(percentdone);//The handler sets the ProgressBar's progress to be
                //The same as what the percentdone is.
            }
        };
    }

    /**
     * After the creation of the class, this method is run. It will start the ProgressBar. For now,
     * all that it does is create a new thread that goes through a for loop, and every interation
     * it sends a message to the handler, which increments the progress bar by 1. It also has
     * a command to sleep for 10 milliseconds for every loop, so the bar isn't filled up nearly
     * instantaneously. After the loop, we call startPlayingActivity to move to a playing activity.
     */
    @Override
    public void onStart(){
        super.onStart();

        /*
        Setting up SharedPreferences and its editor. We need to account for three possible
        outcomes, if a new maze has been ordered to be generated, if we are told to pull an old
        maze and there's no seed, or if we are told to pull an old maze and there is a seed.
         */
        SharedPreferences pref = getApplicationContext().getSharedPreferences("Seeds",0);
        SharedPreferences.Editor editor = pref.edit();
        Random random = new Random();//Random number generator

        //If new maze has been ordered to generate.
        if (newMaze){
            Log.v(getString(R.string.TAGACT2),"RECEIVED COMMAND TO GENERATE NEW STRING");
            //Reasonably large int so chance of reselection of seed is low.
            seed = random.nextInt(2000000000);
            //The key is the builder and the level to allow for a unique key for every combination
            editor.putInt(builder+level,seed);//Put that in the SharedPreferences and commit it.
            editor.commit();
        }
        if (!newMaze) {
            Log.v(getString(R.string.TAGACT2),"RECEIVED COMMAND TO REVISIT NEW MAZE");
            //If no relevant seed that fits our criteria we follow the same steps as above
            if (pref.getInt(builder+level,-1) == -1){
                Log.v(getString(R.string.TAGACT2),"NO OLD SEED FOUND, GENERATING NEW ONE");
                seed = random.nextInt(2000000000);
                editor.putInt(builder+level,seed);//DOES IT OVERWRITE?
                editor.commit();
            }
            //If not, then we just retrieve that seed
            else {
                Log.v(getString(R.string.TAGACT2),"FOUND OLD SEED, GENERATING OLD MAZE");
                seed = pref.getInt(builder + level, -1);
            }
        }

        //Need to set up the default parameters of the order
        orderSetup();

        //Matching up the intents that were passed in to set the order's fields
        if (builder == "Default")
            orderBuilder = Order.Builder.DFS;
        if (builder == "Prim")
            orderBuilder = Order.Builder.Prim;
        if (builder == "Kruskal")
            orderBuilder = Builder.Kruskal;
        orderSkillLevel = level;

        //Setting the progressbar.
        progress.setProgress(0);
        //Starting this method, which will start the construction of the maze
        start();

        //The thread that runs in the background
        background = new Thread(new Runnable() {
            /**
             * What we call when we want th thread to run
             */
            public void run() {
                try {
                    //Until the percentdone is 100, will send messages to the handler, which updates
                    //progress to match the percentdone
                    while (percentdone < 100){
                        mailMan.sendMessage(mailMan.obtainMessage());
                    }
                    Log.v(getString(R.string.TAGACT2),"MAZE GENERATED, STARTING PLAY");
                    startPlayingActivity();
                } catch (Throwable e) { }
            }
        });
        Log.v(getString(R.string.TAGACT2),"RECEIVED COMMAND TO START BACKGROUND THREAD");
        background.start();
    }

    /**
     * When we click back, the thread is still running. This means that at the end it is still able
     * to call startPlayingActivity when the loop finishes. We need to be able to terminate the
     * thread when we click back, or else it will return to the title screen for a split second,
     * and then send us to one of the playing activities.
     */
    @Override
    public void onBackPressed(){
        Log.v(getString(R.string.TAGACT2),"RECEIVED COMMAND TO STOP GENERATION");
        //Need to make sure that background has been initialized and is running
        if (background != null){
            background.interrupt();
            factory.cancel();
        }

        finish();
        super.onBackPressed();
    }

    /**
     * This is called only when the ProgressBar has been completely filled. The maze has been
     * theoretically built, so the only data we care about in either of the two playing states is
     * the driver, so we set up the intent to call a different class (either PlayManuallyActivity
     * or PlayAnimationActivity) depending on the driver option selected. If they don't choose
     * to manually navigate to the exit it calls PlayManuallyActivity, and it calls
     * PlayAnimationActivity if it isn't. We then store the type of driver within the intent,
     * and start the activity, making sure to finish this activity.
     */
    private void startPlayingActivity(){
        //Initialize and declare it null to avoid errors, as the program doesn't recognize that
        //the intent will always be declared and have a value.
        Intent intent = null;

        //A Log.v call so we can make sure the driver is the same as what was selected by the user
        //in AMazeActivity.
        Log.v(getString(R.string.TAGACT2),"The driver is " + driver);


        //If the player selected manually, the intent should start PlayManuallyActivity.
        if (driver.equals("Manual"))
            intent = new Intent(this, PlayManuallyActivity.class);

        //If the player selected anything else, the intent should start PlayManuallyActivity.
        if (driver.equals("WallFollower") || driver.equals("Wizard"))
            intent = new Intent(this, PlayAnimationActivity.class);

        //Store the driver into the intent, start the activity, and end this activity.
        intent.putExtra(getString(R.string.driverKey), driver);
        startActivity(intent);
        finish();
    }

    //**************************************ORDER METHODS****************************************
    //These are the private order fields, which will be passed into the MazeFactory for generation
    private int orderSkillLevel;
    private Builder orderBuilder;
    private boolean orderPerfect;

    //The factory that will construct the maze
    protected Factory factory;

    //The variable that tracks how far we're done
    private int percentdone;
    boolean started;

    /**
     * Sets up the order to their default values
     */
    private void orderSetup(){
        Log.v(getString(R.string.TAGACT2),"RECEIVED COMMAND TO SET DEFAULT MAZE VALUES");
        factory = new MazeFactory(true,seed) ;//Implement getSharedPreferences
        orderSkillLevel = 0;
        orderBuilder = Order.Builder.DFS;
        orderPerfect = false;
        percentdone = 0;
        started = false;
    }

    /**
     * Trivial get skill method
     * @return
     */
    @Override
    public int getSkillLevel() {
        Log.v(getString(R.string.TAGACT2),"RETRIEVING SKILL LEVEL");
        return orderSkillLevel;
    }

    /**
     * Trivial get builder method
     * @return
     */
    @Override
    public Builder getBuilder() {
        Log.v(getString(R.string.TAGACT2),"RETRIEVING BUILDER");
        return orderBuilder;
    }

    /**
     * Trivial get perfect boolean method
     * @return
     */
    @Override
    public boolean isPerfect() {
        Log.v(getString(R.string.TAGACT2),"RETRIEVING ROOM STATUS");
        return orderPerfect;
    }

    //Will call the static class MazeHolder, that will hold the maze
    @Override
    public void deliver(Maze maze) {
        Log.v(getString(R.string.TAGACT2),"Called to set maze");
        MazeHolder storedMaze = new MazeHolder();
        storedMaze.setData(maze);
    }

    /**
     * Will update the progress, which is tracked in the MazeFactory/MazeBuilder
     * @param percentage the amount that's done
     */
    @Override
    public void updateProgress(int percentage) {
        if (this.percentdone < percentage && percentage <= 100) {
            this.percentdone = percentage;
        }
    }

    /**
     * To actual start the generation of the maze
     */
    public void start() {
        Log.v(getString(R.string.TAGACT2),"RECEIVED COMMAND TO START MAZE GENERATION");
        started = true;
        percentdone = 0;

        assert null != factory : "Controller.init: factory must be present";
        factory.order(this) ;

    }
}
