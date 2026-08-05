import json

def Tell_info(x):

    file = x

    with open(x, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(data)

print("This is first version of program therefore it uses a file path instead.")

x = input("Enter the path of the JSON file: ")
Tell_info(x)