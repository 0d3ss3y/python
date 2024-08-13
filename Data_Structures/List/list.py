def main():
    lst = [1, 2, 3]
    print(f"Original list: {lst}")
    print(f"Reversed List: {reverse_list(lst)}\n")
    
    lst = [1, 2, 2, 3, 4, 4]
    print(f"Original list: {lst}")
    print(f"Duplicates removed option 1: {remove_duplicates_1(lst)}")
    print(f"Duplicates removed option 2: {remove_duplicates_2(lst)}\n")
    
    lst = [-1, -2, -3]
    print(f"Original list: {lst}")
    print(f"Find max option 1: {find_max_1(lst)}")
    print(f"Find max option 2: {find_max_2(lst)}")
    print(f"Find max option 2: {find_max_3(lst)}\n")
    
    lst = [-1, -2, -3]
    print(f"Original list: {lst}")
    print(f"Find min option 1: {find_min_1(lst)}")
    print(f"Find min option 1: {find_min_2(lst)}")
    print(f"Find min option 2: {find_min_3(lst)}\n")
    
    lst = [1, 2, 2, 3, 4, 4]
    print(f"Original list: {lst}\n Value Selected: 4")
    print(f"Counting Occurrences option 1: {find_occ_1(lst,4)}")
    print(f"Counting Occurrences option 2: {find_occ_2(lst,4)}\n")

    
    lst = [7, 2, 9, 5, 1, 6, 8, 3, 4, 0]
    print(f"Original list: {lst}")
    print(f"Sort ASC option 1: {sort_asc_1(lst)}")
    print(f"Sort ASC option 2: {sort_asc_2(lst)}\n")
    
    lst = [7, 2, 9, 5, 1, 6, 8, 3, 4, 0]
    print(f"Original list: {lst}")
    print(f"Sort DESC option 1: {sort_desc_1(lst)}")
    print(f"Sort DESC option 2: {sort_desc_2(lst)}\n")
    
    lst = [1, 2, 3]
    lst2= [4, 5, 6]
    print(f"Original lists: {lst} and {lst2}")
    print(f"Merge List: {merge_list(lst,lst2)}\n")

    lst = [7, 2, 9, 5, 1, 6, 8, 3, 4, 0]
    print(f"Original lists: {lst}")
    print(f"Merge List: {len(lst)}\n")
    
    lst = [7, 2, 9, 5, 1, 6, 8, 3, 4, 0]
    print(f"Original lists: {lst}")
    print(f"Sum List option 1: {sum_1(lst)}")
    print(f"Sum List option 1: {sum_2(lst)}\n")
    
    lst = [1, 2, 3, 4]
    lst2= [3, 4, 5, 6]
    print(f"Original lists: {lst} and {lst2}")
    print(f"Intersection : {intersection(lst,lst2)}\n")

    lst = [1, 2, 3, 4, 5, 6]
    print(f"Original lists: {lst}")
    print(f"Filter even 1: {filtered_1(lst)}\n")

    lst = [1, 2, 3, 4]
    lst2= [3, 4, 5, 6]
    lst3= [6]
    print(f"Original lists: {lst} and {lst2} and {lst3}")
    print(f"flatten : {flattened(lst,lst2,lst3)}\n")
    
    lst = [1, 2, 3, 4, 5, 6]
    print(f"Original lists: {lst}")
    print(f"List Pair: {pair_list(lst,7)}\n")

def reverse_list(lst):
    return lst[::-1]


def remove_duplicates_1(lst):
    final = []
    
    for i in lst:
        if i not in final:
            final.append(i)
        else:
            continue
    return final

def remove_duplicates_2(lst):
    final = set(lst)
    return list(final)


def find_max_1(lst):
    max = -99999
    
    for i in lst:
        if max<i:
            max = i
        else:
            continue
    return max

def find_max_2(lst):
    return max(lst)

def find_max_3(lst):
    max = lst[0]
    
    for i in lst:
        if max<i:
            max = i
        else:
            continue
    return max


def find_min_1(lst):
    min = 9999999999999
    
    for i in lst:
        if min>i:
            min = i
        else:
            continue
    return min

def find_min_2(lst):
    return min(lst)

def find_min_3(lst):
    min = lst[0]
    
    for i in lst:
        if min>i:
            min = i
        else:
            continue
    return min


def find_occ_1(lst,value):
    count = 0
    
    for i in lst:
        if i == value:
            count += 1
            
    return count

def find_occ_2(lst,value):
    return lst.count(value)


def sort_asc_1(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

def sort_asc_2(lst):
    return sorted(lst)

def sort_desc_1(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

def sort_desc_2(lst):
    return sorted(lst,reverse=True)


def merge_list(lst1,lst2):
    lst1.extend(lst2)
    return lst1


def sum_1(lst):
    return sum(lst)

def sum_2(lst):
    total = 0
    
    for i in lst:
        total += i
        
    return total
    

def intersection(lst,lst2):
    final = []
    
    for item in lst:
        if item in lst2:
            final.append(item)
    return final


def filtered_1(lst):
    final =[]
    
    for i in lst:
        if i % 2 == 0:
            final.append(i)
            
    return final


def flattened(lst,lst2,lst3):
    lst.extend(lst2)
    lst.extend(lst3)
    return list(set(lst))


def pair_list(lst,value):
    pair = []
    n = len(lst)
    for i in range(n):
        for k in range(n-1):
            if lst[i] + lst[k] == value:
                pair.append(f"({lst[i]},{lst[k]})")
    return pair


if __name__ == "__main__":
    main()
