# Modification-Of-Json_Key-Using-Decorators-
With the help of this program we can  easily changed Typical index jsonkey into normal one 

Example:-


{"book[1].desired_os": "nunu", "book[1].hostname": "s", "book[1].ilo_name": "004", "book[1].ip-address": "123.23.12.1", "book[1].mac-address": "00-14-22-01-23-46", "desired_os": "hplio", "hostname": "d", "ilo_name": "silk", "ip-address": "127.9.00", "mac-address": "00-14-22-01-23-45"}


Decoretor Script Convert this kind of json format into well structure form like:-

OUTPUT:-

{
   "s": {"hostname": "s", 
         "mac-address": "00-14-22-01-23-46", 
         "ip-address": "123.23.12.1", 
         "ilo_name": "004", 
         "desired_os": "nunu"}, 
    "d": {"hostname": "d", 
          "mac-address": "00-14-22-01-23-45", 
          "ip-address": "127.9.00", 
          "ilo_name": "silk", 
          "desired_os": "hplio"
          }
}
