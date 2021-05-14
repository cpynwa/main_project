import re
import ipcalc
#
# def config_finder():
#     with open("C:/Users/admin/PycharmProjects/netconf_test/config_finder/config.txt", "r") as file:
#         all_config = file.readlines()
#
#     lines = list(map(lambda s: s.strip(), all_config))
#     set_config_list = []
#     config_list = []
#     interface = 'xe-8/1/2'
#
#     for line in lines:
#         if re.match(f'^set ',line):
#             set_config_list.append(line)
#     for line in set_config_list:
#         if re.match(f'.* {interface} .*',line):
#             config_list.append(line)
#     for line in config_list:
#         if re.match(r'.*inet address.*', line):
#             ipv4 = line.split()[8]
#         elif re.match(r'.*inet6 address.*', line):
#             ipv6 = line.split()[8]
#             print(ipv6)
#     for network in ipcalc.Network(ipv4):
#         if network == ipv4:
#             continue
#         else:
#             for line in set_config_list:
#                 if re.match(f'(.*{network}.*)', line):
#                     config_list.append(line)
#     for network in ipcalc.Network(ipv6):
#         ipv6_comp = network.to_compressed()
#         if network == ipv6:
#             continue
#         else:
#             for line in set_config_list:
#                 if re.match(f'(.*{ipv6_comp}.*)', line):
#                     config_list.append(line)
#     return config_list
#
# for i in config_finder():
#     print(i)
#
# for x in ipcalc.Network("2001:290:1::9/127"):
#     print(x)


a = [1, 2, 3, 4, 5, 6]
b = [7, 8, 9, 10, 11]
a = a + [i for i in b]
print(a)