import xmlrpc.client

if __name__ == '__main__':
    proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

    multicall = xmlrpc.client.MultiCall(proxy)

    multicall.add(7, 3)
    multicall.subtract(7, 3)
    multicall.multiply(7, 3)
    multicall.divide(7, 3)

    result: xmlrpc.client.MultiCallIterator = multicall()

    print("7+3=%d, 7-3=%d, 7*3=%d, 7//3=%d" % tuple(result))
