# What is Rendering
- **Component Code** to **UI** conversion is rendering.
- Types ---> CSR, SSR and RSCs.

---
# Reacts way of Rendering
- React was primarily used for building Single Page Applications (SPAs).

---
# Single Page Application
![[SPA.excalidraw|1000]]

---
# Client Side Rendering
- This whole approach - where your browser (the client) transforms React components into what you see on screen - is called as _Client Side Rendering_.
- **React Components** ---> **UI** , is called as _CSR_.

---
# Drawbacks
##### **SEO**
- When search engines crawl your site, they're mainly looking at HTML content.
- But with CSR, your initial HTML is basically just an empty _div_
- When you have a lot of nested components making API calls, the meaningful content might load too slowly for search engines to even catch it.

##### **Performance and Experience**
- Your browser (the client) has to do everything: _fetch data, build the UI, make everything interactive._
- Users end up staring at a blank screen or a loading spinner.
- Everytime you add a new feature to your app, the **Javascript Bundler** gets bigger.

---
