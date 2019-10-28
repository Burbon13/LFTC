from src.analyzer import lexical_analyze
from src.table import Table
from src.finit_state_machine import FiniteStateMachine


def lab_1():
    # the path of the atoms table file
    ATOMS_FILE_PATH = '../data/atoms.txt'
    # the path of the file to be analyzed and executed
    SOURCE_FILE_PATH = '../data/p1.txt'
    # separators file path
    SEPARATORS_FILE_PATH = '../data/separators.txt'

    # Reading the source file
    with open(SOURCE_FILE_PATH, 'r') as input_file:
        # content = the content of the source file which will be analyzed & executed
        content = input_file.read()

    # Reading the symbol table
    atoms_table = Table()
    with open(ATOMS_FILE_PATH) as atoms_file:
        for index, line in enumerate(atoms_file):
            atoms_table.put(line.strip(), index)

    # Reading the separators
    separators = []
    with open(SEPARATORS_FILE_PATH, 'r') as input_file:
        for line in input_file:
            separators.append(line.strip())

    internal_program_form, id_symbol_table, const_symbol_table = lexical_analyze(content, atoms_table, separators)
    print('Internal program form:\n' + str(internal_program_form))
    print('Id table:\n' + str(id_symbol_table))
    print('Const table:\n' + str(const_symbol_table))


def lab_2():
    finite_state_machine = FiniteStateMachine.read_machine('../data/state_machines/c_constants')
    print(finite_state_machine)


lab_2()
