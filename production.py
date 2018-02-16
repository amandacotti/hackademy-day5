def remove_duplicate (alist):
    new_list = []
    for each in alist:
        if each not in new_list:
            new_list.append(each)

    return new_list

    
