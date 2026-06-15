# Bash Script

Create `~/scripts/api.sh`:
```bash
#!/bin/bash

URL="http://localhost:3000"
ENDPOINT=$1
METHOD=${2:-GET}
DATA=$3

STATUS=$(curl -s -o /tmp/api_response.json \
              -w "%{http_code}" \
              -X "$METHOD" \
              -H "Content-Type: application/json" \
              ${DATA:+-d "$DATA"} \
              "$URL/$ENDPOINT")

echo "Status: $STATUS"
echo "Body:"
cat /tmp/api_response.json | jq
```

Usage:
```bash
chmod +x ~/scripts/api.sh

~/scripts/api.sh books              # GET /books
~/scripts/api.sh books POST '{"title":"Dune","author":"Herbert"}'
```

---
