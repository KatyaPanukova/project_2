time = 178
n = 0
time_ = time
while time_ > 59:
    time_ -= 60
    n += 1
print(n)
mint = n
sec = time - 60 * n
if mint == 0:
    mint = '00'
elif len(str(mint)) == 1:
    mint = '0' + str(mint)
if sec == 0:
    sec = '00'
if len(str(sec)) == 1:
    sec = '0' + str(sec)

result = '{}:{}'.format(str(mint), str(sec))
print(result)