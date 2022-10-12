from typing import *
dictionary = {
    "name": "papaya",
    "phone": 9876545567,
    "height": 6,
    "weight": 60,
    "race": "asian",
    "vaccinated": True
}

ruleSet = {
    "string": {
        "max": 20,
        "min": 3
    },
    "number": {
        "max": 9999999999,
        "min": 9000000000
    }
};

# print(type(dictionary.get('name')));


checkVal = True


def validateDictionary(dictionary, ruleSet):
    # final boolean val

    if (isinstance(dictionary.get('name'), str)):
        if (len(dictionary.get('name')) > ruleSet.get('string').get('max')):
            checkVal = False;
            return checkVal;
        elif (len(dictionary.get('name')) < ruleSet.get('string').get('min')):
            checkVal = False;
            return checkVal;
        else:
            checkVal = True;

    if (isinstance(dictionary.get('phone'), int)):
        if (dictionary.get('phone') > ruleSet.get('number').get('max')):
            checkVal = False;
            return checkVal;
        elif (dictionary.get('phone') < ruleSet.get('number').get('min')):
            checkVal = False;
            return checkVal;
        else:
            checkVal = True;

    return checkVal;


print('Is rule matched?? ', validateDictionary(dictionary, ruleSet))
