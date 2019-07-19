# COMPONENTS
Almost every part of an app’s visuals would be wrapped inside a self-contained module known as a **component**. 

# QUICK REVIEW OF FUNCTIONS
In JavaScript, you have functions that enable you to make your code a bit cleaner and more reusable. Now, there’s reason we’re taking some time to look at functions, and it isn’t to annoy you! Conceptually, functions share a lot of surface area with React components, and the easiest way to understand what components do is to take a quick look at functions first.

In a terrible world where functions don’t exist, you might have some code that looks as follows:

```javascript
var speed = 10;
var time = 5;
alert(speed * time);
 
var speed1 = 85;
var time1 = 1.5;
alert(speed1 * time1);
 
var speed2 = 12;
var time2 = 9;
alert(speed2 * time2);
 
var speed3 = 42;
var time3 = 21;
alert(speed3 * time3);
```

In a really chill world that involves functions, you can condense all that duplicated text into something simple, like the following:

```javascript
function getDistance(speed, time) {
  var result = speed * time;
  alert(result);
}
```
To call this function, all you have to do is this:

```javascript
getDistance(10, 5);
getDistance(85, 1.5);
```

Functions provide another great value, too. Your functions (such as the alert inside getDistance) can call other functions as part of their running. Take a look at using a formatDistance function to change what getDistance returns:

```javascript
function formatDistance(distance) {
  return distance + " km";
}
 
function getDistance(speed, time) {
  var result = speed * time;
  alert(formatDistance(result));
}
```
# CHANGING HOW WE DEAL WITH UI
If we were to decide to add more superheroes to the html we've already created, style it differently, and wrap that in a div, we would have a much more complicated and cluttered code block. See below:

```html
ReactDOM.render(
  <div>
    <h3><i>Batman</i></h3>
    <h3><i>Iron Man</i></h3>
    <h3><i>Nicolas Cage</i></h3>
    <h3><i>Mega Man</i></h3>
  </div>,
  destination
);
```
In doing this, we have violated the DRY principle. 
  
Components will help cut down on the repetitive and time consuming nature of modifying existing html.

# MEET THE REACT COMPONENT

React components are reusable chunks of JavaScript that output (via JSX) HTML elements. That sounds really pedestrian for something capable of solving great things, but as you start to build components and gradually turn up the complexity, you’ll see that components are really powerful and every bit as awesome as I’ve portrayed them.

Let’s start by building a couple of components together. To follow along, start with a blank React document:

```html
<!DOCTYPE html>
<html>
 
<head>
  <meta charset="utf-8">
  <title>React Components</title>
  <script src="https://unpkg.com/react@16/umd/react.development.js"></script>
  <script src="https://unpkg.com/react-dom@16/umd/react-dom.development.js"></script>
  <script src="https://unpkg.com/babel-standalone@6.15.0/babel.min.js"></script>
</head>
 
<body>
  <div id="container"></div>
  <script type="text/babel">
 
  </script>
</body>
 
</html>
```
Nothing exciting is going on in this page. As in the last chapter, this page is pretty barebones, with just a reference to the React and Babel libraries and a div element that proudly sports an id value of container.

# CREATING A HELLO, WORLD! COMPONENT
We want to use a component to help us print the famous “Hello, world!” text to the screen. As we already know, using just the render method of ReactDOM would give us code that looks as follows:

```html
ReactDOM.render(
    <div>
        <p>Hello, world!</p>
    </div>,
    document.querySelector("#container")
);
```

Let's re-create this by using a componenet. There are several ways to create a component, but we are going to use the class syntax. Add the following code just above the existing render method.

```javascript
class HelloWorld extends React.Component {
    render() {
        return <p>Hello, componentized world!</p>
    }
}
```
You’ve told the render function to return the JSX that represents the Hello, componentized world! text. All that remains is to actually use this component. You use a component after you’ve defined it by calling it. Here we call it from our old friend, the ReactDOM.render method.

```html
ReactDOM.render(
  <HelloWorld/>,
  document.querySelector("#container")
);
```
Think of your <HelloWorld/> component as a cool and new HTML tag whose functionality you fully have control over. This means you can do all sorts of HTML-y things to it.

For example, go ahead and modify our ReactDOM.render method to look as follows:
```html
ReactDOM.render(
  <div>
    <HelloWorld/>
  </div>,
  document.querySelector("#container")
);
```
