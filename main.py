# Import libraries
import urllib.request
import csv

# # # Scrape pokedex into a text file
# webPage = urllib.request.urlopen("https://www.smogon.com/dex/ss/pokemon/")
# unformatedPokedex = open("fin.txt", "wb")
# unformatedPokedex.write(webPage.read())
# unformatedPokedex.close()

# Remove "most" unnecessary html
fileIn = open("file.txt","rt")
fileOut = open("fout.txt","wt")

for line in fileIn:
  if line.startswith("            d"):
    # This doesn't work for bulbasaur
    fileOut.write(line.replace("}},","}},\n"))

fileIn.close()
fileOut.close()

# pull raw data from fout into csv
pokedex = []
var = ""
var1 = ""
var2 = ""
var3 = ""
var4 = ""
var5 = ""
var6 = ""
var7 = ""

secondFileIn = open("fout.txt","rt")
formatedPokedex = open("formattedPokedex.csv","wb+")
for line in secondFileIn:
  if line.startswith("{"):
    # Get pokemon's name
    var = line[line.find('"name":')+8 : line.find(",")-1]
    print(var)
    # Get pokemon's health
    var1 = line[line.find('"hp"') + 5 : line.find(',"atk"')]
    print(var1)
    # Get pokemon's attack
    var2 = line[line.find('"atk":') + 6 : line.find(',"def"')]
    print(var2)
    # Get pokemon's defense
    var3 = line[line.find('"def":') + 6 : line.find(',"spa"')]
    print(var3)
    # Get pokemon's special attack
    var4 = line[line.find('"spa":') + 6 : line.find(',"spd"')]
    print(var4)
    # Get pokemon's special defense
    var5 = line[line.find('"spd":') + 6 : line.find(',"spe"')]
    print(var5)
    # Get pokemon's speed
    var6 = line[line.find('"spe":') + 6 : line.find(',"weight"')]
    print(var6)
    # Get pokemon's weight
    var7 = line[line.find('"weight":') + 9 : line.find(',"height"')]
    print(var7)
    # Get pokemon's height
    # Get pokemon's type
    # Get pokemon's abilities
    # Get pokemon's dex number
    # Get pokemon's other forms
    break