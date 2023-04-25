# This code prints a matrix and detects if there is a deadlock in a distributed system

# The following code prints a matrix
print('''
P1 P2 P3 P4 P5
P1 0 1 0 0 0
P2 0 0 1 0 0
P3 0 0 0 1 1
P4 1 0 0 0 0
P5 0 0 0 0 0
''')

# The following code creates a matrix and initializes a flag variable
a = [[0, 1, 0, 0, 0],
     [0, 0, 1, 0, 0],
     [0, 0, 0, 1, 1],
     [1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0]]
flag = 0

# The following function recursively checks for deadlocks in the distributed system
def aman(a, i, k):
    end = 5
    for x in range(end):
        if(a[k][x] == 1):
            if(i == x):
                # Prints the deadlock detected message if a deadlock is found
                print(f' S{k+1} ==> S{x+1} ({i+1}, {k+1}, {x+1}) --------> DEADLOCK DETECTED')
                global flag
                flag = 1
                break
        # Prints the message indicating the current state of the system
        print(f' S{k+1} ==> S{x+1} ({i+1}, {k+1}, {x+1})')
        # Calls the function recursively to check the next state of the system
        aman(a,i,x)

# The following code prompts the user to enter an initiator site number
print("CHANDY-MISRA-HAAS DISTRIBUTED DEADLOCK DETECTION ALGORITHM")
print("____________________")
print()
x = 0
end = 5
i = int(input("Enter Initiator Site No. : "))
j = i - 1
print()

# The following loop checks for deadlocks in the distributed system
for k in range(end):
    if(a[j][k]==1):
        print(f' S{j+1} ==> s{k+1} ({i}, {j+1}, {k+1})')
        # Calls the aman function to check for deadlocks in the current state of the system
        aman(a,j,k)

# Prints the message indicating whether a deadlock was detected or not
if(flag == 0):
    print("\nNO DEADLOCK DETECTED")
print("____________________")
