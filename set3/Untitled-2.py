def be_silly(top_part, bottom_part):
    try:
        return top_part / bottom_part
    except TypeError as my_error:
        print(f"you are so silly! {my_error}")
    except ZeroDivisionError as my_error:
        print(
            f"you are so silly! Can't divide {top_part} by {bottom_part} "
            f"or we get infinity\n{my_error}"
        )
    except Exception as general_error:
        print(general_error)
print(be_silly(10, 0))
print(be_silly("cake", "you"))

try:
        return int(lowerBound)
    except:
       lowerBound
    try:
        return int(upperBound)
    except:
       upperBound
