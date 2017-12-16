import os
import time
import re

#############################################################################
#  Explanation of this script:
#  This script is used to search through .txt files in the directory that you define via the variable "findWHERE".
#  It searches the files for a regex string that looks for a pattern of possible passwords you've used and may have
#  been captured in plain text through logging or what not.  It then overwrites those strings with a bunch of
#  exclamation points (or what every you want).
#############################################################################

# Change the valude of "findWHERE" to be the path to the directory you want to search
findWHERE = '/path/do/directory/'
print("Just a heads up, this just searches through *.txt files...")
time.sleep(2)

# "fileList" is a static variable, you don't need to modify it.
fileList = []

###########################################################################################################################
# The below for loop does a "walk" through the directory you defined in "findWHERE", grabs the name of any
# file that ends in ".txt", then appends it to the list called "fileList".  The variable "fileList" is defined
# above as an empty list.
###########################################################################################################################
for root, dirs, files in os.walk(findWHERE):
    for name in files:
        if name.endswith(('.txt', '.log')):
            filepath = os.path.join(root, name)
            fileList.append(filepath)

# Below just prints some info on the screen so you see something happening
print("OK, here are the files where those strings exist: ")
print(fileList)
print(" ")
print len(fileList)
print(" ")
print("Going to go through and replace that string now...")
time.sleep(2)


###########################################################################################################################
# This definition "findReplace" below opens up the previously appended "fileList", which is a list of all the files in
# the "findWHERE" directory that are .txt files.  As it opens the files, it regex searches for string that are possible
# patterns of passwords you may have used in past and replaces them with exclamation marks.
#
# The Regex pattern explained:
# Let's say you used a the password "B00kedUp@years!!", or variations like "Booked4years!" or "BOOked10days@@":
# The regex pattern to cover any of these possibilities:
#    [Bb][0,Oo]{2}ked\w+\S* <-- find any variation, but will specifically included "ked" in the middle for less false positives.
#
# Next, let's say you used the password "Flock.of.birds!", or variations like "Flock.0f.b1rds!!!" or "Flock.0F.geese!":
#    [Ff]l[0,Oo]ck\W\w+\S\w+\S* <-- find any variation with the "l" and "ck" being constant to prevent false positives.
###########################################################################################################################

def findReplace(files, filePattern):
    """
    This does a find/replace of a single string.

    :param files: Enter "fileList", or what ever name used as the list that get's appended via the for loop above.
    :param filePattern: Currently just ".txt" should be entered, as that is the variable defined in the for loop above.

    Example:

    findReplace(fileList, '*.txt')
    """
    pword_regex = '([Bb][0,Oo]{2}ked\w+\S*|[Ff]l[0,Oo]ck\W\w+\S\w+\S*)'
    replacement = '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
    for files in fileList:
        with open(files) as f:
            s = f.read()
            if re.search(pword_regex, s) is None:
                continue
            else:
                with open(files, 'w') as f:
                    f.write(re.sub(pword_regex, replacement, s))


# This is findReplace being used.
findReplace(fileList, ['*.txt', '*.log'])
