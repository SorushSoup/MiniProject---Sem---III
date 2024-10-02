import time
from slow_print import slow_print

def stolen_necklace():  #replace with case_stolen_necklace
    slow_print("\nCase 1: The Missing Necklace")
    time.sleep(1)
    
    # Case introduction
    slow_print("\n[Senior Detective]: Alright, rookie, here's the situation. Mrs. Thompson's necklace has gone missing.")
    slow_print("[Senior Detective]: Three suspects were in the house when it happened: the maid, the gardener, and her niece.")
    slow_print("[Senior Detective]: You need to figure out who took it.")
    slow_print("[Senior Detective]: I've got a hunch, but I'll let you handle this. Ask questions, gather clues, and don't mess this up.")
    print('''

                o--o--=g=--o--o     
               /      .'       \
               o      '.       o
                \             /
                 o           o
                  \         /
                   o       o
                    \     /
                     o   o
                      \_/
                       =
                      .^.
                     '   '
                     '. .'
                       !    lc
                       

             ''')
    # Present suspects
    slow_print("\n[You]: Let's start by questioning the suspects.")
    
    print("\nSuspects:")
    print("1. The Maid")
    print("2. The Gardener")
    print("3. The Niece")
    
    choice = input("\nWho would you like to question first? (1/2/3): ")
    
    if choice == '1':
        question_maid()  #paste
    elif choice == '2':
        question_gardener()  #paste
    elif choice == '3':
        question_niece()  #paste
    else:
        slow_print("\n[Senior Detective]: Focus, detective! Pick a valid option.")
        stolen_necklace()  # Recursive call for valid choice

def question_maid():  #paste
    slow_print("\n[You]: Can you tell me where you were when the necklace went missing?")
    slow_print("[Maid]: I was in the kitchen preparing lunch. I didn't go anywhere near the bedroom, I swear!")
    slow_print("[Senior Detective]: She seems nervous. Let's see what the others have to say.")
    return_to_suspects()  # Call to return to suspects

def question_gardener():  #paste
    slow_print("\n[You]: What were you doing at the time of the theft?")
    slow_print("[Gardener]: I was outside trimming the hedges. I don’t even know where Mrs. Thompson keeps her jewelry.")
    slow_print("[Senior Detective]: Hmm, a gardener who never steps inside? Sounds suspicious.")
    return_to_suspects()  # Call to return to suspects

def question_niece():  #paste
    slow_print("\n[You]: Where were you when the necklace went missing?")
    slow_print("[Niece]: I was in my room, reading a book. I didn't see or hear anything unusual.")
    slow_print("[Senior Detective]: A quiet alibi... convenient. Let's piece this together, detective.")
    return_to_suspects()  # Call to return to suspects

def return_to_suspects():  # Function to return to suspect questioning
    print("\nWhat would you like to do next?")
    print("1. Question another suspect")
    print("2. Examine the crime scene")
    print("3. Accuse a suspect")
    
    choice = input("\nChoose an action (1/2/3): ")
    
    if choice == '1':
        stolen_necklace()  # Return to suspect questioning
    elif choice == '2':
        examine_crime_scene()  # Call to examine the crime scene
    elif choice == '3':
        accuse_suspect()  # Call to accuse a suspect
    else:
        slow_print("\n[Senior Detective]: Get your act together and pick a valid option.")
        return_to_suspects()  # Recursive call for valid choice

def examine_crime_scene():  #paste
    slow_print("\n[You]: Let's take a closer look at the crime scene.")
    slow_print("[Senior Detective]: Good thinking. Always start with the scene.")
    slow_print("\nYou find a broken window in the bedroom, with dirt on the floor near the window.")
    slow_print("[Senior Detective]: That gardener might have been closer to the house than he said.")
    
    return_to_suspects()  # Return to suspects

def accuse_suspect():  #paste
    print("\nWho do you think is the culprit?")
    print("1. The Maid")
    print("2. The Gardener")
    print("3. The Niece")
    
    choice = input("\nMake your accusation (1/2/3): ")
    
    if choice == '1':
        slow_print("\n[Senior Detective]: The maid? Nah, I don't think she had the opportunity.")
        slow_print("\n[You]: I guess you're right. Let's keep looking.")
        return_to_suspects()
    elif choice == '2':
        slow_print("\n[Senior Detective]: The gardener, eh? I think you're onto something.")
        slow_print("[Senior Detective]: He was trimming hedges but there was dirt in the bedroom... Seems fishy.")
        slow_print("[Senior Detective]: Good job, detective! We've got him.")
        slow_print("\n[You]: Case solved! The gardener broke in through the window and stole the necklace.")
    elif choice == '3':
        slow_print("\n[Senior Detective]: The niece? She didn't seem too suspicious, but let's keep looking.")
        return_to_suspects()
    else:
        slow_print("\n[Senior Detective]: Seriously? Pick a valid option.")
        accuse_suspect()  # Recursive call for valid choice