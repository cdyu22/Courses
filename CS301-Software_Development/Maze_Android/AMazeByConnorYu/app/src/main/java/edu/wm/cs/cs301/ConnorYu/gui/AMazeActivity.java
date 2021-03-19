package edu.wm.cs.cs301.ConnorYu.gui;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.SeekBar;
import android.widget.Spinner;
import android.widget.TextView;

import com.example.amazebyconnoryu.R;

/**
 * This is the first activity/java class we run upon the app being launched. It will have a large
 * array of widgets, including buttons, spinners, and a SeekBar. Many of them serve to allow the
 * user to select the maze that they would like to create, or the skill level of the maze that
 * they would like to load. Once all of the items are selected they are then loaded up when the
 * user signals they are done, and sent off to the next activity/java class, which will generate
 * or load the maze depending on the user's inputs.
 */
public class AMazeActivity extends Activity {
    //Buttons that will tell us when to move on to the next activity (GeneratingActivity)
    Button startGenerating, revisit;

    //Spinners that collect data on the maze-building algorithm and whether the user will navigate
    //the maze, or if a robot (either WallFollower or Wizard) will navigate the maze.
    Spinner builder, driver;

    /*
    A discrete SeekBar that will record the selected skill level which will be passed to the
    GeneratingActivity which will use our old code to create a maze based on the skill level.

    skillText will serve as the text box that shows the current skill level the user selects.
     */
    SeekBar skill;
    TextView skillText;

    /**
     * This method runs at the start of the app. It sets up all of the widgets and has a listener
     * for all of them. It allows the user to select some inputs that will affect the maze, and
     * once the user signals they want to start playing, it will route the control flow to
     * startGeneratingActivity.
     * @param savedInstanceState A bundle object passed into the onCreate method that can carry
     *                           some data.
     */
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        //SeekBar reference: https://developer.android.com/reference/android/widget/SeekBar
        //************************************Handling SeekBars*************************************
        //Matching up the variables to their respective widgets in activity_main.xml
        skill = findViewById(R.id.skill);
        skillText = findViewById(R.id.skillText);

        //Setting up the default text value that displays when the app first launches.
        skillText.setText(getString(R.string.skillDefault));

        //Seekbar text setup source: https://stackoverflow.com/questions/15326290
        skill.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener(){
            /**
             * These methods serve to allow us to update the string values of skillText so we can
             * accurately reflect a change in the skill SeekBar and display the currently selected
             * maze generation level.
             * @param skill the SeekBar
             * @param progress the level chosen
             * @param fromUser
             */
            @Override
            public void onProgressChanged(SeekBar skill, int progress, boolean fromUser){
                //Space in strings.xml reference: https://stackoverflow.com/questions/10862975/
                skillText.setText(getString(R.string.skill) + progress);

                //Tracking the change of skill level
                Log.v(getString(R.string.TAGACT1),
                        "RECEIVED COMMAND TO CHANGE SKILL LEVEL" + progress);
            }

            /**
             * In order to gives messages whenever there's a change in the level
             * @param seekBar the seekbar we use
             */
            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {
                //Create a toast and Log.v whenever the user starts and stops touching the SeekBar
                Log.v(getString(R.string.TAGACT1), "RECEIVED COMMAND TO TRACK USER TOUCH");
            }

            /**
             * To signal when we stop tracking the change in levels
             * @param seekBar the seekbar we use
             */
            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {
                Log.v(getString(R.string.TAGACT1), "RECEIVED COMMAND TO STOP TRACKING TOUCH");
            }
        });


        //Spinner Reference: https://developer.android.com/guide/topics/ui/controls/spinner
        //************************************Handling Spinners*************************************
        //Matching up the variable to its respective widget in activity_main.xml
        builder = findViewById(R.id.generator);
        /*
        We then create an adapter, set it up, and then set it as the spinner's adapter so we can
        match up the string array to the spinner
         */
        ArrayAdapter<CharSequence> builderAdapter = ArrayAdapter.createFromResource(this,
                R.array.builder,android.R.layout.simple_spinner_item);
        builderAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        builder.setAdapter(builderAdapter);

        //To set the listener whenever an item is selected (or isn't) to show a Log.v output and
        //a toast message
        builder.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            /**
             * To show a message whenever we choose a different spinner level.
             * @param adapterView
             * @param view
             * @param i
             * @param l
             */
            @Override
            public void onItemSelected(AdapterView<?> adapterView, View view, int i, long l) {
                Log.v(getString(R.string.TAGACT1), "RECEIVED COMMAND TO CHANGE SPINNER");
            }

            /**
             * To show a message whenever we decide not to change a spinner list
             * @param adapterView
             */
            @Override
            public void onNothingSelected(AdapterView<?> adapterView) {
                Log.v(getString(R.string.TAGACT1),
                        "DID NOT RECEIVE COMMAND TO CHANGE SPINNER");
            }
        });

        //Spinner to select the robot driver algorithm
        driver = findViewById(R.id.driver);
        ArrayAdapter<CharSequence> driverAdapter = ArrayAdapter.createFromResource(this,
                R.array.driver,android.R.layout.simple_spinner_item);
        driverAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        driver.setAdapter(driverAdapter);

        driver.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            /**
             * To show a message whenever we choose a different spinner level.
             * @param adapterView
             * @param view
             * @param i
             * @param l
             */
            @Override
            public void onItemSelected(AdapterView<?> adapterView, View view, int i, long l) {
                Log.v(getString(R.string.TAGACT1), "RECEIVED COMMAND TO CHANGE SPINNER");
            }

            /**
             * To show a message whenever we decide not to change a spinner list
             * @param adapterView
             */
            @Override
            public void onNothingSelected(AdapterView<?> adapterView) {
                Log.v(getString(R.string.TAGACT1),
                        "DID NOT RECEIVE COMMAND TO CHANGE SPINNER");
            }
        });


        //Button Reference: https://developer.android.com/reference/android/widget/Button
        //************************************Handling Buttons**************************************
        //Matching up the variable to its respective widget in activity_main.xml
        startGenerating = findViewById(R.id.generateButton);

        /*
        This will start the generation of a new maze. This is if they hit the 'Generate' button, in
        which case there'll be the new generation of a maze, as well as a new seed that will be
        randomly calculated in GeneratingActivity.
         */
        startGenerating.setOnClickListener(new View.OnClickListener(){
            /**
             * This allows us to give a message when we decide to start generating the maze
             * @param view
             */
                public void onClick(View view){
                /*
                We also set up Log.V for whenever we click a button, which
                we will do for all future buttons. As guided, we will delete toast messages
                in project 5.
                 */
                Log.v(getString(R.string.TAGACT1), "RECEIVED COMMAND TO START GENERATING");

                //As this button will signal to start generating, we call startGenerating.
                //True refers to the generation of a new maze.
                startGeneratingActivity(true);
            }
        });

        /*
        This button signals to GeneratingActivity that it should try to pull out a seed from a maze
        that exited in the past
        A button that will be correctly implemented in project 5. It will load a maze depending
        on the selected skill level the user picks, and will not care about the builder algorithm
        the user passes in.
         */
        revisit = findViewById(R.id.revisitButton);
        revisit.setOnClickListener(new View.OnClickListener(){
            /**
             * This allows us to give a message when we decide to start loading the maze
             * @param view
             */
            public void onClick(View view){
                Log.v(getString(R.string.TAGACT1), "RECEIVED COMMAND TO REVISIT STORED MAZE");

                //Will implement functionality to load stored mazes for now, just starts
                //the generation method.
                //False refers to the fact we're not generating a new maze.
                startGeneratingActivity(false);
            }
        });

        startService(new Intent(this, BackGroundMusic.class));
    }

    /**
     * This method will serve as a way to move from the title screen (AMazeActivity/activity_main)
     * to the generating screen (GeneratingActivity/generate_activity). It takes in all of the
     * inputs that the user has described on this activity and use it to either generate a maze
     * or load a stored maze. It stores all of that into an intent, and then starts the activity.
     * @param newMaze: true if we are generating a new maze, false if we load a stored maze.
     */
    public void startGeneratingActivity(Boolean newMaze){

        //Supporting Log.v calls that display the builder/driver/skill level the user has selected
        Log.v(getString(R.string.TAGACT1),
                "builder is: " + builder.getSelectedItem().toString());
        Log.v(getString(R.string.TAGACT1),
                "driver is: " + driver.getSelectedItem().toString());
        Log.v(getString(R.string.TAGACT1),
                "Skill level is: " + skill.getProgress());
        Log.v(getString(R.string.TAGACT1),
                "New maze generation is: " + false);

        //The creation of a new intent
        Intent intent = new Intent(this, GeneratingActivity.class);

        //The storage of data within that new intent
        intent.putExtra(getString(R.string.builderKey), builder.getSelectedItem().toString());
        intent.putExtra(getString(R.string.driverKey), driver.getSelectedItem().toString());
        intent.putExtra(getString(R.string.skillKey), skill.getProgress());
        intent.putExtra(getString(R.string.generationKey),newMaze);

        //The only activity where we don't call finish() at the end
        startActivity(intent);
    }
}