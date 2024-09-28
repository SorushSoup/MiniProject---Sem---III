import time
from slow_print import slow_print

def mirror_of_lies():
    slow_print("\nCase 6: The Mirror of Lies")
    time.sleep(1)

    # Case Introduction
    slow_print("\n[Senior Detective]: Detective, I’ve got a twisted one for you.")
    slow_print("[Senior Detective]: Anna Brightwood, a well-known psychiatrist, was found dead in her office.")
    slow_print("[Senior Detective]: The police ruled it a suicide, but something feels off. Her diary suggests she believed she was losing her mind.")
    slow_print("[Senior Detective]: But here’s the kicker – everyone close to her is hiding something. The more you talk to them, the less sense it all makes.")
    slow_print("[Senior Detective]: We need to get to the bottom of this. Was it really suicide, or was Anna driven to her death by something much darker?")
    print('''      //-----------\\
                 //       | |   | \\
               //  \__   /   \ /  | \\
              ||       \|     |  / __||
              ||         \    | |_/  ||
              ||\     __  |   |/ __  ||
              ||  \__/   \|   |_/  \_||
              ||  _    ___|  /  \_   ||
              ||_/ \__/   |/_     \_/||
              ||          o  \      _||
              ||\       / |    \___/ ||
              ||  \___/   |     \   /||
              ||     |   / \_    )-<_||
              ||    /  /     \  /    ||
               \\ /   |      _><    //
               //\\   |     /   \ //\\
              ||   \\-----------//   ||
              ||                     ||
             /||\                   /||\
            /____\                 /____\

             ''')
    slow_print("\n[You]: Let’s start by talking to her closest contacts.")
    
    # Present suspects
    print("\nSuspects:")
    print("1. David Brightwood (Her Husband)")
    print("2. Elise Norewood (Her Protégé)")
    print("3. Vincent Cruz (Her Patient)")
    
    choice = input("\nWho would you like to question first? (1/2/3): ")

    if choice == '1':
        question_husband()
    elif choice == '2':
        question_protege()
    elif choice == '3':
        question_patient()
    else:
        slow_print("\n[Senior Detective]: Focus. Choose a suspect to question.")
        mirror_of_lies()  # Recursive call for valid choice

def question_husband():
    slow_print("\n[You]: Where were you on the night of Anna’s death?")
    slow_print("[David]: I was at home. Anna had been distant lately, locked up in her office most of the time.")
    slow_print("[You]: Any idea why she might have felt that way?")
    slow_print("[David]: She started becoming paranoid, talking about her patients controlling her thoughts. I thought it was burnout.")
    slow_print("[You]: Did she mention any specific patient causing these feelings?")
    slow_print("[David]: She didn’t name anyone, but she kept a journal. She wrote down everything.")
    slow_print("[Senior Detective]: We should get our hands on that journal. Could reveal a lot about her state of mind.")
    return_to_suspects()

def question_protege():
    slow_print("\n[You]: You were Anna’s protégé. What was your relationship like?")
    slow_print("[Elise]: She was a mentor to me. Brilliant, but she started changing. She became obsessed with the idea that someone was manipulating her mind.")
    slow_print("[You]: Did she ever accuse anyone?")
    slow_print("[Elise]: No, but she said something chilling the last time we spoke.")
    slow_print("[You]: What did she say?")
    slow_print("[Elise]: 'I see my lies reflected in others, but they don’t belong to me.' I didn’t understand what she meant at the time, but now…")
    slow_print("[Senior Detective]: Sounds like psychological manipulation. Someone was messing with her perception.")
    return_to_suspects()

def question_patient():
    slow_print("\n[You]: You were seeing Dr. Brightwood as a patient. What can you tell me?")
    slow_print("[Vincent]: She was helping me deal with my paranoia. But a few months ago, she changed.")
    slow_print("[You]: How did she change?")
    slow_print("[Vincent]: She said my delusions were rubbing off on her. That my thoughts were becoming hers.")
    slow_print("[You]: Do you believe someone else could have been manipulating her?")
    slow_print("[Vincent]: She believed so, but I didn’t think it was real. Now I’m not so sure.")
    slow_print("[Senior Detective]: This patient could’ve influenced her somehow, or maybe someone else made her believe that. Let’s dig deeper.")
    return_to_suspects()

def return_to_suspects():
    print("\nWhat would you like to do next?")
    print("1. Question another suspect")
    print("2. Investigate Anna’s office")
    print("3. Read Anna’s journal")
    print("4. Check her phone records")
    print("5. Make an accusation")

    choice = input("\nChoose an action (1/2/3/4/5): ")

    if choice == '1':
        mirror_of_lies()  # Return to suspect questioning
    elif choice == '2':
        investigate_office()
    elif choice == '3':
        read_journal()
    elif choice == '4':
        check_phone_records()
    elif choice == '5':
        accuse_suspect()
    else:
        slow_print("\n[Senior Detective]: Stay sharp. Choose wisely.")
        return_to_suspects()

def investigate_office():
    slow_print("\n[You]: Let’s check her office for clues.")
    slow_print("[Senior Detective]: We need to understand what was going through her mind.")
    slow_print("\nYou walk into Anna's office. It’s a mess—papers scattered, books thrown to the floor. Her desk holds an antique mirror.")
    slow_print("[You]: This mirror seems important. It’s out of place.")
    slow_print("\nYou notice scratches around the mirror’s edges. The glass is cracked slightly.")
    slow_print("[Senior Detective]: Could this mirror be connected to her state of mind?")
    slow_print("\nYou find a note beneath the mirror.")
    slow_print("[You]: It’s part of a journal entry: 'I see their lies reflected in me. It’s like they’re controlling my thoughts.'")
    slow_print("[Senior Detective]: Someone made her believe she was losing control. The question is, who?")
    return_to_suspects()

def read_journal():
    slow_print("\n[You]: Let’s read through Anna’s journal.")
    slow_print("[Senior Detective]: This might reveal her mental state in the days leading up to her death.")
    slow_print("\nYou open the journal and flip through the entries.")
    slow_print("[You]: Most of it is about her patients, but here’s an entry about Vincent.")
    slow_print("[You]: 'Vincent says he feels controlled. But is it me who’s controlling him? Or am I the one being controlled?'")
    slow_print("\nFurther down, you find a disturbing entry.")
    slow_print("[You]: 'The mirror shows me things that aren’t real. Am I hallucinating, or is someone messing with my mind?'")
    slow_print("[Senior Detective]: Sounds like someone planted the idea in her head that she was losing her sanity.")
    slow_print("\nThe journal ends with the words: 'I’m not me anymore.'")
    return_to_suspects()

def check_phone_records():
    slow_print("\n[You]: Let’s pull her phone records.")
    slow_print("[Senior Detective]: Maybe she reached out to someone for help before she died.")
    slow_print("\nYou sift through the phone logs and find repeated calls to an unknown number.")
    slow_print("[You]: She called this number almost daily in the last two weeks.")
    slow_print("[Senior Detective]: We’ll need to trace that number. It could be the key to understanding who was influencing her.")
    return_to_suspects()

def accuse_suspect():
    print("\nWho do you think was responsible for Anna’s death?")
    print("1. David Brightwood (Husband)")
    print("2. Elise Norewood (Protégé)")
    print("3. Vincent Cruz (Patient)")

    choice = input("\nMake your accusation (1/2/3): ")

    if choice == '1':
        slow_print("\n[Senior Detective]: Her husband had the most access to her, but there’s no hard evidence linking him to the manipulation.")
        return_to_suspects()
    elif choice == '2':
        slow_print("\n[Senior Detective]: Elise was close to her, but was she manipulating Anna? There’s no conclusive proof.")
        return_to_suspects()
    elif choice == '3':
        slow_print("\n[Senior Detective]: Vincent... It was him all along, wasn’t it?")
        slow_print("[You]: I think so. Vincent’s delusions became Anna’s reality. He was manipulating her, maybe without even realizing it.")
        slow_print("[Senior Detective]: His paranoia infected her mind, and she couldn’t tell what was real anymore.")
        slow_print("[You]: He may not have meant to kill her, but his influence drove her to the edge.")
        slow_print("[Senior Detective]: You cracked it, detective. Good work.")
    else:
        slow_print("\n[Senior Detective]: Keep your head in the game, detective. Make a solid choice.")
        return_to_suspects()
