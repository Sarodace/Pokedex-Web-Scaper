# TODO: Actually use the CSV library maybe?
# Import libraries
import urllib.request
# import csv

# Function that'll I'll move to the function file
def listToStringCSV(string):
  variable = '"' + string.replace('"',"") + '"'
  variable = evo.replace(",",", ")
  return variable


# # # Scrape pokedex into a text file
webPage = urllib.request.urlopen("https://www.smogon.com/dex/ss/pokemon/")
unformatedPokedex = open("fin.txt", "wb")
unformatedPokedex.write(webPage.read())
unformatedPokedex.close()

# Remove "most" unnecessary html
fileIn = open("file.txt","rt")
fileOut = open("fout.txt","wt")

for line in fileIn:
  if line.startswith("            d"):
    # This doesn't work for bulbasaur
    fileOut.write(line.replace("}},","}},\n"))

fileIn.close()
fileOut.close()

# Handle File I/O
secondFileIn = open("fout.txt","rt")
formatedPokedex = open("formattedPokedex.csv","w+")

# Define and add CSV header fields
fieldNames = ['Dex Number', 'Name', 'Type (1)', 'Type (2)','Abilities (1)', 
              'Abilities (2)', 'Abilities (3)', 'Health', 'Attack', 'Defense', 'Special Attack', 
              'Special Defense', 'Speed', 'Weight', 'Height', 'Other forms', 
              'Evolutions']

# TODO: Turn this into a function
for i in range(0,len(fieldNames)):
  if not i == len(fieldNames) - 1:
    formatedPokedex.write(fieldNames[i] + ',')
  else:
    formatedPokedex.write(fieldNames[i] + '\n')

# Fill CSV
for line in secondFileIn:
  if line.startswith("{"):
    name = line[line.find('"name":') + 8 : line.find(",") - 1]
    hp = line[line.find('"hp"') + 5 : line.find(',"atk"')]
    atk = line[line.find('"atk":') + 6 : line.find(',"def"')]
    dfn = line[line.find('"def":') + 6 : line.find(',"spa"')]
    spa = line[line.find('"spa":') + 6 : line.find(',"spd"')]
    spd = line[line.find('"spd":') + 6 : line.find(',"spe"')]
    spe = line[line.find('"spe":') + 6 : line.find(',"weight"')]
    weight = line[line.find('"weight":') + 9 : line.find(',"height"')]
    height = line[line.find('"height":') + 9 : line.find(',"types"')]

    # Get pokemon's type
    types = line[line.find('"types":') + 9 : line.find('abilities') - 3]
    typeList = types.split(",")
    if len(typeList) == 1:
      types = types + ',""'

    # Get pokemon's abilities
    ability = line[line.find('abilities') + 12 : line.find('formats') - 3]
    abilityList = ability.split(",")
    # TODO: Clean this
    if len(abilityList) == 1:
      ability = ability + ',"",""'
    if len(abilityList) == 2:
      ability = ability + ',""'

    # Get pokemon's dex number
    dexNumber = line[line.find('dex_number') + 12 : line.find('cap') - 2]

    # Get pokemon's evolutions
    evo = line[line.find('evos') + 7 : line.find('alts') - 3]
    listToStringCSV(evo)

    # Get pokemon's other forms
    alts = line[line.find('alts') + 7 : line.find('genfamily') - 3]
    listToStringCSV(alts)

    contents = [dexNumber, name, types, ability, hp, atk, dfn, spa, spd, spe, 
    weight, height, alts, evo]

    # Actually fill in the CSV!
    for i in range(0,len(contents)):
      if not i == len(contents) - 1:
        formatedPokedex.write(contents[i] + ',')
      else:
        formatedPokedex.write(contents[i] + '\n')