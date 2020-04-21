
#Given a non-empty string like "Code" return a string like "CCoCodCode".


#string_splosion('Code') → 'CCoCodCode'
#string_splosion('abc') → 'aababc'
#string_splosion('ab') → 'aab'

def string_splosion(str):
    if str != '':
        newstr = str
        for i in range(1,len(str)):
            newstr = str[0:-i] + newstr
        return newstr