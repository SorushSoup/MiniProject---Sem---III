import time
from slow_print import slow_print

def missing_pet():
    slow_print("\n[Senior Detective]: Welcome, rookie! We have a simple case to solve.")
    slow_print("[Senior Detective]: Mrs. Johnson's cat, Whiskers, is missing!")
    slow_print("[Senior Detective]: Let's question the suspects to find out who might have seen him.")

    question_suspects()

def question_suspects():
    slow_print("\nSuspects:")
    print("1. The Dog Walker")
    print("2. The Neighbor")
    print("3. The Gardener")
    
    choice = input("\nWho do you want to question? (1/2/3): ")
    
    if choice == '1':
        question_dog_walker()
    elif choice == '2':
        question_neighbor()
    elif choice == '3':
        question_gardener()
    else:
        slow_print("\n[Senior Detective]: Please choose a valid suspect.")
        question_suspects()

def question_dog_walker():
    slow_print("\n[You]: Did you see Whiskers around here?")
    slow_print("[Dog Walker]: No, I haven’t seen him. But I saw the neighbor's dog acting strangely.")
    conclude_case("Dog Walker")

def question_neighbor():
    slow_print("\n[You]: Have you noticed Whiskers lately?")
    slow_print("[Neighbor]: I saw him playing in the garden just yesterday. He seemed fine.")
    conclude_case("Neighbor")

def question_gardener():
    slow_print("\n[You]: What about Whiskers? Any sightings?")
    slow_print("[Gardener]: I saw him climbing a tree a couple of days ago. He loves it up there!")
    conclude_case("Gardener")

def conclude_case(suspect):
    slow_print("\n[Senior Detective]: Let's analyze what we've learned...")

    if suspect == "Neighbor":
        slow_print("[Senior Detective]: The neighbor last saw him playing in the garden.")
        slow_print("[Senior Detective]: Let's check there to find Whiskers!")
    else:
        slow_print("[Senior Detective]: The dog walker and gardener didn't see him recently.")
        slow_print("[Senior Detective]: We need to follow up on the neighbor's lead!")