from urllib.request import urlopen
from urllib.error import URLError, HTTPError

url = "https://collection.hyundai.com"

# https://collection.hyundai.com
# https://autoway.hyundai.net
# https://partner.hyundai.com
# https://Vaatzit.autoever.com
# https://smpass.hyundai-autoever.com
# https://www.ihl.co.kr
# https://ngqms.wia.co.kr
# https://m.people-lounge.wia.co.kr
# https://push.people-lounge.wia.co.kr
# https://mgqms.wia.co.kr
# https://mtam.wia.co.kr
try:
    res = urlopen(url)
    print(res.status)
except HTTPError as e:
    err = e.read()
    code = e.getcode()
    print(code)  ## 404

