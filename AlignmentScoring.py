def get_best_alignment(sequence, alignments):
    #Create a function that returns the highest scoring alignment
    #Scores/penalties: Match +2, Mismatch -1, Gap -1

    return 0

def main():
    sequence = 'GATTACA'
    sequence2 = 'GTACA'
    alignments = [
        '--GTACA', '-G-TACA', '-GT-ACA', '-GTA-CA', '-GTAC-A',
        '-GTACA-', 'G-TACA-', 'G-T-ACA', 'G-TA-CA', 'G-TAC-A',
        'G-TACA-', 'GT-ACA-', 'GT-A-CA', 'GT-AC-A', 'GT-ACA-',
        'GTA-CA-', 'GTA-C-A', 'GTA-CA-', 'GTAC-A-', 'G--TACA',
        'G-T-ACA', 'G-TA-CA', 'G-TAC-A', 'G-TACA-', 'GT--ACA',
        'GT-A-CA', 'GT-AC-A', 'GT-ACA-', 'GTA--CA', 'GTA-C-A',
        'GTA-CA-', 'GTAC--A', 'GTAC-A-', 'GTACA--'
    ]
    best = get_best_alignment(sequence, alignments)
    print(f'The best alignment is: \n{sequence}\n{best}')

if __name__ == "__main__":
    main()