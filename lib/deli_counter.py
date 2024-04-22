katz_deli = []

def line(deli_queue:list):
    if len(deli_queue) != 0:
        index = 0
        string = ""
        while index != len(deli_queue):
            string+=(f"{index+1}. {deli_queue[index]} ")
            index += 1
        print((f"The line is currently: {string}").strip())
    else:
        print("The line is currently empty.")

def take_a_number(deli_queue:list, name:str):
    deli_queue.append(name)
    print(f"Welcome, {name}. You are number {deli_queue.index(name)+1} in line.")
    
def now_serving(deli_queue:list):
    if len(deli_queue) != 0:
        print(f"Currently serving {deli_queue[0]}.")
        deli_queue.pop(0)
    else:
        print("There is nobody waiting to be served!")