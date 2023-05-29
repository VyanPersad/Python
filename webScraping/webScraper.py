import requests
from bs4 import BeautifulSoup

r = requests.get(
    "https://www.amazon.com/s?k=computer+components&adgrpid=81801918615&hvadid=585362546850&hvdev=c&hvlocphy=9075961&hvnetw=g&hvqmt=b&hvrand=847316709651011563&hvtargid=kwd-10827891&hydadcr=22309_13333543&tag=hydglogoo-20&ref=pd_sl_9aul9hj8bg_b"
)
c = r.content

soup = BeautifulSoup(c, "html.parser")
all=soup.find_all("span",{"class":})
