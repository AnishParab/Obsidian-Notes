``` ts
bcrypt.genSalt(10, (err, salt) => {
  bcrypt.hash("myPassword", salt, (err, hash) => {
    // store hash
  });
});

bcrypt.compare("myPassword", hash, (err, result) => {
  console.log(result); // true/false
});
```

---
