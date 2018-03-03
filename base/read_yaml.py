import yaml,sys,os
# print(os.path.abspath(r'C:\Users\XHY\PycharmProjects\PO_object'))
def r_ymal(filename):
    filepath = os.path.abspath(r'C:\Users\XHY\PycharmProjects\PO_object') +os.sep+'data'+os.sep+filename

    print(filepath)
    with open(filepath,'r',encoding='utf-8') as f:
        # data=yaml.load(f)
        # print(data)
        return yaml.load(f)

# # r_ymal('data_search.yaml')
# data_first=r_ymal('data_search.yaml')
# data_secend=data_first.get('test_search')
# # print(data_secend)
# data_list=[]
# for k in data_secend.keys():
#     # text=data_secend.get(k).get('text')
#     # expect=data_secend.get(k).get('expect')
#     # my_tuple=(k,text,expect)
#     data_list.append((k,data_secend.get(k).get('text'),data_secend.get(k).get('expect')))
# print(data_list)
# #
# r_ymal('data_address.yaml')

