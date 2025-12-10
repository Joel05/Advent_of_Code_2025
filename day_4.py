test_input = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""
#10x10 matrix

split_input = test_input.split()

rolls_list: list[list[str]] = []

for line in split_input:
    internal_list: list= []
    for roll in line:
        internal_list.append(roll)
    rolls_list.append(internal_list.copy())
    internal_list.clear()
        
    
#Check left column

        
#Check right column

#Check first line

#Check last line

result = 0
#Check the rest
for row_id, row in enumerate(rolls_list): #Für jede reihe
    for column_id, roll in enumerate(row): #Für jede Spalte
        counter = 0
        #print(row_id, column_id, roll)
        if row_id == 0 or row_id == len(rolls_list)-1 or column_id == 0 or column_id == len(row)-1: #If we are in first or last row, or in leftmost or rightmost column (special cases)
            #print("skibidi")
            continue
        else:   #If we arent in these rows or columns
            for check_row in range(row_id-1, row_id+2): # Für alle 3 umgebenden Reihen
                print("Check row:", check_row)
                for check_column in range(column_id-1, column_id+2): # Für alle 3 umgebenden Spalten
                    print("Check column:", check_column)
                    if rolls_list[check_row][check_column] == "@":
                        counter += 1
                        print("yessirski")
        #Check if there are less than 4 rolls nearby
        if counter < 4:
            result += 1

print("Result:", result)