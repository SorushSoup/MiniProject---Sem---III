import time
from slow_print import slow_print

def time_paradox():
    slow_print("\nCase 5: The Time Paradox")
    time.sleep(1)

    # Case introduction
    slow_print("\n[Senior Detective]: Alright detective, buckle up for this one. We’ve got something… strange.")
    slow_print("[Senior Detective]: A young tech genius, Alice Hawthorne, has been found dead in her penthouse.")
    slow_print("[Senior Detective]: But there’s a catch… Her body was found in two places at once.")
    slow_print("[You]: What do you mean, two places at once?")
    slow_print("[Senior Detective]: Her body was discovered in the living room *and* on the rooftop, both at the same time.")
    slow_print("[You]: That’s impossible.")
    slow_print("[Senior Detective]: Exactly. Both bodies are identical, down to the last detail.")
    slow_print("[Senior Detective]: We’re calling it the Time Paradox case. Let’s figure out how a person can die in two places at once. Welcome to the craziest mystery you’ve ever encountered.")
    print('''             O
                            (_)
                          _ )_( _
                        /`_) H (_`\
                      .' (  { }  ) '.
                    _/ /` '-'='-' `\ \_
                   [_.'   _,...,_   '._]
                    |   .:"`````":.   |
                    |__//_________\\__|
                     | .-----------. |
                     | |  .-"""-.  | |
                     | | /    /  \ | |
                     | ||-   <   -|| |
                     | | \    \  / | |
                     | |[`'-...-'`]| |
                     | | ;-.___.-; | |
                     | | |  |||  | | |
                     | | |  |||  | | |
                     | | | _|||_ | | |
                     | | | >===< | | |
                     | | | |___| | | |
                     | | |  |||  | | |
                     | | |  ;-;  | | |
                     | | | (   ) | | |
                     | | |  '-'  | | |
                     | | '-------' | |
                    _| '-----------' |_
                   [= === === ==== == =]
                   [__--__--___--__--__]
                  /__-___-___-___-___-__\
                 `"""""""""""""""""""""""`
             ''')
    # Present suspects
    slow_print("\n[You]: I’ll start by questioning the suspects.")
    
    print("\nSuspects:")
    print("1. The Lab Assistant")
    print("2. The Investor")
    print("3. The Time Paradox Expert")

    choice = input("\nWho would you like to question first? (1/2/3): ")

    if choice == '1':
        question_lab_assistant()
    elif choice == '2':
        question_investor()
    elif choice == '3':
        question_expert()
    else:
        slow_print("\n[Senior Detective]: Keep it together! Pick one from the list.")
        time_paradox()  # Recursive call for valid choice

def question_lab_assistant():
    slow_print("\n[You]: Where were you when Alice was found dead?")
    slow_print("[Lab Assistant]: I was in the lab working on her latest project. She was obsessed with the idea of time travel.")
    slow_print("[You]: Did she make any breakthroughs?")
    slow_print("[Lab Assistant]: More than you could imagine. She was close to something big, but it scared her. She said there were ‘side effects’ she wasn’t expecting.")
    slow_print("[You]: Side effects?")
    slow_print("[Lab Assistant]: She didn’t explain much, but I think she was testing something on herself. The last thing she said to me was, 'Time is slipping.'")
    slow_print("[Senior Detective]: That’s eerie. Could her experiments have backfired?")
    return_to_suspects()

def question_investor():
    slow_print("\n[You]: How much were you invested in Alice's work?")
    slow_print("[Investor]: I poured millions into her company, but lately, she was becoming unreliable. Delays, missed deadlines. She started talking nonsense about timelines and parallel worlds.")
    slow_print("[You]: Do you think her research was dangerous?")
    slow_print("[Investor]: I didn’t believe in her time travel nonsense, but she did. I’m just here to get my money back. She promised me returns, but now she's dead, and my investment’s gone.")
    slow_print("[You]: Were you at the penthouse on the night of her death?")
    slow_print("[Investor]: I was supposed to meet her, but she canceled last minute. Said she had to 'reset' something.")
    slow_print("[Senior Detective]: This guy’s after money, but he might know more than he’s letting on.")
    return_to_suspects()

def question_expert():
    slow_print("\n[You]: As an expert in time paradoxes, what’s your take on this case?")
    slow_print("[Expert]: I’ve studied theoretical physics my whole life, and what Alice was attempting is… dangerous.")
    slow_print("[You]: What do you mean by dangerous?")
    slow_print("[Expert]: Time isn’t something you can just play with. If she was tampering with time loops or parallel realities, it could explain the two bodies.")
    slow_print("[You]: Could she have somehow split herself into two versions?")
    slow_print("[Expert]: It’s possible. I’ve theorized that manipulating time can create divergent timelines that co-exist for brief moments. But for both bodies to be in this reality simultaneously… it’s unheard of.")
    slow_print("[Senior Detective]: This is sounding more and more like sci-fi, but we can’t ignore it. Let’s see if there’s any evidence to back up these wild claims.")
    return_to_suspects()

def return_to_suspects():
    print("\nWhat would you like to do next?")
    print("1. Question another suspect")
    print("2. Investigate the penthouse")
    print("3. Examine Alice's time-travel device")
    print("4. Check the security footage")
    print("5. Accuse a suspect")

    choice = input("\nChoose an action (1/2/3/4/5): ")

    if choice == '1':
        time_paradox()  # Return to suspect questioning
    elif choice == '2':
        investigate_penthouse()
    elif choice == '3':
        examine_device()
    elif choice == '4':
        check_footage()
    elif choice == '5':
        accuse_suspect()
    else:
        slow_print("\n[Senior Detective]: Don’t lose focus. Choose carefully.")
        return_to_suspects()

def investigate_penthouse():
    slow_print("\n[You]: Let’s search the penthouse for any clues.")
    slow_print("[Senior Detective]: We need to understand how she died in two places at once.")
    slow_print("\nYou enter the penthouse. The living room body looks peaceful, as if she fell asleep. But the rooftop body looks different.")
    slow_print("[You]: There are no signs of struggle here, but the rooftop version has injuries. Could she have fallen?")
    slow_print("\nYou find a journal on the table.")
    slow_print("[Senior Detective]: It’s Alice’s journal. She wrote something about a ‘Temporal Anchor’ she was working on.")
    slow_print("[You]: This anchor might explain how her experiment went wrong. Let’s dig deeper into this.")
    return_to_suspects()

def examine_device():
    slow_print("\n[You]: I want to examine Alice’s time-travel device.")
    slow_print("[Senior Detective]: If this thing really works, it might explain everything.")
    slow_print("\nYou approach a machine in the lab labeled 'Temporal Anchor.' It’s large, with wires and screens showing distorted images of the future.")
    slow_print("[You]: The device is operational, but it looks unstable.")
    slow_print("[Senior Detective]: There are logs on the machine. Alice was testing it on herself. She wrote that she felt ‘out of sync’ with time.")
    slow_print("[You]: The logs show multiple timelines converging at once. This might have split her into two versions.")
    return_to_suspects()

def check_footage():
    slow_print("\n[You]: Let’s check the security footage from the penthouse.")
    slow_print("[Senior Detective]: We might see something unusual.")
    slow_print("\nYou play the footage from the night Alice died.")
    slow_print("[You]: Wait, what’s that? There are two versions of Alice walking around at the same time.")
    slow_print("[Senior Detective]: Impossible. How can there be two Alices?")
    slow_print("\nThe footage shows both Alices interacting with each other before one of them collapses on the rooftop.")
    slow_print("[Senior Detective]: It looks like her experiment did this to her. Two versions of her in the same timeline couldn’t exist together.")
    return_to_suspects()

def accuse_suspect():
    print("\nWho do you think is responsible for Alice’s death?")
    print("1. The Lab Assistant")
    print("2. The Investor")
    print("3. The Time Paradox Expert")

    choice = input("\nMake your accusation (1/2/3): ")

    if choice == '1':
        slow_print("\n[Senior Detective]: The lab assistant? She might have helped Alice with the experiments, but there’s no solid proof.")
        return_to_suspects()
    elif choice == '2':
        slow_print("\n[Senior Detective]: The investor? He’s shady, but it seems like he was more interested in money than time travel.")
        return_to_suspects()
    elif choice == '3':
        slow_print("\n[Senior Detective]: The expert… He knew the risks of messing with time, and he didn’t stop Alice.")
        slow_print("[Senior Detective]: His theories could’ve pushed Alice into a dangerous experiment that cost her life.")
        slow_print("[You]: I think he’s responsible. His warnings were too little, too late.")
        slow_print("[Senior Detective]: Good work, detective. Looks like Alice’s obsession with time paradoxes was encouraged by the expert.")
        slow_print("[Senior Detective]: She pushed her experiment too far and ended up with two versions of herself. One couldn’t survive.")
    else:
        slow_print("\n[Senior Detective]: Focus, detective! Pick a real")