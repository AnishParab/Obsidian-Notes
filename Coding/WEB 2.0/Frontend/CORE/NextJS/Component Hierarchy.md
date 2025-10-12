# Next.js App Router — Special Files Explained

| File             | Purpose                                                              | Scope & Behavior                                                                                   |
| ---------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| **layout.js**    | Defines persistent UI (e.g., navbars, sidebars, theme providers)     | Mounted **once** and stays mounted as user navigates; can be nested to provide different layouts   |
| **template.js**  | Similar to layout, but remounts on navigation between siblings       | Creates a **fresh React tree** each time; useful for reset animations or non-persistent state      |
| **error.js**     | React error boundary component with `error` prop                     | Isolated per route segment; errors in `/dashboard/settings` won’t break `/dashboard/users`         |
| **loading.js**   | Fallback UI while a route segment or component is waiting (Suspense) | Automatically shown when child segment suspends; great for spinners, skeleton screens              |
| **not-found.js** | Shown when `notFound()` is called or data/resource isn’t found       | Custom 404 per route segment; acts like an error boundary                                          |
| **page.js**      | Entry point for the actual content of the route                      | Contains route-specific content; can fetch data (`generateStaticParams`, `generateMetadata`, etc.) |

✨ **Summary:**  
- `layout.js` and `template.js` are great for structuring consistent UI.  
- Use `error.js` & `loading.js` to isolate and gracefully handle states per segment.  
- Customize `not-found.js` to provide better UX for missing data or wrong URLs.

---
# Nesting and Rendering Explained

`sample folder structure`
``` bash
/app
 ├─ layout.js          <-- root layout
 ├─ error.js           <-- root error boundary
 ├─ loading.js         <-- root loading boundary
 ├─ dashboard/
 │   ├─ layout.js      <-- dashboard-specific layout
 │   ├─ page.js        <-- /dashboard
 │   ├─ settings/
 │   │   ├─ page.js    <-- /dashboard/settings
 │   │   ├─ error.js   <-- error boundary for /dashboard/settings
 │   │   └─ loading.js <-- loading for /dashboard/settings
 │   └─ users/
 │       ├─ page.js    <-- /dashboard/users
 │       └─ not-found.js <-- handles 404 in /dashboard/users
 └─ about/
     └─ page.js        <-- /about
```

##### **Render hierarchy when you visit `/dashboard/settings`**:
``` bash
Root layout.js
  → dashboard/layout.js
    → dashboard/settings/page.js
```

##### **If data fetching is suspenseful or fails**:
- While waiting → shows `dashboard/settings/loading.js`
- On JavaScript error → shows `dashboard/settings/error.js`
- On `notFound()` → would show nearest `not-found.js`

---
# Recursive Nesting
Each segment’s components are rendered _inside_ its parent segment’s layout.  
For example, `/dashboard/settings`:
``` jsx
Root layout.js
└─ dashboard/layout.js
   └─ dashboard/settings/page.js
```

If `/dashboard/settings` had its own `template.js`, it would wrap around `page.js`:
``` jsx
Root layout.js
└─ dashboard/layout.js
   └─ dashboard/settings/template.js
       └─ page.js
```

---
# How nextJS wraps everything at Runtime
``` jsx
<Layout> {/* dashboard/layout.js */}
  <ErrorBoundary fallback={<Error />}> {/* dashboard/error.js */}
    <Suspense fallback={<Loading />}> {/* dashboard/loading.js */}
      
      <Layout> {/* dashboard/settings/layout.js */}
        <ErrorBoundary fallback={<Error />}> {/* dashboard/settings/error.js */}
          <Suspense fallback={<Loading />}> {/* dashboard/settings/loading.js */}
            
            <Page /> {/* dashboard/settings/page.js */}
            
          </Suspense>
        </ErrorBoundary>
      </Layout>
      
    </Suspense>
  </ErrorBoundary>
</Layout>
```

Error and loading boundaries are applied **independently per segment**:
- If loading takes time in `settings`, only the inner `<Suspense>` shows its loading fallback.
- If there’s an error in `settings/page.js`, only the inner `<ErrorBoundary>` catches it.

---
