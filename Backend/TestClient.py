import grpc
import Bierboerse_pb2_grpc
import Bierboerse_pb2

def printPricelist(datapoint: Bierboerse_pb2.Datapoint):
    print("Prices at", datapoint.timestamp)
    for bev in datapoint.beverages:
        print(bev.id, "\t", bev.name, "\t", bev.currentPrice / 100, "€")
    print("=========================")


channel = grpc.insecure_channel('localhost:1337', options=(('grpc.enable_http_proxy', 0),))
stub = Bierboerse_pb2_grpc.BierboerseStub(channel)

datapoint = stub.getPrices(Bierboerse_pb2.PricesRequest())
printPricelist(datapoint)

while(True):

    buyId = int(input("Buy: "))

    req = Bierboerse_pb2.BuyRequest(buyId=buyId)
    datapoint = stub.buyBeverage(req)

    printPricelist(datapoint)
