import time
from slow_print import slow_print

def library_robbery():
    slow_print("\nStarting: Case 2 - The Library Robbery")
    slow_print("[Senior Detective]: A valuable book has gone missing from the library.")
    slow_print("[Senior Detective]: We have three suspects: the librarian, a regular visitor, and a book club member.")
    slow_print("[Senior Detective]: Let’s start questioning the suspects.")
    print('''   ____________________________________________________
              |____________________________________________________|
              | __     __   ____   ___ ||  ____    ____     _  __  |
              ||  |__ |--|_| || |_|   |||_|**|*|__|+|+||___| ||  | |
              ||==|^^||--| |=||=| |=*=||| |~~|~|  |=|=|| | |~||==| |
              ||  |##||  | | || | |JRO|||-|  | |==|+|+||-|-|~||__| |
              ||__|__||__|_|_||_|_|___|||_|__|_|__|_|_||_|_|_||__|_|
              ||_______________________||__________________________|
              | _____________________  ||      __   __  _  __    _ |
              ||=|=|=|=|=|=|=|=|=|=|=| __..\/ |  |_|  ||#||==|  / /|
              || | | | | | | | | | | |/\ \  \\|++|=|  || ||==| / / |
              ||_|_|_|_|_|_|_|_|_|_|_/_/\_.___\__|_|__||_||__|/_/__|
              |____________________ /\~()/()~//\ __________________|
              | __   __    _  _     \_  (_ .  _/ _    ___     _____|
              ||~~|_|..|__| || |_ _   \ //\\ /  |=|__|~|~|___| | | |
              ||--|+|^^|==|1||2| | |__/\ __ /\__| |==|x|x|+|+|=|=|=|
              ||__|_|__|__|_||_|_| /  \ \  / /  \_|__|_|_|_|_|_|_|_|
              |_________________ _/    \/\/\/    \_ _______________|
              | _____   _   __  |/      \../      \|  __   __   ___|
              ||_____|_| |_|##|_||   |   \/ __|   ||_|==|_|++|_|-|||
              ||______||=|#|--| |\   \   o    /   /| |  |~|  | | |||
              ||______||_|_|__|_|_\   \  o   /   /_|_|__|_|__|_|_|||
              |_________ __________\___\____/___/___________ ______|
              |__    _  /    ________     ______           /| _ _ _|
              |\ \  |=|/   //    /| //   /  /  / |        / ||%|%|%|
              | \/\ |*/  .//____//.//   /__/__/ (_)      /  ||=|=|=|
            __|  \/\|/   /(____|/ //                    /  /||~|~|~|__
              |___\_/   /________//   ________         /  / ||_|_|_|
              |___ /   (|________/   |\_______\       /  /| |______|
                  /                  \|________)     /  / | |       ''')
    # Present suspects
    slow_print("\n[You]: Who should I question first?")
    
    print("\nSuspects:")
    print("1. The Librarian")
    print("2. The Regular Visitor")
    print("3. The Book Club Member")
    
    choice = input("\nWho would you like to question first? (1/2/3): ")
    
    if choice == '1':
        question_librarian()
    elif choice == '2':
        question_visitor()
    elif choice == '3':
        question_book_club_member()
    else:
        slow_print("\n[Senior Detective]: Focus, detective! Pick someone to question.")
        library_robbery()

def question_librarian():
    slow_print("\n[You]: What were you doing when the book went missing?")
    slow_print("[Librarian]: I was organizing the shelves. I didn’t notice anything unusual.")
    return_to_library_suspects()

def question_visitor():
    slow_print("\n[You]: Where were you in the library?")
    slow_print("[Visitor]: I was reading at the back. I didn't see anyone suspicious.")
    return_to_library_suspects()

def question_book_club_member():
    slow_print("\n[You]: What can you tell me about the missing book?")
    slow_print("[Book Club Member]: I was here for our meeting, but I didn’t see anyone take it.")
    return_to_library_suspects()

def return_to_library_suspects():
    print("\nWhat would you like to do next?")
    print("1. Question another suspect")
    print("2. Examine the library")
    print("3. Accuse a suspect")
    
    choice = input("\nChoose an action (1/2/3): ")
    
    if choice == '1':
        library_robbery()  # Return to suspect questioning
    elif choice == '2':
        examine_library()
    elif choice == '3':
        accuse_library_suspect()
    else:
        slow_print("\n[Senior Detective]: Come on, get your act together.")
        return_to_library_suspects()

def examine_library():
    slow_print("\n[You]: Let’s take a look around the library.")
    slow_print("[Senior Detective]: Good idea. Look for anything out of place.")
    slow_print("\nYou find a torn piece of paper near the shelf where the book was last seen.")
    slow_print("[Senior Detective]: That might be a clue. Let’s connect the dots.")
    
    return_to_library_suspects()

def accuse_library_suspect():
    print("\nWho do you think took the book?")
    print("1. The Librarian")
    print("2. The Regular Visitor")
    print("3. The Book Club Member")
    
    choice = input("\nMake your accusation (1/2/3): ")
    
    if choice == '1':
        slow_print("\n[Senior Detective]: The librarian? Not likely. Let's think again.")
        return_to_library_suspects()
    elif choice == '2':
        slow_print("\n[Senior Detective]: The visitor? They were just reading. Not enough evidence.")
        return_to_library_suspects()
    elif choice == '3':
        slow_print("\n[Senior Detective]: Aha, the book club member! They had the opportunity during the meeting.")
        slow_print("[Senior Detective]: Well done! You’ve solved this case.")
    else:
        slow_print("\n[Senior Detective]: Focus, detective. You’ve got to do better.")
        accuse_library_suspect()