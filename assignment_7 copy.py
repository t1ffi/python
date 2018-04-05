#Tiffi Westcott
#Vowel Verifier

def vowelVerifier(word):
    word = word.lower();
    vowelDict = {'a':0, 'e':0,'i':0, 'o':0, 'u':0};

    for letter in word:
        if letter in vowelDict:
            vowelDict[letter]=1;

    ifanymissing = 0;
    for x in vowelDict:
        if vowelDict [x] == 0:
            print x, "is missing in", word
            ifanymissing = 1;

    if ifanymissing == 0:
        print word, "contains all the vowels"

vowelVerifier('World');
vowelVerifier('EVALuATION');
vowelVerifier('BEAtLES');
vowelVerifier('lOAFER');
vowelVerifier('EVACUATION');
