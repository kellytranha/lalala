import sys

def main():
    contents = sys.stdin.readlines()

    first = contents[0].split()
    l, n, k, q = [int(num) for num in first]

    string_list = contents[1:l+1]

    strings = "".join(string.strip() for string in string_list)

    data = {}
    for i in range(n - k + 1):
        word = strings[i:i+k]
        data[word] = data.get(word, 0) + 1
    
    kmers = [kmer.strip() for kmer in contents[-q:]]
    
    for kmer in kmers:
        if kmer in data:
            print("{} {}".format(kmer, data[kmer]))
        else:
            print("{} {}".format(kmer, 0))

if __name__ == "__main__":
    main()