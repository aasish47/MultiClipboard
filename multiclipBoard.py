import sys,json,clipboard
# a json(javascript object notation) file help to save a key value pair

SAVED_DATA = "clipboard.json"

def save_data(filepath,data):
    # this "w" will either override an existitng file or create a new file if it dosen't exist
    with open(filepath,"w") as f:
        # write the data in the file f as like in java here f is like an object of the json file and dump means it will put the key and value in it, here dumping the data in the file f
        json.dump(data,f)

# save_data("test.json",{"key":"value"})

def load_data(filepath):
    try:
        with open(filepath,"r") as f:
            data = json.load(f)
            return data
    except:
        return {}
    

if len(sys.argv)>1:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)
    
    if command == "save":
        key = input("Enter a key: ")
        value = input("Enter a value: ")
        # data[key] = clipboard.paste()
        data[key] = value
        save_data(SAVED_DATA,data)
        print("data saved to clipboard.")
    elif command == "load":
        loadKey = input("Enter a key:")
        if loadKey in data:
            clipboard.copy(data[loadKey])
            print("data copied to clipboard. ")
        else:
            print("data dosen't exist.")
    elif command == "delete":
        delKey = input("Enter a key:")
        with open('clipboard.json','r') as jsonFile:
            jsonData = json.load(jsonFile)
            if delKey in jsonData:
                del jsonData[delKey]
                with open('clipboard.json','w') as jsonFile:
                    json.dump(jsonData,jsonFile)
                print("data deleted.")
            else:
                print("data not found.")
    elif command == "list":
        print(data)
    else:
        print("Invalid Comand!!!")