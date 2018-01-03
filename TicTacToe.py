import os #To clear console
ttt=['0','1','2','3','4','5','6','7','8']
def Board():
	#os.system('clear')	
	print "  Tic Tac Toe\n"
	print "Player 1=X","  ","Player 2=O"	 
	print ttt[0],"  |  ",ttt[1],"  |  ",ttt[2]
	print "____|_______|_____"
	print ttt[3],"  |  ",ttt[4],"  |  ",ttt[5]
	print "____|_______|_____" 
	print ttt[6],"  |  ",ttt[7],"  |  ",ttt[8]
	print "____|_______|_____"	
def  Winner():
	if ttt[0]==ttt[1] and ttt[1]==ttt[2]:
            if ttt[0]=='X':
	        return 1
	    else:
		return 2
	elif ttt[3]==ttt[4] and ttt[4]==ttt[5]:
            if ttt[3]=='X':
	        return 1
	    else:
		return 2
	elif ttt[6]==ttt[7] and ttt[7]==ttt[8]:
            if ttt[6]=='X':
	        return 1
	    else:
		return 2
	elif ttt[0]==ttt[3] and ttt[3]==ttt[6]:
            if ttt[0]=='X':
	        return 1
	    else:
		return 2
	elif ttt[1]==ttt[4] and ttt[4]==ttt[7]:
            if ttt[1]=='X':
	        return 1
	    else:
		return 2
	elif ttt[2]==ttt[5] and ttt[5]==ttt[8]:
            if ttt[2]=='X':
	        return 1
	    else:
		return 2
	elif ttt[0]==ttt[4] and ttt[4]==ttt[8]:
            if ttt[0]=='X':
	        return 1
	    else:
		return 2
	elif ttt[2]==ttt[4] and ttt[4]==ttt[6]:
            if ttt[2]=='X':
	        return 1
	    else:
		return 2
	
def Play():
	turn=0
	n=0
        draw=0
        while 1:	
		    Board()
		    if turn==0:
		        n=input('Player 1 Enter a number from 0 to 8: ')
			if n>=0 and n<9 and (ttt[n]!='X' and ttt[n]!='O'):
			    ttt[n]='X'
			    Board()
			    turn=1 
                            draw=draw+1
                            if draw==9: 
                                 print "Game Tie\n"
                                 break
			if Winner()==1:
			    print("Player 1 wins")
			    break
                        
		    if turn==1:
		        n=input('Player 2 turn,Enter a number from 0 to 8: ')
			if n>=0 and n<9 and (ttt[n]!='X' and ttt[n]!='O'):
			    ttt[n]='O'
			    Board()
			    turn=0
                            draw=draw+1
                        else:
		        	print "Wrong Choice\n"	
		    else:
			print("Wrong Choice Turn Lost")
		 
		    if Winner()==2:
			print("Player 2 wins")	
		        break
                    
	 		
						
Play()


