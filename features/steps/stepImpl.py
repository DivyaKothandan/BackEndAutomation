import json

import requests
from behave import *
from payLoad import *
from utils.configurations import *


@given('the Book details which needs to be added to Library')
def step_impl(context):
    context.url = getConfig()['API']['endpoint'] + '/orders'
    context.headers = {"Content-Type": "application/json", "Authorization" : "Bearer 7e38caf03f3a66180a5d1d65ffd92011c07e6707191d5d460dc39b6362219bd5"}
    context.payLoad = addBookPayload("1","John");
    print("------ REQUEST DEBUG ------")
    print("URL:", context.url)
    print("Headers:", context.headers)
    print("Payload:", context.payLoad)
    print("Payload Type:", type(context.payLoad))
    print("---------------------------")


@when('we execute the AddBook PostAPI method')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payLoad , headers=context.headers)


@then('book is successfully added')
def step_impl(context):
    response_json = context.response.json()
    print(context.response.json())
    context.order_Id = response_json['orderId']
    print("Order Id: " , context.order_Id)
    context.created = response_json['created']
   # assert context.created == "True"



@then(u'status code of response should be {statusCode:d}')
def step_impl(context,statusCode):
    print(context.response.status_code)
    assert context.response.status_code == statusCode


@given('the Book details with {bookId} and {customerName}')
def step_impl(context,isbn,aisle):
    context.url = getConfig()['API']['endpoint'] + '/orders'
    context.headers = {"Content-Type": "application/json"}
   # context.payLoad = addBookPayload(bookId, customerName);



