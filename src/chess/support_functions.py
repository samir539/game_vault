
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

    
class DynamicKeyDict():
    def __init__(self):
        self._store = {}
        
    def add(self,obj):
        self._store[obj.position] = obj

    def __getitem__(self,key):
        return self._store[key]
    
    def __setitem__(self,key,obj):
        if key in self._store:
            del self._store[key]
        self._store[obj.position] = obj
        
    def __delitem__(self,key):
        del self._store[key]
        
    def __iter__(self):
        return iter(self._store)
    
    def __len__(self):
        return len(self._store)
    
    def __repr__(self):
        return repr(self._store)
    
    def update_key(self,obj,new_name):
        if obj.position in self._store:
            del self._store[obj.position]
        obj.position = new_name
        self._store[new_name] = obj
        



