class Instance():

    def __init__(self):

    ''' if lists to be used
    def __len__(self):
        return len(self.grid)

    def __getitem__(self, key):
        return self.grid[key]

    def __setitem__(self, key, value):
        self.grid[key] = value
    '''

class Parser():
    
    def __init__(self):
        self.instance = None
        
    def parse_first_line(self, line):
        sl = line.rstrip().split(' ')
        return sl[0], sl[1], sl[2], sl[3]

    def parse_line(self, line):
        sl = list(line.rstrip())

        #grid_line = [1 if x == 'T' else 0 for x in sl]
        return grid_line

    def parse_file(self, input):
        line = input.readline()
        rows, cols, min_ing, max_slice = self.parse_first_line(line)
        self.instance = Instance()
        line = input.readline()
        while(line):
            gline = self.parse_line(line)
            # do something like self.instance.add_line(gline)
            line = input.readline()
        if (len(self.instance) != int(rows)):
            raise ValueError('Incorrect number of lines in file')

if __name__ == '__main__':
    import sys

    filename = sys.argv[1]
    file = open(filename, 'r')

    parser = Parser()
    parser.parse_file(file)
    instance = parser.instance
