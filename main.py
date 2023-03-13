class Node:

    # Object methods
    def __init__(self, number, final, paths):

        # naming convetion q{number}
        self.number = number
        # if the node is final
        self.final = final
        # the node that are adjacent
        self.paths = {}

        #
        for elem in paths:
            try:
                self.paths[elem[0]].append(elem[1])
            except Exception:
                self.paths[elem[0]] = [elem[1]]

    def display(self):
        print(self.number, self.final, self.paths)

    def next(self, letter):
        # we try to get the next node
        try:
            return self.paths[letter]
        # if we receive an invalid letter
        # we are out of transitions
        except Exception:
            return [-1]

    

class DFA:
    
    def __init__(self):
        self.current_state = 0
        self.nodes = []

    # reads the DFA from filename
    def read_from(self, filename):
        with open(filename, 'r') as f:
            for line in f.readlines():
                data = line.strip().split()
                paths = [(data[i+1], int(data[i])) for i in range(2,len(data),2)]
                final = True if data[1] == 'f' else False

                self.nodes.append(Node(data[0], final, paths))

    # deletes the read nodes
    def empty(self):
        self.nodes = []

    # check if a word is accepted
    # prints on the screen the result
    def validate_word(self, word):

        word = list(word)

        while len(word) and self.current_state != -1:
            # get the current letter to be processed
            current_letter = word.pop(0)
            # get the next node
            self.current_state = self.nodes[self.current_state].next(current_letter)[0]
            # check to see if we have an invalid state
            if self.current_state == -1:
                print('neacceptat')
                return

        # check if we proceed all letters
        # and we are in a final state
        if len(word) == 0 and self.nodes[self.current_state].final:
            print('acceptat')
        else:
            print("neacceptat")
        
    

actual = DFA()
actual.read_from("in.txt")
actual.validate_word("ababab")
