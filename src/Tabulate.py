from tabulate import tabulate

def f2c(f):
    return round((f - 32) * 5 / 9, 2)


if __name__ == '__main__':
    temps = [[f, f2c(f)] for f in range (30, 60)]

    print(tabulate(temps, headers=['F', 'C',]))                         #Tabulates table and make 'F', 'C' the first row
    print()
    print(tabulate(temps, headers=['F', 'C',], tablefmt="fancy_grid"))  #Provides a neat format you can also use 'plain'
    print()
    print(tabulate(temps, headers="firstrow"))                          #Makes the first row the header eg. "30   -1.11"
    print()
    print(tabulate(temps, headers=['F', 'C',], tablefmt="html"))        #Creates hmtl markup that can be opened in browser




