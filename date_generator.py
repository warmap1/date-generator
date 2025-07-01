import random as r

def day(y, m):
    if m in (1, 3, 5, 7, 8, 10, 12):
        return r.randint(1, 31)
    elif m in (4, 6, 9, 11):
        return r.randint(1, 30)
    return r.randint(1, 29 if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0) else 28)

def main():
    y = r.randint(2010, 2025)
    m = r.randint(1, 12)
    print(f"{y}-{m:02}-{day(y, m):02}")

if __name__ == "__main__":
    main()
