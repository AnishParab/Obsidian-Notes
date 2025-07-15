# Pre-requisites
- NextJS 15
- TailwindCSS v4
- React Icons

---
# Setup
``` css
src
├── app
│   ├── globals.css
│   ├── layout.tsx
│   └── page.tsx
├── components
│   ├── Helper
│   │   └── Helper.tsx
│   └── Home
│       ├── Home.tsx
│       └── Navbar
│           ├── MobileNavbar.tsx
│           ├── Navbar.tsx
│           └── ResponsiveNavbar.tsx
└── constants
    └── navLinks.ts
```

---
# **`app` directory**
- This defines your applications routes.
- Enables Server Components, loading state, error boundaries, etc.

---
### `globals.css`
- Define your app's global style.
`globals.css`
``` css
@import "tailwindcss"
```

---
### `layout.tsx`
- Defined **Manrope font** and **Metadata**.
- Loads **Responsive Navbar** for navbar to appear on every page.
`layout.tsx`
``` tsx
import type { Metadata } from "next";
import { Manrope } from "next/font/google";
import "./globals.css";
import ResponsiveNavbar from "@/components/Home/Navbar/ResponsiveNavbar";

const font = Manrope({
  weight: ['200', '300', '400', '500', '600', '700', '800'],
  subsets: ['latin'],
});

export const metadata: Metadata = {
  title: "Food Landing Page",
  description: "A Simple Food Landing Page",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${font.className} antialiased`}
      >
        <ResponsiveNavbar />
        {children}
      </body>
    </html>
  );
}
```

---
### `page.tsx`
- Added the **Home Component**.
`page.tsx`
``` tsx
import React from "react";
import Home from "../components/Home/Home";

const HomePage = () => {
  return <div>
    <Home />
  </div>
};

export default HomePage;
```

---
# `components/Home`
- Defines the contents of the Home Page, which is loaded in `app/page.tsx`
`Home.tsx`
``` tsx
import React from "react"

const Home = () => {
	return <div className="overflow-hidden">Home</div>;
}

export default Home;
```

---
### `components/Home/Navbar`
- Includes `Navbar.tsx`, `MobileNavbar.tsx`, `ResponsiveNavbar.tsx`.

---
##### `ResponsiveNavbar.tsx`
- Loads `Navbar.tsx` and `MobileNavbar.tsx`.
- `ResponsiveNavbar.tsx` is loaded in `app/layout.tsx`.
- Any animations relating to navbar's will be added here.

`ResponsiveNavbar.tsx`
``` tsx
import React from "react"
import Navbar from "./Navbar";
import MobileNavbar from "./MobileNavbar";

const ResponsiveNavbar = () => {
	return (
		<div>
			<Navbar />
			<MobileNavbar />
		</div>
	);
}

export default ResponsiveNavbar
```

---
##### `Navbar.tsx`

`Navbar.tsx`
``` tsx
"use client";
import { NavLinks } from "@/constants/navLinks"
import Link from "next/link"
import React, { useEffect, useState } from "react"
import { HiBars3BottomRight } from "react-icons/hi2"
import { MdDeliveryDining } from "react-icons/md"

const Navbar = () => {

	const [navBg, setNavBg] = useState(false)

	useEffect(() => {
		const handler = () => {
			if (window.scrollY >= 90) setNavBg(true);
			if (window.scrollY < 90) setNavBg(false);
		};

		window.addEventListener("scroll", handler)

		return () => window.removeEventListener("scroll", handler)
	}, [])

	return (
		<div className={`transition-all ${navBg ? 'bg-white shadow-md' : 'fixed'} duration-200 h-[12vh] z-[100] fixed w-full`}>---
			<div className="flex items-center h-full justify-between w-[90%] x1:w-[80%] mx-auto">

				{/* LOGO */}
				<div className="flex items-center space-x-2">
					<div className="w-10 h-10 bg-blue-950 rounded-full flex items-center justify-center flex-col">
						<MdDeliveryDining className="w-6 h-6 text-white" />
					</div>
					<h1 className="text-x1 hidden sm:block md:text-2xl text-black font-bold">Foodie</h1>
				</div>

				{/* NavLinks */}
				<div className="hidden lg:flex items-center space-x-10">
					{NavLinks.map((link) => {
						return (
							<Link
								key={link.id}
								href={link.url}
								className="text-black hover:text-green-700 font-bold transition-all duaration-200"
							>
								<p>{link.label}</p>
							</Link>
						)
					})}
				</div>

				{/* buttons */}
				<div className="flex items-center space-x-4">
					{/* Join Now Button */}
					<button className="bg-blue-950 px-8 py-2.5 text-white font-bold rounded-lg hover:bg-black transition-all duration-300 cursor-pointer">
						Join Now
					</button>
					{/* Theme Toggler */}
				</div>
			</div>
		</div>
	)
}

export default Navbar
```

---
