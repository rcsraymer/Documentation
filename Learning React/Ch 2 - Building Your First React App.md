# GETTING YOUR REACT ON

Create a new HTML document with the following contents:
  
```html
<!DOCTYPE html>
<html>
 
<head>
  <meta charset="utf-8">
  <title>React! React! React!</title>
</head>
 
<body>
  <script>
 
  </script>
</body>
 
</html>

<script src="https://unpkg.com/react@16/umd/react.development.js"></script>
<script src="https://unpkg.com/react-dom@16/umd/react-dom.development.js"></script>
<script src="https://unpkg.com/babel-standalone@6.15.0/babel.min.js"></script>
```
If you preview your page right now, you’ll notice that this page is still blank, with nothing visible going on. That’s okay. We’re going to fix that next.

# DISPLAYING YOUR NAME
Now you’re going to use React to display your name onscreen. You do that by using a method called render. Inside your empty script tag in the body, add the following:

```html
<script type="text/babel">
  ReactDOM.render(
    <h1>Batman</h1>,
    document.body
  );
</script>
```
Your browser should display Sherlock Holmes.

This introduces you to one of the most frequently used methods you’ll use in the React universe: the ReactDOM.render method.

The render method takes two arguments:

1. The HTML-like elements (a.k.a. JSX) you want to output

2. The location in the DOM where React will render the JSX into

# Changing the Destination
First we’ll change where the JSX gets output. Using JavaScript to place things directly in your body element is never a good idea. A lot can go wrong, especially if you’re going to be mixing React with other JS libraries and frameworks. The recommended path is to create a separate element that you will treat as a new root element. This element will serve as the destination your render method will use. To make this happen, go back to the HTML and add a div element with an id value of container:

```html
<body>
  <div id="container"></div>
  <script type="text/babel">
    ReactDOM.render(
      <h1>Batman</h1>,
      document.body
    );
  </script>
</body>
```
With the container div element safely defined, let’s modify the render method to use it instead of document.body. Here’s one way of doing this:

```html
ReactDOM.render(
  <h1>Batman</h1>,
  document.querySelector("#container")
);
```
Another option is to do some things outside the render method itself:

```html
var destination = document.querySelector("#container");
 
ReactDOM.render(
  <h1>Batman</h1>,
  destination
);
```
Notice that the destination variable stores the reference to your container DOM element. Inside the render method, you simply reference the same destination variable instead of writing the full element-finding syntax as part of the argument itself. The reason for this is simple: I want to show you that you’re still writing JavaScript and that render is just another boring old method that happens to take two arguments.

# Styling It Up!
Right now, our names show up in whatever default h1 styling the browser provides. That’s just terrible, so let’s fix that by adding some CSS. Inside your head tag, let’s add a style block with the following CSS:

```html
<style>
  #container {
    padding: 50px;
    background-color: #EEE;
  }
  #container h1 {
    font-size: 144px;
    font-family: sans-serif;
     color: #0080A8;
  }
</style>
```
This works because, after running all the React code, the DOM’s body contains our container element with an h1 tag inside it. It doesn’t matter that the h1 tag was defined entirely inside JavaScript in this JSX syntax or that your CSS was defined well outside the render method.