from google.protobuf.internal.encoder import _VarintBytes
from google.protobuf.internal.decoder import _DecodeVarint32
import base64
import grpc
import Bierboerse_pb2_grpc
import Bierboerse_pb2

def getLatestDatapoint():
    return getHistory().history[-1]

def addDatapoint(dataPoint):
    history = getHistory()
    newList = history.history

    newList.append(dataPoint)

    newHistory = Bierboerse_pb2.History(history=newList)

    f = open("demofile.txt", "w")

    data = newHistory.SerializeToString()
    encodedBytes = base64.b64encode(data)
    encodedStr = str(encodedBytes, "utf-8")

    f.write(encodedStr)

def initDatabase():
    bevList = []
    dataPoint = Bierboerse_pb2.Datapoint(beverages=bevList)

    hisList = []
    hisList.append(dataPoint)
    
    history = Bierboerse_pb2.History(history=hisList)

    f = open("demofile.txt", "w")

    data = history.SerializeToString()
    encodedBytes = base64.b64encode(data)
    encodedStr = str(encodedBytes, "utf-8")

    f.write(encodedStr)

def getHistory():
    f = open("demofile.txt", "r")
    
    history = Bierboerse_pb2.History()

    encodedStr = f.read()
    decodedBytes = base64.b64decode(encodedStr)
    history.ParseFromString(decodedBytes)

    return history


