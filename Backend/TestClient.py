import grpc
import Bierboerse_pb2_grpc
import Bierboerse_pb2


channel = grpc.insecure_channel('localhost:1337', options=(('grpc.enable_http_proxy', 0),))
stub = Bierboerse_pb2_grpc.BierboerseStub(channel)

rothaus = 1
augustiner = 0

while(True):
    
    req = Bierboerse_pb2.UpdateBeerRequest(numRothaus=rothaus,numAugustiner=augustiner)
    res = stub.updateBeers(req)

    if (res.prices.augustinerPrice < 200):
        rothaus = 0
        augustiner = 1
    else:
        rothaus = 1
        augustiner = 0

    if (res.prices.rothausBought == 1000):
        print(res)
        break

