my_dict = {"a": 1, "b": 2, "c": 3}
try:
    value = my_dict["f"]
except IndexError:
    print("Index doesnt exist")
except KeyError:
    print("Key doesnt exist")
except:
    print("Some other error occured")
else:
    print(f"The value is {value}")
finally:
    print("The code did run...")
    
    

try:
    with open("test.txt") as fin:
        for line in fin:
            print(line)
except FileNotFoundError:
    print("The file does not exist")
except IOError:
    print("Error: There is an unknown problem with the file.")
