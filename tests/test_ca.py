from check_actions.ca import simple_add
from check_actions.ca import simple_multi


def test_simple_add():
    assert simple_add(1, 2) == 3
   
 
def test_simple_multi():
    assert simple_multi(1, 2) == 2
    
