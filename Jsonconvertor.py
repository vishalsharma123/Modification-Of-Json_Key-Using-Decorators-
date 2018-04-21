from jsonkey_converor import json_file
import json
import collections

@json_file("hostlist_user.json")
def some_calculation(ret):
    pass
some_calculation('')

def write_output():
    dp = {}
    i = +0
    with open("hostlist_user10.json", "r") as fin:
        finl = json.load(fin)
        host_value = (finl['hostname'])
        mac_value = (finl['mac-address'])
        ip_value = (finl['ip-address'])
        ilo_value = (finl['ilo_name'])
        osdist_value = (finl['desired_os'])

        for item, item1, item3, item4, item5 in zip(host_value, mac_value, ip_value, ilo_value, osdist_value):
            host = dp[item] = collections.OrderedDict()
            host_dict = dp[item]['hostname'] = item
            Mac_dict = dp[item]['mac-address'] = item1
            IP_Dict = dp[item]['ip-address'] = item3
            ILo_dict = dp[item]['ilo_name'] = item4
            Os_Dict = dp[item]['desired_os'] = item5

    print(dp)
    with open("hostlist_user12.json", "w") as file1:
        l = json.dump(dp, file1)
        print(l)
    return l
write_output()
