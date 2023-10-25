import os


def print_header(header_text):
    print(f"{'=' * 35}")
    print(f"{header_text.center(35)}")
    print(f"{'=' * 35}")


def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")


def get_valid_path(prompt_text):
    while True:
        path = input(prompt_text)
        if os.path.isdir(path):
            print_colored("Path verified.", "92")
            return path
        print_colored("Invalid path. Please try again.", "91")


def remove_code_block_markers(input_string):
    # Remove first three backticks and "jsx"
    cleaned_string = input_string.replace("```jsx", "", 1)

    # Remove last three backticks
    cleaned_string = cleaned_string.rstrip("```")

    return cleaned_string
