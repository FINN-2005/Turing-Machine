def get_unary_addition():
    states = [
    [0,1],    
    [2],
    [],     
    ]
    rules = [
        [0, '1', 'R', 0, '1'],
        [0, '_', 'R', 1, '1'],
        [1, '_', 'L', 2, '1'],
    ]
    final_states = [2]
    tape = '111'
    return states, rules, final_states, tape

def get_palindrome():
    states = [
        [0,7],
        [1,2,3],
        [4,5,6],
        [8,9],
        []
    ]
    rules = [
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
    final_states = [4]
    tape = 'aaabbb'
    return states, rules, final_states, tape