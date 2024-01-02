

def main():
  

  # first we take in an input for the number of players

  #lazy man's do-while loop
  while True:
    player_num = input("Please enter the current number of players (maximum 8): ")
    # if we have a reasonable number, allow the program to continue
    try:
      player_num = int(player_num)
      if 1 < player_num <= 8:
        break
    except ValueError:
      print("Invalid input. Please enter a number.")
  
  # which round is it, as we'll have that many cards in hand for each player
  while True:
    round_num = input("Please enter the current round number: ")
    try:
      round_num = int(round_num)
      if 0 < round_num <= 12:
        break
    except ValueError:
      print("Invalid input. Please enter a number.")


  total_cards_in_hand_start = player_num * round_num

  print(f"Starting calculations: {player_num} players during round #{round_num} possess {total_cards_in_hand_start} cards in hand")




if __name__ == '__main__':
  main()