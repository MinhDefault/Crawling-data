import asyncio
from urllib import response
from venv import create
from xml.dom.minidom import TypeInfo
from aiohttp import ClientSession
import pathlib
from bs4 import BeautifulSoup
import pandas as pd

async def sort(response) :
    student_info = await response.text()
    student_info.replace(" ","")
    soup = BeautifulSoup(student_info, features="lxml")
    info = soup.find(class_="o-detail-thisinh").getText(strip=True)
    return info

# async def fetch(url, session, year):
async def fetch(url, session):
    # async with session.get(url) as response:
    #     html_body = await response.read()
    #     return {"body": html_body, "year": year}

    async with session.get(url) as response:
        student_info = await sort(response)
        return student_info

# async def main(start_year=2020, years_ago=2):
async def main(start_id = 8000000,
end_id = 8000000 + 10):
    # html_body = ""
    tasks = []
    # semaphore
    async with ClientSession() as session:
        for i in range(start_id, end_id):
            # year = start_year - i


            # url = f'https://www.boxofficemojo.com/year/{year}/'

            url = f'https://diemthi.vnexpress.net/index/detail/id/{i}'
            # print("year", year, url)

            print(f'{i}: ', url)

            tasks.append(
                # asyncio.create_task(
                #     fetch(url, session, year)
                # )
                asyncio.create_task(
                    fetch(url, session)
                )
            )
        # pages_content = await asyncio.gather(*tasks) # [{"body": "..", "year": 2020 }]

        student_data = await asyncio.gather(*tasks)
        return student_data
        # return pages_content

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
results = asyncio.run(main())

for result in results:
    html_data = result
    print(html_data) 