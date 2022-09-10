import sys
import datetime

def age_calculator():
    if len(sys.argv) > 1:
        try:
            year_of_birth = int(sys.argv[1])
            age = (datetime.datetime.now().year) - year_of_birth
            print("Your age is: {} years".format(age))
        except ValueError:
            print("Enter valid year")
        sys.exit()

def main():
    age_calculator()

if __name__ == "__main__":
    main()
    
