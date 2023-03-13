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
        self.result = [0]

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
            
            # save the path
            self.result.append(self.current_state)

        # check if we proceed all letters
        # and we are in a final state
        if len(word) == 0 and self.nodes[self.current_state].final:
            print('acceptat')
            print("Drum: ", *self.result, end=' ')
            print()
        else:
            print("neacceptat")
        
    

class NFA:
    
    def __init__(self):
        self.current_state = 0
        self.nodes = []
        self.result = [0]
        self.accepted = False

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
    def validate_word(self, word, current_state=0):

        # if self.accepted:
        #     return

        word = list(word)
        self.current_state = current_state

        while len(word) and self.current_state != -1:

            # get the current letter to be processed
            current_letter = word.pop(0)

            # get the next node
            # for i
            # self.current_state = self.nodes[self.current_state].next(current_letter)[0]
            # print(self.current_state, current_letter, word)

            states = self.nodes[self.current_state].next(current_letter)

            if len(states) > 1 and self.accepted == False:
                for state in states:
                    # print(state, word)
                    self.validate_word("".join(word), state)
                    if self.accepted:
                        break
            else:
                self.current_state = states[0]

            # check to see if we have an invalid state
            if self.current_state == -1 and self.accepted:
                print('neacceptat')
                return
            
            # save the path
            self.result.append(self.current_state)

        # check if we proceed all letters
        # and we are in a final state
        if len(word) == 0 and self.nodes[self.current_state].final and self.accepted != True:
            print('acceptat')
            print("Drum: ", *self.result, end=' ')
            self.accepted = True
            print()
        elif self.accepted == False:
            print("neacceptat")
        


actual = NFA()
actual.read_from("nfa2.txt")
actual.validate_word("")
# for node in actual.nodes:
#     node.display()
