from src.table import Table
from src.finit_state_machine import FiniteStateMachine

NEWLINE = '\n'
SPACE = ' '
EMPTY_STRING = ''

int_consts_finite_state_machine = FiniteStateMachine.read_machine('../data/state_machines/c_int_constants')
# print('Integer const finite state machine')
# print(int_consts_finite_state_machine)

real_consts_finite_state_machine = FiniteStateMachine.read_machine('../data/state_machines/c_real_constants')
# print('Real const finite state machine')
# print(real_consts_finite_state_machine)

ids_finite_state_machine = FiniteStateMachine.read_machine('../data/state_machines/ident')


# print('Ids finite state machine')
# print(ids_finite_state_machine)


def get_atoms_recursive(text, line_number, separator_list):
    """
    Splits the text based on the separators
    :param text: the text to be splitter
    :param line_number: the number of the line from the file
    :param separator_list: the separators which decide the separation
    :return: a list with the splited tokens
    """
    text = text.strip()

    if text == '':
        return ['']

    if text in separator_list:
        return [text]

    for separator in separator_list:
        if separator in text:
            to_return = []
            token_lists_list = [get_atoms_recursive(token, line_number, separator_list) for token in
                                text.split(separator)]
            for token_list in token_lists_list:
                for token in token_list:
                    to_return.append(token)
                to_return.append(separator)

            return to_return[:-1]

    return [text]


def atom_is_const(atom):
    """
    Verifies if an atom is a const
    :param atom: to be verifies (string)
    :return: true if it is an id, false otherwise
    """
    return int_consts_finite_state_machine.verify_if_string_accepted(atom) \
           or real_consts_finite_state_machine.verify_if_string_accepted(atom)


def atom_is_id(atom):
    """
    Verifies if an atom is an identification
    :param atom: to be verifies (string)
    :return: true if it is an id, false otherwise
    """
    return ids_finite_state_machine.verify_if_string_accepted(atom)


def lexical_analyze(text, atoms_table, separator_list):
    """
    Lexically analyses the source code (text)

    @param text: string which represents the code to be analyzed
    @param atoms_table: instance of Table class which holds the codes for the atoms
    @param separator_list: list of separators
    @return: (internal form of the program, symbols table, const table)
    @throws: exception if any error is found inside the text
    """
    atom_list = []
    for index, line in enumerate(text.split(NEWLINE)):
        for token in [x for x in line.split(SPACE) if x != '']:
            line_atom_list = [(index + 1, atom) for atom in get_atoms_recursive(token, index, separator_list) if
                              atom != '']
            atom_list = [*atom_list, *line_atom_list]

    const_symbol_table = Table()
    id_symbol_table = Table()
    internal_program_form = []

    for atom in atom_list:
        line_number = atom[0]
        atom_value = atom[1]

        if atoms_table.has(atom_value):
            internal_program_form.append((None, atoms_table.get(atom_value)))
        elif atom_is_const(atom_value):
            if not const_symbol_table.has(atom_value):
                const_symbol_table.append(atom_value)
            internal_program_form.append((const_symbol_table.get(atom_value), 0))
        elif atom_is_id(atom_value):
            if not id_symbol_table.has(atom_value):
                id_symbol_table.append(atom_value)
            internal_program_form.append((id_symbol_table.get(atom_value), 1))
        else:
            raise SyntaxError('Invalid syntax at line ' + str(line_number) + '. Atom: ' + atom_value)

    return internal_program_form, id_symbol_table, const_symbol_table
