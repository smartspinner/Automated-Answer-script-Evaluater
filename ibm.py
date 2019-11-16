import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, CategoriesOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2019-07-12',
    iam_apikey='zKER0-EWLh9GEQXwCp9Y-W9WIQqLFp2bUvpbSAa29oID',
    url='https://gateway-syd.watsonplatform.net/natural-language-understanding/api'
)

data='''Good afternoon class!

So today we are going to discuss about linked lists.

Linked-lists have different functions

The first of it is creating the list. A new structure of type list is first created, by dynamically allocating memory.
The malloc function is used for the same.


For adding a new node to the linked-list, one must first travel till the last node of the linked list.
A node is created, and the next of the last node is assigned to this new node.

Deleting a node from the list, again one must travese all the way till the end, along with a second pointer that points to the 
last but one list. The next of the last but one list is made null, and the current node is freed using the free function.

To display the details of the list, or, print the list, one must travel to the end of the list, and while doing so, print the data in each node.

Navigating through the list happpens by using a pointer of type node starting from head. The pointer is then assigned to its next value for traversal or navigation, until the required condition is satisfied.

Lastly, deleting a linked list involves calling the delete last function untill the head node points to NULL.'''


response = natural_language_understanding.analyze(
    text=data,
    features=Features(categories=CategoriesOptions(limit=1))).get_result()

mylabel=response["categories"][0]["label"][1:].split('/')[0]


li=[]
l2=data.split(".")

response = natural_language_understanding.analyze(
    text=l2[0],
    features=Features(categories=CategoriesOptions(limit=1))).get_result()

label=response["categories"][0]["label"][1:].split('/')[0]
if label==mylabel:
    li.append(l2[0])



response = natural_language_understanding.analyze(
    text=l2[1],
    features=Features(categories=CategoriesOptions(limit=1))).get_result()

label=response["categories"][0]["label"][1:].split('/')[0]
if label==mylabel:
    li.append(l2[1])


response = natural_language_understanding.analyze(
    text=l2[2],
    features=Features(categories=CategoriesOptions(limit=1))).get_result()

label=response["categories"][0]["label"][1:].split('/')[0]
if label==mylabel:
    li.append(l2[2])


response = natural_language_understanding.analyze(
    text=l2[3],
    features=Features(categories=CategoriesOptions(limit=1))).get_result()

label=response["categories"][0]["label"][1:].split('/')[0]
if label==mylabel:
    li.append(l2[3])


response = natural_language_understanding.analyze(
    text=l2[4],
    features=Features(categories=CategoriesOptions(limit=1))).get_result()

label=response["categories"][0]["label"][1:].split('/')[0]
if label==mylabel:
    li.append(l2[4])


response = natural_language_understanding.analyze(
    text=l2[5],
    features=Features(categories=CategoriesOptions(limit=1))).get_result()

label=response["categories"][0]["label"][1:].split('/')[0]
if label==mylabel:
    li.append(l2[5])


response = natural_language_understanding.analyze(
    text=l2[6],
    features=Features(categories=CategoriesOptions(limit=1))).get_result()

label=response["categories"][0]["label"][1:].split('/')[0]
if label==mylabel:
    li.append(l2[6])


response = natural_language_understanding.analyze(
    text=l2[7],
    features=Features(categories=CategoriesOptions(limit=1))).get_result()

label=response["categories"][0]["label"][1:].split('/')[0]
if label==mylabel:
    li.append(l2[7])


response = natural_language_understanding.analyze(
    text=l2[8],
    features=Features(categories=CategoriesOptions(limit=1))).get_result()

label=response["categories"][0]["label"][1:].split('/')[0]
if label==mylabel:
    li.append(l2[8])


s=".".join(li)
print(s)


    
