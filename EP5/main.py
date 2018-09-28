from percolation import Percolation

def main():

    exemplo = Percolation(4)
    exemplo.open(1,2)
    exemplo.open(2,2)
    exemplo.open(0,2)
    exemplo.open(0,0)
    exemplo.open(1,0)
    exemplo.open(2,0)
    exemplo.open(3,2)
    print(exemplo.no_open())

if __name__ == '__main__':
    main()