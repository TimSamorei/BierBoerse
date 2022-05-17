from concurrent import futures
from Backend.Bierboerse_pb2 import Beverage
import Database
import grpc
import math
import Bierboerse_pb2_grpc
import Bierboerse_pb2


class BierBoerseServer(Bierboerse_pb2_grpc.BierboerseServicer):

    currentDatapoint = None

    def addBeverage(self, request, context):
        oldDatapoint = Database.getLatestDatapoint()

        newBevList = oldDatapoint.beverages
        newBevList.append(request.beverage)

        newDatapoint = Bierboerse_pb2.Datapoint(beverages=newBevList)

        Database.addDatapoint(newDatapoint)
        return


    def updateBeverage(self, request, context):
        return


    def getBeverage(self, request, context):
        return


def serve():
    PORT = 1337

    beverages = [
        Bierboerse_pb2.Beverage(name="Rothaus", id=0, purchasingPrice = 70, currentPrice = 120, sold=0),
        Bierboerse_pb2.Beverage(name="Augustiner", id=1, purchasingPrice = 90, currentPrice = 150, sold=0)
    ]

    dataPoint = Bierboerse_pb2.PriceDatapoint()
    list = []
    list.insert(0, dataPoint)
    history = Bierboerse_pb2.PriceHistory(history=list)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    Bierboerse_pb2_grpc.add_BierboerseServicer_to_server(BierBoerseServer(), server)
    server.add_insecure_port("[::]:" + str(PORT))
    server.start()
    print("Starting Server on port " + str(PORT))
    server.wait_for_termination()

if __name__ == "__main__":
    Database.initDatabase()
    serve()
