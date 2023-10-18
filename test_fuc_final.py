#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pytest
from m7_assn import Solution



input1 = """
JULY:*****Red Hot Chili Peppers---CAPACITY---:10000 -- $ATTENDANCE: 9,500--GATE:--$380,000 ;*****Taylor Swift ----CAPACITY---:30000--- $ATTENDANCE: 29,500---GATE:--$885,000#;*****Metallica ----CAPACITY---:20000 ---$ATTENDANCE: 19,000 ---GATE:-$760,000;*****Adele---CAPACITY---:15000 ---$ATTENDANCE: 14,750 ---GATE: -$1,180,000;*****DRAKE---CAPACITY--:18000---$ATTENDANCE: 17,000—-GATE:$1,530,000*****

"""

input2 = """
# AUGUST:*****Linkin Park---CAPACITY---:25000 -- $ATTENDANCE: 24,100--GATE:--$602,500 ;*****Bruno Mars ----CAPACITY---:22000--- $ATTENDANCE: 21,000---GATE:--$630,000#;*****Coldplay ----CAPACITY---:27000 ---$ATTENDANCE: 26,000 ---GATE:-$1,040,000;*****Katy Perry---CAPACITY---:23000 ---$ATTENDANCE: 22,800 ---GATE: -$685,000;*****ED SHEERAN---CAPACITY--:28000---$ATTENDANCE: 27,500—-GATE:$1,100,000*****

"""

input3 = """
SEPTEMBER:*****Foo Fighters---CAPACITY---:16000 -- $ATTENDANCE: 15,000--GATE:--$600,000 ;*****Ariana Grande ----CAPACITY---:19000--- $ATTENDANCE: 18,000---GATE:--$684,000#;*****Imagine Dragons ----CAPACITY---:21000 ---$ATTENDANCE: 20,500 ---GATE:-$820,000;*****Maroon 5---CAPACITY---:17000 ---$ATTENDANCE: 16,500 ---GATE: -$660,000;*****JUSTIN BIEBER---CAPACITY--:20000---$ATTENDANCE: 19,500—-GATE:$780,000*****

"""



@pytest.mark.parametrize('text', [input1, input2, input3])
def test_task_four(text):
    """This tests that your task_four returns the correct outputs for different inputs."""
    solution = MySolution(text)
    value_to_check = solution.task_four()
    assert isinstance(value_to_check, dict)
    
    for artist, data in value_to_check.items():
        assert 'Average Ticket Price' in data
        assert 'Is Multi-Word Name' in data
        assert 'Venue Fill Percentage' in data
    


# In[ ]:





# In[ ]:




