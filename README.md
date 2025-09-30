# Turing-Machine
A general purpose TM sim

## Install
Git clone
```bash
git clone https://github.com/FINN-2005/Turing-Machine.git
```

## Usage
Run `python main.py`

There are two pre-made Tape and TM configurations:
- Unary Addition
- Palindrome  
You can define any configuration you want with the format (look at the code, this is from the TM class):

### Turing-Machine::set_values (
    states:list[list[int]], 
    rules:list[list[int | str]], 
    final_states:list[int | None], 
    state_index=0, 
    step_limit=5000
):  
Returns `True` for success, `False` for Failure.

### States:
Stores the index of rules each state follows  
Example:
```python
states = [[0,7],[]]         # leave empty for final states (optional, final state's production rules are ignored)
```

### Rules:
Format: `[ start_state, read, direction, next_state, write ]`  
Example:
```python
rules = [[0, 'a', 'R', 1, 'X'],[1, 'a', 'R', 1, 'a']]
```

### Final States:
Stores the index of state (from `states`) that are `Final States`
Example:
```python
final_states = [1]
```

`state_index` --> starting state (Default 0)  
`step_limit`  --> max number of allowed transition steps (Default 5000)
