import numpy as np
import csv
import itertools
import re


def natural_sort(s, _nsre=re.compile('([0-9]+)')):
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(_nsre, s)]


def create_random_seating(section_map_dict, room_map_dict):
	seating_map = {}
	total_seat_ids = sum(section_map_dict.values())
	seat_id_list = set()
	seat_id = ""
	sorted_seating = []
	sorted_seat_ids = {}
	# Create valid seat number ids
	for i in range(0, total_seat_ids):
		while seat_id in seat_id_list or seat_id == "":
			row = np.random.choice(list(room_map_dict.keys()))
			valid_seat_list = list(range(1, room_map_dict[row]))
			column = np.random.choice(valid_seat_list, replace=False)
			seat_id = str(row) + str(column)
		if seat_id not in seat_id_list:
				seat_id_list.add(seat_id)
	# Randomly assign seat number ids to all the sections
	for section in section_map_dict:
		print(len(seat_id_list))
		num_sec = section_map_dict[section]
		set_list = list(seat_id_list)
		seat_sec = np.random.choice(set_list, num_sec, replace=False).tolist()
		seating_map[section] = seat_sec
		sorted_seating.extend(seat_sec)
		seat_id_list = seat_id_list - set(seat_sec)
	# Natural sort and divide the selected seat ids
	sorted_seating.sort(key=natural_sort)
	for j in sorted_seating:
		if j[0] in sorted_seat_ids:
			sorted_seat_ids[j[0]].append(j)
		else:
			sorted_seat_ids[j[0]] = [j]
	return seating_map, sorted_seat_ids


if __name__ == "__main__":

	sections_map = {101: 23, 102: 22, 103: 15, 104: 24, 105: 26, 106: 25, 107: 25, 108: 24, 109: 25, 110: 26, 111: 25,
	                112: 23, 113: 26, 114: 26, 115: 25, 116: 25}

	room_map = {'A': 18, 'B': 20, 'C': 21, 'D': 24,
				 'E': 24, 'F': 27, 'G': 27,'H': 30,
				 'I': 32, 'J': 33, 'K': 36,'L': 36,
				 'M': 39, 'N':34 }

	dict_section, sorted_seats = create_random_seating(sections_map, room_map)
	print(sorted_seats)

	keys = sorted(dict_section.keys())
	with open("seating.csv", "wb") as outfile:
		writer = csv.writer(outfile)
		writer.writerow(dict_section.keys())
		writer.writerows(itertools.izip_longest(*dict_section.values()))

	keys = sorted(sorted_seats.keys())
	with open("sorting.csv", "wb") as outfile:
		writer = csv.writer(outfile)
		writer.writerow(sorted_seats.keys())
		writer.writerows(itertools.izip_longest(*sorted_seats.values()))






