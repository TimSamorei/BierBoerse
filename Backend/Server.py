from concurrent import futures
from Bierboerse_pb2 import Beverage
import Database
import grpc
import datetime
from google.protobuf.timestamp_pb2 import Timestamp
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


    def buyBeverage(self, request, context):
        return


    def getPrices(self, request, context):
        return Database.getLatestDatapoint()


    def getHistory(self, request, context):
        return Database.getHistory()

    def getTimestamp():
        t = datetime.datetime.now().timestamp()
        return Timestamp(seconds=int(t), nanos=int(t % 1*1e9))


def serve():
    PORT = 1337

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    Bierboerse_pb2_grpc.add_BierboerseServicer_to_server(BierBoerseServer(), server)
    server.add_insecure_port("[::]:" + str(PORT))

    server.currentDatapoint = Database.getLatestDatapoint()

    server.start()
    print("Starting Server on port " + str(PORT))
    server.wait_for_termination()

if __name__ == "__main__":
    Database.initDatabase()
    serve()
