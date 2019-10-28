class State:
    def __init__(self, key, is_final):
        self.key = key
        self.is_final = is_final
        self.next_states = []

    def __hash__(self):
        return int(self.key)

    def __eq__(self, other):
        return self.key == other.key


class FiniteStateMachine:
    def __init__(self):
        self.states = {}
        self.graph = {}

    @staticmethod
    def read_machine(file_name):
        finite_state_machine = FiniteStateMachine()

        with open(file_name, 'r') as file:
            first_line = file.readline()

            for state in first_line.split(' '):
                value, is_final = state.split(',')
                state = State(value, True if is_final == '1' else False)
                finite_state_machine.states[value] = state
                finite_state_machine.graph[state] = []

            for line in file:
                line = line.strip()
                start_node, end_node, char = line.split(' ')
                finite_state_machine.graph[finite_state_machine.states[start_node]].append((end_node, char))
        a = 3
