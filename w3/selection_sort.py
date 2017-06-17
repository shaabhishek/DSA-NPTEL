def selection_sort(seq):

    for i in range(len(seq)):
        min = i;
        for j in range(i+1,len(seq)):
            if seq[j] < seq[min]:
                min = j;
        if (i != min):
            (seq[i], seq[min]) = (seq[min], seq[i])