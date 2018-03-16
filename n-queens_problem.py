
def initialize(n):
  for key in ['queen','row','col','nwtose','swtone']:
    board[key] = {}
  for i in range(n):
    board['queen'][i] = -1
    board['row'][i] = 0
    board['col'][i] = 0
  for i in range(-(n-1),n):
    board['nwtose'][i] = 0
  for i in range(2*n-1):
    board['swtone'][i] = 0

def printboard():
    global Matrix
    for row in sorted(board['queen'].keys()):
        Matrix[row][board['queen'][row]] = 'Q'
        print((row,board['queen'][row]),end='')
    print("\n")


def printmul():
    global Matrix
    for i in range(8):
        for j in range(8):
            print(Matrix[i][j], end=' ')
        print("\n")

def free(i,j):
  return(board['row'][i] == 0 and board['col'][j] == 0 and
          board['nwtose'][j-i] == 0 and board['swtone'][j+i] == 0)

def addqueen(i,j):
  board['queen'][i] = j
  board['row'][i] = 1
  board['col'][j] = 1
  board['nwtose'][j-i] = 1
  board['swtone'][j+i] = 1

def undoqueen(i,j):
  board['queen'][i] = -1
  board['row'][i] = 0
  board['col'][j] = 0
  board['nwtose'][j-i] = 0
  board['swtone'][j+i] = 0

def placequeen(i):
  n = len(board['queen'].keys())
  for j in range(n):
    if free(i,j):
      addqueen(i,j)
      if i == n-1:
        return(True)
      else:
        extendsoln = placequeen(i+1)
      if extendsoln:
        return(True)
      else:
        undoqueen(i,j)
  else:
    return(False)

board = {}
n = int(input("How many queens?\n"))
Matrix = [['X' for x in range(n)] for y in range(n)] 
initialize(n)
if placequeen(0):
  printboard()
  printmul()
