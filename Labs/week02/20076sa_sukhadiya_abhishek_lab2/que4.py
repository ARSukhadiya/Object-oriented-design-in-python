"""
A program to Calculate and print the time shifts, prior and following according to the input minutes.
"""

def main():
    print("Find the time x minutes before and after the input time")
    input_time = input("Enter a time (hh:mm):")
    input_hours = int(input_time.split(':')[0])
    input_mins = int(input_time.split(':')[1])

    shift_mins = int(input("Enter a time shift in mins: "))
    total_time_mins = input_hours * 60 + input_mins

    # Calculate the before time
    total_before_mins = total_time_mins - shift_mins
    before_hours = (total_before_mins // 60) % 24
    before_mins = total_before_mins % 60
    print("{:02d}:{:02d}".format(before_hours, before_mins))

    # Calculate the after time
    total_after_mins = total_time_mins + shift_mins 
    after_mins = total_after_mins % 60
    after_hours = (total_after_mins // 60) % 24
    print("{:02d}:{:02d}".format(after_hours, after_mins))


if __name__ == "__main__":
    main()
