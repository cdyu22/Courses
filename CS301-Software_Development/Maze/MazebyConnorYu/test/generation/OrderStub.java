package generation;

import gui.DefaultState;


public class OrderStub extends DefaultState implements Order {
    private int skillLevel; 
    private Builder builder;
    private boolean perfect;
   
    private MazeContainer mazeHolder;
    protected Factory factory;

    boolean started;
    
    /**
     * Constructor uses default settings such that unless the attributes are set, it 
     * develops the smallest maze possible with the default algorithm, as it is too small,
     * while it is told to deliver mazes, non are placed.
     */
    public OrderStub() {
        factory = new MazeFactory() ;
        skillLevel = 0; // default size for maze
        builder = Order.Builder.DFS; // default algorithm
        perfect = false; // default: maze can have rooms
        started = false;
    }
    
    ///////////// trivial set methods from State interface ////////////////////////
    @Override
    public void setSkillLevel(int skillLevel) {
        this.skillLevel = skillLevel;
    }
    @Override
    public void setBuilder(Builder builder) {
        this.builder = builder;
    }
    @Override
    public void setPerfect(boolean isPerfect) {
        perfect = isPerfect;
    }
    
    public void start() {
        started = true;
        factory.order(this);    
    }
   
    /**
     * This is ran at the end of the MazeBuilder thread, usually delivers the maze to the
     * controller, but in this stub we just want to store it to deliver it to the tests.
     */
    @Override
    public void deliver(Maze mazeConfig) {
        mazeHolder = (MazeContainer) mazeConfig;
    }
    
    /**
     * The deliver method stores the maze that the builder creates,
     * and this method returns it.
     * @return the maze created by MazeFactory/MazeBuilder
     */
    public MazeContainer mazeDeliver() {
    	return mazeHolder;
    }
    //////////// set of trivial get methods ////////////////////////
    @Override
    public int getSkillLevel() {
        return skillLevel;
    }
    @Override
    public Builder getBuilder() {
        return builder;
    }
    @Override
    public boolean isPerfect() {
        return perfect;
    }

    @Override
    public void updateProgress(int percentage) {;}

}