def get_formatted_name(first, last, mid=''):
    # full_name = f"{first} {mid} {last}"
    if mid:
        full_name = f"{first} {mid} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
