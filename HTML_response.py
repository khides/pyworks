import telnetlib
tn=telnetlib.Telnet('localhost',8000)
tn.write(b'GET /index.html HTTP/1.1\r\n\r\n')
res=tn.read_all()
print(res.decode('utf-8'),end='')
