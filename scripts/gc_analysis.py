
def calculate_gc(seq):
    seq = seq.upper()
    g = seq.count('G')
    c = seq.count('C')
    return ((g + c) / len(seq)) * 100

# A real snippet from the TB katG gene
tb_sample = "GACCAGCGGCTCGTAGCGCTTGAGCGTGCGCTGGCCGACCTGCTGGCGCT"
human_sample = "ATATATTAGCCATATAGCCGATATAGCTATAATATCGCCGATATAGCTAA"

print(f"TB Sample GC: {calculate_gc(tb_sample):.2f}%")
print(f"Human Sample GC: {calculate_gc(human_sample):.2f}%")
