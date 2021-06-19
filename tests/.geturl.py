#http://api.qrserver.com/v1/read-qr-code/?fileurl=

from urllib import parse, request
from json import loads

enc = parse.urlencode({"" : "https://media.discordapp.net/attachments/844755531049467915/855601044410728478/SPOILER_431590024559984641.png"})

response = request.urlopen("http://api.qrserver.com/v1/read-qr-code/?fileurl{}".format(enc))
s = loads(response.read())
print(s)