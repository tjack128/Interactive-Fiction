import time

#Insert a welcome function
def Welcome():
    Welcome_T = open("Interactive_Fiction_Welcome_User.txt", encoding="utf8")

    Welcome_Text = Welcome_T.read()

    #Split the contents of the welcome text file.
    Split_Welcome = Welcome_Text.split(".")

    #Print out the contents of the text file one step at a time.
    for i in range(len(Split_Welcome)):
        print(Split_Welcome[i])
        time.sleep(4)

    #Insert an instruction function

def Commands():
    # Insert the code for the story here
    f = open("Commands.txt", encoding="utf8")
    Com_text = f.read()

    # Splitting the text into an array
    Split_Text = Com_text.split("|")

    # Printing out the values of the text one line at a time
    for i in range(len(Split_Text)):
        print(Split_Text[i])
        time.sleep(2)

    print()

def Main_Story():
    #Insert the code for the story here
    f = open("interactivefiction.txt", encoding="utf8")
    text = f.read()

    #Splitting the text into an array
    Split_Text = text.split(".")

    #Printing out the values of the text one line at a time
    for i in range(len(Split_Text)):
        print(Split_Text[i])
        time.sleep(4)

def Decisions():
    # Insert the code for the story here
    f = open("Decisions.txt", encoding="utf8")
    text = f.read()

    # Splitting the text into an array
    Second_Split_Text = text.split("|")


    done = True

    while(done):

        User_Input = input("Try inputting a guess")

        if (User_Input == "Candles" or User_Input == "Flashlights" or User_Input == "Phones"):

            print(Second_Split_Text[0])
            print()
        else:
            continue

        while(done):
            # User making the decisions in response to the story
            User_Input = input("Try inputting a guess")

            if (User_Input == "Bathroom" or User_Input == "Roman"):
                print("Clever observation!")
                print(Second_Split_Text[1])
                print()
            else:
                continue

            while (done):
                # User making the decisions in response to the story
                User_Input = input("Try inputting a guess")
                if (User_Input == "Shadowy Figure" or User_Input == "Other Room"):

                    print("Clever observation!")
                    print(Second_Split_Text[2])
                    print()
                else:
                    continue



#Use the Welcome function as a greeting to the user.
Welcome()

Commands()

Main_Story()

Decisions()

