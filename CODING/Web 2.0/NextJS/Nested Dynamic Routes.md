# What are Nested Dynamic Routes
- You have already accessed `/products/1` dynamic route to show details of product 1 only.
- Now, in order to access the reviews section of product 1 we should use the route `/products/1/reviews/1`.

---
# Implementation
- Create `src/app/products/[productId]/reviews/[reviewId]/page.tsx`

---
# Syntax
``` tsx
export default async funstion ( {params: 
	params: Promise<{productId: string, reviewId: string}>;
}) {
	const {productId, reviewId} = await params

	return <h1>Review: {reviewId}, Product: {productId}</h1> 
}
```

---
Explanation of the code is in [[Nested Routes]].

---
