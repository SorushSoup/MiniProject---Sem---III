import time
from slow_print import slow_print

def broken_vase():
    slow_print("\nCase 2: The Broken Vase")
    time.sleep(1)
    
    # Case introduction
    slow_print("\n[Senior Detective]: Well, rookie, here’s another one for you.")
    slow_print("[Senior Detective]: Mr. Wilson’s priceless vase has been smashed to pieces.")
    slow_print("[Senior Detective]: He swears none of the three people in the house could’ve done it.")
    slow_print("[Senior Detective]: But we know better, don’t we?")
    slow_print("[Senior Detective]: The suspects are the butler, Mr. Wilson's daughter, and his friendly neighbor. Time to figure out who’s behind this mess.")
    
    # Present suspects
    slow_print("\n[You]: Let’s start questioning the suspects.")
    
    print("\nSuspects:")
    print("1. The Butler")
    print("2. Mr. Wilson's Daughter")
    print("3. The Neighbor")
    
    choice = input("\nWho would you like to question first? (1/2/3): ")
    
    if choice == '1':
        question_butler()
    elif choice == '2':
        question_daughter()
    elif choice == '3':
        question_neighbor()
    else:
        slow_print("\n[Senior Detective]: Get serious, detective. Pick someone to question.")
        broken_vase()

def question_butler():
    slow_print("\n[You]: Where were you when the vase was broken?")
    slow_print("[Butler]: I was in the kitchen preparing tea. I didn’t even know the vase was broken until Mr. Wilson called me.")
    slow_print("[Senior Detective]: Hmm... doesn't sound like he’s lying, but let's not rule anyone out just yet.")
    return_to_suspects()

def question_daughter():
    slow_print("\n[You]: What were you doing when the vase was broken?")
    slow_print("[Daughter]: I was in the garden reading a book. The vase was already broken when I came back in.")
    slow_print("[Senior Detective]: A likely story. But she could’ve easily slipped in and out, don’t you think?")
    return_to_suspects()

def question_neighbor():
    slow_print("\n[You]: What were you doing at the time of the incident?")
    slow_print("[Neighbor]: I was in the living room, sitting on the couch. I didn’t touch the vase!")
    slow_print("[Senior Detective]: You were in the same room, but didn’t see anything? Suspicious.")
    return_to_suspects()

def return_to_suspects():
    print("\nWhat would you like to do next?")
    print("1. Question another suspect")
    print("2. Examine the crime scene")
    print("3. Accuse a suspect")
    
    choice = input("\nChoose an action (1/2/3): ")
    
    if choice == '1':
        broken_vase()  # Return to suspect questioning
    elif choice == '2':
        examine_crime_scene()
    elif choice == '3':
        accuse_suspect()
    else:
        slow_print("\n[Senior Detective]: Don’t waste my time. Choose something useful.")
        return_to_suspects()

def examine_crime_scene():
    slow_print("\n[You]: Let’s take a closer look at the crime scene.")
    slow_print("[Senior Detective]: Always a smart move.")
    slow_print("\nYou examine the shattered vase and notice small pieces of glass on the couch, right where the neighbor was sitting.")
    slow_print("[Senior Detective]: Well, well, look at that! The neighbor was sitting right in the middle of the mess.")
    
    return_to_suspects()

def accuse_suspect():
    print("\nWho do you think is responsible for breaking the vase?")
    print("1. The Butler")
    print("2. Mr. Wilson's Daughter")
    print("3. The Neighbor")
    
    choice = input("\nMake your accusation (1/2/3): ")
    
    if choice == '1':
        slow_print("\n[Senior Detective]: The butler? Unlikely. He wasn’t even in the room.")
        slow_print("[Senior Detective]: Think harder.")
        return_to_suspects()
    elif choice == '2':
        slow_print("\n[Senior Detective]: The daughter? Doesn't quite fit. Try again.")
        return_to_suspects()
    elif choice == '3':
        slow_print("\n[Senior Detective]: Ah, the neighbor. Sitting right on the couch where the glass was found.")
        slow_print("[Senior Detective]: He must have accidentally knocked it over. Nice work, detective!")
        slow_print("[Senior Detective]: The case is closed, the neighbor’s careless behavior is to blame for the broken vase.")
    else:
        slow_print("\n[Senior Detective]: You’re better than this, detective. Choose properly.")
        accuse_suspect()