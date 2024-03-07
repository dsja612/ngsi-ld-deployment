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

    # populating address space with variables
    sensor = await server.nodes.objects.add_object(idx, "")
    temperature = await sensor.add_variable(idx, "temperature", 0.0) # set var type to double

    # set variable to be writable by clients
    await temperature.set_writable()
    _logger.info("Starting server!")

    async with server:
        while True:
            await asyncio.sleep(2)
            temp_val = await temperature.get_value()
            _logger.info("Temperature is now %s", temp_val)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main(), debug=True)
