import math
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
        if sequence_1[i] != sequence_2[i] and sequence_2[i] != '-' and sequence_1[i] != 'N' and sequence_1[i] != '-':
            positions.append(i)

    return positions


def find_insertion_mutations(sequence_1, sequence_2):
    n = len(sequence_1)
    m = len(sequence_2)
    shortest_sequence_length = n if n <= m else m

    positions = []

    for i in range(shortest_sequence_length):
        # found insertion mutation
        if sequence_1[i] != sequence_2[i] and sequence_1[i] == '-':
            positions.append(i)

    return positions


def find_deletion_mutations(sequence_1, sequence_2):
    n = len(sequence_1)
    m = len(sequence_2)
    shortest_sequence_length = n if n <= m else m

    positions = []

    for i in range(shortest_sequence_length):
        # found insertion mutation
        if sequence_1[i] != sequence_2[i] and sequence_2[i] == '-':
            positions.append(i)

    return positions


def find_all_mutations(sequence_1, sequence_2):
    n = len(sequence_1)
    m = len(sequence_2)
    shortest_sequence_length = n if n <= m else m

    positions = []

    for i in range(shortest_sequence_length):
        if sequence_1[i] != sequence_2[i]:
            positions.append(i)

    return positions


def create_bins(sequence_mt):
    # divide sequence into bins of length 20 for better visualization
    num_bins = math.ceil(len(sequence_mt) / 20)

    bins = []

    starting_index = 0
    ending_index = 19

    for i in range(num_bins):
        bins.append(range(starting_index, ending_index))
        starting_index += 20
        ending_index += 20

    return bins


def apply_bins(bins, positions):
    bin_counts = [0] * len(bins)

    for mutation in positions:
        for i in range(len(bins)):
            if mutation in bins[i]:
                bin_counts[i] += 1

    return bin_counts


def get_mutation_types(sequence_1, sequence_2):
    n = len(sequence_1)
    m = len(sequence_2)
    shortest_sequence_length = n if n <= m else m

    mutation_types = {'deletion': 0,
                      'substitution': 0,
                      'insertion': 0}

    for i in range(shortest_sequence_length):
        if sequence_1[i] == '-':
            mutation_types['insertion'] += 1
        elif sequence_1[i] != sequence_2[i] and sequence_2[i] == '-':
            mutation_types['deletion'] += 1
        elif sequence_1[i] != sequence_2[i] and sequence_2[i] != '-':
            mutation_types['substitution'] += 1

    return mutation_types


def loc_mutation_types(sequence_1, sequence_2):
    n = len(sequence_1)
    m = len(sequence_2)
    shortest_sequence_length = n if n <= m else m

    mutations = {}

    for i in range(shortest_sequence_length):
        if sequence_1[i] == '-':
            mutations[i] = 'insertion'
        elif sequence_1[i] != sequence_2[i] and sequence_2[i] == '-':
            mutations[i] = 'deletion'
        elif sequence_1[i] != sequence_2[i] and sequence_2[i] != '-':
            mutations[i] = 'substitution'

    return mutations