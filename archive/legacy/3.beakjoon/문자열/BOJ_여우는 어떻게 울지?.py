from collections import defaultdict 

t = int(input())

for _ in range(t):
    sounds = input().split()
    dict = defaultdict(str)
    while True:
        animal_sounds = input()
        if animal_sounds == "what does the fox say?":
            break 
        a,goes,s = animal_sounds.split()
        dict[a] = s

    for sound in sounds:
        if sound not in dict.values():
            print(sound, end=' ')



