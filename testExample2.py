from pathlib import Path

current_dir = Path.cwd()
file_name = "input_f.txt"
file_path = current_dir / file_name

def solve_1(file) :
    dialPosition = 50
    zerosCounted = 0

    for line in file:
        # .strip() removes the newline character (\n) from the end
        #print(line.strip())

        #print(line[0])

        theRest = line[1:len(line)]

        numberValue = int(theRest)
        
        #print(f"{numberValue} rest")

        if (line[0] == "L") :
            #print("this is an L")
            if (numberValue > 99) :
                dialPosition-=(numberValue % 100)
            else:
                dialPosition-=numberValue 

            if (dialPosition < 0):
                dialPosition+=100

        if (line[0] == "R" ) :
            if (numberValue > 99) :
                dialPosition+=(numberValue % 100)
            else:
                dialPosition+=numberValue 

            if (dialPosition > 99):
                dialPosition-=100
                
        if (dialPosition == 0) :
            zerosCounted += 1
        
    print(f"✅ Part 1 Answer: {zerosCounted}")

def solve_2(file) :
    
    print(f"✅ Part 2 Answer: {0}")

try:
    # Use 'with' to ensure the file is closed automatically
    with open(file_path, 'r', encoding='utf-8') as file:
        # Iterating directly over the file object is memory-efficient
    
        solve_1(file)

        solve_2(file)

                
except FileNotFoundError:
    print(f"Error: The file at {file_path} was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")