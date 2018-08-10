# coding: utf-8
# @Time : 10/08/2018 6:35 PM

import Cookie


def excute(raw_cookie):
    cookie = Cookie.SimpleCookie()
    cookie.load(raw_cookie)
    cookies = {key: morsel.value for key, morsel in cookie.items()}
    return cookies


if __name__ == '__main__':
    raw_cookie = "JSESSIONID=A3C196C1A0361108DD1CDC18B2080129; _gscu_1138507821=33602706z0v3a020; _gscbrs_1138507821=1; _gscu_125736681=336049870cz1v510; _gscbrs_125736681=1; Hm_lvt_9e03c161142422698f5b0d82bf699727=1533604990; Hm_lpvt_9e03c161142422698f5b0d82bf699727=1533624577; wzwsconfirm=9eba9fc3d74610ac58f7a3a8b16350c2; _gscs_1138507821=t338944902oc4m218|pv:14"
    print(excute(raw_cookie))
