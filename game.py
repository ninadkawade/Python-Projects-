import sys
import random
from enum import Enum

def rps():
  game_count=0
  player_wins=0
  python_wins=0

  def play_rps():
    nonlocal player_wins
    nonlocal python_wins
    
    class RPS(Enum):
      ROCK=1
      PAPER=2
      SCISSOR=3
      
    playerchoice=input("\nEnter....\n1 for rock,\n2 for paper,\n3 for scissor\n\n")
    
    if playerchoice not in ["1","2","3"]:
      print("you must enetr 1 ,2,3,")
      return play_rps()
    player=int(playerchoice)

      
    computerChoice=random.choice("123")

    computer=int(computerChoice)

    print("")
    print("your choice\t"+str(RPS(player)).replace('RPS.','')+".")
    print("computer choice\t"+str(RPS(computer)).replace('RPS.','')+".")
    print("")

    def decide_winner(player,computer):
      nonlocal player_wins
      nonlocal python_wins
      if player==1 and computer==3:
        player_wins+=1
        return"🥳you win"
      elif player==3 and computer==2:
        player_wins+=1
        return"🥳you win"
      elif player==2 and computer==1:
        player_wins+=1
        return"🥳you win"
      elif player==computer:
        return"😲tie game"
      else:
        python_wins+=1
        return"🐍computer wins"
        
    game_winner=decide_winner(player,computer)
    print(game_winner)
      
    nonlocal game_count
    game_count+=1
    
    print("game count is:",game_count)
    print("player count is:",player_wins)
    print("python count is:",python_wins)
      
    print("\nplay again?")

    while True:
      playagain=input(" \nY for yes \nQ for quit\n")
      if playagain.lower() not in["y","q"]:
        continue
      else:
        break 

    if playagain.lower()=="y":
      return play_rps() 
    else:
      print("thank you")
      sys.exit("byee")

  return play_rps

play=rps()
play()

        

    