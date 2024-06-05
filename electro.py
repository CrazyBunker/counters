import requests
import json
import time
class electro:
    def __init__(self, modem_id, api_key , url='https://lk.waviot.ru/api.data/get_modem_channel_values/'):
        self.data = {
                'modem_id': modem_id,
                "key": api_key, 
                "channel": "electro_ac_p_lsum_tsum",
                "from": int(time.time()-60),
                "to": int(time.time())
                }
        self.url = url

    def get_counter(self):
        self.curSession = requests.Session()
        responseLogin=self.curSession.get(self.url, #+"?modem_id="+ self.data["modem_id"]+"&channel="+self.data["channel"]+"&key="+self.data["key"]+"&from=new")
                                          params=self.data)
        try:
            counter = json.loads(responseLogin.text)['values']
            counter = counter[list(counter.keys())[0]]
        except:
            return 'Error'
        else:
            return counter
