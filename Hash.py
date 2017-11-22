import random
import matplotlib.pyplot as plt


def function_1(x):
    return ord(x)-65


def function_2(x, num_buckets):
    return (ord(x)-65)*random.randrange(0,num_buckets)


def hash_string(name_string, num_buckets):
    hash_location_1 = 0
    hash_location_2 = 0
    name_list = list(name_string)
    for word in name_list:
        hash_location_1 = hash_location_1 + function_1(word)
        hash_location_2 = hash_location_2 + function_2(word, num_buckets)
    hash_location_1 = hash_location_1 % num_buckets
    hash_location_2 = hash_location_2 % num_buckets

    return hash_location_1, hash_location_2


def calculate_hashes(input_stream, num_buckets):
    hash_1 = []
    hash_2 = []
    hd_1 = {}
    hd_2 = {}
    loc_1 = {}
    loc_2 = {}
    for index, name in enumerate(input_stream):
        location_1, location_2 = hash_string(name, num_buckets)
        hash_1.append(location_1)
        hash_2.append(location_2)

        if location_1 in hd_1:
            hd_1[location_1] = hd_1[location_1] + 1
        else:
            hd_1[location_1] = 1

        if location_2 in hd_2:
            hd_2[location_2] = hd_2[location_2] + 1
        else:
            hd_2[location_2] = 1

        loc_1[index] = max(hd_1.values())
        loc_2[index] = max(hd_2.values())

    return hash_1, hash_2, loc_1, loc_2, hd_1, hd_2


def read_input(input_file):
    input_stream = []
    i = 0
    for line in open(input_file):
        column = line.split('\t')
        if column:
            if i % 2 == 0:
                input_stream.append(column[0])
            i = i + 1
    return input_stream


def procedure(input_file, num_buckets):
    input_strings = read_input(input_file)
    hash_1, hash_2, loc_1, loc_2, hd_1, hd_2 = calculate_hashes(input_strings, num_buckets)
    plt.hist(hd_1.values(), histtype='bar')
    plt.hist(hd_2.values(), histtype='bar')
    plot_hist(hash_1, hash_2, loc_1, loc_2, num_buckets)


def comparision(inp):
    list_primes = [701,1601,2707,3701,4703,5701]
    input_strings = read_input(inp)
    collisions_1 = {}
    collisions_2 = {}

    for num in list_primes:
        h_1, h_2, l_1, l_2, hd_1, hd_2 = calculate_hashes(input_strings, num)
        collisions_1[num] = len(input_strings) - len(hd_1)
        collisions_2[num] = len(input_strings) - len(hd_2)

    plt.xlabel("prime number")
    plt.ylabel("collision count")
    plt.plot(list(collisions_1.keys()), list(collisions_1.values()))
    plt.show()
    plt.plot(list(collisions_2.keys()), list(collisions_2.values()))
    plt.show()




def plot_hist(hist_1, hist_2, loc_1, loc_2, num_buckets):
    plt.xlabel("hash location")
    plt.ylabel("count")
    bins = []
    for i in range(0, 5701):
        bins.append(1*i)
    #plt.hist(hist_1, bins, histtype='bar')
    #plt.hist(hist_2, bins, histtype='bar')
    plt.plot(list(loc_1.keys()), list(loc_1.values()))
    plt.plot(list(loc_2.keys()), list(loc_2.values()))
    plt.show()


if __name__ == "__main__":
    ip = r'dist.all.last.txt'
    buckets = 5701
    procedure(ip, buckets)
    #comparision(ip)










