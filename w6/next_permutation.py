def next_permutation(l):
    for k in range(len(l)-1, 0, -1):
        if (l[k-1] < l[k]):
            idx_swap = return_last_larger_elem(l, l[k-1], k, len(l)-1)
            # print(l[k-1], l[idx_swap])
            l[k-1], l[idx_swap] = l[idx_swap], l[k-1]
            l = l[:k] + sort(l[k:])
            break
    return (l)

def sort(l):
    def merge(l1, l2):
        l_new = []
        for k in range(len(l1)+len(l2)):
            if len(l2) == 0:
                l_new.extend(l1)
                break
            elif len(l1) == 0:
                l_new.extend(l2)
                break
            elif l1[0] < l2[0]:
                l_new.append(l1[0])
                l1 = l1[1:]
            else:
                l_new.append(l2[0])
                l2 = l2[1:]
        return(l_new)

    if len(l) <= 1:
        return (l)
    else:
        l1 = sort(l[:len(l)//2])
        l2 = sort(l[len(l)//2:])
        return(merge(l1,l2))

def return_last_larger_elem(l, elem, start, stop):
    for k in range(start, stop):
        if elem > l[k]:
            return (k-1)
    return(stop)


l = ['d', 'c', 'h', 'b', 'a', 'e', 'g', 'l', 'k', 'o', 'n', 'm', 'j', 'i']
# l = [2,1,9,11,5,12]
print(next_permutation(l))