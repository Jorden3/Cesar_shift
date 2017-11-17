#Creator: Jorden Garcia
#This is a simple cesar shift program that bring in a .txt and shift the letters
#in it. no support for space and \n yet

#Import enum class Must be running 3.2 of python or higher
from enum import Enum
class Letters(Enum):
 A = 1
 B = 2
 C = 3
 D = 4
 E = 5
 F = 6
 G = 7
 H = 8
 I = 9
 J = 10 
 K = 11
 L = 12
 M = 13
 N = 14 
 O = 15
 P = 16 
 Q = 17
 R = 18
 S = 19
 T = 20 
 U = 21
 V = 22
 W = 23
 X = 24
 Y = 25
 Z = 26
 a = 27
 b = 28
 c = 29
 d = 30
 e = 31
 f = 32
 g = 33
 h = 34
 i = 35
 j = 36
 k = 37
 l = 38
 m = 39
 n = 40
 o = 41
 p = 42
 q = 43
 r = 44
 s = 45
 t = 46
 v = 47
 u = 48
 w = 49
 x = 50
 y = 51
 z = 52
 
#create an empty list to store the shifted letters
shifted = []
#define the amount to shift
shift = 6
#Give a .txt name to parse and shift
filename = "gettys.txt"

#open the file
with open(filename) as f:
 #grab a line from that file
 for line in f:
  #grab a charcater from the line
  for ch in line:
   #search the Emu list of letters
   for letters in Letters:
    #Check if the letter matches the a enum
    if(letters.name == ch):
	 #find the shifted letter
     result = letters.value + shift
     #if we are out of the enum bounds sub 52 from result to get overflow
     if(result > 52):
      result = result - 52
     #grab the letter using the result from above
     ch_1 = Letters(result) 
     #append to the end of the shifted list
     shifted.append(ch_1.name)
    elif(ch == '\n'):
     shifted.append('\n')    #do the same if we find a newline
    elif(ch == ' '):
     shifted.append(' ')     #do the same if we find a space
    #else:
     #print() #prints a bunch of newlines don't actually need it 

#close the file to prevent leaks
f.close()

#open a new file called shifted
theFile = open("shifted.txt", 'w')
#iterate shifted and dump it into the file
for ch_2 in shifted:
 theFile.write(ch_2)

#close the file and report success
theFile.close()
print("text shifted and new shifted.txt add to current directory")
