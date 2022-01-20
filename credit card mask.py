def maskify(cc):
    count_cc = len(cc)
    #print(count_cc)
    first_split_count = count_cc - 4
    #print(first_split_count)
    last_4 = cc[-4:]
    #print(last_4)
    new_cc = "#" * first_split_count + last_4
    return new_cc
    
maskify("passwordloser")
maskify("mypasswordisverylong")