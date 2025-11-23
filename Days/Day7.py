import random as r

ascii_art = r"""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
"""

print(ascii_art)

lives = 6
random_words_list = [
    "Server",
    "Commit",
    "Cloud",
    "Logic",
    "Scale",
    "Pipeline",
    "Integration",
    "Monitoring",
    "Repository",
    "Deployment"
]
random_element = r.choice(random_words_list)
r_list = list(random_element.lower())
# print(r_list)
underscores = len(random_element) * "_"
underscores_list = list(underscores)

print(underscores)
while lives > 0:
    letter = str(input("write your letter: "))
    if letter in r_list:
        print("Yeah you guessed this one")
        for i, v in enumerate(r_list, start=0):
            if v == letter:
                # print(v)
                underscores_list[i] = v
                print(" ".join(underscores_list))
                if "_" not in underscores_list:
                    print("YOU WOON!!!")
                    break
    else:
        lives -= 1
        if lives > 1:
            print(f"NOO, -1 life left, now only {lives}")
        else:
            print("\tYou DIED!\n  No lives left.")
            print(f"P.s: it was: {random_element}")






