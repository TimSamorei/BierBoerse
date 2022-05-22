from concurrent import futures
from Bierboerse_pb2 import Beverage
import Database
import grpc
import datetime
from google.protobuf.timestamp_pb2 import Timestamp
import Bierboerse_pb2_grpc
import Bierboerse_pb2



class BierBoerseServer(Bierboerse_pb2_grpc.BierboerseServicer):

    soldBeers = 0

    def addBeverage(self, request, context):
        oldDatapoint = Database.getLatestDatapoint()

        newBevList = oldDatapoint.beverages
        newBevList.append(request.beverage)

        newDatapoint = Bierboerse_pb2.Datapoint(beverages=newBevList)

        Database.addDatapoint(newDatapoint)
        return


    def buyBeverage(self, request, context):
        self.soldBeers += 1
        latestDatapoint = Database.getLatestDatapoint()
        oldBeverageList = latestDatapoint.beverages
        newBeverageList = []

        for beverage in oldBeverageList:
            if (beverage.id == request.buyIndex):
                newBeverage = self.makePrice(beverage, 1, latestDatapoint)
            else:
                newBeverage = self.makePrice(beverage, 0, latestDatapoint)
            newBeverageList.append(newBeverage)

        newDatapoint = Bierboerse_pb2.Datapoint(beverages=newBeverageList, timestamp=self.getTimestamp())

        Database.addDatapoint(newDatapoint)

        return Bierboerse_pb2.BuyReply(oldPrices=latestDatapoint, newPrices=newDatapoint)





    def getPrices(self, request, context):
        return Database.getLatestDatapoint()


    def getHistory(self, request, context):
        return Database.getHistory()

    def getTimestamp(self):
        t = datetime.datetime.now().timestamp()
        return Timestamp(seconds=int(t), nanos=int(t % 1*1e9))

    def makePrice(self, oldBeverage, inc, latestDatapoint):
        diff = ((oldBeverage.sold + inc)/self.soldBeers) - (1/len(latestDatapoint.beverages))
        newPrice = oldBeverage * (1 + diff)


        beverageNew = Bierboerse_pb2.Beverage(
            name=oldBeverage.name,
            id=oldBeverage.id,
            purchasingPrice=oldBeverage.purchasingPrice,
            currentPrice=newPrice,
            sold=oldBeverage.sold + inc,
            profit=oldBeverage.profit + oldBeverage.currentPrice
        )


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
