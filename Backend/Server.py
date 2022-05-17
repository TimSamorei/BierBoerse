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
        latestDatapoint = Database.getLatestDatapoint()
        oldBeverageList = latestDatapoint.beverages
        oldBeverage = oldBeverageList[request.buyIndex]
        beverageNew = Bierboerse_pb2.Beverage(
            name=oldBeverage.name,
            id=oldBeverage.id,
            purchasingPrice=oldBeverage.purchasingPrice,
            currentPrice=oldBeverage.currentPrice,
            sold=oldBeverage.sold + 1,
            profit=oldBeverage.profit + oldBeverage.currentPrice
        )
        print("bought", beverageNew)

        newBeverageList = []

        for beverage in oldBeverageList:
            if (beverage.id != beverageNew.id):
                newBeverageList.append(beverage)
            else:
                newBeverageList.append(beverageNew)

        newDatapoint = Bierboerse_pb2.Datapoint(beverages=newBeverageList)

        Database.addDatapoint(newDatapoint)

        return Bierboerse_pb2.BuyReply(oldPrices=latestDatapoint, newPrices=newDatapoint, timestamp=self.getTimestamp())





    def getPrices(self, request, context):
        return Database.getLatestDatapoint()


    def getHistory(self, request, context):
        return Database.getHistory()

    def getTimestamp(self):
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
