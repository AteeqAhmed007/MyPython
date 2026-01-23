
def check_age(age):
    """
    This Program Checks if someone is an adult.
    """
    # PEP 8 Rule: Use 4 spaces for indentation or a single Tab
    if age >= 18:
        return True
    else:
        return False

# PEP 8 Rule: Leave blank lines between functions
if __name__ == "__main__":
    
    # PEP 8 Rule: Recommended to Use 'snake_case' (lowercase with underscores) for names
    user_name = "John_Doe"
    user_age = 20

    # PEP 8 Rule: Put spaces around operators (=, >)
    is_adult = check_age(user_age)

    print(f"User: {user_name}")
    print(f"Is Adult: {is_adult}")