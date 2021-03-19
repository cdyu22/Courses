/**
 * Instantiates a controller with settings according to the given parameter.
 * @param parameter can identify a generation method (Prim, Kruskal, Eller)
 * or a filename that contains a generated maze that is then loaded,
 * or can be null
 * @return the newly instantiated and configured controller
 */
 Controller createController(String parameter) {
    // need to instantiate a controller to return as a result in any case
    Controller result = new Controller() ;
    String msg = null; // message for feedback
    // Case 1: no input
    if (parameter == null) {
        msg = "MazeApplication: maze will be generated with a randomized algorithm.";
    }
    // Case 2: Prim
    else if ("Prim".equalsIgnoreCase(parameter))
    {
        msg = "MazeApplication: generating random maze with Prim's algorithm.";
        result.setBuilder(Order.Builder.Prim);
    }
    // Case 3 a and b: Eller, Kruskal or some other generation algorithm
    else if ("Kruskal".equalsIgnoreCase(parameter))
    {
      msg = "MazeApplication: generating random maze with Kruskal's algorithm.";
      result.setBuilder(Order.Builder.Kruskal);
    }
    else if ("Eller".equalsIgnoreCase(parameter))
    {
        throw new RuntimeException("Don't know anybody named Eller ...");
    }
    // Case 4: a file
    else {
        File f = new File(parameter) ;
        if (f.exists() && f.canRead())
        {
            msg = "MazeApplication: loading maze from file: " + parameter;
            result.setFileName(parameter);
            return result;
        }
        else {
            // None of the predefined strings and not a filename either:
            msg = "MazeApplication: unknown parameter value: " + parameter + " ignored, operating in default mode.";
        }
    }
    // controller instantiated and attributes set according to given input parameter
    // output message and return controller
    System.out.println(msg);
    return result;
}

/*
  	System.out.println("Left: " + robot.distanceToObstacle(Direction.LEFT));
  	System.out.println("Right: " + robot.distanceToObstacle(Direction.RIGHT));
  	System.out.println("Foward: " + robot.distanceToObstacle(Direction.FORWARD));
  	System.out.println("Backward: " + robot.distanceToObstacle(Direction.BACKWARD));
*/
  
