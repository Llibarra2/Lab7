'''
Lester Ibarra
80578839
Diego Aguirre
The pupose of this lab is to find the number of alterations needed to make
to a word in order to match the another word given, and vise versa
'''
import time # will be used to calculate the speed of  the program

def Edit_Distance(word1, word2, length1, length2):
    if length1 == 0:#checks in case either given string is empty
        return length2
    if length2==0:
        return length1
    
    if word1[length1 - 1] == word2[length2 -1]: #checks if the last two characters of the strings are the same
        return Edit_Distance(word1, word2, length1 -1, length2 -1)#returns remaining of the strings
    
    return 1 + min(#this will determine which of the following is the smallest in order to determine the size of the next input
                #Insert
                Edit_Distance(word1, word2, length1 , length2 - 1),
                #delete
                Edit_Distance(word1, word2, length1 - 1, length2),
                #replace
                Edit_Distance(word1, word2, length1 - 1, length2 - 1) )
def Word_Comparison(word1, word2):
    print("Edit the distance:")
    print("Words:\n1) %s\n2) %s" %(word1, word2))
    print("Edit Distance: %d" % Edit_Distance(word1, word2, len(word1), len(word2)))

def main():
    
    user1 = input("Enter 1st word to compare: ")
    user2 = input("Enter 2nd word to compare: ")
    start_time = time.time()
    Word_Comparison(user1, user2)
    print("--- %s seconds ---" % (time.time() - start_time))

    # " M O N E Y 
    #[0][1][2][3][4][5] "
    #[1][0][1][2][3][4] M           
    #[2][1][1][2][3][4] I
    #[3][2][2][1][2][3] N
    #[4][3][3][2][1][2] E
    #[5][4][4][3][2][2] R<-------This last value should be the output of the program when using these two words


main()