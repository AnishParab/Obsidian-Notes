# NOTE

> `sm:grid-cols-3` ---> **This just means that smaller and above screens ko 3 grid column lagta hai.**

---
# Reality
- In any course of tailwind, we are taught to build mobile first.
- But, in reality many developers actually build for bigger screens.

> **NOTE :** **Hence, always worry about the smaller and above screens first**.

---
# Layout 1
![[layout_1.excalidraw|400]]
``` html
<div class="m-4 grid grid-cols-2 gap-4 sm:grid-cols-2">

	<div class="min-h-[100px] rounded-lg bg-orange-500"></div>
	<div class="min-h-[100px] rounded-lg bg-teal-500"></div>
	
</div>
```
#### Steps
- Made a grid of **2 columns** using `sm:grid-cols-2`.
- For _smaller screens_ the grid is also of **2 columns** using `grid-cols-2`.

---
# Layout 2
![[non_equal.excalidraw|400]]
``` html
<div class="m-4 grid grid-cols-1 gap-4 sm:grid-cols-12">

	<div class="min-h-[100px] rounded-lg bg-orange-500 sm:col-span-2"></div>
	<div class="min-h-[100px] rounded-lg bg-teal-500 sm:col-span-10"></div>
	
</div>
```
#### Steps
- Made a grid of **12 columns** using `sm:grid-cols-12.
- First div ---> `sm:col-span-2`, takes **2 spaces**.
- Second div ---> `sm:col-span-10`, takes **12-2 = 10 spaces
- For _smaller screens_, the grid is of **2 columns** using `grid-cols-1`

---
# Layout 3
![[layout_3.excalidraw|400]]
``` html
<div class="m-4 grid gap-4 sm:grid-cols-12">

	<div class="bg-green-500 sm:col-span-2 sm:block hidden"></div>
	<div class="bg-orange-500 sm:col-span-8"></div>
	<div class="bg-blue-500 sm:col-span-2 sm:block hidden"></div>
	
</div>
```
### Steps
- `hidden` ---> For smaller screens
- `block` ---> For smaller screens and above.

---
