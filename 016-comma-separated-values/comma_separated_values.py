# Comma-Separated Values
# Retrieve records from a comma-separated values file
#   using a finite-state machine
# Programming Praxis Exercise 16
# http://programmingpraxis.com/2009/03/17/comma-separated-values/


class FiniteStateMachine:
    """Implement a generic state machine.

    A state machine has a current state_name and state_data.
    Initial state_name and state_data must be provided at
    instantiation. A transition is a function from (input, state_data)
    to (new_state_name, new_state_data). Transitions are added
    for each state_name with the add_transition method.
    Consume_one method consumes one input datum and updates
    current state_name and data. Consume_all reduces over an
    input sequence with consume_one.
    At consumption time, the input datum is first matched with
    the value of input provided with add_transition. If the match
    is negative the type of the input is matched. This provide a
    method to provide general transition when the particular
    transitions fail. The finisher functions must be provided
    to present status_data at the end in a reasonable format."""

    def __init__(self, first_state_name, initial_state_data, finisher):
        "Initialize state name and data for the state machine."
        self.first_state_name = first_state_name
        self.initial_state_data = initial_state_data

        self.state_name = first_state_name
        self.state_data = initial_state_data
        self.state_transition = {}
        self.finisher = finisher

    def add_transition(self, from_state_name, inp, transition):
        """Add a transition from (input, state_name).
        The transition will be called as transition(input, state_data)"""
        self.state_transition[(from_state_name, inp)] = transition

    def consume_one(self, inp):
        "Consume one input datum and update local state."
        try:
            transition = self.state_transition[(self.state_name, inp)]
        except:
            transition = self.state_transition[(self.state_name, type(inp))]
        new_state_name, new_state_data = transition(inp, self.state_data)
        self.state_name = new_state_name
        self.state_data = new_state_data

    def consume_all(self, sequence):
        "Consume all input data in a sequence."
        for inp in sequence:
            self.consume_one(inp)

    def finish(self):
        """Update state with a last transition.
        Then present state_data in a suitable fashion."""
        product = self.finisher(self.state_data)
        self.state_name = self.first_state_name
        self.state_data = self.initial_state_data
        return product


# CSV PARSER STATE NAMES
NEW_FIELD = "NEW_FIELD"
ENTER_STRING = "ENTER_STRING"
IN_STRING = "IN_STRING"
IN_STRING_DQUOTE = "IN_STRING_DQUOTE"
IN_FIELD = "IN_FIELD"


def enter_string(inp, state_data):
    "When a new string begins, intialize it as an empty list."
    curr_field, curr_string, curr_rec, past_recs = state_data
    new_state_data = (curr_field, [], curr_rec, past_recs)
    return ENTER_STRING, new_state_data


def filling_string(inp, state_data):
    "We are adding input to the string."
    curr_field, curr_string, curr_rec, past_recs = state_data
    new_curr_string = curr_string + [inp]
    new_state_data = (curr_field, new_curr_string, curr_rec, past_recs)
    return IN_STRING, new_state_data


def close_string(inp, state_data):
    "The string has ended, so it's added to the current field and emptied."
    curr_field, curr_string, curr_rec, past_recs = state_data
    new_curr_field = curr_field + curr_string
    new_curr_string = None
    new_state_data = (new_curr_field, new_curr_string, curr_rec, past_recs)
    return IN_FIELD, new_state_data


def exit_string_in_field(inp, state_data):
    "A double quoted string has ended, but we are still into the field."
    curr_field, curr_string, curr_rec, past_recs = state_data
    new_curr_field = curr_field + (curr_string + [inp])
    new_curr_string = None
    new_state_data = (new_curr_field, new_curr_string, curr_rec, past_recs)
    return IN_FIELD, new_state_data


def exit_string_next_field(inp, state_data):
    "A double quoted string has ended, and the field it was in too."
    curr_field, curr_string, curr_rec, past_recs = state_data
    new_curr_field = []
    new_curr_string = None
    new_curr_rec = curr_rec + [curr_field + curr_string]
    new_state_data = (new_curr_field, new_curr_string, new_curr_rec, past_recs)
    return NEW_FIELD, new_state_data


def exit_string_next_record(inp, state_data):
    "A double quoted string has ended, and both the field and record too."
    curr_field, curr_string, curr_rec, past_recs = state_data
    new_past_recs = past_recs + [curr_rec + [curr_field + curr_string]]
    new_state_data = ([], None, [], new_past_recs)
    return NEW_FIELD, new_state_data


def next_record(inp, state_data):
    "End of a record, beginning of the next."
    curr_field, curr_string, curr_rec, past_recs = state_data
    new_past_recs = past_recs + [curr_rec + [curr_field]]
    new_state_data = ([], None, [], new_past_recs)
    return NEW_FIELD, new_state_data


def next_field(inp, state_data):
    "End of field, beginning of the next."
    curr_field, curr_string, curr_rec, past_recs = state_data
    new_curr_field = []
    new_curr_string = None
    new_curr_rec = curr_rec + [curr_field]
    new_state_data = (new_curr_field, new_curr_string, new_curr_rec, past_recs)
    return NEW_FIELD, new_state_data


def filling_field(inp, state_data):
    "We are adding the input to the current field."
    curr_field, curr_string, curr_rec, past_recs = state_data
    new_curr_field = curr_field + [inp]
    new_curr_string = None
    new_state_data = (new_curr_field, new_curr_string, curr_rec, past_recs)
    return IN_FIELD, new_state_data


def in_string_dquote(inp, state_data):
    "Beginning of a double quoted string."
    new_state_data = state_data
    return IN_STRING_DQUOTE, new_state_data


def sweep_trailing_and_stringify(state_data):
    """At the end of the input stream, close the current field and record,
    then transform the input character lists into strings"""
    curr_field, curr_string, curr_rec, past_recs = state_data
    if curr_string:
        curr_field += curr_string
    if curr_field:
        curr_rec += [curr_field]
    if curr_rec:
        past_recs += [curr_rec]
    records = []
    for rec in past_recs:
        record = []
        for fld in rec:
            record.append("".join(fld))
        records.append(record)
    return records


def parse_csv(text, separator=','):
    "Parse a comma-separated value text, return a list of records of fields."

    # CSV PARSER STATE DATA
    # current field, current string, current record, past records
    initial_state = ([], None, [], [])

    csv_parser = FiniteStateMachine(NEW_FIELD,
                                    initial_state,
                                    sweep_trailing_and_stringify)

    csv_parser.add_transition(NEW_FIELD, '"', enter_string)
    csv_parser.add_transition(NEW_FIELD, '\n', next_record)
    csv_parser.add_transition(NEW_FIELD, separator, next_field)
    csv_parser.add_transition(NEW_FIELD, str, filling_field)

    csv_parser.add_transition(IN_FIELD, '\n', next_record)
    csv_parser.add_transition(IN_FIELD, separator, next_field)
    csv_parser.add_transition(IN_FIELD, str, filling_field)

    csv_parser.add_transition(ENTER_STRING, '"', close_string)
    csv_parser.add_transition(ENTER_STRING, str, filling_string)

    csv_parser.add_transition(IN_STRING, '"', in_string_dquote)
    csv_parser.add_transition(IN_STRING, str, filling_string)

    csv_parser.add_transition(IN_STRING_DQUOTE, '"', filling_string)
    csv_parser.add_transition(IN_STRING_DQUOTE,
                              separator,
                              exit_string_next_field)
    csv_parser.add_transition(IN_STRING_DQUOTE, '\n', exit_string_next_record)
    csv_parser.add_transition(IN_STRING_DQUOTE, str, exit_string_in_field)

    csv_parser.consume_all(text)
    return csv_parser.finish()
