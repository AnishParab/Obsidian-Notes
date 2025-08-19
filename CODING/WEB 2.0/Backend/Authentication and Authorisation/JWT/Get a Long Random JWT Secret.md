``` bash
node -e "console.log(require('crypto').randomBytes(64).toString('hex'))"

```

Example Output :
``` bash
c2fa5171c2e30a9f5cdaf49af9abe5f0d18951a937ca98141b9eb24ef863154c7c15bd6f6721f9a0808646c5ce9ec01e150eabaa76b1b6bef2586e7b0a7cfef7
```

---
# `.env` OR `.env.local`
``` txt
JWT_SECRET="c2fa5171c2e30a9f5cdaf49af9abe5f0d18951a937ca98141b9eb24ef863154c7c15bd6f6721f9a0808646c5ce9ec01e150eabaa76b1b6bef2586e7b0a7cfef7"
```
- If your secret has any special characters, it should be wrapped in **Double Quotes** `" "`.

---
