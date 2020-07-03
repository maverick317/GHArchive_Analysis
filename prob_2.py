
def main():
    input_string = str(input("Enter text: "))
    input_string = " ".join(input_string.split())
    if len(input_string) == 0:
        print("Invalid input string")
        return

    word_list = [word for word in input_string.split(" ") if len(word)>1]
    histogram = {}


    for word in word_list:
    
        for start_index in range(0, len(word) - 1):

            key = word[start_index:start_index + 2]

            if key in histogram.keys():
                value = histogram[key] + 1

            else:
                value = 1

            histogram[key] = value

    print("Histogram: ", end = "")

    if (len(word_list) < 1):
        return

    sorted_tuples = sorted(histogram.items(), key=lambda x: x[1], reverse=True)

    for index in range(len(sorted_tuples) - 1):
        print(sorted_tuples[index][0], ":", sorted_tuples[index][1], end = ", ")

    print(sorted_tuples[-1][0], ":", sorted_tuples[-1][1])

if __name__ == "__main__":
    main()