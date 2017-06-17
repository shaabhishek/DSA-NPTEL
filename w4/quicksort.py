# sort seq[l:r]
def quicksort(seq, l, r):
    if r - l <= 1:
        return ()

    pivot = seq[l];
    # yellow is the pointer for the subsequence lesser than or equal to pivot
    # green is the pointer for the subsequence greater than the pivot
    (yellow, green) = (l+1,l+1)

    for green in range(l+1,r):
        # print(seq, l, r, yellow, green)
        # rightmost elem is smaller than pivot, swap it with the first green elem
        if seq[green] <= pivot:
            (seq[yellow], seq[green]) = (seq[green], seq[yellow])
            yellow = yellow + 1;

    # replace the last yellow elem with the pivot elem
    (seq[l], seq[yellow-1]) = (seq[yellow - 1], seq[l])
    
    quicksort(seq, l, yellow-1);
    quicksort(seq, yellow, r);

a = list(range(1100, 1, -1))
quicksort(a, 0, len(a))
print(a)