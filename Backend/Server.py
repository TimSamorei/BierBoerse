from concurrent import futures
import Database
import grpc
import math
import Bierboerse_pb2_grpc
import Bierboerse_pb2


class BierBoerseServer(Bierboerse_pb2_grpc.BierboerseServicer):

    purchasePriceRothaus = 1600/24
    purchasePriceAugustiner = 1730/20
    rothausGewicht = purchasePriceRothaus/purchasePriceAugustiner
    augustinerGewicht = purchasePriceAugustiner/purchasePriceRothaus
    combinePurchasePrice = purchasePriceRothaus + purchasePriceAugustiner
    rothausTargetPrice = purchasePriceRothaus * 1.8
    augustinerTargetPrice = purchasePriceAugustiner * 1.8
    combineTargetPrice = rothausTargetPrice + augustinerTargetPrice

    targetSum = 0
    actualSum = 0

    def updateBeers(self, request, context):
        addAugustiner = request.numAugustiner
        addRothaus = request.numRothaus

        latestDatapoint = Database.getLatestDatapoint()
        soldRothaus = latestDatapoint.rothausBought
        soldAugustiner = latestDatapoint.augustinerBought
        soldRothaus += addRothaus
        soldAugustiner += addAugustiner
        soldBeers = soldAugustiner + soldRothaus

        self.targetSum += addAugustiner*self.augustinerTargetPrice
        self.targetSum += addRothaus*self.rothausTargetPrice
        self.actualSum += addAugustiner*latestDatapoint.augustinerPrice
        self.actualSum += addRothaus*latestDatapoint.rothausPrice
        print("Targetsum: " + str(self.targetSum))
        print("Actualsum: " + str(self.actualSum))
        print("Diff in Euro: " + str(((self.actualSum - self.targetSum) / 100)))
        print("DiffRatio: " + str(((self.actualSum - self.targetSum) / 100) / (self.targetSum / 100)))


        print("Targetprice: " + str(self.combineTargetPrice / 2))

        if (soldAugustiner > 0 and soldRothaus > 0):
            rothausRatio = soldRothaus/soldAugustiner
            augustinerRatio = soldAugustiner/soldRothaus
        else:
            if (soldRothaus > 0):
                rothausRatio = soldRothaus/1
                augustinerRatio = 1/soldRothaus

            if (soldAugustiner > 0):
                rothausRatio = 1/soldAugustiner
                augustinerRatio = soldAugustiner/1

            if (soldRothaus == 0 and soldAugustiner == 0):
                rothausRatio = 1
                augustinerRatio = 1

    

        winLossRatio = self.targetSum/self.actualSum

        newRothausPrice = math.ceil(20 * math.sin(3 * (soldBeers)) + (self.rothausTargetPrice * rothausRatio * winLossRatio))
        newRothausPrice = round(newRothausPrice/10) * 10

        newAugustinerPrice = math.ceil(20 * math.sin(3 * (soldBeers) + 2.5) + (self.augustinerTargetPrice * augustinerRatio * winLossRatio))
        newAugustinerPrice = round(newAugustinerPrice/10) * 10
        




        print("Rothauspreis: " + str(newRothausPrice))
        print("Augustpreis: " + str(newAugustinerPrice))
        print("")
        print("")

        dataPoint = Bierboerse_pb2.PriceDatapoint(rothausPrice=newRothausPrice,augustinerPrice=newAugustinerPrice,rothausBought=soldRothaus,augustinerBought=soldAugustiner)
        Database.addDatapoint(dataPoint)
        return Bierboerse_pb2.ServerReply(prices=dataPoint)
        

    
        


def serve():
    PORT = 1337

    dataPoint = Bierboerse_pb2.PriceDatapoint(rothausPrice=120,augustinerPrice=150,rothausBought=0,augustinerBought=0)
    list = []
    list.insert(0, dataPoint)
    history = Bierboerse_pb2.PriceHistory(history=list)


    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    Bierboerse_pb2_grpc.add_BierboerseServicer_to_server(BierBoerseServer(), server)
    server.add_insecure_port("[::]:" + str(PORT))
    server.start()
    print("Starting Server on port  " + str(PORT))
    server.wait_for_termination()

if __name__ == "__main__":
    Database.initDatabase()
    serve()