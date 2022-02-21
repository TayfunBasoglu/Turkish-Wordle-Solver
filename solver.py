# -*- coding: utf-8 -*-

import pandas as pd
import re


print("""

### Enter letters separated by commas
### Do not use commas after the last letter
### If there is no information, press enter and skip that part
                                        TayfunBasoglu
""")

read = pd.read_csv("letter_frequency_results.csv")

while True:
    #part 1
    letters_inside = input("\n\nLetters in the word - location unknown (like : a,b,c)\n\n --- >    ").replace(" ", "")
    letters_inside = letters_inside.split(",")
    if letters_inside:
        reg = '^'
        for i in letters_inside:
            reg += "(?=.*"+i+")"
        read = read[read["words"].str.contains(""+reg+"",regex= True, na=False)]
        print(read.head(10))
    else:
        pass
        
    #part 2
    letters_n_inside = input("\n\nLetters not in the word (like : a,b,c)\n\n --- >    ").replace(" ", "")
    letters_n_inside = letters_n_inside.split(",")
    try:
        if letters_n_inside:
            for i in letters_n_inside:
                read = read[~read["words"].str.contains("[{}]".format(i))]
            print(read.head(10))
    except:
        pass

    #part 3
    letters_location  = input("\n\nKnown letters location (like : 1b,2c,3a)\n\n --- >    ").replace(" ", "")
    if letters_location:
        b = letters_location.split(",")
        space = [".",".",".",".","."]
        for i in b:
            space[int(i[0])-1] = i[1]
        formul = "".join(space)
        read = read[read["words"].str.contains(""+formul+"",regex= True, na=False)]
        print(read.head(10))
    else:
        pass