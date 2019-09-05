The way this Todo List app works is pretty simple. You type in a task or item or whatever you want into the input field and then press Add (or click Enter/Return). After you’ve submitted your item, you’ll see it appear as an entry. You can keep adding items and have them all show up. To remove an item, just click on an existing entry.

## Getting Started
```console
create-react-app todolist
```

Delete everything in src and public folders, yadda yadda.

In the public folder, create index.html:

```html
<!DOCTYPE html>
<html>

<head>
  <title>Todo List</title>
</head>

<body>
  <div id="container">

  </div>
</body>

</html>
```

In the src directory, create index.css:

```css
body {
  padding: 50px;
  background-color: #66CCFF;
  font-family: sans-serif;
}
#container {
  display: flex;
  justify-content: center;
}
```

Now, in src, add index.js:

```javascript
import React from "react";
import ReactDOM from "react-dom";
import "./index.css";

var destination = document.querySelector("#container");

ReactDOM.render(
    <div>
        <p>Hello!</p>
    </div>,
    destination
);
```

## Creating the Initial UI