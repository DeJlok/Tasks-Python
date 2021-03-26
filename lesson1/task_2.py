list_countrys =['Ukraine', 'Poland', 'USA', 'GB', 'China']
dict_countrys = {
    'Ukraine':'Kyiv',
    'Poland':'Warsaw',
    'USA':'Washington',
    'GB':'London',
    'Germany':'Berlin'
}
for k, v in dict_countrys.items():
    if(k in list_countrys):
        print(k,":", v)