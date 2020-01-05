import re

string = 'abdhwi-MM-abcd-aa-aa'
pat_1 = 'MM(.*?)aa'
print(re.findall(pat_1,string))
#['-abcd-']

pat_2 = 'MM(.*)aa'
print(re.findall(pat_2,string))
#['-abcd-aa-']

#example1 匹配网址
string_1 = "IT面试题博客中包含很多 <a href=http://hi.baidu.com/mianshiti/blog/category> 微软面试题 </a>"
#匹配得到 " http://hi.baidu.com/mianshiti/blog/category"
#one methoed 
pat_3 = 'href=(.*?)>'
print(re.findall(pat_3,string_1))
#['http://hi.baidu.com/mianshiti/blog/category']


#example 2 匹配邮箱
string_2 = 'asadwaeojfieor1546433@abc.comfertergt'
pat_5 = r"([a-zA-Z0-9_.]{3,8}@[a-pr-zA-PRZ0-9-]+\.\w{3})"
#含义：匹配大小写字母数字下划线以及其他符号3-8次+@+不含q的字母数字+.+3个结尾
print(re.findall(pat_5,string_2))
#['r1546433@abc.com']

# example 3 匹配电话号码
string_3 = 'werwjterjtyieyjieytel:12345678911fhewruigtytrbgTel:12345678912huwrefthweigrtptel:1233gifrdrwb'
pat_6 = '[Tt]el:([0-9]{11})'
print(re.findall(pat_6,string_3))
#['12345678911', '12345678912']
