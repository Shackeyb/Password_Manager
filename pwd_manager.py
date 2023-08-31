master_pwd = input("What is the Master Password? ")


def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines(): # f.readlines will read the lines
            data = line.rstrip() # rstrip will strip the carriage return form the line 
            user, passw = data.split("|") #
            print("User:", user, ", Password:", passw)

def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('password.txt', 'a') as f: # a mode allows you to add something to the end of an existing file and create a new file if one doesn't exist
        f.write(name + "|" + pwd + "\n")  # \n is a line break and will go to the next line when I add something

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue