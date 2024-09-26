import time
from slow_print import slow_print

def disappearing_artist():
    slow_print("\nCase 4: The Disappearing Artist")
    time.sleep(1)
    
    # Case introduction
    slow_print("\n[Senior Detective]: Strange one, this is. Renowned painter Thomas Vance has gone missing. Last seen in his studio.")
    slow_print("[Senior Detective]: His wife reported him missing this morning, but here’s the weird part… the studio was locked from the inside.")
    slow_print("[Senior Detective]: No signs of struggle, no ransom notes, nothing. Just an empty studio.")
    slow_print("[Senior Detective]: We’ve got three suspects: his wife, his agent, and a rival artist.")
    slow_print("[Senior Detective]: Let’s figure out what happened. Was it an abduction, or did he just vanish into thin air?")

    # Present suspects
    slow_print("\n[You]: I’ll start by questioning the suspects.")
    
    print("\nSuspects:")
    print("1. The Wife")
    print("2. The Agent")
    print("3. The Rival Artist")
    
    choice = input("\nWho would you like to question first? (1/2/3): ")
    
    if choice == '1':
        question_wife()
    elif choice == '2':
        question_agent()
    elif choice == '3':
        question_rival()
    else:
        slow_print("\n[Senior Detective]: Get focused, detective! Pick one from the list.")
        disappearing_artist()  # Recursive call for valid choice

def question_wife():
    slow_print("\n[You]: Where were you when Thomas disappeared?")
    slow_print("[Wife]: I was home, in our bedroom. Thomas often worked late into the night, so I didn’t think much of it when I didn’t see him until morning.")
    slow_print("[Wife]: But when I went to check on him this morning, the studio was locked. I had to break in, but he wasn’t there.")
    slow_print("[You]: How was your relationship with your husband?")
    slow_print("[Wife]: We had our ups and downs, like any couple, but I’d never harm him. He was… distant lately, absorbed in his work.")
    slow_print("[Senior Detective]: She seems genuine, but we should confirm her story. Let’s keep digging.")
    return_to_suspects()

def question_agent():
    slow_print("\n[You]: What can you tell me about Thomas Vance’s recent activities?")
    slow_print("[Agent]: Thomas was working on a major piece, a new painting that was supposed to be his magnum opus. He was stressed, talking about it obsessively.")
    slow_print("[Agent]: He told me he’d been feeling watched, but I thought it was just the pressure getting to him.")
    slow_print("[You]: Was there anyone else in his life who might want to harm him?")
    slow_print("[Agent]: Not that I know of, but rivalries in the art world can get… intense.")
    slow_print("[Senior Detective]: Hmm… this ‘feeling watched’ bit could mean something. Let’s check the studio for clues.")
    return_to_suspects()

def question_rival():
    slow_print("\n[You]: What was your relationship with Thomas like?")
    slow_print("[Rival]: We weren’t friends, that’s for sure. We competed for the same gallery spots, but nothing serious. His work was too abstract for my taste.")
    slow_print("[Rival]: I heard he was working on something big. Maybe he just ran off to get away from the pressure. Who knows with artists?")
    slow_print("[You]: Any reason why you’d want him gone?")
    slow_print("[Rival]: Look, I don’t care for the guy, but I don’t have anything to gain from his disappearance.")
    slow_print("[Senior Detective]: He’s dismissive, but rivals can have hidden motives. Let’s see if we can find any leads at the gallery.")
    return_to_suspects()

def return_to_suspects():
    print("\nWhat would you like to do next?")
    print("1. Question another suspect")
    print("2. Investigate the studio")
    print("3. Examine Thomas’ latest painting")
    print("4. Check phone records")
    print("5. Accuse a suspect")
    
    choice = input("\nChoose an action (1/2/3/4/5): ")
    
    if choice == '1':
        disappearing_artist()  # Return to suspect questioning
    elif choice == '2':
        investigate_studio()
    elif choice == '3':
        examine_painting()
    elif choice == '4':
        check_phone_records()
    elif choice == '5':
        accuse_suspect()
    else:
        slow_print("\n[Senior Detective]: Stay sharp, detective. Make a valid choice.")
        return_to_suspects()

def investigate_studio():
    slow_print("\n[You]: Let’s take a closer look at the studio.")
    slow_print("[Senior Detective]: Good idea. Maybe there’s something we missed.")
    slow_print("\nYou enter the studio and notice the canvas is covered with a cloth. The paint is fresh.")
    slow_print("[Senior Detective]: It looks like he was working until late, but there’s something odd here.")
    slow_print("\nYou find a hidden door behind a bookshelf. The latch is slightly ajar.")
    slow_print("[Senior Detective]: A secret room? What was Thomas hiding?")
    slow_print("[You]: Let’s check this room out.")
    return_to_suspects()

def examine_painting():
    slow_print("\n[You]: I want to examine Thomas’ latest painting.")
    slow_print("[Senior Detective]: Good call. It could have some clues.")
    slow_print("\nYou remove the cloth from the canvas. The painting is incomplete, but the imagery is haunting.")
    slow_print("[You]: It’s a surreal scene of a man trapped in a maze. The details are intricate, almost as if Thomas was trying to communicate something.")
    slow_print("\nUpon closer inspection, you notice a series of numbers painted faintly in the background: 1975-12-15.")
    slow_print("[Senior Detective]: Could these be important? Let’s make a note of them. There’s a message in this art, no doubt.")
    return_to_suspects()

def check_phone_records():
    slow_print("\n[You]: Time to check Thomas’ phone records. Maybe he contacted someone before disappearing.")
    slow_print("[Senior Detective]: I’ve got the records right here. Looks like he made a few late-night calls.")
    slow_print("\nThe last call was made at 2 AM to his agent. Before that, several calls to an unknown number were made.")
    slow_print("[You]: Can we trace that number?")
    slow_print("[Senior Detective]: It’s a burner phone. Whoever he was talking to didn’t want to be traced.")
    return_to_suspects()

def accuse_suspect():
    print("\nWho do you think is involved in Thomas Vance’s disappearance?")
    print("1. The Wife")
    print("2. The Agent")
    print("3. The Rival Artist")
    
    choice = input("\nMake your accusation (1/2/3): ")
    
    if choice == '1':
        slow_print("\n[Senior Detective]: The wife? She found him missing, but there’s no evidence that she was involved.")
        return_to_suspects()
    elif choice == '2':
        slow_print("\n[Senior Detective]: The agent… He mentioned that Thomas was feeling watched. And that late-night call is suspicious.")
        slow_print("[Senior Detective]: He could have been manipulating Thomas, pushing him to the brink.")
        slow_print("\n[You]: I think the agent had a hand in this. He knew too much about Thomas’ mental state.")
        slow_print("[Senior Detective]: Well done, detective. It seems like the agent was behind this. He pressured Thomas to finish the painting, knowing it would drive him mad.")
        slow_print("[Senior Detective]: Thomas’ disappearance was orchestrated. He’s probably still alive, but in hiding. We’ll get a warrant for the agent’s arrest.")
    elif choice == '3':
        slow_print("\n[Senior Detective]: The rival artist? He didn’t have much motive to be involved in the disappearance.")
        return_to_suspects()
    else:
        slow_print("\n[Senior Detective]: Focus, detective! Pick a real option.")
        accuse_suspect()