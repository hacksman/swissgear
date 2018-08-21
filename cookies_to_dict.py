# coding: utf-8
# @Time : 10/08/2018 6:35 PM

import Cookie


def execute(raw_cookies):
    cookie = Cookie.SimpleCookie()
    cookie.load(raw_cookies)
    cookies = {key: morsel.value for key, morsel in cookie.items()}
    return cookies


if __name__ == '__main__':
    raw_cookies = "yunsuo_session_verify=90075c720c3e3b578cbc5eb838e765c8; Hm_lvt_83853859c7247c5b03b527894622d3fa=1534212998; srcurl=687474703a2f2f7777772e6c616e646368696e612e636f6d2f64656661756c742e617370783f74616269643d333234; security_session_mid_verify=27d7693bf51366d5d556cac5e94d9ee8; ASP.NET_SessionId=3lwpspqbj1kyurcn22vrc0oa; Hm_lpvt_83853859c7247c5b03b527894622d3fa=1534213995"
    print(execute(raw_cookies))


