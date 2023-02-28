import pyping

r = pyping.ping('google.com')

if r.ret_code == 0:
    print("Success")
else:
    print("Failed with {}".format(r.ret_code))
