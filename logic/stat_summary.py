def get_gc_content(sequence):
    gc = 0
    
    for base in sequence:
        gc += 1 if base == 'G' or base == 'C' else 0
    
    gc_content = gc/float(len(sequence)) * 100

    return f"{gc_content:.2f}%"


def get_base_proportion(sequence, symbol):
    base = 0

    for nucleotide in sequence:
        base += 1 if nucleotide == symbol else 0
    
    proportion = base/float(len(sequence)) * 100

    return f"{proportion:.2f}%"


def find_repeats(sequence):
    k = 2
    min_repeats = 3
    repeats = 0

    for i in range(len(sequence) - k * min_repeats + 1):
        unit = sequence[i:i+k]
        if unit * min_repeats in sequence[i:i+k*min_repeats]:
            repeats += 1

    repeat_proportion = repeats/float(len(sequence)) * 100

    return f"{repeat_proportion:.2f}%"