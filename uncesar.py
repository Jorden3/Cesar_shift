#Creator: Jorden Garcia
#This is a simple cesar shift program that bring in a .txt and shift the letters

import Letters
Letters1 = Letters.enum_Letters 
#create an empty list to store the shifted letters
shifted = []
#define the amount to shift
shift = 6
#Give a .txt name to parse and shift
filename = "shifted.txt"

#open the file
with open(filename) as f:
 #grab a line from that file
 for line in f:
  #grab a charcater from the line
  for ch in line:
   #search the Emu list of letters
   for letters in Letters1:
    #Check if the letter matches the a enum
    if(letters.name == ch):
	 #find the shifted letter
     result = letters.value - shift
     #if we are out of the enum bounds sub 52 from result to get overflow
     if(result < 0):
      result = 52 + result
     #grab the letter using the result from above
     ch_1 = Letters1(result) 
     #append to the end of the shifted list
     shifted.append(ch_1.name)
     break
    elif(ch == '\n'):
     shifted.append('\n')    #do the same if we find a newline
     break
    elif(ch == ' '):
     shifted.append(' ')     #do the same if we find a space
     break
    #else:
     #print() prints a bunch of newlines don't actually need it 

#close the file to prevent leaks
f.close()

#open a new file called shifted
theFile = open("unshifted.txt", 'w')
#iterate shifted and dump it into the file
for ch_2 in shifted:
 theFile.write(ch_2)

#close the file and report success
theFile.close()
print("Text unshifted and new unshifted.txt add to current directory")
