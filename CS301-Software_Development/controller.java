Controller createController(String[] parameter) {
	Controller result = new Controller() ;
	String msg = null;
		String parser;
		int i = 0;

		while (i < parameter.length) {
			parser = parameter[i];
			System.out.println(parameter[3]);

			if (parser.equals("-g")){
				i++;
				parser = parameter[i];

				if ("Prim".equalsIgnoreCase(parser)){
						 msg = msg + "MazeApplication: generating random maze with Prim's algorithm.";
						 result.setBuilder(Order.Builder.Prim);
				}

				else if ("Kruskal".equalsIgnoreCase(parser)){
					 msg = msg + "MazeApplication: generating random maze with Kruskal's algorithm.";
					 result.setBuilder(Order.Builder.Kruskal);
				}

				else if ("Eller".equalsIgnoreCase(parser)){
						 throw new RuntimeException("Don't know anybody named Eller ...");
				}

				else
					msg = msg + "MazeApplication: unknown parameter value: " + parameter + " ignored, operating in default mode.";
				}

			if (parser.contains("-d")){
				i++;
				parser = parameter[i];

				if ("WallFollower".equalsIgnoreCase(parser)){
					msg = msg + "MazeApplication: initializing WallFollower robot.";
					 BasicRobot robot1 = new BasicRobot();
					 WallFollower robotDriver = new WallFollower();
					 robot1.setMaze(result);
					 robotDriver.setRobot(robot1);
					 //Need to set dimensions later(?)
					 result.setRobotAndDriver(robot1,robotDriver);
				 }

				 else if ("Wizard".equalsIgnoreCase(parser)){
					 throw new RuntimeException("Don't know no Wizard ...");
				 }
			}

			if (parser.contains("-f")){
				i++;
				parser = parameter[i];
				File f = new File(parser) ;
				if (f.exists() && f.canRead()){
					msg = msg + "MazeApplication: loading maze from file: " + parameter;
					result.setFileName(parser);
				}
			}
		}

		// TODO :: DELETE THIS
		if (result.getDriver() != null)
			System.out.println("Driver is not null");

		System.out.println(msg);
		return result;
}
