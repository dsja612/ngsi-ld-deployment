import asyncio
import logging

from asyncua import Server, ua
# from asyncua.common.methods import uamethod

# @uamethod
# def func(parent, value):
#     return value * 2

async def main():
    _logger = logging.getLogger(__name__)

    # setup our server
    server = Server()
    await server.init()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")

    # set up our own namespace, not really necessary but should as spec
    uri = "http://examples.freeopcua.github.io"
    idx = await server.register_namespace(uri)

    # populating our address space
    myobj = await server.nodes.objects.add_object(idx, "TemperatureSensor001")
    # Change variable name here to "temperature"
    myvar = await myobj.add_variable(idx, "temperature", 6.7)

    # Set MyVariable (now "temperature") to be writable by clients
    await myvar.set_writable()

    # await server.nodes.objects.add_method(
    #     ua.NodeId("ServerMethod", idx),
    #     ua.QualifiedName("ServerMethod", idx),
    #     func,
    #     [ua.VariantType.Int64],
    #     [ua.VariantType.Int64],
    # )
    _logger.info("Starting server!")

    async with server:
        while True:
            await asyncio.sleep(1)
            new_val = await myvar.get_value() + 0.1
            _logger.info("Set value of %s to %.1f", myvar, new_val)
            await myvar.write_value(new_val)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main(), debug=True)
