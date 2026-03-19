def welcome():
    print("Let's collect some information before we start the game.\n")
    
def prompt(display="Please input a string", require=True):
    if require:
        s = False
        while not s:
            s = input(display + " ")
    else:
        s = input(display + " ")
    return s
    

def convert_to_float(s):
    # if conversion fails, assing it to 0
    try: 
        f = float(s)
    except ValueError:
        f = 0
    return f

def x_of_y(x, y):
    num_list = []
    # returns list of x copies of y
    for i in range(x):
        num_list.append(y)
    return num_list