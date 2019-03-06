import json
Song = {
    "Title": None,
    "Artist": None,
    "Album": None,
    "Track": None,
    "Year": None,
    "Genre": None}

def add_song():
    Song["Title"] = input("Enter song tile: ")
    Song["Artist"] = input("Enter artist name: ")
    Song["Album"] = input("Enter album title: ")
    Song["Track"] = input("Enter track number: ")
    Song["Year"] = input("Enter year: ")
    Song["Genre"] = input("Enter genre: ")

def save_song():
    if Song["Title"] != None:
        writefile = open("MusicDB.txt", "a")
        writefile.write(json.dumps(Song))
    elif Song["Title"] == None:
        print("You must first add a song! ")

def clear_file():
    file = open("MusicDB.txt", "w")
    file.truncate(0)

def list_song():
    count = 0
    f = open("MusicDB.txt", "r")
    try:
        for entry in f:
            clean = []
            clean_entry = entry.replace('"', '').strip("{").strip("}").strip(",").split("}{") #removes the ugly stuff
        for s in clean_entry:
            count = count + 1
            print("Song #",count,":",s,"\n")
    except UnboundLocalError:
        print("\nYour file is empty!\n")

def call_menu():
    print("add : Add a new song to the music database\n"
     "list : List the songs in the music database\n"
     "save : Save the music database\n"
     "help : Display this menu\n"
     "exit : Exit the Program\n")

def get_count():
    count = 0
    f = open("MusicDB.txt", "r")
    try:
        for entry in f:
            entries = entry.split("}{")
        for entry in entries:
            count = count + 1
    except:
        return 0
    return count

call_menu()
while True:
    count = get_count() #calculates the global count at the beginning of the program so that the user can exit
                        #without resetting the global count
    command = input("Enter one of the listed commands: ")
    if command == "add":
        add_song()
    elif command == "save" and count < 8:
        save_song()
        Song = Song.fromkeys(Song, None) #resets all values in Song to None once they've been saved
    elif command == "save" and count >= 8:
        print("Your file is full!")
    elif command == "list":
        list_song()
    elif command == "help":
        call_menu()
    elif command == "exit":
        break
    elif command == "clear":
        clear_file()
    else:
        print("Error, that's not a valid command")
        continue
