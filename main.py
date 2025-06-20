import asyncio
from connect import Session
import my_select


async def main():
    async with Session() as session:
        print(await my_select.select_1(session))
        print(await my_select.select_2(session, "Math"))
        print(await my_select.select_3(session, "Math"))
        print(await my_select.select_4(session))
        print(await my_select.select_5(session, "Matthew Gray"))
        print(await my_select.select_6(session, "Group-1"))
        print(await my_select.select_7(session, "Group-1", "Math"))
        print(await my_select.select_8(session, "James Duncan"))
        print(await my_select.select_9(session, "James Booth"))
        print(await my_select.select_10(session, "James Booth", "Matthew Gray"))


if __name__ == "__main__":
    asyncio.run(main())
