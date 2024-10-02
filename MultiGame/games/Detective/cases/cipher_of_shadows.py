import time
from slow_print import slow_print

def cipher_of_shadows():
    slow_print("\nCase 7: The Cipher of Shadows")
    time.sleep(1)

    # Case Introduction
    slow_print("\n[Senior Detective]: Detective, we’ve got a national security case on our hands.")
    slow_print("[Senior Detective]: Alexander Raines, a cryptographer who specialized in breaking high-level encryption, was found dead in his study.")
    slow_print("[Senior Detective]: The cause of death is unclear—no signs of struggle, no obvious injuries. But he left behind a coded message.")
    slow_print("[Senior Detective]: The problem is, his work was so sensitive that whatever’s hidden in that message could cause massive damage.")
    slow_print("[You]: What do we know about his current projects?")
    slow_print("[Senior Detective]: He was working on something big—something he couldn’t talk about. We need to crack that cipher before anyone else does.")
    print('''__]_____]____]_____]______]_______]_____]______]______]______]___]
                         _                       _______  |||"||;;|.||##||=|||
              _                           _     |   *  3| |||-|| =|-||==||+|||
              ____________       _              |       | |||_||__|_||__||_|||
            |`.   --__     `.        _______    |       | ||================||
            |  `._____________`.  .'|.-----.|   _ ======| ||| | -|&|^^|!!|-|||
            |   | .-----------.| |  ||     ||  (o))   _ | ||| |**|=|+-|##|=|||
            |   | |  .-------.|| |  ||     ||  /||   / \`._|  .-.|_|__|__|_|||
            |   | |  |       |||_`..|'_____'| //||___\_/.'\| (( ))==========||
            |   | |`.|  ==== ||| | `---------(o)||         \  /-'-=|+|.-|-'|||
            |`. | |`.|_______|||/|______________||__.--._ (o)/|=|;:|-|&&|&&|||
            |  `|_|===========||_|                 (____)-.'(o)_|__|_|__|__|||
            |   | |  .-------.||                           `._\=============||
            |   | |  |       |||                             `.     |       ||
            |   | |`.|  ==== |||`._____________________________`.  o|o      ||
            |`. | |`.|_______||| |._.----------------.__.-------.|__|_______||
            |  `|_|===========|| || '----------------'  | .---. ||  __
            |   | |  .-------.|| ||               |     |_______||.'\.'.
            |   | |  |       ||| || ______________|     | .---. ||'.__.'
            |   | |`.|  ==== ||| ||                `.   |_______|||  _ |
             `. | |`.|_______||| ||                  `. | .---. |||_  ||
               `|_|========LGB||`||                    `|_______|||____|
                                   `.                    `.
                                     `.____________________`.''')
    # Present evidence
    slow_print("\n[Senior Detective]: Here’s what we found at the scene: A coded letter, a strange key, and his computer—locked with another encryption.")
    slow_print("[Senior Detective]: There were also three people who visited him in the last 48 hours. Start wherever you think is best.")
    
    # Evidence and suspects
    print("\nEvidence:")
    print("1. Coded Letter")
    print("2. Strange Key")
    print("3. Locked Computer")

    print("\nSuspects:")
    print("1. Sarah Linden (His Colleague)")
    print("2. Marcus Boyd (A Corporate Rival)")
    print("3. Isabelle Reyes (His Fiancée)")

    choice = input("\nWhich piece of evidence or suspect would you like to investigate first? (1-6): ")

    if choice == '1':
        investigate_coded_letter()
    elif choice == '2':
        investigate_strange_key()
    elif choice == '3':
        investigate_locked_computer()
    elif choice == '4':
        question_colleague()
    elif choice == '5':
        question_rival()
    elif choice == '6':
        question_fiancee()
    else:
        slow_print("\n[Senior Detective]: Choose wisely, detective. This is a matter of national security.")
        cipher_of_shadows()  # Recursive call for valid choice

def investigate_coded_letter():
    slow_print("\n[You]: Let’s take a closer look at the coded letter.")
    slow_print("\nYou unfold the letter. It’s filled with cryptic symbols and numbers, but there’s one phrase you can read: 'Shadow’s edge.'")
    slow_print("[You]: The phrase 'Shadow’s edge'—it feels deliberate.")
    slow_print("[Senior Detective]: That could be a clue to break the cipher.")
    return_to_investigation()

def investigate_strange_key():
    slow_print("\n[You]: Let’s examine the strange key.")
    slow_print("\nThe key is heavy, made of an unknown metal, and inscribed with what looks like coordinates.")
    slow_print("[You]: These coordinates…they could lead to a location, but they don’t match anything we’ve seen.")
    slow_print("[Senior Detective]: Check if this key connects with anything else we’ve found, or if it unlocks more than just a door.")
    return_to_investigation()

def investigate_locked_computer():
    slow_print("\n[You]: Let’s see what we can find on his computer.")
    slow_print("[Senior Detective]: The computer’s locked with an advanced encryption. We need the key.")
    slow_print("\nAs you examine the lock, you realize it’s connected to the phrase 'Shadow’s edge.' The cipher from the letter might help unlock it.")
    slow_print("[You]: We need to decode the letter first to access his files.")
    return_to_investigation()

def question_colleague():
    slow_print("\n[You]: Sarah Linden. You were one of Alexander’s closest colleagues. What can you tell me about his work?")
    slow_print("[Sarah]: He was brilliant, but paranoid. He believed someone was after his research.")
    slow_print("[You]: Did he ever mention 'Shadow’s edge' to you?")
    slow_print("[Sarah]: Yes, once. He said it was the key to unlocking the most dangerous secret he’d ever uncovered.")
    slow_print("[You]: Any idea what that secret might be?")
    slow_print("[Sarah]: He didn’t trust anyone enough to share it. But I think it had something to do with national security—something big.")
    return_to_investigation()

def question_rival():
    slow_print("\n[You]: Marcus Boyd. You’ve been competing with Alexander for years. Was there bad blood between you?")
    slow_print("[Marcus]: Look, I respected the guy, but yeah, we were rivals. He always seemed two steps ahead, and it drove me nuts.")
    slow_print("[You]: Did you know he was working on something related to 'Shadow’s edge?'")
    slow_print("[Marcus]: Never heard of it. But if it’s what I think, he might’ve stumbled onto something worth billions.")
    slow_print("[You]: Did you have anything to do with his death?")
    slow_print("[Marcus]: Are you kidding me? I didn’t need to take him out—his own paranoia was doing that just fine.")
    return_to_investigation()

def question_fiancee():
    slow_print("\n[You]: Isabelle Reyes. You were engaged to Alexander. Did you notice anything strange about him recently?")
    slow_print("[Isabelle]: He was distant, consumed by his work. He said he was close to cracking something, but it scared him.")
    slow_print("[You]: Did he ever mention 'Shadow’s edge' to you?")
    slow_print("[Isabelle]: Yes. He said it was the key to either saving everything…or losing everything.")
    slow_print("[You]: Do you think he was murdered?")
    slow_print("[Isabelle]: I don’t know. But whatever he was working on, it was dangerous.")
    return_to_investigation()

def return_to_investigation():
    print("\nWhat would you like to do next?")
    print("1. Investigate another piece of evidence")
    print("2. Question another suspect")
    print("3. Try to decode the letter")
    print("4. Make an accusation")

    choice = input("\nChoose your next action (1/2/3/4): ")

    if choice == '1':
        cipher_of_shadows()  # Return to investigation
    elif choice == '2':
        cipher_of_shadows()  # Return to suspect questioning
    elif choice == '3':
        decode_letter()
    elif choice == '4':
        accuse_suspect()
    else:
        slow_print("\n[Senior Detective]: Stay focused, detective. This is a high-stakes case.")
        return_to_investigation()

def decode_letter():
    slow_print("\n[You]: Let’s try to decode the letter.")
    slow_print("[Senior Detective]: We need to figure out what 'Shadow’s edge' means.")
    slow_print("\nAfter analyzing the symbols and numbers, you notice a pattern. The phrase 'Shadow’s edge' refers to a specific encryption method.")
    slow_print("[You]: It’s a code used by intelligence agencies. The cipher hides the real message behind the coordinates on the key!")
    slow_print("[Senior Detective]: We’ve got the key—let’s use it to unlock his computer.")
    return_to_investigation()

def accuse_suspect():
    print("\nWho do you think is responsible for Alexander’s death?")
    print("1. Sarah Linden (Colleague)")
    print("2. Marcus Boyd (Corporate Rival)")
    print("3. Isabelle Reyes (Fiancée)")

    choice = input("\nMake your accusation (1/2/3): ")

    if choice == '1':
        slow_print("\n[You]: Sarah was the only one who knew about the encryption method and the meaning of 'Shadow’s edge.'")
        slow_print("[Senior Detective]: She wanted his research for herself, didn’t she?")
        slow_print("[You]: Yes, she knew it was the key to unlocking untold power. She killed him to steal his work.")
        slow_print("[Senior Detective]: Well done, detective. You cracked it.")
    elif choice == '2':
        slow_print("\n[You]: Marcus had the motive—he wanted Alexander’s research for corporate gain.")
        slow_print("[Senior Detective]: But there’s no solid evidence connecting him to the murder.")
        return_to_investigation()
    elif choice == '3':
        slow_print("\n[You]: Isabelle had the opportunity, but no clear motive. I don’t think she did it.")
        return_to_investigation()
    else:
        slow_print