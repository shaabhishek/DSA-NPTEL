def merge(l1, l2):
    mergedseq = []
    while len(l1) or len(l2):
        if not len(l1):
            mergedseq.extend(l2)
            l2.clear()
        elif not len(l2):
            mergedseq.extend(l1)
            l1.clear()
        elif l1[0] < l2[0]:
            mergedseq.append(l1[0]);
            l1.remove(l1[0]);
        else:
            mergedseq.append(l2[0]);
            l2.remove(l2[0]);
    return (mergedseq)

# computes merge as A \ B
def merge_difference(l1, l2):
    mergedseq = [];
    for el in l1:
        if el not in l2:
            mergedseq.append(el);
    return (mergedseq)



def sort(seq):
    if len(seq) > 1:
        seq = merge(sort(seq[:len(seq)//2]), sort(seq[len(seq)//2:]))
    return (seq)

# b = list(range(100000,1,-1));
# b_sorted = sort(b);
# print(b_sorted)