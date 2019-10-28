class State:
    def __init__(self, key, is_final):
        self.key = key
        self.is_final = is_final
        self.next_states = []

    def __hash__(self):
        return int(self.key)

    def __eq__(self, other):
        return self.key == other.key

    def __str__(self):
        return f'Key:{self.key} Is final:{self.is_final}'


class FiniteStateMachine:
    def __init__(self):
        self.states = {}
        self.graph = {}
        self.alphabet = set()

    def __str__(self):
        str_result = ''

        str_result += '###### States ######\n'
        for _, state in self.states.items():
            str_result += str(state) + '\n'

        str_result += '###### Alphabet ######\n'
        for element in self.alphabet:
            str_result += element + '\n'

        str_result += '###### Transitions ######\n'
        for key, value in self.graph.items():
            for edge in value:
                str_result += key.key + ' -- ' + edge[1] + ' --> ' + edge[0] + '\n'

        str_result += '###### Final states ######\n'
        for _, state in self.states.items():
            if state.is_final:
                str_result += str(state) + '\n'

        return str_result

    @staticmethod
    def read_machine(file_name):
        finite_state_machine = FiniteStateMachine()

        with open(file_name, 'r') as file:
            alphabet_line = file.readline().strip()
            for letter in alphabet_line:
                finite_state_machine.alphabet.add(letter)

            states_line = file.readline()
            for state in states_line.split(' '):
                value, is_final = state.strip().split(',')
                state = State(value, True if is_final == '1' else False)
                finite_state_machine.states[value] = state
                finite_state_machine.graph[state] = []

            for line in file:
                line = line.strip()
                start_node, end_node, char = line.strip().split(' ')
                finite_state_machine.graph[finite_state_machine.states[start_node]].append((end_node, char))

        return finite_state_machine
