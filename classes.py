class Turing_Machine:
    def __init__(self):
        self.tape = [i for i in ('_'+ 'a'*20 + 'b'*20 +'_')]
        self.tape_len = len(self.tape)

        self.cursor = 1
        self.state_index = 0
        self.recursion_steps = 0
        self.recursion_limit = 5000

        self.final_states = [4]
        self.states = [         # store the index of rules each state follows
            [0,7],
            [1,2,3],
            [4,5,6],
            [8,9],
            []      # final
        ]
        self.rules = [          # [ start_state, read, direction, next_state, write ]
            [0, 'a', 'R', 1, 'X'],
            [1, 'a', 'R', 1, 'a'],
            [1, 'Y', 'R', 1, 'Y'],
            [1, 'b', 'L', 2, 'Y'],
            [2, 'Y', 'L', 2, 'Y'],
            [2, 'a', 'L', 2, 'a'],
            [2, 'X', 'R', 0, 'X'],
            [0, 'Y', 'R', 3, 'Y'],
            [3, 'Y', 'R', 3, 'Y'],
            [3, '_', 'L', 4, '_'],
        ]

    def set_values(self, states:list[list[int]], rules:list[list[int | str]], final_states:list[int | None], state_index=0, step_limit=5000):
        '''
        Returns `True` for success, `False` for Failure.

        ---
        ### States:
        Stores the index of rules each state follows
        Example:
        ```
        states = [[0,7],[]]         # leave empty for final states (optional, final state's production rules are ignored)
        ```
        ---
        ### Rules:
        Format: `[ start_state, read, direction, next_state, write ]`
        Example:
        ```
        rules = [[0, 'a', 'R', 1, 'X'],[1, 'a', 'R', 1, 'a']]
        ```
        ---
        ### Final States:
        Stores the index of state (from `states`) that are `Final States`
        Example:
        ```
        final_states = [1]
        ```
        ---
        `state_index` --> starting state `Default 0`\n
        `step_limit`  --> max number of allowed transition steps `Default 5000`
        '''
        if not states: print('Mismatch in `States`:\n', states, sep='')
        elif not all(len(rule) == 5 for rule in rules): print('Mismatch in `Rules`:\n', rules, sep='')
        elif not final_states: print('Mismatch in `Final States`:\n', final_states, sep='')
        else:
            self.states = states
            self.rules = rules
            self.final_states = final_states
            self.recursion_limit = step_limit
            self.state_index = state_index
            return True
        return False
    
    def set_tape(self, tape:str):
        '''
        Sets the tape to a new string, surrounded by blanks `_`. Enter a string that you want to validate with the Machine.
        Example:
        ```
        tm.set_tape("ab")  # tape becomes ['_', 'a', 'b', '_']
        ```
        '''

        self.tape = [i for i in ('_' + tape + '_')]
        self.tape_len = len(self.tape)
        self.cursor = 1

    def _run(self):
        '''returns ```True``` for accept, ```False``` for reject and non halt'''
        while True:
            # check current final
            if self.state_index in self.final_states:
                return True
            
            # read current symbol from tape
            state_rule_indexes = self.states[self.state_index]
            rules = [self.rules[i] for i in state_rule_indexes]
            if self.tape_len == 2:
                input = '_'
                self.cursor = 0
            else:
                input = self.tape[self.cursor]

            # match rules
            found_input = False
            if len(rules):
                for cs, r, d, ns, w in rules:
                    if input == r:
                        self.state_index = ns
                        self.tape[self.cursor] = w
                        match d:
                            case 'R': 
                                self.cursor += 1
                                if self.cursor == self.tape_len-1:
                                    self.tape_len += 1
                                    self.tape.append('_')
                            case 'L': 
                                self.cursor -= 1
                                if self.cursor == 0:
                                    self.cursor += 1
                                    self.tape_len += 1
                                    self.tape.insert(0,'_')
                        found_input = True
                        break
            if not found_input:
                break

            # update recursion steps
            if self.recursion_steps >= self.recursion_limit:
                print('Non Halting | steps limit:', self.recursion_limit)
                break
            self.recursion_steps += 1
        
        return False
    
    def compute(self):
        print('input:', ''.join(self.tape)[1:-1])
        if self._run():
            print('Accepted', end=' ')
            print('| num of steps:', self.recursion_steps, '| tape len:', self.tape_len) 
            print('tape:', ''.join(self.tape))
        else:
            print('Rejected', end=' ')
            print('| num of steps:', self.recursion_steps, '| tape len:', self.tape_len)
            print('tape:', ''.join(self.tape))