# **With Pug (Template Engine)**

**Route**
```js
res.render('index', { name: 'asp' })
```

**index.pug**
```pug
h1 Hello #{name}
```

**Output (Browser receives)**
```html
<h1>Hello asp</h1>
```

---
# **Without Pug (Plain Express)**

**Route**
```js
res.send('<h1>Hello asp</h1>')
```

**Output (Browser receives)**
```html
<h1>Hello asp</h1>
```

---
# Difference (Core Idea)

```text
Pug       → Write compressed template → Express compiles → HTML
No Pug    → Write HTML manually → Express sends directly
```

---
