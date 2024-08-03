import csv

def read_cooldowns_and_stones(gt_filename, bh_filename):
    """
    Read cooldown and stones values from two CSV files.
    """
    gt_data = []
    bh_data = []

    def get_column_indices(header):
        """
        Get the indices of the 'Cooldown' and 'Stones (Cooldown)' columns.
        """
        cooldown_index = None
        stones_cooldown_index = None
        for i, column_name in enumerate(header):
            if 'Cooldown' in column_name and 'Stones' not in column_name:
                cooldown_index = i
            elif 'Stones (Cooldown)' in column_name:
                stones_cooldown_index = i
        if cooldown_index is None or stones_cooldown_index is None:
            raise ValueError("Required columns not found")
        return cooldown_index, stones_cooldown_index

    def read_data(filename):
        """
        Read cooldown and stones data from a CSV file.
        """
        data = []
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the first line (file name)
            header = next(reader)  # Read the header row
            cooldown_index, stones_cooldown_index = get_column_indices(header)
            for row in reader:
                try:
                    cooldown = int(row[cooldown_index].replace('s', ''))
                    stones_cooldown = int(row[stones_cooldown_index].replace('s', ''))
                    data.append({'cooldown': cooldown, 'stones_cooldown': stones_cooldown})
                except (ValueError, IndexError):
                    continue  # Skip rows with non-numeric values or missing columns
        return data

    gt_data = read_data(gt_filename)
    bh_data = read_data(bh_filename)

    return gt_data, bh_data