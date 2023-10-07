
Board = [' ', ' ',' ',' ',' ',' ',' ',' ',' ']
Key = True
flag=0
def change_char():
     for i in range(0,9):
        if Board[i]==1:
            Board[i]='X'
        elif Board[i]==-1:
            Board[i]='O'

def print_Board():
    print(Board[0],Board[1],Board[2])
    print(Board[3],Board[4],Board[5])
    print(Board[6],Board[7],Board[8])

def empty(num):
    if Board[num-1]==' ':
        return True

def check_Win(Board , position):
    # product = {"mode":True , "state":0}
    # if position =='X':
        # product["state"]=-1
    # else:
        # product["state"]=1
    product=0
    if position =='X':
        product=-1
    else:
        product=1

    if Board[0]==Board[1] and Board[0]==Board[2] and Board[0]==position:
        return product
    elif  Board[3]==Board[4] and Board[3]==Board[5] and Board[3]==position:
        return product
    elif  Board[6]==Board[7] and Board[6]==Board[8] and Board[6]==position:
        return product
    elif  Board[0]==Board[3] and Board[0]==Board[6] and Board[0]==position:
        return product
    elif  Board[1]==Board[4] and Board[1]==Board[7] and Board[1]==position:
        return product
    elif  Board[2]==Board[5] and Board[2]==Board[8] and Board[2]==position:
        return product
    elif  Board[0]==Board[4] and Board[0]==Board[8] and Board[0]==position:
        return product
    elif  Board[2]==Board[4] and Board[2]==Board[6] and Board[2]==position:
        return product
    else :
        return 2

def minmax(num):
    position=-1;
    val=-2;
    for i in range(1,10):
        if(empty(i)):
            Board[i-1]=num;
            score=-minmax(num*-1);
            if(score>val):
                val=score;
                position=i-1;
            Board[i-1]=' ';

    if(position==-1):
        change_char()
        return 0;
    change_char()
    return val;


def computer_move():
    position=-1;
    val=-2;
    for i in range(1,10):
        if(empty(i)):
            Board[i-1]=1
            change_char()
            score=-minmax(-1)
            Board[i-1]=' '
            if(score>val):
                val=score
                position=i-1
    Board[position]=1
    change_char()

while Key:
    number = int(input("Enter the palce for O , number[1,...,9]:"))
    if empty(number):
        Board[number-1]='O'
        o=check_Win(Board , 'O')
        if o==1:
            flag=1
            print_Board()
            print("you win ")
            Key=False
            break
        computer_move()
        x=check_Win(Board , 'X')
        if x==2 and o==2:
            print_Board()
        elif x==-1: 
            flag=1
            print_Board()
            print("you lose")
            Key=False
    else:
        number = int (input("this palce is not empty , enter another :"))
        Board[number-1]='O'
        o=check_Win(Board , 'O')
        if o==1:
            flag=1
            print_Board()
            print("you win ")
            Key=False
            break
        computer_move()
        x=check_Win(Board , 'X')
        if x==2 and o==2:
            print_Board()
        elif x==-1:
            flag=1
            print_Board()
            print("you lose")
            Key=False
        elif o==1:
            flag=1
            print_Board()
            print("you win ")
            Key=False

if flag==0:
    print("Draw")

     


