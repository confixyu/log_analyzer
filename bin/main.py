import fire
from sources.snippets.snippet import *

userFile = []


# Load user file with file path
def loadFile(filePath):
    userFile = inputFile(filePath)

    for line in userFile:
        word = line.find('initiator')
        if (word > 0):
            print("initiator")
            print(word)
            logList = readLogList()
        elif (word > 0):
            print("Reciver")
        else:
            print("Type of log is unknow")


#
# Execute command
#  python main.py loadFile <..\sample\log.txt>
#

if __name__ == '__main__':
    fire.Fire()