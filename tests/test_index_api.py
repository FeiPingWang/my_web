import requests, nose


class Test_api:

    def test_api(self):
        r = requests.get("http://127.0.0.1:3000/test/api")
        assert ('Hello' in r.text)

    # 测试注册
    def test_register(self):
        payload = {
            'user_name' : 'wfp',
            'password' : '123',
            'confirm' : '234'
        }
        r = requests.post("http://127.0.0.1:3000/register", data=payload)
        print(r.headers)

