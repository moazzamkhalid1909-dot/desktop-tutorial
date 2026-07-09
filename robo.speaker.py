import os

if __name__ == '__main__':
    print("Welcome to Robospeaker  1.1. created by Moazzam")
    while True:
        x = input("Enter what you want ro speak  me to speak: ")
        if x == "q":
            os.system("say 'bye bye friend' ")
            break
    command = f"say  {x}"
    os.system(command)