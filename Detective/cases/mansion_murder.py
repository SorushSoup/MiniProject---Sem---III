import time
from slow_print import slow_print

def mansion_murder():
    slow_print("\nCase 3: The Mansion Murder Mystery")
    time.sleep(1)
    
    # Case introduction
    slow_print("\n[Senior Detective]: This one’s a mess, detective. A high-profile party at a mansion turned into a murder scene.")
    slow_print("[Senior Detective]: The victim, Mr. Randolph, was found dead in the study.")
    slow_print("[Senior Detective]: He was stabbed in the chest, but the weapon is missing.")
    slow_print("[Senior Detective]: We’ve got four suspects: the butler, Mr. Randolph’s business partner, the widow, and a close family friend.")
    slow_print("[Senior Detective]: We need to figure out who did it, how, and why.")
    print('''                              .     .
                               !!!!!!!
                       .       [[[|]]]    .
                       !!!!!!!!|--_--|!!!!!
                       [[[[[[[[\_(X)_/]]]]]
               .-.     /-_--__-/_--_-\-_--\
               |=|    /-_---__/__-__-_\__-_\
           . . |=| ._/-__-__\===========/-__\_
           !!!!!!!!!\========[ /]]|[[\ ]=====/
          /-_--_-_-_[[[[[[[[[||==  == ||]]]]]]
         /-_--_--_--_|=  === ||=/^|^\ ||== =|
        /-_-/^|^\-_--| /^|^\=|| | | | ||^\= |
       /_-_-| | |-_--|=| | | ||=|_|_|=||"|==|
      /-__--|_|_|_-_-| |_|_|=||______=||_| =|
     /_-__--_-__-___-|_=__=_.`---------'._=_|__
    /-----------------------\===========/-----/
   ^^^\^^^^^^^^^^^^^^^^^^^^^^[[|]]|[[|]]=====/
       |.' ..==::'"'::==.. '.[ /~~~~~\ ]]]]]]]
       | .'=[[[|]]|[[|]]]=`._||==  =  || =\ ]
       ||== =|/ _____ \|== = ||=/^|^\=||^\ ||
       || == `||-----||' = ==|| | | |=|| |=||
       ||= == ||:^s^:|| = == ||=| | | || |=||
       || = = ||:___:||= == =|| |_|_| ||_|=||
      _||_ = =||o---.|| = ==_||_= == =||==_||_
      \__/= = ||:   :||= == \__/[][][][][]\__/
      [||]= ==||:___:|| = = [||]\\//\\//\\[||]
      }  {---'"'-----'"'- --}  {//\\//\\//}  {
    __[==]__________________[==]\\//\\//\\[==]_
   |`|~~~~|================|~~~~|~~~~~~~~|~~~~||
jgs|^| ^  |================|^   | ^ ^^ ^ |  ^ ||
  \|//\\/^|/==============\|/^\\\^/^.\^///\\//|///
 \\///\\\//===============\\//\\///\\\\////\\\/////
 ""'""'""".'..'. ' '. ''..'.""'""'""'""''"''"''""
             ''')
    # Present suspects
    slow_print("\n[You]: Let’s start by questioning the suspects.")
    
    print("\nSuspects:")
    print("1. The Butler")
    print("2. The Business Partner")
    print("3. The Widow")
    print("4. The Family Friend")
    
    choice = input("\nWho would you like to question first? (1/2/3/4): ")
    
    if choice == '1':
        question_butler()
    elif choice == '2':
        question_partner()
    elif choice == '3':
        question_widow()
    elif choice == '4':
        question_friend()
    else:
        slow_print("\n[Senior Detective]: Focus, rookie! Pick someone from the list.")
        mansion_murder()  # Recursive call for valid choice

def question_butler():
    slow_print("\n[You]: Where were you when Mr. Randolph was killed?")
    slow_print("[Butler]: I was preparing dinner in the kitchen. I didn’t hear anything unusual until someone screamed.")
    slow_print("[Butler]: I’ve worked for Mr. Randolph for years. I’d never harm him.")
    slow_print("[Senior Detective]: He seems loyal, but we need more than his word. Let’s keep digging.")
    return_to_suspects()

def question_partner():
    slow_print("\n[You]: What were you doing at the time of the murder?")
    slow_print("[Partner]: I was discussing business matters with a few guests in the living room. I didn’t see Randolph after dinner.")
    slow_print("[Partner]: Our business has been doing well, no reason for me to kill him.")
    slow_print("[Senior Detective]: Hmm, seems like a solid alibi, but let’s check his motives.")
    return_to_suspects()

def question_widow():
    slow_print("\n[You]: Where were you when your husband was killed?")
    slow_print("[Widow]: I was in the garden, taking a walk to clear my mind. I only came back when I heard the commotion.")
    slow_print("[Widow]: Randolph was difficult at times, but I didn’t want this.")
    slow_print("[Senior Detective]: The grieving widow… or a suspect? We need more evidence.")
    return_to_suspects()

def question_friend():
    slow_print("\n[You]: Where were you when the murder happened?")
    slow_print("[Friend]: I was in the library, reading. I had no idea what was happening until the butler called everyone in.")
    slow_print("[Friend]: Randolph and I were close, I’d never hurt him.")
    slow_print("[Senior Detective]: Another alibi, but this could be a smokescreen.")
    return_to_suspects()

def return_to_suspects():
    print("\nWhat would you like to do next?")
    print("1. Question another suspect")
    print("2. Investigate the study")
    print("3. Examine the mansion grounds")
    print("4. Check for a motive")
    print("5. Accuse a suspect")
    
    choice = input("\nChoose an action (1/2/3/4/5): ")
    
    if choice == '1':
        mansion_murder()  # Return to suspect questioning
    elif choice == '2':
        investigate_study()
    elif choice == '3':
        examine_mansion_grounds()
    elif choice == '4':
        check_motive()
    elif choice == '5':
        accuse_suspect()
    else:
        slow_print("\n[Senior Detective]: Get your act together, detective. Make a valid choice.")
        return_to_suspects()

def investigate_study():
    slow_print("\n[You]: Let’s take a closer look at the study.")
    slow_print("[Senior Detective]: Good call. The study is where the body was found, so there may be some clues.")
    slow_print("\nYou notice an open window, and there’s a broken vase on the floor. No blood near the window, though.")
    slow_print("[Senior Detective]: Could the killer have escaped this way? Or was it a distraction?")
    return_to_suspects()

def examine_mansion_grounds():
    slow_print("\n[You]: Let’s examine the grounds, maybe there’s something we missed outside.")
    slow_print("[Senior Detective]: The grounds are large. Keep an eye out for anything out of place.")
    slow_print("\nYou find footprints in the garden that lead to the back door, but they don’t seem fresh.")
    slow_print("[Senior Detective]: These prints could be a red herring, but they lead towards the garden where the widow said she was.")
    return_to_suspects()

def check_motive():
    slow_print("\n[You]: Time to dig into the suspects' motives.")
    slow_print("[Senior Detective]: Money, jealousy, revenge… there’s always something.")
    
    slow_print("\n[Butler]: He seems loyal, but he’s been unhappy with his pay lately. Could that push him to murder?")
    slow_print("[Business Partner]: Their business was thriving, but there were rumors of disagreements over recent deals.")
    slow_print("[Widow]: The marriage had its ups and downs, but no sign of open hostility. Still, inheritance is a strong motive.")
    slow_print("[Family Friend]: A long-time friend, but maybe he was jealous of Randolph’s wealth or position.")
    
    slow_print("\n[Senior Detective]: Everyone has a potential motive, but we need to match it with opportunity.")
    return_to_suspects()

def accuse_suspect():
    print("\nWho do you think is the culprit?")
    print("1. The Butler")
    print("2. The Business Partner")
    print("3. The Widow")
    print("4. The Family Friend")
    
    choice = input("\nMake your accusation (1/2/3/4): ")
    
    if choice == '1':
        slow_print("\n[Senior Detective]: The butler? It’s a classic choice, but I don’t think he had the guts to go through with it.")
        return_to_suspects()
    elif choice == '2':
        slow_print("\n[Senior Detective]: The business partner… interesting. He had the motive, but could he have sneaked out of the living room unnoticed?")
        slow_print("\n[You]: Maybe… but it feels off.")
        return_to_suspects()
    elif choice == '3':
        slow_print("\n[Senior Detective]: The widow, huh? She had access to the house, and those footprints in the garden are suspicious.")
        slow_print("[Senior Detective]: Plus, there’s the matter of the inheritance.")
        slow_print("[Senior Detective]: Well done, detective. It looks like she did it after all. Jealousy, money, and anger… a dangerous combination.")
        slow_print("\n[You]: Case solved! The widow is the murderer.")
    elif choice == '4':
        slow_print("\n[Senior Detective]: The family friend? Nah, I don’t think he was close enough to have done this.")
        return_to_suspects()
    else:
        slow_print("\n[Senior Detective]: You’re wasting time! Pick a real option.")
        accuse_suspect()
