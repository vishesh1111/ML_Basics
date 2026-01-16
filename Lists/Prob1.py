""" problem statement -> 
You start with an empty list.
You will be given a set of commands, and each command tells you to do something to the list. The commands can be:
1. insert i e → Put the number e at position i in the list
2. print → Display the current list
3. remove e → Remove the first occurrence of number e from the list
4. append e → Add the number e to the end of the list
5. sort → Arrange the list elements in ascending order
6.pop → Remove the last element of the list
7.reverse → Reverse the order of the list
Your task is to perform each command one by one on the list and print the list whenever the print command appears.
"""

if __name__ == '__main__':
    N = int(input("Enter Number of Commands: "))
    List = []
    
    for k in range(N):
        command = input().split()
        
        
        if not command:
            continue
        
        if command[0] == "insert":
            index = int(command[1])
            e = int(command[2])
            List.insert(index,e)
            
        elif command[0] == "print":
            print(List)
            
        elif command[0] == "remove":
            e = int(command[1])
            List.remove(e)
            
        elif command[0] == "append":
            e = int(command[1])
            List.append(e)
        
        elif command[0] == "sort":
            List.sort()
            
        elif command[0] == "pop":
            List.pop()
            
        elif command[0] == "reverse":
            List.reverse()

        
            