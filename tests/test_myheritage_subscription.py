from src.utils.test_helpers import verify_plans_below_threshold, save_filtered_plans


def test_myheritage_subscription_plans(pages):
    pages.google_search_page.navigate()
    pages.google_search_page.search_and_click_link("MyHeritage", 'myheritage.com')

    pages.myheritage_home_page.click_price_list()
    plans = pages.myheritage_price_list_page.fetch_myheritage_plans()

    verify_plans_below_threshold(plans, 200)
    save_filtered_plans(plans, 250)  # Filtered plan file saved under tests/results/sorted_plans.txt
