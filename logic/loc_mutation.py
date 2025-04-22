
# finds substitution mutations
# input sequences must be aligned at this point
# sequence 1 -> wild type
# sequence 2 -> mutated

# returns array of positions of substitution mutations in the mutated sequence
def find_sub_mutation(sequence_1, sequence_2):
    n = len(sequence_1)
    m = len(sequence_2)
    shortest_sequence_length = n if n <= m else m

    positions = []

    for i in range(shortest_sequence_length):
        # found substitution mutation
        if sequence_1[i] != sequence_2[i] and sequence_2[i] != '-':
            positions.append(i)

    return positions