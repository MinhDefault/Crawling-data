import asyncio
from fileinput import filename
from time import sleep
from urllib import response
from venv import create
from xml.dom.minidom import TypeInfo
from aiohttp import ClientSession
import pathlib
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

sbd = []
cum_thi = []
toan = []
ngu_van = []
ngoai_ngu = []
vat_ly = []
hoa_hoc = []
sinh_hoc = []
lich_su = []
dia_ly = []
gdcd = []

def exportfile(results, dfName) :
    for result in results:
        html_data = result
    # print(html_data) 
        a = html_data.replace("\n", "")
        b = a.replace("\t","")
        c = b.replace("FacebookTwitter","")

        # số báo danh
        sbd.append(c[12:20])

        # Cụm thi
        cum_thi.append(c[c.find("thi")+5:c.find("Môn")])

        # Toán
        if c.find("Toán") != -1:
            toan.append(c[c.find("Toán")+4:c.find("Toán")+8])
        else:
            toan.append(np.nan)

        #Văn
        if c.find("văn") != -1:
            ngu_van.append(c[c.find("văn")+3:c.find("văn")+7])
        else:
            ngu_van.append(np.nan)

        #Anh
        if c.find("Ngoại ngữ") != -1:
            ngoai_ngu.append(c[c.find("Ngoại ngữ")+9:c.find("Ngoại ngữ")+9+4])
        else:
            ngoai_ngu.append(np.nan)

        #Lý
        if c.find("lý") != -1:
            vat_ly.append(c[c.find("lý")+2:c.find("lý")+6])
        else:
            vat_ly.append(np.nan)
            
        # Hóa
        if c.find("Hóa") != -1:
            hoa_hoc.append(c[c.find("Hóa")+7:c.find("Hóa")+11])
        else:
            hoa_hoc.append(np.nan)
            
        # Sinh
        if c.find("Sinh") != -1:
            sinh_hoc.append(c[c.find("Sinh")+8:c.find("Sinh")+12])
        else:
            sinh_hoc.append(np.nan)
        # Sử
        if c.find("sử") != -1:
            lich_su.append(c[c.find("sử")+2:c.find("sử")+6])   
        else:
            lich_su.append(np.nan)

        # Địa
        if c.find("Địa") != -1:
            dia_ly.append(c[c.find("Địa")+6:c.find("Địa")+10])
        else:
            dia_ly.append(np.nan)

        # GDCD
        if c.find("dân") != -1:
            gdcd.append(c[c.find("dân")+4:c.find("dân")+10])
        else:
            gdcd.append(np.nan)

        df9 = pd.DataFrame({
            "Số báo danh":sbd,
            "Cụm thi":cum_thi,
            "Toán":toan,
            "Ngữ văn": ngu_van,
            "Ngoại ngữ": ngoai_ngu,
            "Vật lý": vat_ly,
            "Hóa học": hoa_hoc,
            "Sinh học": sinh_hoc,
            "Lịch sử":lich_su,
            "Địa lý": dia_ly,
            "GDCD": gdcd
        })

        df9.to_csv("DataFrame"+dfName+".csv")


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
async def main(startid, endid):
    # html_body = ""
    tasks = []
    async with ClientSession() as session:
        for i in range(startid,endid):
            # year = start_year - i
            # url = f'https://www.boxofficemojo.com/year/{year}/'
            url = f'https://diemthi.vnexpress.net/index/detail/id/{i}'
            # print("year", year, url)
            # print(f'{i}: ', url)
            tasks.append(
                # asyncio.create_task(
                #     fetch(url, session, year)
                # )
                asyncio.create_task(
                    fetch(url, session)
                )
            )
        # pages_content = await asyncio.gather(*tasks) # [{"body": "..", "year": 2020 }]
        #  tasks chứa những function fetch 
        # print(tasks)
        # student data là 1 list chứa những return của list tasks
        student_data = await asyncio.gather(*tasks)
        return student_data
        # return pages_content

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# Test lần 1: gửi 2 request mỗi request 1000 item, xuất ra 2 files Succeed
# Test lần 2: gửi 5 req mỗi req 1000 item, xuất ra 5 files (Fail do timeout)
# Test lần 3: gửi 5 req mỗi req 1000 item, xuất ra 5 files; mỗi lần xuất 1 file thì sleep 10s (Fail do sv shut)
# Test lần 4: gửi 5 req mỗi req 1000 item, xuất ra 5 files; mỗi lần xuất 1 file thì sleep 10-13s (fail do sv shut)
# Test lần 5: gửi 5 req mỗi req 1000 item, xuất ra 5 files; mỗi lần xuất 1 file thì sleep 60-63s (fail tại result2 do sv shut)
# Test lần 6: gửi 5 req mỗi req 1000 item, xuất ra 5 files; mỗi lần xuất 1 file thì sleep 123s 98s 66s... (fail nhanh tại result2)
# Test lần 7: gửi 5 req mỗi req 1000 item, xuất ra 5 files; mỗi lần xuất 1 file thì sleep hẳn 6p (fail tại result3 do sv shut)
# Test lần 8: gửi 5 req mỗi req 500 item, xuất ra 5 files; mỗi lần xuất 1 file (fail tại result 4 do sv shut)
# Test lần 9: gửi 2 req mỗi req 2000 item, xuất ra 2 files; mỗi lần xuất 1 file, sleep 600 (Succeed)
# Test lần 10: gửi 5req mỗi req 2000 item, xuất ra 5 files; mỗi lần xuất 1 file, sleep 480 (fail tại result 3 do sv shut)
# Test lần 10: gửi 2req mỗi req 2000 item, xuất ra 2 files; mỗi lần xuất 1 file, sleep 180 (fail tại result 3 do sv shut)
# Test lần 11: gửi 2req mỗi req 1500 item, xuất ra 2 files; mỗi lần xuất 1 file, sleep 180

#  ==> thời gian sleep k qtrong, qtorng là within some hours, ban lifted ko biết bao lâu; chỉ import đc 4k per vpn

# Ngoại lệ (mạng cực khỏe) scrape 4000 mỗi vpn; sleep 480
# Trước 10h (mạng khỏe) scrape 2500-3000 mỗi vpn; sleep 150 
# (hiện tại khi scrape 2500 (1500,1000) files chưa lỗi lần nào; còn 3000 thì lỗi vài lần)

# Sau 10h (mạng yếu) scrape 1000 user mỗi vpn thôi

# Cách dùng: sửa 2 số ở hàm main tương ứng với start và end; minimum mỗi lần asyncio để run là 1000 users

result1 = asyncio.run(main(8601587,8603087))
print("đã lấy data cho result1")

sleep(150)
result2 = asyncio.run(main(8600087,8601586))
print("đã lấy data cho results2")

print("thực hiện merge result1 và result2")
result = result1 + result2

print("merge xong 2 mảng")
fileNameNumber = "2"
exportfile(result, fileNameNumber)
print("exported ra file "+fileNameNumber)