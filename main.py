class Node:

    # Object methods
    def __init__(self, number, final, paths):

        # naming convetion q{number}
        self.number = number
        # if the node is final
        self.final = final
        # the node that are adjacent
        self.paths = {}

        # creating the dict with key a letter
        # and the value a list with all nodes
        for elem in paths:
            try:
                self.paths[elem[0]].append(elem[1])
            except Exception:
                self.paths[elem[0]] = [elem[1]]

    def display(self):
        print(self.number, self.final, self.paths)

    # next node from a given letter
    def next(self, letter):
        # we try to get the next node
        try:
            return self.paths[letter]
        # if we receive an invalid letter
        # we are out of transitions
        except Exception:
            return [-1]


class FA:

    def __init__(self):
        # f for final n for non-final
        self.current_state = 0
        # all the component nodes
        self.nodes = []
        # a list with the nodes visited for a result
        self.result = [0]

    # reads the FA from filename
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


class DFA(FA):
    
    def __init__(self):
        super().__init__()

    def validate_word(self, word):

        # we use a mutable object
        word = list(word)

        # iterating until we have lambda or we are in
        # an invalid state
        while len(word) and self.current_state != -1:

            # get the current letter to be processed
            current_letter = word.pop(0)

            # get the next node
            self.current_state = self.nodes[self.current_state].next(current_letter)[0]

            # check to see if we have an invalid state
            if self.current_state == -1:
                print('not accepted')
                return
            
            # save the path
            self.result.append(self.current_state)

        # check if we proceed all letters
        # and we are in a final state
        if len(word) == 0 and self.nodes[self.current_state].final:
            # print('accepted')
            print("Path: ", *self.result, end=' ')
            print()
            return 'accepted'
        else:
            print("not accepted")
            return 'not accepted'
        
    
class NFA(FA):
    
    def __init__(self):
        super().__init__()
        # if we have at least one accepted path
        self.accepted = False
        self.message = 'not accepted'


    # check if a word is accepted
    # prints on the screen the result
    def validate_word(self, word, current_state=0):

        # mutable object
        word = list(word)
        # state left to be checked
        self.current_state = current_state

        while len(word) and self.current_state != -1:

            # get the current letter to be processed
            current_letter = word.pop(0)

            # get the next node
            states = self.nodes[self.current_state].next(current_letter)

            # if the current node has a nondeterministic behavior
            if len(states) > 1 and self.accepted == False:
                # we iterate all posible nodes
                # with backtracking
                for state in states:
                    self.validate_word("".join(word), state)
                    # if we find already found a valid path
                    # we stop looking for another
                    if self.accepted:
                        break
            # if we have a deterministic behavior
            else:
                self.current_state = states[0]

            # check to see if we have an invalid state
            if self.current_state == -1 and self.accepted:
                return
            
            # save the path
            self.result.append(self.current_state)

        # check if we proceed all letters
        # and we are in a final state
        if len(word) == 0 and self.current_state != -1 and self.nodes[self.current_state].final \
           and self.accepted != True:
            
            print("Path: ", *self.result, sep='->',  end=' ')
            self.accepted = True
            self.message = 'accepted'
            print()
            return self.message
        
        return self.message

        
def menu():
    
    from os import system
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename

    processor = None

    while True:

        print("Menu")
        print("1. Read data from a DFA")
        print("2. Read data from a NFA")
        print("3. Process a given word")
        print("   Press q to exit")

        option = input("Choose an option: ")

        system('cls')

        if option in ['1', '2']:

            # read the input file
            root = Tk()
            # we don't want a full GUI, so keep the root window from appearing
            root.withdraw() 
            # move the window in focus
            root.lift()
            root.attributes("-topmost", True)
            # file asking
            filename = askopenfilename(filetypes=(('Text files', '*.txt'),)) # show an "Open" dialog box and return the path to the selected file
            
            if filename == '':
                print("No file selected")

            else :
                # choosing the right FA
                processor = DFA() if option == 1 else NFA()
                processor.read_from(filename)

                #verify if the user chose a bad FA
                for node in processor.nodes:
                    for letter in node.paths:
                        if len(node.paths[letter]) > 1 and option == '1':
                            print("You wanted to read a DFA, but this file contains a NFA!")
                            processor = None
                            break

        elif option == '3':
            
            if processor == None:
                print("Read data first!")
            
            else:
                word = input("Enter a word to be validated: ")
                result = processor.validate_word(word)
                print('not accepted' if result == None else result)

        elif option == 'q':
            exit(0)

        else:
            print("Enter a valid option!\n")


if __name__ == '__main__':
    menu()
