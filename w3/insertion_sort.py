def insertionsort(seq):

    for sliceEnd in range(len(seq)):
        
        pos = sliceEnd;

        # keep going left until you reach beginning of list or the element is smaller
        while pos > 0 and seq[pos] <= seq[pos-1]:
            (seq[pos], seq[pos-1]) = (seq[pos-1], seq[pos]);
            pos = pos - 1;

a = list(range(2000,1,-1));
insertionsort(a);
# print(a)