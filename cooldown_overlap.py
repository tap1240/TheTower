from csv_reader import read_cooldowns_and_stones

def calculate_overlap(gt_cooldown, bh_cooldown, runtime_hours):
    """
    Calculate the overlap percentage of cooldowns within a given runtime.
    """
    runtime_seconds = runtime_hours * 3600
    gt_activations = runtime_seconds // gt_cooldown
    bh_activations = runtime_seconds // bh_cooldown
    overlap_count = 0

    for second in range(runtime_seconds):
        if second % gt_cooldown == 0 and second % bh_cooldown == 0:
            overlap_count += 1

    # Calculate the total possible activations
    total_possible_activations = min(gt_activations, bh_activations)

    # Calculate the overlap percentage
    overlap_percentage = (overlap_count / total_possible_activations) * 100
    return overlap_percentage

def find_optimal_cooldowns():
    """
    Find the optimal cooldowns that maximize the overlap percentage.
    """
    gt_data, bh_data = read_cooldowns_and_stones('golden_tower.csv', 'black_hole.csv')
    runtime_hours = 24  # Example runtime

    results = []

    for gt in gt_data:
        for bh in bh_data:
            overlap_percentage = calculate_overlap(gt['cooldown'], bh['cooldown'], runtime_hours)
            total_gt_stones = gt['stones_cooldown']
            total_bh_stones = bh['stones_cooldown']
            total_stones = total_gt_stones + total_bh_stones
            results.append((gt['cooldown'], bh['cooldown'], total_stones, overlap_percentage))

    # Sort results by overlap percentage (descending) and total stones (ascending)
    results.sort(key=lambda x: (-x[3], x[2]))

    return results

def main():
    """
    Main function to find and print the optimal cooldowns.
    """
    print("Read cooldowns from CSV files.")
    results = find_optimal_cooldowns()

    for gt_cooldown, bh_cooldown, total_stones, overlap_percentage in results:
        print(f"GT Cooldown: {gt_cooldown}s, BH Cooldown: {bh_cooldown}s, Total Stones: {total_stones}, Overlap Percentage: {overlap_percentage:.2f}%")

if __name__ == "__main__":
    main()