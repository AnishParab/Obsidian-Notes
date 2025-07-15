# What are Dynamic Routes
**example**:
- `/products` ---> Shows _Product 1, Product 2 and Product 3_
- `/products/1` ---> Shows _Product 1 details_

---
# Implementation
- Create `src/app/products/page.tsx` ---> List all products here

- Now, create a special folder and a file inside it namely, `src/app/products/[productId]/page.tsx` ---> Explained below. 
**NOTE: Use this for `zsh`** _(Use This)_
``` bash
mkdir -p 'products/[productId]'

touch 'products/[productId]/page.tsx'
```

---
# Route Parameters
- Every **page** inside the `app` directory **receives route parameters** through the `params` prop.
- The `params` prop is an **object** containing the dynamic segments as **key–value pairs**.

---
# Correct type-of  `params`
- `params` is **not** a Promise.
- It is always a plain synchronous object:
``` tsx
{ params: { serviceId: string } }

```
- So you **do not** need `async` or `await` just to get `params`.

---
# Syntax
``` tsx
export default function ProductDetails({ params }: { params: { productId: string } }) {
  return <h1>Details about product {params.productId}</h1>;
}

```

---
