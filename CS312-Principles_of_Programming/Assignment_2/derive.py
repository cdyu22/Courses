import sys
import string

# Int tracking the derived string length
str_Length = 3
# Boolean tracking whether we print derivations
print_Der = False

#########################Take Command Line Arguments############################
for item in sys.argv:
    # If -d is detected we print the derivations
    if "-d" in item:
        print_Der = True

    # If -l is detected we make the string a list and check the 3rd entry for
    # the specified length we will use
    if "-l" in item:
        item = list( item )
        str_Length = int( item[ 2 ] )

    # If there is a .txt we know that that is the grammarfile that is passed in
    if ".txt" in item:
        file = item

###############################Creating Dictionary##############################
# Dictionary containing all nonterminals mapping to terminals
grammar = {}

for line in open( file, "r" ):
    # Split the line into a list
    equation = line.split()

    # We pop out the first two entries, the left hand side (LHS) and derives
    # symbol, and store the LHS symbol (to be key). We then combine the rest of
    # the right hand side (RHS) into a string.
    LHS = equation.pop( 0 )
    equation.pop( 0 )
    RHS = " ".join( equation )

    # Putting RHS in dictionary, first checking if key (LHS) is already present
    if LHS in grammar:
        grammar[ LHS ].append( RHS )
    else:
        grammar[ LHS ] = [ RHS ]

###################################Derive Strings###############################
# Open the grammar file again to take starting nonterminal and derives sign
fileline = open( file, "r" ).readline()
fileline = fileline.split()
start = fileline[ 0 ]
# Equals has spaces surrounding it for printing it out later
equals = " " + fileline[ 1 ] + " "

# Create worklist holding start symbol and derivation list with start symbol
worklist = [ [ start, [ start ] ] ]

# Counter that tracks amount of strings printed
counter = 0

# Set that tracks all previous strings printed (disallowing duplicates)
str_set = set()

# Needed to insert a blank line if we don't write the derivation history,
if ( not print_Der ):
    print("")

# Loop until worklist is empty
while 0 < len( worklist ):
    # Pop the string and its derivation history
    entry = worklist.pop( 0 )

    # Split the string into a list
    string = entry[ 0 ].split()

    # Checking if length is greater than max length, if it is, loop again
    if str_Length < len( string ):
        continue

    # Checking if we can print it out
    for i in range( len( string ) ):

        # Nonterminal detected, so break
        if string[ i ] in grammar:
            break

        # If we loop thru entire list
        if ( i == str_Length - 1 ):
            string = " ".join( string )

            # Check if printed string before, if not, add to string set
            if string in str_set:
                continue
            else:
                str_set.add( string )

            # If we are signaled to print derivation
            if ( print_Der ):
                # Offset tracks how many spaces we need before derives sign
                offset = len( start ) * " "

                # Start symbol and first replacement printed
                print( "\n" + str( start ) + equals + str( entry[ 1 ][ 1 ] ) )
                # Loop through every replacement
                for i in range( len( entry[ 1 ] ) - 3 ):
                    print( offset + equals + entry[ 1 ][ i + 2 ] )
                # Final string
                print( offset + equals + string )

            else:
                # If we don't print derivation history, just print final string
                print( string )

            # Increment string counter
            counter = counter + 1

    # If nonterminals detected, pick leftmost nonterminal in string
    for i in range( len( string ) ):
        if string[ i ] in grammar:

            # Replace the nonterminal with all terminals
            for item in grammar[ string[ i ] ]:
                # Create new string with replacing terminal
                newList = string
                newList[ i ] = item
                newList = " ".join( newList )

                # Create new derivation history
                history = entry[ 1 ][ : ]

                # Append the new replacement to the end of history
                history.append( newList )

                # Append the new string and derivation history to worklist
                worklist.append( [ newList, history ] )

            # Once we've looped through all possible replacements, break
            break

print( "\n# of strings generated: " + str( counter ) + "\n\n" )
