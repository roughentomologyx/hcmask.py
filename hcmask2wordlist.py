import itertools


mask_elements = {
    '?d': '0123456789',
    '?l': 'abcdefghijklmnopqrstuvwxyz',
    '?u': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    '?s': ' !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~',
    '?h': '0123456789abcdef',
    '?H': '0123456789ABCDEF'
}

def parse_mask(mask):
    """Parse the hashcat mask into its component character sets."""
    parts = []
    i = 0
    while i < len(mask):
        if mask[i] == '?':
            parts.append(mask_elements[mask[i:i+2]])
            i += 2
        else:
            parts.append(mask[i])
            i += 1
    return parts

def total_combinations(parts):
    return itertools.product(*parts)

def write_combinations_to_file(filename, combinations, total):
    with open(filename, 'w') as file:
        for i, combination in enumerate(combinations, 1):
            file.write(combination + '\n')
            if i % 1000 == 0:  # Update progress every 1000 combinations
                print(f'Progress: {i}/{total} combinations written.', end='\r')

def main():
    # Prompt the user for the input filename
    mask_file = input('Enter the input filename: ')
    output_file = f'{mask_file}.wordlist'
    
    # Initialize variables for total calculation and combinations generation
    total = 0
    all_combinations = []

    # Process each mask from the file
    with open(mask_file, 'r') as file:
        for mask in file:
            mask = mask.strip()
            parts = parse_mask(mask)
            combinations = [''.join(combination) for combination in itertools.product(*parts)]
            all_combinations.extend(combinations)
            total += len(combinations)

    # Write combinations to the output file and show progress
    write_combinations_to_file(output_file, all_combinations, total)

    print(f'\nAll {total} combinations have been written to {output_file}.')

if __name__ == '__main__':
    main()
