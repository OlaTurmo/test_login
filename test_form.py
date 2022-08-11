import requests
from requests.structures import CaseInsensitiveDict

url = "https://eservices.rs.ge/WebServices/hsServiceRequests.ashx/SendServiceRequest"

cookies = {'ASP.NET_SessionId': 'rvtzitsdrlvh2hu3cjsru10u','userToken': '2f97fa1a-7b0d-4510-a5a9-e29a204cc545-1108202202305', 'rsGrid_grdServiceRequestsGridPageSize': '100','rsGrid_grdTurnoverGridPageSize': '15',}

headers = {
		'Accept': 'application/json, text/javascript, */*; q=0.01',
		'Accept-Language': 'en-US,en;q=0.9',
		'Connection': 'keep-alive',
		'Content-Type': 'application/json; charset=UTF-8',
		'Origin': 'https://eservices.rs.ge',
		'Referer': 'https://eservices.rs.ge/ServiceRequestNew.aspx?p=414',
		'Sec-Fetch-Dest': 'empty',
		'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Site': 'same-origin',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
		'X-Requested-With': 'XMLHttpRequest',
		'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
	}

data = '{"pageID": "e6a431f0-69f9-4809-aaa6-500a0d046f93","serviceID": "414","addAppID": "","drpScUserListVal": "","inputFields":[{"ATTRIBUTE1": "test1"},{"ATTRIBUTE2": "test2"}{"ATTRIBUTE3": "test3"},{"ATTRIBUTE4": "test4"},{"ATTRIBUTE5": "test5"},{"ATTRIBUTE6": "test6"},{"ATTRIBUTE7": "2022"},{"PRICE_FIELD": "A577"}],"lockedFields": "","representative": null,"representativeName": null}'


resp = requests.post(url, cookies=cookies, headers=headers, json=data)

print(resp.text)

