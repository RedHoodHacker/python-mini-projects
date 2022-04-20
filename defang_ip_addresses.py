def ip_address(address):
    new_address = ""
    split_address = address.split(".")
    separator = "[.]"
    new_address = separator.join(split_address)
    return new_address
ipaddress = ip_address(input("What ip address would you like to defang: "))

print(ipaddress)


#https://thecleverprogrammer.com/2021/02/22/defang-ip-address-using-python/
