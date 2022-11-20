import requests
import pandas as pd  # 可以解析表格数据

url = "https://tianqi.2345.com/Pc/GetHistory"

headers = {
    "User-Agent": """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35"""
}

def craw_table(year, month):
    params = {
        "areaInfo[areaId]": 71919,
        "areaInfo[areaType]": 2,
        "date[year]": year,
        "date[month]": month
    }

    resp = requests.get(url, headers=headers, params=params)
    data = resp.json()["data"]
    df = pd.read_html(data)[0]
    return df


df_list = []
for year in range(2011, 2022):
    for month in range(1, 13):
        print("爬取：", year, month)
        try:
            df = craw_table(year, month)
        except:
            print("没有当月数据")
            continue
        df_list.append(df)

pd.concat(df_list).to_excel("集美区10年天气数据.xlsx", index=False)
