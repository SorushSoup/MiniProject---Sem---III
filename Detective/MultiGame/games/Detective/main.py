import time
from slow_print import slow_print

from cases.broken_vase import broken_vase
from cases.cipher_of_shadows import cipher_of_shadows
from cases.disappearing_artist import disappearing_artist
from cases.library_robbery import library_robbery
from cases.mansion_murder import mansion_murder
from cases.mirror_of_lies import mirror_of_lies
from cases.missing_pet import missing_pet
from cases.poisoned_painting import poisoned_painting
from cases.stolen_necklace import stolen_necklace
from cases.time_paradox import time_paradox



def main():
    slow_print("Welcome to the Detective Agency, where mysteries abound and coffee is a vital resource!")
    
    slow_print("\n[Senior Detective]: Ah, finally! The ‘great’ detective has decided to show up.")
    slow_print("[Senior Detective]: I hope you're ready to put in some effort today, or are you just planning to lounge around?")
    
    slow_print("\n[User]: Come on! A true detective knows how to conserve energy for the big cases!")
    
    slow_print("\n[Senior Detective]: Right... because solving crimes is just a hobby, isn't it? Let's see what mess we have to clean up today.")
    
    slow_print("\nHere are the cases you can tackle today:")
    print("1. The Missing Necklace (Easy)")
    print("2. The Vase Robbery (Easy)")
    print("3. The Library Robbery (Easy)")
    print("4. The Missing Pet (Easy)")
    print("5. The Poisoned Painting (Medium)")
    print("6. The Disappearing Artist (Medium)")
    print("7. The Mansion Murder Mystery (Medium)")
    print("8. The Mirror of Lies (Hard)")
    print("9. The Time Paradox (Hard)")

    choice = int(input("\nChoose a case number (1-9): "))
    
    switch_case(choice)

def switch_case(case_number):
    if case_number == 1:
        stolen_necklace()  # Case 1: The Missing Necklace (Easy)
    elif case_number == 2:
        broken_vase()         # Case 2: The Vase Robbery (Easy)
    elif case_number == 3:
        library_robbery()      # Case 3: The Library Robbery (Easy)
    elif case_number == 4:
        missing_pet()          # Case 4: The Missing Pet (Easy)
    elif case_number == 5:
        poisoned_painting() # Case 5: The Poisoned Painting (Medium)
    elif case_number == 6:
        disappearing_artist() # Case 6: The Disappearing Artist (Medium)
    elif case_number == 7:
        mansion_murder()    # Case 7: The Mansion Murder Mystery (Medium)
    elif case_number == 8:
        mirror_of_lies()    # Case 8: The Mirror of Lies (Hard)
    elif case_number == 9:
        time_paradox()      # Case 9: The Time Paradox (Hard)
    else:
        slow_print("\n[Senior Detective]: Really? That’s your choice? Let’s stick to the cases at hand.")
        main()  # Restart the selection process

# Call the main function to start the game
main()