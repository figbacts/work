import random
KREWES = {
    'orpheus': ['Emily','Kevin','Vishwaa','Eric','ray','Jesse',
                'Tiffany','Amanda','Junhee','Jackie','Tyler','Emory',
                'Ivan','Michael','Kiran','Amanda','Joseph','Tanzim','David','Yevgeniy'],
    'rex': ['William', 'Joseph','Calvin','Ethan', 'Moody', 'Mo',
            'Big Mo', 'Peihua', 'Saad','Benjamin','Justin','Alice','Hilary',
            'Ayham','Michael','Matthew','Jionghao','Devin','David',
            'Jacob','Will','Hannah','Alex'],
    'endymion': ['Grace','Nahi','Derek','Jun Tao','Connor','Jason','Tammy','Albert',
                 'Kazi','Derek','Brandon','Kenneth','Lauren','Biraj','Jess','Jackson',
                 'Taejoon','Kevin', 'Jude','Sophie','Henry','Coby','Mandfred','Leia',
                 'Ahmed','Winston']
    }
index = input('Enter either orpheus, rex, or endymion:  ')


if (index == 'orpheus'):
    print(KREWES['orpheus'][random.randint(0,len(KREWES['orpheus']) -1)])
    
if (index == 'rex'):
    print(KREWES['rex'][random.randint(0,len(KREWES['rex']) -1)])
    
if (index == 'endymion'):
    print(KREWES['endymion'][random.randint(0,len(KREWES['endymion']) -1)])



