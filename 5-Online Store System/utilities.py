# helpers to prevent impossible data
# e.g. the user enters the discount as 150%, then a price of a 100 item becomes -50
def get_int(prompt, min_val = None, max_val = None) :
    while True :
        raw = input(prompt).strip()
        try :
            value = int(raw)
        except ValueError :
            print("Please enter a whole number : ")
            continue
        if min_val is not None and value < min_val :
            print(f"Value must be at least {min_val}")
            continue
        if max_val is not None and value > max_val :
            print(f"Value must be at most {max_val}")
            continue
        return value

def get_float(prompt, min_val = None, max_val = None) :
    while True :
        raw = input(prompt).strip()
        try :
            value = float(raw)
        except ValueError :
            print("Please enter a numeric number : ")
            continue
        if min_val is not None and value < min_val :
            print(f"Value must be at least {min_val}")
            continue
        if max_val is not None and value > max_val :
            print(f"Value must be at most {max_val}")
            continue
        return value

def get_nonempty(prompt) :
    while True :
        value = input(prompt).strip()
        if value :
            return value
        print("This field cannot be empty! ")
        
def divider() :
    print("-"*50)

def header(title) :
    print("\n" + "=" * 50)
    print(f"{title}")
    print("=" * 50)