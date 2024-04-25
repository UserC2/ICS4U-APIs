import requests

req = requests.get("https://whatthecommit.com/index.txt")

# won't catch no-wifi errors
if (req.status_code != 200):
  print("failure")
  exit()

print(req.text)