import webbrowser, sys, time, random, os  

X1 = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

def input_math():
    try:
        while True:
            user_input = input("1 times 1 = ")
            if user_input == 1: 
                opEn_vIdeo() 
                break
            elif user_input == "exit":
                sys.exit()
            else:
                print("Wrong! Try again.")
    except:
        pass 

def opEn_vIdeo():
    webbrowser.open(X1)
    return 0 

input_math()
