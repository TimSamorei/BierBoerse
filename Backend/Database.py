import base64

from google.protobuf.internal.encoder import _VarintBytes
from google.protobuf.internal.decoder import _DecodeVarint32
import grpc

import Bierboerse_pb2_grpc
import Bierboerse_pb2

def getLatestDatapoint():
    return getHistory().history[-1]

def addDatapoint(dataPoint):
    history = getHistory().history

    history.append(dataPoint)

    newHistory = Bierboerse_pb2.History(history=history)

    with open("database.txt", "w", encoding="utf-8") as file:

        data = newHistory.SerializeToString()
        encodedBytes = base64.b64encode(data)
        encodedStr = str(encodedBytes, "utf-8")

        file.write(encodedStr)

def initDatabase():
    beverages = [
        Bierboerse_pb2.Beverage(name="Rothaus", id=0,
                                purchasingPrice=70, currentPrice=120, sold=0),
        Bierboerse_pb2.Beverage(name="Augustiner", id=1,
                                purchasingPrice=90, currentPrice=150, sold=0)
    ]
    dataPoint = Bierboerse_pb2.Datapoint(beverages=beverages)


    history = Bierboerse_pb2.History(history=[dataPoint])

    with open("database.txt", "w", encoding="utf-8") as file:

        data = history.SerializeToString()
        encodedBytes = base64.b64encode(data)
        encodedStr = str(encodedBytes, "utf-8")

        file.write(encodedStr)

def getHistory():
    with open("database.txt", "r", encoding="utf-8") as file:

        history = Bierboerse_pb2.History()

        encodedStr = file.read()
        decodedBytes = base64.b64decode(encodedStr)
        history.ParseFromString(decodedBytes)

        return history
