import re
pattern_1 = 'abcd'
pattern_2 = 'saih'
string = 'saih-dwohaf-abcd-oergwheihrfgqhdpfcshdshu-abcd-wfe1wr56145102154'

match_1 = re.match(pattern_1,string)
match_2 = re.match(pattern_2,string)

print(match_1)
print(match_2)

'''
None
<_sre.SRE_Match object; span=(0, 4), match='saih'>
'''

search_1 = re.search(pattern_1,string)
search_2 = re.search(pattern_2,string)
print(search_1)
print(search_2)

'''
<_sre.SRE_Match object; span=(11, 15), match='abcd'>
<_sre.SRE_Match object; span=(0, 4), match='saih'>

'''



findall_ = re.findall(pattern_1,string)
print(findall_)

'''
['abcd', 'abcd']
'''
repl = 'dcba'
string_2 = re.sub(pattern_1,repl,string)
print(string_2)

'''
saih-dwohaf-dcba-oergwheihrfgqhdpfcshdshu-dcba-wfe1wr56145102154
'''

split_ = re.split(pattern_1,string)
print(split_)

'''
['saih-dwohaf-', '-oergwheihrfgqhdpfcshdshu-', '-wfe1wr56145102154']
'''

prog = re.compile(pattern_1)
result_1= prog.search(string)
print(result_1)
result_2 = prog.findall(string)
print(result_2)

'''
<_sre.SRE_Match object; span=(12, 16), match='abcd'>
['abcd', 'abcd']
'''


