package edu.wm.cs.cs301.slidingpuzzle;

import java.util.Arrays;
import java.util.Random;

import edu.wm.cs.cs301.slidingpuzzle.PuzzleState.Operation;

public class SimplePuzzleState implements PuzzleState {
	
	//Declaring the individual fields
	public int[] state;
	public SimplePuzzleState Parent;
	public Operation stateOperation;
	public int path_Length = 0;
	public int sDimension;
	public int emptySlots;
	
	@Override
	public void setToInitialState(int dimension, int numberOfEmptySlots) {
		
		//Field instantiation (path_Length defaults to 0, though)
		Parent = null;
		stateOperation = null;
		path_Length = 0;
		sDimension = dimension;
		emptySlots = numberOfEmptySlots;
		
		//Sets array length and sets it to the initial order
		int emptySlotTracker = dimension*dimension + 1 - numberOfEmptySlots;
		int numerator = 1;
		state = new int[dimension*dimension];
		for (int i = 0; i < state.length; i++) {
			state[i] = numerator;
			//If an empty tile is detected, make it 0.
			if (numerator == emptySlotTracker) {
				state[i] = 0;
				emptySlotTracker++;
			}
			numerator++;
		}
	}

	//*********************************************************************
	
	//Methods that simply return data
	@Override
	public int getValue(int row, int column) {
		
		//Math calculation to allow 1-d array to represent a 2-d board.
		return state[row*sDimension+column];
	}

	@Override
	public PuzzleState getParent() {
		return (PuzzleState) Parent;
	}

	@Override
	public Operation getOperation() {
		return stateOperation;
	}

	@Override
	public int getPathLength() {
		return path_Length;
	}
	
	@Override
	public boolean isEmpty(int row, int column) {
		if (state[row*sDimension+column] == 0)
			return true;
		return false;
	}		

	//*********************************************************************
	
	@Override
	public PuzzleState move(int row, int column, Operation op) {
		
		//Disallowing empty tiles to be moved, in case of multiple empty tiles.
		if (getValue(row,column) == 0)
			return null;
		
		//Converting index values from two-dimensional to one-dimensional
		int index = row*sDimension+column;
		if (index < 0 || sDimension*sDimension <= index)
			return null; //Don't allow movements for tiles out of bounds
		SimplePuzzleState Child = new SimplePuzzleState();
		
		//All of these check if it's a spot that allows their movement type, then it checks if the spot is open
		//Using &&, so if fails one test (isn't operation passed into move())it exits if statement, no indexing error
		
		//Right
		if (op == Operation.MOVERIGHT && index % sDimension != sDimension - 1 && state[index+1] == 0){
			//Creating identical PuzzleState
			Child = parentSetup(Child, Operation.MOVERIGHT);
			//Actual swap of values
			Child.state[index+1] = Child.state[index];
			Child.state[index] = 0;
			return (PuzzleState) Child;
		}
		//Left
		if (op == Operation.MOVELEFT && index % sDimension != 0 && state[index-1] == 0){
			Child = parentSetup(Child,Operation.MOVELEFT);
			Child.state[index-1] = Child.state[index];
			Child.state[index] = 0;
			return (PuzzleState) Child;
		}
		//Up
		if (op == Operation.MOVEUP && index > sDimension-1 && state[index-sDimension] == 0){
			Child = parentSetup(Child, Operation.MOVEUP);
			Child.state[index-sDimension] = Child.state[index];
			Child.state[index] = 0;
			return (PuzzleState) Child;
		}
		//Down
		if (op == Operation.MOVEDOWN && index < sDimension * sDimension - sDimension && state[index+sDimension] == 0){
			Child = parentSetup(Child, Operation.MOVEDOWN);
			Child.state[index+sDimension] = state[index];
			Child.state[index] = 0;
			return (PuzzleState) Child;
		}
		return null;
	}
	
	//Move Support Method: Similar to clone(); just wanted complete control of method
	private SimplePuzzleState parentSetup(SimplePuzzleState New_Child, Operation ops) {
		
		//Copies all of the fields except for stateOperation, which is different
		//The switching of values occurs in the move method itself
		New_Child.stateOperation = ops;

		New_Child.sDimension = sDimension;
		New_Child.emptySlots = emptySlots;
		New_Child.path_Length = path_Length + 1;
		New_Child.state = new int[state.length];
		New_Child.Parent = this;
		for (int l=0; l < state.length;l++) 
			New_Child.state[l] = state[l];
		return New_Child;
	}

	//*********************************************************************
	
	//Implemented recursively
	@Override
	public PuzzleState drag(int startRow, int startColumn, int endRow, int endColumn) {
		
		//Base case, tile has reached its destination
		if (getValue(startRow,startColumn) == 0 || (startRow == endRow && startColumn == endColumn))
			return (PuzzleState) this;
		
		//Calculations to let us know which direction we're trying to go
		int rowDifference = endRow - startRow;
		int columnDifference = endColumn - startColumn;
		int index = startRow*sDimension+startColumn;
		
		PuzzleState dChild = new SimplePuzzleState();
		dChild = this;
		
		//Checks if we want to move in the direction, then performs similar checks to move
		
		//Right
		if (0 < columnDifference && index % sDimension != sDimension - 1 && getValue(startRow,startColumn+1) == 0){
			dChild = this.move(startRow,startColumn,Operation.MOVERIGHT);
			//If moved, we call drag again to continue movement, except with new index
			//Will return if in the final destination
			return dChild.drag(startRow, startColumn+1, endRow, endColumn);
		}
		//Left
		if (columnDifference < 0 && index % sDimension != 0 && getValue(startRow,startColumn-1) == 0) {
			dChild = this.move(startRow,startColumn,Operation.MOVELEFT);
			return dChild.drag(startRow, startColumn-1, endRow, endColumn);
		}
		//Up
		if (rowDifference < 0 && index > sDimension -1 && getValue(startRow-1,startColumn) == 0) {
			dChild = this.move(startRow,startColumn,Operation.MOVEUP);
			return dChild.drag(startRow-1, startColumn, endRow, endColumn);
		}
		//Down
		if (0 <	rowDifference && index < sDimension * sDimension - sDimension && getValue(startRow+1,startColumn) == 0) {
			dChild = this.move(startRow,startColumn,Operation.MOVEDOWN);
			return dChild.drag(startRow+1, startColumn, endRow, endColumn);
		}
		//No spots open, got as far as we could, return
		return (PuzzleState) dChild;
	}


	//*********************************************************************
	
	@Override
	public PuzzleState shuffleBoard(int pathLength) {
		
		//Recording current path length so we can add pathLength to it.
		int currentPathLength = getPathLength();
		
		//Naming the PuzzleState that we will shuffle
		PuzzleState Shuffler = new SimplePuzzleState();
		Shuffler = this;
		
		Random rand = new Random();
		Operation ops = null;
		int row;
		int column;
		int n;
		
		while (Shuffler.getPathLength() < pathLength + currentPathLength) {	
			
			//Picking random operation
			n = rand.nextInt(4);
			if (n == 0) 
				ops = Operation.MOVERIGHT;
			if (n == 1) 
				ops = Operation.MOVELEFT;
			if (n == 2) 
				ops = Operation.MOVEUP;
			if (n == 3) 
				ops = Operation.MOVEDOWN;
			
			row = rand.nextInt(4);
			column = rand.nextInt(4);
			
			if (Shuffler.move(row,column,ops) != null) {

				//To avoid back and forth cycle
				if (Shuffler.move(row, column, ops).equals(Shuffler.getParent())) 
					continue;
				
				Shuffler = Shuffler.move(row, column, ops);
				}
			}
		return Shuffler;
	}
	
	//*********************************************************************

	@Override
	public PuzzleState getStateWithShortestPath() {
		SimplePuzzleState Shortest = new SimplePuzzleState();
		Shortest = this;
		
		SimplePuzzleState Scanner = new SimplePuzzleState();
		Scanner = Shortest.Parent;
		
		//Scans to see if current state is identical to any of its parents
		//If it is, set current state equal to its parent
		while (Scanner != null) {
			if (Shortest.equals(Scanner))
				Shortest = Scanner;
			Scanner = Scanner.Parent;
		}
		
		SimplePuzzleState Holder = new SimplePuzzleState();
		Holder = Shortest.Parent;	
		
		//Perform the same above operation on all parents, checking the parents of all of the parents
		while (Holder != null) {
			Scanner = Holder.Parent;
			while (Scanner != null) {
				if (Holder.equals(Scanner))
					Holder = Scanner;
				Scanner = Scanner.Parent;
			}
			Holder = Holder.Parent;
		}
		//Updating the path length for all of the parents
		this.pathLengthSetup();
		return (PuzzleState) Shortest;
	}
	
	//getStateWithShortestPath Supporting Method
	private void pathLengthSetup() {
		if (Parent == null)
			path_Length = 0;
		else if (Parent != null) {
			Parent.pathLengthSetup();
			path_Length = Parent.path_Length + 1;
		}
	}

	//*********************************************************************
	
	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + Arrays.hashCode(state);
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (!(obj instanceof SimplePuzzleState))
			return false;
		SimplePuzzleState other = (SimplePuzzleState) obj;
		//Only care if the board state is the same
		if (!Arrays.equals(state, other.state))
			return false;
		return true;
	}
	
}