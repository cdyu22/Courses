package edu.wm.cs.cs301.ConnorYu.gui;

import edu.wm.cs.cs301.ConnorYu.generation.Maze;

//https://stackoverflow.com/questions/4878159/

/**
 * This is a class that was implemented in order to statically call the maze. While it can be stored
 * in a static variable, this also separates the code for ease of readability.
 */
public class MazeHolder {
    /*
    The variable that will hold the maze, static, so only one possible maze at a time.
     */
    private static Maze data = null;

    /**
     * Called at the end of GeneratingActivity, will store the data. If there's already a maze, it
     * drops that maze, and starts generating a new one.
     */
    public static void setData(Maze mazeData){
        data = null;
        data = mazeData;
    }

    /**
     * Returns the maze that has been generated, called by both PlayManuallyActivity and
     * PlayAnimationActivity.
     * @return The stored maze
     */
    public static Maze getData(){
        return data;
    }
}
