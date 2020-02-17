import fire
from sources.snippets.snippet import *

userFile = []
choices = ['Initiator', 'responder']

# Load user file with file path
def loadFile(filePath):
    userFile = inputFile(filePath)

    for line in userFile:
        #word = line.find('initiator')
        if any(word in line for word in choices):
            print(line)
            if (line.find('Initiator') > 0):
                print("Load Initiator file")
            
            if (line.find('Responder') > 0):
                print("Load Responder File")
            break


#
# Execute command
#  python main.py loadFile <..\sample\log.txt>
#

if __name__ == '__main__':
    fire.Fire()