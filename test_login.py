import requests
import uuid

def get_session_id():
	
	session_id=requests.get("https://eservices.rs.ge/Login.aspx").cookies.get_dict()["ASP.NET_SessionId"]
	return session_id
	



def login(session_id):
	
	cookies = {
		'ASP.NET_SessionId': session_id,
	}

	headers = {
		'Accept': 'application/json, text/javascript, */*; q=0.01',
		'Accept-Language': 'en-US,en;q=0.9',
		'Connection': 'keep-alive',
		'Content-Type': 'application/json; charset=UTF-8',
		'Origin': 'https://eservices.rs.ge',
		'Referer': 'https://eservices.rs.ge/Login.aspx?redirect_url=https://eservices.rs.ge/MainPage.aspx',
		'Sec-Fetch-Dest': 'empty',
		'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Site': 'same-origin',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
		'X-Requested-With': 'XMLHttpRequest',
		'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
	}

	json_data = {
		'pageID': str(uuid.uuid4()),
		'username': 'satesto2',
		'password': '123456',
		'screen': '1280',
		'vcode': None,
		'check': '0',
		'latitude': '',
		'longitude': '',
		'SessionID': session_id,
	}

	response = requests.post('https://eservices.rs.ge/WebServices/hsUsers.ashx/Authenticate', cookies=cookies, headers=headers, json=json_data)

	print(response.text)


if __name__=='__main__':


	session_id=get_session_id()
	
	login(session_id)