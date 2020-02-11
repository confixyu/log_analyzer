import fire
from sources.snippets.snippet import *

userFile = []
logList = readLogList()

# Load user file with file path
def loadFile(filePath):
    userFile = inputFile(filePath)


#
# Execute command
#  python main.py loadFile <..\sample\log.txt>
#

if __name__ == '__main__':
    fire.Fire()