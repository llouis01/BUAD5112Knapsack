# -*- coding: utf-8 -*-

import time
import json

def checkCapacity(contents,knapsack_cap):
    """ contents is expected as a dictionaryof the form {item_id:(volume,value), ...} """
    """ This function returns True if the knapsack is within capacity;
        False if the knapsack is overloaded """
    load = 0
    if isinstance(contents,dict):
        for this_key in contents.keys():
            load = load + contents[this_key][0]
        if load <= knapsack_cap:
            return True
        else:
            return False
    else:
        print("function checkCapacity() requires a dictionary")

def knapsack_value(items):
    value = 0.0
    if isinstance(items,dict):
        for this_key in items.keys():
            value = value + items[this_key][1]
        return(value)
    else:
        print("function knapsack_value() requires a dictionary")

def getData():
    f = open('knapsack.json','r')
    x = json.load(f)
    f.close()
    for i in range(len(x)):
        myData = x[i]['data']
        x[i]['data'] = {}
        for j in range(len(myData)):
            x[i]['data'][j] = tuple(myData[j]) 
    return x

def loadKnapsack(items,knapsack_cap):
    """ You write this function which is your heuristic
        knapsack algorithm
    
        Indicate items to be included in the backpack by
        including their dictionary keys within a list
        data structure and, subsequently, returning that
        list of IDs from this function  """
        
    """ Compute existing load in knapsack """
    myUsername = 'llouis' # always return this variable as the first item
    nickname = 'Grand_Loup' # This idenfier will appear on the leaderboard, if you desire to be identified.  This may be left as an empty string.
    items_to_pack = []    # use this list for the indices of the items you load into the knapsack
    
    load = 0.0            # use this variable to keep track of how much volume is already loaded into the backpack
    value = 0.0           # value in knapsack
    
    
    """
    Step 1: as usual for i in range(len(my_data)):

    Step 2: if the weight of the items you index from
            "my_data" is < knapsack_cap - the items you've added then load into the pack

    my_data(then do your indexing) < knapsack_cap
    load = load + my_data(with your indexing)

    Step 3: append my_data[i][0] (b/c we want the return to be keys to the empty
            "items_to_pack" list we made

    items_to_pack.append(my_data[i][0])
    """
    
    ##### my code #####
    
    data = [i for i in probData]
    
    
    ###################
    
        
   
    
    return myUsername, nickname, items_to_pack       # use this return statement when you have items to load in the knapsack


## try it ####

f1 = open('knapsack.json', 'r')
data = json.load(f1)
f1.close()

loadKnapsack(data, 5)


##############


""" Main code """
""" Get data and define problem ids """
probData = getData()
problems = range(len(probData))
silent_mode = False    # use this variable to turn on/off appropriate messaging depending on student or instructor use
""" Error Messages """
error_bad_list_key = []

""" A list was received from load_knapsack() for the item numbers to be loaded
    into the knapsack.  However, that list contained an element that was not a key
    in the dictionary of the items that were not yet loaded.   This could be either
    because the element was non-numeric, it was a key that was already loaded into
    the knapsack, or it was a numeric value that didn't match with any of the dictionary keys.
    Please check the list that your load_knapsack function is returning. It will be assumed
    that the knapsack is fully loaded with any items that may have already been loaded and a
    score computed accordingly. 
"""
error_response_not_list = []

""" load_knapsack() returned a response for items to be packed that was not a list. 
    Scoring will be terminated   """

for problem_id in problems:
    in_knapsack = {}
    knapsack_cap = probData[problem_id]['cap']
    items = probData[problem_id]['data']
    errors = False
    response = None
    
    startTime = time.time()
    team_num, nickname, response = loadKnapsack(items,knapsack_cap)
    execTime = time.time() - startTime
    if isinstance(response,list):
        for this_key in response:
            if this_key in items.keys():
                in_knapsack[this_key] = items[this_key]
                del items[this_key]
            else:
                errors = True
                if silent_mode:
                    status = "bad_list_key"
                else:
                    print("P"+str(problem_id)+"bad_key_")
                #finished = True
    else:
        if silent_mode:
            status = "P"+str(problem_id)+"_not_list_"
        else:
            print(error_response_not_list)
                
    if errors == False:
        if silent_mode:
            status = "P"+str(problem_id)+"knap_load_"
        else:
            print("Knapsack Loaded for Problem ", str(problem_id)," ....", '    Execution time: ', execTime, ' seconds')
        knapsack_ok = checkCapacity(in_knapsack,knapsack_cap)
        knapsack_result = knapsack_value(in_knapsack)
        if silent_mode:
            print(status+"; knapsack within capacity: "+knapsack_ok)
        else:
            print("knapcap: ", knapsack_ok)
            print("knapsack value : ", knapsack_value(in_knapsack))