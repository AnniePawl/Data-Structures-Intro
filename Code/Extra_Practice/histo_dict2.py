
# READ FROM THIS FILE
# file = open("../sample_text.txt")


def get_word_list(file_name='./golden_bird.txt'):
    '''Gets words, gets rid of nonsense'''
    file = open(file_name, 'r')
    read_words = file.readlines()
    # Don't forget to close file!
    file.close()
    words = list()
    for line in read_words:
        split_line = line.strip().split(" ")
        for word in split_line:
            if(word.lower() != ""):
                words.append(word.lower().strip("(),!."""))

    return words


# Results should look like: # Results should look like this:
''' histogram = {'one': 1, 'blue': 1, 'two': 1, 'fish': 4, 'red': 1} '''
# Define Hisodict variable
histo_dict2 = {}
# Check if you've seen word
# If not, add it as new key and make value 1
# If yes, just increae value by 1
# Return histogram


if __name__ == '__main__':
    # print(get_word_list())
