import copy




def concat(a,b):
    """
    function to concatenate two integers 8,9 -> 89
    """
    return int(f"{a}{b}")


def de_con_cat(position:int) -> list[int]:
    """
    helper function to deconcatenate a position back into a list of two integers representing the positon of a piece on the board
    """
    #could use mod method but this is easier to read
    pos_list = [int(x) for x in str(position)]
    return pos_list
    

def check_in_bounds(position_as_list: list[int]) -> bool:
    """
    helper function to check if proposed position is indeed on the board
    param position_as_list: the position as a list of integers
    """
    for i in position_as_list:
        if i < 1 or i > 8:
            return False
    return True

def format_of_move_valid(move):
    """
    check if proposed move could be valid (still does not mean it is necessarily valid)
    """
    if len(move) != 4:
        return False
    
    if check_in_bounds(move[:2]) and check_in_bounds(move[-2:]):
        return True 

    return False

    


class DynamicKeyDict:
    def __init__(self):
        self._store = {}

    def add(self, obj):
        self._store[obj.position] = obj

    def __getitem__(self, key):
        return self._store[key]

    def __setitem__(self, key, obj):
        if key in self._store:
            del self._store[key]
        self._store[obj.position] = obj

    def __delitem__(self, key):
        del self._store[key]

    def __iter__(self):
        return iter(self._store)

    def __len__(self):
        return len(self._store)

    def __repr__(self):
        return repr(self._store)

    def update_key(self, obj, new_pos):
        if obj.position in self._store:
            del self._store[obj.position]
        obj.position = new_pos
        self._store[new_pos] = obj

    def items(self):
        return self._store.items()

    def values(self):
        return self._store.values()

    def keys(self):
        return self._store.keys()

    def copy(self):
        new_copy = DynamicKeyDict()
        new_copy._store = self._store.copy()
        return new_copy

    def deepcopy(self):
        new_copy = DynamicKeyDict()
        new_copy._store = copy.deepcopy(self._store)
        return new_copy 
    
    
nums_to_letters = {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h"}
letters_to_nums = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}  
str_nums_to_nums = {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8}  

def move_convert(move:str)-> list[int]:
    """
    input moves are given by letter:number where letters span the x axis and numbers the y axis
    the internals of the chess game work with number1:number2 where number1 is the row on the grid and number 2 is the col of the grid this function looks to make this conversion
    :param move[str]:
    """
    processed_move = []
    for i in move:
        if i in str_nums_to_nums:
            processed_move.append(str_nums_to_nums[i])
        elif i in letters_to_nums:
            processed_move.append(letters_to_nums[i])
            
    #swap pairs
    swap_pairs = lambda lst: [lst[i+1] if i % 2 == 0 else lst[i-1] for i in range(len(lst))]
    processed_move = swap_pairs(processed_move)
    return processed_move


        
            
    