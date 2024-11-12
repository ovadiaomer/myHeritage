import os

def save_sorted_plans(plans, file_name="sorted_plans.txt"):
    # Ensure the directory exists
    results_dir = os.path.join("results")
    os.makedirs(results_dir, exist_ok=True)  # Create directory if it doesn't exist

    # Construct the full file path
    file_path = os.path.join(results_dir, file_name)

    # Save the file
    with open(file_path, "w") as file:
        for idx, (name, price) in enumerate(plans, start=1):
            file.write(f"{idx} {name} ${price}\n")
