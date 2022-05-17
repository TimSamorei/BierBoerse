from google.protobuf.internal.encoder import _VarintBytes
from google.protobuf.internal.decoder import _DecodeVarint32
import base64
import grpc
import Bierboerse_pb2_grpc
import Bierboerse_pb2

def getLatestDatapoint():
    return getHistory().history[-1]

def addDatapoint(dataPoint):
    history = getHistory().history

    history.append(dataPoint)

    newHistory = Bierboerse_pb2.History(history=history)

    with open("database.txt", "w") as file:

        data = newHistory.SerializeToString()
        encodedBytes = base64.b64encode(data)
        encodedStr = str(encodedBytes, "utf-8")

        file.write(encodedStr)

def initDatabase():
    bevList = []
    dataPoint = Bierboerse_pb2.Datapoint(beverages=bevList)

    hisList = []
    hisList.append(dataPoint)

    history = Bierboerse_pb2.History(history=hisList)

    with open("database.txt", "w") as file:

        data = history.SerializeToString()
        encodedBytes = base64.b64encode(data)
        encodedStr = str(encodedBytes, "utf-8")

        file.write(encodedStr)

def getHistory():
    with open("demofile.txt", "r") as file:

        history = Bierboerse_pb2.History()

        encodedStr = file.read()
        decodedBytes = base64.b64decode(encodedStr)
        history.ParseFromString(decodedBytes)

        return history
