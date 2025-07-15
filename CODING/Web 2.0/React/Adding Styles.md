# `className`
- In React, you specify a CSS class with `className`.
``` jsx
<img className="avatar" />
```

- Then you can write the CSS rules fot it in a separate CSS file:
``` css
.avatar {  
	border-radius: 50%;
}
```

---
> **NOTE:** React does not prescribe how you add CSS files. In the simplest case, you’ll add a [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/link) tag to your HTML. If you use a build tool or a framework, consult its documentation to learn how to add a CSS file to your project.

---
