import time
from slow_print import slow_print

def poisoned_painting():
    slow_print("\nCase 2: The Poisoned Painting")
    time.sleep(1)
    
    # Case introduction
    slow_print("\n[Senior Detective]: Listen up, rookie. We have a death at the gallery.")
    slow_print("[Senior Detective]: The victim, Mr. Harrison, collapsed during an art exhibition.")
    slow_print("[Senior Detective]: He had been poisoned, but the real mystery is how.")
    slow_print("[Senior Detective]: The suspects are the gallery curator, an art collector, and the artist herself.")
    slow_print("[Senior Detective]: Watch your back on this one. I’ve got a bad feeling about it.")
    print(''' ________________________
|.----------------------.|
||                      ||
||       ______         ||
||     .;;;;;;;;.       ||
||    /;;;;;;;;;;;\     ||
||   /;/`    `-;;;;; . .||
||   |;|__  __  \;;;|   ||
||.-.|;| e`/e`  |;;;|   ||
||   |;|  |     |;;;|'--||
||   |;|  '-    |;;;|   ||
||   |;;\ --'  /|;;;|   ||
||   |;;;;;---'\|;;;|   ||
||   |;;;;|     |;;;|   ||
||   |;;.-'     |;;;|   ||
||'--|/`        |;;;|--.||
||;;;;    .     ;;;;.\;;||
||;;;;;-.;_    /.-;;;;;;||
||;;;;;;;;;;;;;;;;;;;;;;||
||jgs;;;;;;;;;;;;;;;;;;;||
'------------------------'
             ''')
    # Present suspects
    slow_print("\n[You]: Time to question the suspects and investigate the crime scene.")
    
    print("\nSuspects:")
    print("1. The Curator")
    print("2. The Art Collector")
    print("3. The Artist")
    
    choice = input("\nWho would you like to question first? (1/2/3): ")
    
    if choice == '1':
        question_curator()
    elif choice == '2':
        question_collector()
    elif choice == '3':
        question_artist()
    else:
        slow_print("\n[Senior Detective]: Stick to the plan. Pick someone.")
        poisoned_painting()  # Recursive call for valid choice

def question_curator():
    slow_print("\n[You]: Where were you when Mr. Harrison was poisoned?")
    slow_print("[Curator]: I was overseeing the exhibition, as usual. I saw Mr. Harrison admiring a painting when he suddenly collapsed.")
    slow_print("[Curator]: I immediately called for help. Why would I harm one of my most important guests?")
    slow_print("[Senior Detective]: She sounds convincing, but we need more clues.")
    return_to_suspects()

def question_collector():
    slow_print("\n[You]: What were you doing at the time of the incident?")
    slow_print("[Collector]: I was in the corner discussing a deal with another guest. I didn’t notice anything until the commotion.")
    slow_print("[Collector]: I’ve been in this business for years; why would I jeopardize my reputation?")
    slow_print("[Senior Detective]: Hmm. He seems calm, but appearances can be deceiving.")
    return_to_suspects()

def question_artist():
    slow_print("\n[You]: Can you tell me where you were when Mr. Harrison collapsed?")
    slow_print("[Artist]: I was mingling with the guests. I only heard about the incident afterward.")
    slow_print("[Artist]: He was admiring one of my paintings. Why would I hurt someone who appreciates my work?")
    slow_print("[Senior Detective]: Interesting... her alibi is vague. We’ll need to dig deeper.")
    return_to_suspects()

def return_to_suspects():
    print("\nWhat would you like to do next?")
    print("1. Question another suspect")
    print("2. Examine the crime scene")
    print("3. Investigate the painting")
    print("4. Check victim's background")
    print("5. Accuse a suspect")
    
    choice = input("\nChoose an action (1/2/3/4/5): ")
    
    if choice == '1':
        poisoned_painting()  # Return to suspect questioning
    elif choice == '2':
        examine_crime_scene()
    elif choice == '3':
        investigate_painting()
    elif choice == '4':
        check_victim_background()
    elif choice == '5':
        accuse_suspect()
    else:
        slow_print("\n[Senior Detective]: Focus, detective. Make a valid choice.")
        return_to_suspects()

def examine_crime_scene():
    slow_print("\n[You]: Let's take a look around the gallery.")
    slow_print("[Senior Detective]: Always good to start with the scene.")
    slow_print("\nYou notice a glass of champagne near the victim's body. There’s a faint smell of almonds coming from it.")
    slow_print("[Senior Detective]: Cyanide... It seems likely, but we need to figure out how it was delivered.")
    return_to_suspects()

def investigate_painting():
    slow_print("\n[You]: Let’s check out the painting Mr. Harrison was admiring.")
    slow_print("[Senior Detective]: Good thinking. Maybe there's something we're missing.")
    slow_print("\nThe painting depicts a stormy sea. Oddly, there are small scratches near the frame that seem out of place.")
    slow_print("[Senior Detective]: Someone tampered with this... but why?")
    return_to_suspects()

def check_victim_background():
    slow_print("\n[You]: Time to check Mr. Harrison's background.")
    slow_print("[Senior Detective]: Smart move. There might be something in his past.")
    slow_print("\nYou discover that Mr. Harrison was a wealthy businessman who recently made several enemies in the art world.")
    slow_print("[Senior Detective]: This could be revenge. Let’s see who had the most to gain.")
    return_to_suspects()

def accuse_suspect():
    print("\nWho do you think is the culprit?")
    print("1. The Curator")
    print("2. The Art Collector")
    print("3. The Artist")
    
    choice = input("\nMake your accusation (1/2/3): ")
    
    if choice == '1':
        slow_print("\n[Senior Detective]: The curator? She had access to the champagne and knew Mr. Harrison well.")
        slow_print("[Senior Detective]: But... those scratches on the painting, I don’t think she’s the one.")
        slow_print("\n[You]: You’re right. It doesn’t fit.")
        return_to_suspects()
    elif choice == '2':
        slow_print("\n[Senior Detective]: The collector, huh? He had motive, but no real opportunity. Try again.")
        return_to_suspects()
    elif choice == '3':
        slow_print("\n[Senior Detective]: The artist... she had both the motive and the means. Those scratches on the painting? She was likely trying to hide something.")
        slow_print("[Senior Detective]: Plus, Harrison's enemies... she could have been paid off to make this look like an accident.")
        slow_print("\n[You]: Case solved! The artist tampered with the painting and poisoned Mr. Harrison through a rigged champagne glass.")
    else:
        slow_print("\n[Senior Detective]: Are you even trying? Pick a valid option.")
        accuse_suspect()