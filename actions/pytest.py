import json

payload = {"server": {"name": "client4","imageRef": "6075f74d-49f2-417c-b231-c730c5ae1fb6","flavorRef": "0","security_groups": [{"name": "hcl"}],"networks": [{"uuid":"1f8e9a5c-181d-49a0-994f-6a1029167231"},{"uuid":"74ed69b7-30fb-423e-8800-8470de569c5d"}]}}

print json.dumps(payload)

