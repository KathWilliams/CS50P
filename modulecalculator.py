def main():
#    x = int(input("What is x? "))
# what if i remove the int and then enter cat - we get a TypeError
    x = input("What is x? ")
    print(f"square of {x} is",square(x))

def square(n):
    return n * n

if __name__ == "__main__":
    main()