import numpy as np


def create_random_seating(section_map_dict, room_map_dict):
	seating_map = {}
	for section in section_map_dict:
		for i in range(0, section_map_dict[section]):
			row = np.random.choice(list(room_map_dict.keys()))
			seat_list = np.linspace(1, room_map_dict[row])
			column = np.random.choice(seat_list)
			seat_number = str(row) + str(column)
			if section in sections_map:
				if seat_number not in sections_map[section]:
					sections_map[section].append(seat_number)
			else:
				list_sec = [seat_number]
				sections_map[section] = list_sec
	return seating_map

if __name__ == "__main__":

	sections_map = { 101: 25, 102: 25, 103: 19, 104: 23, 105: 25, 106: 26,
	                 107: 26, 108: 25, 109: 25, 110: 25, 111:26, 112: 25 }

	room_map = {'A': 12, 'B': 22, 'C': 24, 'D': 25,
	             'E': 26, 'F': 26, 'G': 29,'H': 29,
	             'I': 30, 'J': 33, 'K': 33,'L': 34,
	             'M': 37, 'N':37 ,'O': 28}
	create_random_seating(sections_map, room_map)




