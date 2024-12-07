# import os
#
# if __name__ == '__main__':
#     print("Welcome to RoboSpeaker 1.1. Created by Charan")
#     while true:
#         x=input("What do you want me to speak")
#         if x=="q":
#             os.system("Say bye bye friend")
#             break
#         command = f"say{x}"
#         os.system(command)

import pyttsx3


def main():
    print("Welcome to RoboSpeaker 1.1. Created by Charan")

    # Initialize the TTS engine
    engine = pyttsx3.init()

    while True:
        x = input("What do you want me to speak: ")

        if x.lower() == "q":
            engine.say("Bye bye friend!")
            engine.runAndWait()
            break

        engine.say(x)
        engine.runAndWait()


if __name__ == "__main__":
    main()
