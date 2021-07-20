#Ian Butler
#Intro to CS Final Project
#Due 12/9/16 at 11:30 PM


def getHawkIDs():
    return ["imbutler"]

#Explanation of this program: This program reads in a file of a team's roster, it creates a new list that is empty and then strips all the tags from the data WITHOUT modifying the original file, the original file is then closed. As it strips the tags it adds the data to a list so it is easily ready. After creating the list containing the data WITH the XML tags removes it calculates how many players are on the roster. After doing that it creates a new file that can be written to called "TeamnameRoster.txt" for example, if the original file was called Broncos.txt is would create a new file called BroncosRsoter.txt. Once the file is created it removes the first element from the list (since this is ALWWAYS a blank element). Then the list is iterated over to see if there are any other whitespaces, these are then removed. It then writes the first sentence to the file using the first element (which is the team name) and the number of players on the roster. After the first sentence is written it begins swapping the elements in the list. It puts the list in a order so the elements can easily be added to form the correct sentences. It first swaps the jersey number and the player's first name and last name to make the list go in the order of ["FIRST NAME", "LAST NAME", JERSEY NUMBER","HEIGHT", "WEIGHT", "AGE", "POSITION", "SCHOOL"] it then swaps the "POSITION" element until it is in the correct order, this is done because the elements are now in corresponding order they are in the senteces. Next it deals with the height element. It splits it from ["5-11"] to ["5", "11"] because in the sentence it would be 5 foot 11 so the "-" has to be removed. Once this is done it begins writing the sentences to the file, it goes through the list and since it is in the correct order it plugs the element into the sentece. The file is then closed.
def summarizeData(filename):
    #Opens the specified file name and reads it.
    fr = open(filename, 'r')
    #Creates a new empty list
    j = []
    #Goes through the file line by line and adds the line into the the list
    for i in fr:
        j.append(i.strip("< ").strip(" > \n").strip("/").strip(" > \n").strip("age>").strip("position").strip("height").strip("weight").strip("jno>").strip("fname").strip("lname").strip("yer").strip("school").strip("> \n").strip("</").strip(" "))
    #Closes the file since it is done reading the data.
    fr.close()
    #Gets the total length of the array
    total = len(j) - 5
    #Takes the total length and divides it by 10 to find the number of players on the roster
    numberOfPlayers = total / 10
    #Chops off the ".txt" from the file name so that it can be used in naming the new file
    filename = filename[:-4]
    #Creates the name of the new file using the filename + Roster.txt
    myFile = str(filename) + "Roster.txt"
    #Creates the new file and allows it to be written to.
    fw = open(myFile, "w")
    #Removes the first element in the list
    j.pop(0)
    #Removes all the white space in the list
    j = [i for i in j if i != '']
    #Writes the first line on the new file.
    fw.write("Here is the roster for the " +str(j[0]) + ". There are " +str(numberOfPlayers) + " players on the team. \n")
    #Removes the first element because it is no longer needed.
    j.pop(0)
    #Sets i = 0
    i = 0
    #Swaps the jersey number with the player's last name and then the first name with the last name so that it is in correct order for the sentences.
    while i<=((numberOfPlayers*8)-8):
        j[i], j[i+2] = j[i+2], j[i]
        j[i], j[i+1] = j[i+1], j[i]
        i = i + 8
    #Sets i to 6
    i = 6
    #Swaps the player's position all the way until it is in the 3rd element and the correct order for the sentences.
    while i<=(numberOfPlayers*8):
        j[i], j[i-1] = j[i-1], j[i]
        j[i-1], j[i-2] = j[i-2], j[i-1]
        j[i-2], j[i-3] = j[i-3], j[i-2]
        j[i-3], j[i-4] = j[i-4], j[i-3] 
        i = i + 8
    #Sets i to 4
    i=4
    #This while loop splits the element that contains the height into 2 so it can be properly displayed in the sentence. ["5-1"] becomes ["5","11"]
    while i < (numberOfPlayers*8):
        j[i] = j[i].split("-")
        i = i + 8
    #Sets i equal to 0
    i=0
    #Writes each line to the file until the counter reaches the number of players on the roster
    while i<(numberOfPlayers*8):
        fw.write(str(j[i]) + " " +str(j[i+1]) + ", " +str(j[i + 2]) + ", wears #" +str(j[i+3]) + ". He is " +str(j[i + 4][0]) + " foot " +str(j[i+4][1]) + " inches tall, and weighs " +str(j[i + 5]) + " pounds. He is " + str(j[i + 6]) + " years old. He went to " +str(j[i + 7]) + ". \n")
        i = i + 8
    #Closes the file.
    fw.close()
