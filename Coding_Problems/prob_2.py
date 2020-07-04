#!/usr/local/bin/python
# encoding: utf-8


def main():

    input_string = str(input("Enter text: "))

    # split the input_string to words and remove words with length = 1
    word_list = [word for word in input_string.split() if len(word)>1]

    # Error out if there are no words longer than 2 characters
    if len(word_list) == 0 :
        print("ERROR: Too short words to process")
        return

    # Histogram to store character pairs and their counts.
    # key: character pairs, value: count. Example: {'th':2}
    histogram = {}

    for word in word_list:
        for index in range(0, len(word)-1):

            # Extract character pairs from the word
            key = word[index:index+2]

            if key in histogram.keys():
                histogram[key] += 1
            else:
                histogram[key] = 1

    print("Histogram: ", end="")

    sorted_tuples = sorted(histogram.items(), key=lambda x: x[1], reverse=True)

    # printing the sorted tuples by count
    for index in range(len(sorted_tuples)):

        if index != len(sorted_tuples)-1:
            print(sorted_tuples[index][0], ":", sorted_tuples[index][1], end=", ")
        else:
            # printing last element without comma in the end
            print(sorted_tuples[index][0], ":", sorted_tuples[index][1])


if __name__ == "__main__":
    main()