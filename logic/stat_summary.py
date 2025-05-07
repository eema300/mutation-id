from collections import Counter

def get_gc_content(sequence):
    clean_sequence = sequence.replace('-', '')
    gc = 0
    
    for base in clean_sequence:
        gc += 1 if base == 'G' or base == 'C' else 0
    
    gc_content = gc/float(len(clean_sequence)) * 100

    return f"{gc_content:.2f}%"


def get_base_proportion(sequence, symbol):
    clean_sequence = sequence.replace('-', '')
    base = 0

    for nucleotide in clean_sequence:
        base += 1 if nucleotide == symbol else 0
    
    proportion = base/float(len(clean_sequence)) * 100

    return f"{proportion:.2f}%"


def get_base_proportions(sequence):
    clean_sequence = sequence.replace('-', '')
    
    # sort the dictionary and put the N counts at the end
    counts = dict(sorted(Counter(clean_sequence).items()))
    if 'N' in counts:
        counts_N = counts.pop('N')
        counts['N'] = counts_N

    return counts


def find_repeats(sequence):
    clean_sequence = sequence.replace('-', '')
    k = 2
    min_repeats = 3
    repeats = 0

    for i in range(len(clean_sequence) - k * min_repeats + 1):
        unit = clean_sequence[i:i+k]
        if unit * min_repeats in clean_sequence[i:i+k*min_repeats]:
            repeats += 1

    repeat_proportion = repeats/float(len(clean_sequence)) * 100

    return f"{repeat_proportion:.2f}%"