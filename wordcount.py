words_dict = {}

word_file = open("twain.txt")

for line in word_file:
# iterate through each line in file
    line = line.rstrip()
    line = line.split()

    for word in line:
    # for every word in line
        if words_dict.get(word, 0) == 0:
        # if word is not in dictionary
            words_dict[word] = 1
            # add it to dictionary
        else:
            words_dict[word] += 1

for word, count in words_dict.iteritems():
    print word, count