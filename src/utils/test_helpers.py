# test_helpers module contains functions that support test logic, such as data filtering and processing

def verify_plans_below_threshold(plans, threshold):
    assert any(price < threshold for _, price in plans), f"No plans found below ${threshold}."

def save_filtered_plans(plans, price_threshold):
    filtered_plans = sorted(
        [plan for plan in plans if plan[1] < price_threshold],
        key=lambda x: x[1]
    )
    from src.utils.file_utils import save_sorted_plans
    save_sorted_plans(filtered_plans)
