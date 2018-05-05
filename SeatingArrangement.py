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
			valid_seat_list = list(range(1, room_map_dict[row]-1))
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

	sections_map = {101: 25, 102: 25, 103: 19, 104: 24, 105: 25, 106: 26,
	                 107: 26, 108: 25, 109: 25, 110: 25, 111:26, 112: 25}

	room_map = {'A': 12, 'B': 22, 'C': 24, 'D': 25,
	             'E': 26, 'F': 26, 'G': 29,'H': 29,
	             'I': 30, 'J': 33, 'K': 33,'L': 34,
	             'M': 37, 'N':37 ,'O': 28}

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






