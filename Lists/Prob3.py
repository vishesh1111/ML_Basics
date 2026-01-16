# Prob statement:> In this challenge, the user enters a string and a substring. 
# You have to print the number of times that the substring occurs in the given string.
# String traversal will take place from left to right, not from right to left
#e.g. if the string is "ABCDCDC" and the substring is "CDC", then the output should be 2.

def count_substring(string, sub_string):
    count = 0 # creating a variable to store the count of substring occurrences
    for i in range (len(string) - len(sub_string)+1): # +1 to check the last possible position is checked
        if string[i:i+len(sub_string)] == sub_string: # extracting a slice of the string starting at i , length is exacty equal to substring
            count +=1
            
    return count
    
if __name__ == '__main__':
    string = input("Enter the main string : ")
    sub_string = input("enter the substring :")
    print(count_substring(string,sub_string))
    
    
    
# Method 2:
#find() = returns the index position 


def count_substring(string,sub_string):
    count = 0
    start = 0
    
    while True:
        pos = string.find(sub_string, start)
        if pos == -1:
            break
        count += 1
        start = pos + 1
        
    return count







if __name__ == '__main__':
    string = input("Enter the main string : ")
    sub_string = input("enter the substring :")
    print(count_substring(string,sub_string))
    