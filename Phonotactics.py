#English Phonemes Data
consonants = ['p', 't', 'k', 'tʃ', 'b', 'd', 'g', 'dʒ', 'f', 'θ', 's', 'ʃ', 'h' ,'v', 'ð', 'z', 'ʒ', 'm', 'n', 'ŋ', 'l', 'r', 'hw', 'x', 'j', 'w']
vowels = ['a', 'eܼܼܼܼܼɪ', 'eə', 'ɑː', 'e', 'iː', 'ɪ', 'aɪ', 'ɪə', 'ɒ', 'əʊ', 'ɔː', 'ɔɪ', 'ʊ', 'uː', 'ʌ', 'aʊ', 'ɜː', 'ʊə', 'ə']

#Onset Consonants Constraints
onset_consonants = [c for c in consonants if c !='ŋ']

import random

#Phonotactics GEN function
#def phonotactics_sequence():
    #onset = random.choices(consonants, k=random.randint(1,3))
    #nucleus = random.choices(vowels, k=random.randint(1,2))
    #coda = random.choices(consonants, k=random.randint(1,2))
    #return ''.join(onset + nucleus + coda)

#print(phonotactics_sequence())

#Phonotactics GEN function with constraints
def phonotactics_sequence_with_constraints():
    onset = random.choices(consonants, k=random.randint(1,3))
    nucleus = random.choices(vowels, k=random.randint(1,2))
    coda = random.choices(consonants, k=random.randint(1,2))
    return ''.join(onset + nucleus + coda)

print(phonotactics_sequence_with_constraints())