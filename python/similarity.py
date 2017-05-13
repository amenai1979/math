__author__ = 'amenai@amenai.net'
############################################################
# A few utilities to calculate similarities between samples#
############################################################

'''
as a useful example we will compare multiple websites in terms of
traffic volume
median object size
offload
'''
from math import *
websites={'site1':{'traffic':10000,'median_obj_sz':100,'offload':0.8}\
         ,'site2':{'traffic':15000,'median_obj_sz':123,'offload':0.7}\
         ,'site3':{'traffic':14000,'median_obj_sz':82,'offload':0.5}\
         ,'site4':{'traffic':9000,'median_obj_sz':15,'offload':0.2}\
         ,'site5':{'traffic':9000,'median_obj_sz':15,'offload':0.3}
         }
#just checking everything is OK
#print(websites)

def euclidian_similarity(elem1,elem2):
    '''
    :param elem1: first element to compare (expect a dict of items)
    :param elem2: second element to compare (expects a dict of items)
    :return:a float, the Eucledian similarity between two elements. 1 if they are identical, and between 0 and 1 otherwize
    '''
    #first let's check the elements that are comparable in both dicts to cover the case of incomplete data
    comparable_parameters=[]
    for k1 in elem1.keys():
        for k2 in elem2.keys():
            if k1==k2:
                comparable_parameters.append(k1)

    #calculate the euclidian distance

    if len(comparable_parameters) > 0:
        summing=0
        for k in comparable_parameters:
            summing+=pow(elem1[k]-elem2[k],2)
        return 1/(1+sqrt(summing))
    else:
        #nothing to compare
        return 0
def pearson_similarity(elem1,elem2):
