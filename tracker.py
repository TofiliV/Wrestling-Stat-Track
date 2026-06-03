wrestlers = {}
while True:
  print("n--- Wrestling Season Tracker ---")
  print("1. Add Wrestler")
  print("2. View Records")
  print("3. Exit")
  choice = input("Choose an option: ")
  if choice == "1":
    name = input ("Wrestler name: ")
    wins = int(input("Wins: "))
    losses = int(input( "Losses: "))
    wrestlers[name] = { "wins": wins, "losses": losses}
    print(f"{name} added!")
  elif choice == "2":
    print ("\nTeam Records")
    for name, record in wrestler.items():
      wins = record["wins"]
      losses = record["losses"]
      total_matches = wins + losses
      if total_matches > 0:
        win_percent = (wins/ total_matches) * 100
      else:
        win_percent = 0
      print( f"{name}: {wins}-{losses} "
      f"({win percent:.1f}% win rate
          elif choice == "3""
      break
      else: print(Invalid option.")
