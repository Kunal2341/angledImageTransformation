import os
print("-"*20)
size = 100000000
print("Deleting files of size:", size/1000000, "MB")
print("Deleting files of size:", size/1000000000, "GB")
for root, dirs, files in os.walk("/Users/kunal/Pictures/Video Projects"):
    for name in files:
        filepath = root + os.sep + name
        if os.path.getsize(filepath) > size: 
            print(filepath)
            deleteValue = input("Do you want to delete this file? (y/n)")
            if deleteValue == "y":
                os.remove(filepath)
                print("-----------File deleted-----------")
            else:
                print("-----------File not deleted-----------")
print("-"*20)