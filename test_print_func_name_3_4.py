def print_name(param1, param2, param3):
    b = param1.replace('_', ' ').title()
    print(f"{b} {param2} {param3}")


def open_browser(browser_name):
    print_name(open_browser.__name__, browser_name, "")


def go_to_companyname_homepage(page_url):
    print_name(go_to_companyname_homepage.__name__, page_url, "")


def find_registration_button_on_login_page(page_url, button_text):
    print_name(find_registration_button_on_login_page.__name__, page_url, button_text)

open_browser("Chrome")
go_to_companyname_homepage("Google.com")
find_registration_button_on_login_page("Google.com", "Log In")