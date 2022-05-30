x = ("1635677370503.png")
o = ("1635677379331.png")

doubleClick("1635325295978.png")
wait("1635325319911.png",5)
click(Pattern("1635325326921.png").targetOffset(23,1))
type("playtictactoe.org")
type(Key.ENTER)
wait("1635677408947.png",5)


r1 = (Region(644,244,215,219))
r2 = (Region(861,264,197,192))
r3 = (Region(1066,254,193,203))
r4 = (Region(662,461,193,198))
r5 = (Region(862,461,196,200))
r6 = (Region(1066,462,194,199))
r7 = (Region(660,668,195,194))
r8 = (Region(861,666,198,197))
r9 = (Region(1066,668,192,194))

Hor1 = ["r1","r2","r3"]
Hor2 = ["r4","r5","r6"]
Hor3 = ["r7","r8","r9"]

Ver1 = ["r1","r4","r7"]
Ver2 = ["r2","r5","r8"]
Ver3 = ["r3","r6","r9"]

Diag1 = ["r1","r5","r9"]
Diag2 = ["r3","r5","r7"]

All_Lines = [Hor1,Hor2,Hor3,Ver1,Ver2,Ver3,Diag1,Diag2]

fake_board = {
  "r1": "",
  "r2": "",
  "r3": "",
  "r4": "",
  "r5": "",
  "r6": "",
  "r7": "",
  "r8": "",
  "r9": ""
}

board ={
    "r1": r1,
    "r2": r2,
    "r3": r3,
    "r4": r4,
    "r5": r5,
    "r6": r6,
    "r7": r7,
    "r8": r8,
    "r9": r9
}

def find_element(reg,element):
    if(reg.has(element)):
        return True 
    else:
        return False    

def board_scan():
    global fake_board
    counter = 1
    wait(1)
    for n in sorted(board.keys()):
        board[n].highlight(0.5)
        if(find_element(board[n],x)):
            fake_board["r"+str(counter)] = "x"
        elif(find_element(board[n],o)):
            fake_board["r"+str(counter)] = "o"
        else:
            fake_board["r"+str(counter)] = ""
        counter += 1
    for m in fake_board:
        print(m + ": " + str(fake_board[m]))


def next_move(fake_board):
    opponent_moves = []
    player_moves = []
    main_moves = []
    
    def best_move(moves,player_moves,opponent_moves):
        differences = [item for item in moves if item not in player_moves]
        if (len(differences) == 1):
            differences = [item for item in differences if item not in opponent_moves]
            if(len(differences) == 1):
                print("Wonderful move" + str(differences))
                return differences
            else:
                return []
        else:
            return []
    
    
    def opponent_best_move(moves,player_moves,opponent_moves):
        differences = [item for item in moves if item not in opponent_moves]
        if (len(differences) == 1):
            differences = [item for item in differences if item not in player_moves]
            if(len(differences) == 1):
                print("Dangerous move" + str(differences))
                return differences
            else:
                return []
        else:
            return []

    def normal_move(moves,player_moves,opponent_moves):
        differences = [item for item in moves if item not in player_moves]
        if (len(differences) >= 2):
            differences = [item for item in differences if item not in opponent_moves]
            if(len(differences) == 2):
                differences = [item for item in differences if item in Diag1 or item in Diag2]
                print("normal move" + str(differences))
                return differences
            elif(len(differences) ==1):
                return differences
            else:
                return []
        else:
            return []

    for i in fake_board:
        if fake_board[i] == "o":
            opponent_moves.append(i)
        if fake_board[i] == "x":
            player_moves.append(i)

       
    for i in All_Lines:
        main_moves = main_moves + best_move(i,player_moves,opponent_moves) 
    if (len(main_moves) > 0):
        return main_moves
    for i in All_Lines:
        main_moves = main_moves + opponent_best_move(i,player_moves,opponent_moves)
    if (len(main_moves) > 0):
        return main_moves
    for i in All_Lines:
        main_moves = main_moves + normal_move(i,player_moves,opponent_moves)
    if (len(main_moves) == 0):
        main_moves = ["r1"]
    print ("moves: " + str(main_moves))
    print ("opponent moves: " + str(opponent_moves))
    print ("player moves: " + str(player_moves))
    return main_moves

   
while (not (SCREEN.exists (Pattern("1635677705316.png").similar(0.89))or SCREEN.exists(Pattern("1635677736363.png").similar(0.80)))):
    board_scan()
    test = []
    test = next_move(fake_board)
    click(board[next_move(fake_board)[0]])
    wait(2)
    print("test: " + str(test))





