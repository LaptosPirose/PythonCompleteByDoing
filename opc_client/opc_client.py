"""_summary_
    """
import asyncio
from asyncua import Client  # type: ignore[import]

ENDPOINT = "opc.tcp://192.168.0.237:49370"

NODE_AUTO = "ns=2;s=Schneider.API3.Elevadores.SE1.AUTO"
NODE_CD0 = "ns=2;s=Schneider.API3.Elevadores.SE1.CD0_TIR_SE1"


async def main():
    """_summary_
    """
    client = Client(url=ENDPOINT)

    try:
        await client.connect()
        print("Connected to OPC UA server")

        node_auto = client.get_node(NODE_AUTO)
        node_cd0 = client.get_node(NODE_CD0)

        value_auto = await node_auto.read_value()
        value_cd0 = await node_cd0.read_value()

        print(f"AUTO: {value_auto}")
        print(f"CD0: {value_cd0}")

    finally:
        await client.disconnect()
        print("Disconnected")


if __name__ == "__main__":
    asyncio.run(main())
