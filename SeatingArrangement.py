import numpy as np


def create_random_seating(section_map_dict, room_map_dict):
	seating_map = {}
	total_seat_ids = sum(section_map_dict.values())
	seat_id_list = []
	for i in range(0, total_seat_ids):
		row = np.random.choice(list(room_map_dict.keys()))
		valid_seat_list = list(range(1, room_map_dict[row]-1))
		column = np.random.choice(valid_seat_list)
		seat_id = str(row) + str(column)
		if seat_id not in seat_id_list:
			seat_id_list.append(seat_id)
		else:
			while seat_id in seat_id_list:
				column = np.random.choice(valid_seat_list, replace=False)
				seat_id = str(row) + str(column)
			seat_id_list.append(seat_id)
	for section in section_map_dict:
		num_sec = section_map_dict[section]
		seat_sec = np.random.choice(seat_id_list, num_sec)
		section_map_dict[section] = seat_sec
		seat_id_list = seat_id_list.remove(seat_sec)
	return seating_map









if __name__ == "__main__":

	sections_map = {101: 25, 102: 25, 103: 19, 104: 23, 105: 25, 106: 26,
	                 107: 26, 108: 25, 109: 25, 110: 25, 111:26, 112: 25}

	room_map = {'A': 12, 'B': 22, 'C': 24, 'D': 25,
	             'E': 26, 'F': 26, 'G': 29,'H': 29,
	             'I': 30, 'J': 33, 'K': 33,'L': 34,
	             'M': 37, 'N':37 ,'O': 28}
	print(create_random_seating(sections_map, room_map))




