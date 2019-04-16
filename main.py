import difflib
import requests

block_links = ["https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts",
                  "https://mirror1.malwaredomains.com/files/justdomains",
                  "http://sysctl.org/cameleon/hosts",
                  "https://zeustracker.abuse.ch/blocklist.php?download=domainblocklist",
                  "https://s3.amazonaws.com/lists.disconnect.me/simple_tracking.txt",
                  "https://s3.amazonaws.com/lists.disconnect.me/simple_ad.txt",
                  "https://hosts-file.net/ad_servers.txt",
                  "https://raw.githubusercontent.com/hectorm/hmirror/master/data/adaway.org/list.txt",
                  "https://raw.githubusercontent.com/hectorm/hmirror/master/data/adblock-nocoin-list/list.txt",
                  "https://raw.githubusercontent.com/hectorm/hmirror/master/data/adguard-simplified/list.txt",
                  "https://raw.githubusercontent.com/hectorm/hmirror/master/data/anudeepnd-adservers/list.txt",
                  "https://raw.githubusercontent.com/hectorm/hmirror/master/data/disconnect.me-ad/list.txt",
                  "https://raw.githubusercontent.com/hectorm/hmirror/master/data/disconnect.me-malvertising/list.txt",
                  "https://raw.githubusercontent.com/hectorm/hmirror/master/data/disconnect.me-malware/list.txt",
                  "https://raw.githubusercontent.com/hectorm/hmirror/master/data/disconnect.me-tracking/list.txt",
                  "https://raw.githubusercontent.com/hectorm/hmirror/master/data/easylist/list.txt",
                  "https://raw.githubusercontent.com/hectorm/hmirror/master/data/easyprivacy/list.txt",
                  "https://raw.githubusercontent.com/hectorm/hmirror/master/data/eth-phishing-detect/list.txt",
                  "https://raw.githubusercontent.com/hectorm/hmirror/master/data/fademind-add.2o7net/list.txt",
                  "https://raw.githubusercontent.com/hectorm/hmirror/master/data/fademind-add.dead/list.txt",
                  "https://raw.githubusercontent.com/hectorm/hmirror/master/data/fademind-add.risk/list.txt",
                  "https://raw.githubusercontent.com/hectorm/hmirror/master/data/fademind-add.spam/list.txt",
                  "https://raw.githubusercontent.com/hectorm/hmirror/master/data/kadhosts/list.txt",
                  "https://raw.githubusercontent.com/hectorm/hmirror/master/data/malwaredomainlist.com/list.txt",
                  "https://raw.githubusercontent.com/hectorm/hmirror/master/data/malwaredomains.com-immortaldomains/list.txt",
                  "https://raw.githubusercontent.com/hectorm/hmirror/master/data/malwaredomains.com-justdomains/list.txt",
                  "https://raw.githubusercontent.com/hectorm/hmirror/master/data/matomo.org-spammers/list.txt",
                  "https://raw.githubusercontent.com/hectorm/hmirror/master/data/mitchellkrogza-badd-boyz-hosts/list.txt",
                  "https://raw.githubusercontent.com/hectorm/hmirror/master/data/pgl.yoyo.org/list.txt",
                  "https://raw.githubusercontent.com/hectorm/hmirror/master/data/ransomwaretracker.abuse.ch/list.txt",
                  "https://raw.githubusercontent.com/hectorm/hmirror/master/data/someonewhocares.org/list.txt",
                  "https://raw.githubusercontent.com/hectorm/hmirror/master/data/spam404.com/list.txt",
                  "https://raw.githubusercontent.com/hectorm/hmirror/master/data/stevenblack/list.txt",
                  "https://raw.githubusercontent.com/hectorm/hmirror/master/data/winhelp2002.mvps.org/list.txt",
                  "https://raw.githubusercontent.com/hectorm/hmirror/master/data/zerodot1-coinblockerlists-browser/list.txt",
                  "https://raw.githubusercontent.com/hectorm/hmirror/master/data/zeustracker.abuse.ch/list.txt",
                  "https://raw.githubusercontent.com/CHEF-KOCH/Audio-fingerprint-pages/master/AudioFp.txt",
                  "https://raw.githubusercontent.com/CHEF-KOCH/Canvas-fingerprinting-pages/master/Canvas.txt",
                  "https://raw.githubusercontent.com/CHEF-KOCH/WebRTC-tracking/master/WebRTC.txt",
                  "https://raw.githubusercontent.com/CHEF-KOCH/CKs-FilterList/master/Anti-Corp/hosts/NSABlocklist.txt",
                  "https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-blocklist.txt",
                  "https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-malware.txt",
                  "https://www.stopforumspam.com/downloads/toxic_domains_whole.txt",
                  "https://raw.githubusercontent.com/EvaTheSalmon/Pi-Hole-List/master/hosts.txt",
                  "https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/firewall/spy.txt",
                  "https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/firewall/extra.txt"
                  ]


white_links = ["https://raw.githubusercontent.com/EvaTheSalmon/Pi-Hole-List/master/whitelist.txt"]

open(r'D:\Hosts_list_merger\final.txt', 'w').close()

for link_bl in block_links:
    open(r'D:\Hosts_list_merger\block.txt', 'w').close()

    with open(r'D:\Hosts_list_merger\block.txt', 'w+', encoding='utf-8') as black:
        black.write(requests.get(link_bl.rstrip('\n')).text)
        print(black.readlines())
        
        open(r'D:\Hosts_list_merger\white.txt', 'w').close()            
        
        for link_wh in white_links:
            with open(r'D:\Hosts_list_merger\white.txt', 'w+', encoding='utf-8') as white:
                white.write(requests.get(link_wh.rstrip('\n')).text)

                final = open(r'D:\Hosts_list_merger\final.txt', 'w', encoding='utf-8')

                while 1:
                    a = black.readline().rstrip('\n')
                    if a[0:1] == "#":
                        break
                    if a == "":
                        break
                    while 1:
                        b = white.readline().rstrip('\n')
                        if a == b: 
                            break
                        if b == "":
                            break
                    if a!=b: 
                        final.write(a+"\n")  
                    white.seek(0)
                final.close()
