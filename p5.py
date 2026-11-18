import sys

def calculate_si(principal, rate, time):
    si = (principal * rate * time) / 100
    return si

if __name__ == "__main__":
    principal = float(sys.argv[1])
    rate = float(sys.argv[2])
    time = float(sys.argv[3])

    si = calculate_si(principal, rate, time)

    print("Simple Interest:", si)