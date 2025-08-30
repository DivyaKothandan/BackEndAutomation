from utils.configurations import *


def addBookPayload(bookId, customerName):
    body = {

        "bookId": int(bookId),
        "customerName": customerName
    }
    return body
