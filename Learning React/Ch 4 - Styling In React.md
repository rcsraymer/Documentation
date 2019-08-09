# Displaying Some Vowels

Create a new HTML document that will host your React content:

```html
<!DOCTYPE html>
<html>
 
<head>
  <meta charset="utf-8">
  <title>Styling in React</title>
  <script src="https://unpkg.com/react@16/umd/react.development.js"></script>
  <script src="https://unpkg.com/react-dom@16/umd/react-dom.development.js"></script>
  <script src="https://unpkg.com/babel-standalone@6.15.0/babel.min.js"></script>
 
  <style>
    #container {
      padding: 50px;
      background-color: #FFF;
    }
  </style>
</head>
 
<body>
  <div id="container"></div>
 
</body>
 
</html>
```

To display the vowels, you'll need to add React specific code below the container div element:

```html
<script type="text/babel">
  var destination = document.querySelector("#container");
 
  class Letter extends React.Component {
    render() {
      return(
        <div>
          {this.props.children}
        </div>
      );
    }
  }
 
  ReactDOM.render(
    <div>
      <Letter>A</Letter>
      <Letter>E</Letter>
      <Letter>I</Letter>
      <Letter>O</Letter>
      <Letter>U</Letter>
    </div>,
    destination
  );
</script>
```
# Styling Content the React Way
React favors an inline approach for styling content that doesn’t use CSS.

You specify styles inside your component by defining an object whose content is the CSS properties and their values. When you have that object, you assign that object to the JSX elements you want to style by using the style attribute. This will make more sense when you perform these two steps yourself, so let’s apply all of this to style the output of the Letter component.

## Creating a Style Object
Define an object that contains the styles we want to apply:
```javascript
class Letter extends React.Component {
  render() {
    var letterStyle = {
      padding: 10,
      margin: 10,
      backgroundColor: "#FFDE00",
      color: "#333",
      display: "inline-block",
      fontFamily: "monospace",
      fontSize: 32,
      textAlign: "center"
    };
```
We have an object called letterStyle, and the properties inside it are just CSS property names and their value. If you’ve never defined CSS properties in JavaScript (by setting object.style), the formula for converting them into something JavaScript-friendly is pretty simple:

1. Single-word CSS properties (such as padding, margin, and color) remain unchanged.

2. Multiword CSS properties with a dash in them (such as background-color, font-family, and border-radius) are turned into one camel-case word, with the dash removed and the first letter of the second word capitalized. For example, using our example properties, background-color becomes backgroundColor, font-family becomes fontFamily, and border-radius becomes borderRadius.

## Actually Styling Our Content
Now that we have our object containing the styles we want to apply, the rest is easy. Find the element you want to apply the style on and set the style attribute to refer to that object. In our case, that is the div element returned by our Letter component’s render function.

```html
return (
    <div style={letterStyle}>
        {this.props.children}
    </div>
)
```
The object is called letterStyle, so that's what we specify inside the curly brackets to let React know to evaluate the expression.
## Making the Background Color Customizable
We can specify the background color as part of each Letter declaration. We first add a bgcolor attribute and specify colors:
```html
ReactDOM.render(
    <div>
        <Letter bgcolor="#58B3FF">A</Letter>
        <Letter bgcolor="#FF605F">E</Letter>
        <Letter bgcolor="#FFD52E">I</Letter>
        <Letter bgcolor="#49DD8E">O</Letter>
        <Letter bgcolor="#AE99FF">U</Letter>
    </div>,
    destination
);
```
Then in the letterStyle object, set the value of backgroundColor to this.props.bgcolor.
```javascript
var letterStyle = {
    padding: 10,
    margin: 10,
    backgroundColor: this.props.bgcolor,
    color: "#333",
    display: "inline-block",
    fontFamily: "monospace",
    fontSize: 32,
    textAlign: "center"
};
```