from google.protobuf.internal.encoder import _VarintBytes
from google.protobuf.internal.decoder import _DecodeVarint32
import base64
import grpc
import Bierboerse_pb2_grpc
import Bierboerse_pb2

def getHistory():
    f = open("demofile.txt", "r")
    
    history = Bierboerse_pb2.PriceHistory()

    encodedStr = f.read()
    decodedBytes = base64.b64decode(encodedStr)
    history.ParseFromString(decodedBytes)

    return history

def getLatestDatapoint():
    return getHistory().history[-1]

def addDatapoint(dataPoint):
    history = getHistory()
    newList = history.history

    newList.append(dataPoint)

    newHistory = Bierboerse_pb2.PriceHistory(history=newList)

    f = open("demofile.txt", "w")

    data = newHistory.SerializeToString()
    encodedBytes = base64.b64encode(data)
    encodedStr = str(encodedBytes, "utf-8")

    f.write(encodedStr)





def initDatabase():
    dataPoint = Bierboerse_pb2.PriceDatapoint(rothausPrice=120,augustinerPrice=150,rothausBought=0,augustinerBought=0)
    list = []
    list.append(dataPoint)
    history = Bierboerse_pb2.PriceHistory(history=list)

    f = open("demofile.txt", "w")

    data = history.SerializeToString()
    encodedBytes = base64.b64encode(data)
    encodedStr = str(encodedBytes, "utf-8")

    f.write(encodedStr)


