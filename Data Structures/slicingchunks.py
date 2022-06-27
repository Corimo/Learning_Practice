sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

def chunk (a, b, c, working_list):
    section = working_list[a : b]
    rev_chunk1 = section[::-1]
    print (f"\n Chunk {c + 1}")
    print (f" Chunk: {section}")
    print (f" Reversed: {rev_chunk1}")

iter = 0
length = (len(sample_list) // 3) - 1 
start = 0
stop = 3

while iter <= length:
    chunk(start, stop, iter, sample_list)
    iter += 1
    start += 3
    stop += 3

print ("\n")