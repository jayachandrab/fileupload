import asyncio
payload = "{\"currency\":\"USD\",\"timeframe\":\"Last 7 days\",\r\n           \"startdate\":\"2022-05-26\",\"enddate\":\"2022-05-27\",\r\n           \"operator\": 101,\"brand\": 377}\r\n"
import json
import requests
headers = {
        'token': "Qi9Fdy9HaFhFeXQrNEFRbSt0eTFIQUhweTZvR3IzZXEvL1RXaHpVdmVpVT0=",
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "ababb8dc-6d0d-6982-47e2-466420df6905"
        }
async def task1():
    print("t1")
    
    import requests

    url = "https://api-reports.dragongaming.com/dmbo/api/v1/metrics/homescreenstats"

    

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    t2=asyncio.create_task(task2())
    t3=asyncio.create_task(task3())
    await asyncio.sleep(3)
   
    
    
    
    print("t1 completed")
    return "t1",t2,t3

async def task2():
    print("t2")
    
    top_games_url="https://api-reports.dragongaming.com/dmbo/api/v1/metrics/homescreentopgames"
    response = requests.request("POST", top_games_url, data=payload, headers=headers)
    top_ten_games = json.loads(response.text)
    print("top ten games",top_ten_games)
    
    print("t2 completed")
    return "t2"
async def task3():
    print("t3")
    top_ten_player_urls="https://api-reports.dragongaming.com/dmbo/api/v1/metrics/homescreentopplayers"
    response = requests.request("POST", top_ten_player_urls, data=payload, headers=headers)
    top_ten_players=json.loads(response.text)
    print("in ------ third task")
    print("top ten players ",top_ten_players)
    
    print("t3 completed")
    return "t3"
re=asyncio.run(task1())
    
    
