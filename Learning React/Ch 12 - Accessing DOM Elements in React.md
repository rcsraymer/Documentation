## The Colorizer Example

Sometimes you want to access properties and methods on an HTML element directly. In our React-colored world, where JSX represents everything that is good and pure about markup, why would you ever want to deal directly with the horribleness that is HTML? As you will find out (if you haven’t already), in many cases, dealing with HTML elements through the JavaScript DOM API directly is easier than fiddling with “the React way” of doing things. To highlight one such situation, take a look at the Colorizer. The Colorizer colorizes the (currently) white square with whatever color you provide it. After you provide a color and submit it, the white square turns whatever color value you provided.
  
```html
<!DOCTYPE html>
<html>
 
<head>
  <meta charset="utf-8">
  <title>The Colorizer!</title>
  <script src="https://unpkg.com/react@16/umd/react.development.js"></script>
  <script src="https://unpkg.com/react-dom@16/umd/react-dom.development.js"></script>
  <script src="https://unpkg.com/babel-standalone@6.15.0/babel.min.js"></script>
 
  <style>
    #container {
      padding: 50px;
      background-color: #FFF;
    }
 
    .colorSquare {
      box-shadow: 0px 0px 25px 0px #333;
      width: 242px;
      height: 242px;
      margin-bottom: 15px;
    }
 
    .colorArea input {
      padding: 10px;
      font-size: 16px;
      border: 2px solid #CCC;
    }
 
    .colorArea button {
      padding: 10px;
      font-size: 16px;
      margin: 10px;
      background-color: #666;
      color: #FFF;
      border: 2px solid #666;
    }
 
    .colorArea button:hover {
      background-color: #111;
      border-color: #111;
      cursor: pointer;
    }
  </style>
</head>
 
<body>
  <div id="container"></div>
  <script type="text/babel">
 
    class Colorizer extends React.Component {
      constructor(props) {
        super(props);
 
        this.state = {
          color: "",
          bgColor: "white"
        };
 
        this.colorValue = this.colorValue.bind(this);
        this.setNewColor = this.setNewColor.bind(this);
      }
 
      colorValue(e) {
        this.setState({
          color: e.target.value
        });
      }
 
      setNewColor(e) {
        this.setState({
          bgColor: this.state.color
        });
 
        e.preventDefault();
      }
 
      render() {
        var squareStyle = {
          backgroundColor: this.state.bgColor
        };
 
        return (
          <div className="colorArea">
            <div style={squareStyle} className="colorSquare"></div>
 
            <form onSubmit={this.setNewColor}>
              <input onChange={this.colorValue}
                placeholder="Enter a color value"></input>
              <button type="submit">go</button>
            </form>
          </div>
        );
      }
    }
 
    ReactDOM.render(
      <div>
        <Colorizer />
      </div>,
      document.querySelector("#container")
    );
  </script>
</body>
 
</html>

```

## Meet REFs
As you know very well by now, inside our various render methods we’ve been writing HTML-like things known as JSX. Our JSX is simply a description of what the DOM should look like. It doesn’t represent actual HTML, despite looking a whole lot like it. To provide a bridge between JSX and the final HTML elements in the DOM, React provides us with something funnily named as refs (short for references).
  
Inside the render method, we are returning a big chunk of JSX representing (among other things) the input element where we enter our color value. We want to access the input element’s DOM representation so that we can call some APIs on it using JavaScript.
  
The way we do that using refs is by setting the *ref* attribute on the element whose HTML we want to reference:
```javascript
render() {
  var squareStyle = {
    backgroundColor: this.state.bgColor
  };
 
  return (
    <div className="colorArea">
      <div style={squareStyle} className="colorSquare"></div>
 
      <form onSubmit={this.setNewColor}>
        <input onChange={this.colorValue}
               ref={}
               placeholder="Enter a color value"></input>
        <button type="submit">go</button>
      </form>
    </div>
  );
}
```
Because we’re interested in the input element, our ref attribute is attached to it. Right now, our ref attribute is empty. What you typically set as the ref attribute’s value is a JavaScript callback function. This function gets called automatically when the component housing this render method gets mounted. If we set our ref attribute’s value to a simple JavaScript function that stores a reference to the referenced DOM element, it would look something like the following lines:

```javascript
render() {
  var squareStyle = {
    backgroundColor: this.state.bgColor
  };
  // new line below
  var self = this;
 
  return (
    <div className="colorArea">
      <div style={squareStyle} className="colorSquare"></div>
 
      <form onSubmit={this.setNewColor}>
        <input onChange={this.colorValue}
               ref={
                 function(el) {
                   self._input = el;
                 }
               }
               placeholder="Enter a color value"></input>
        <button type="submit">go</button>
      </form>
    </div>
  );
}
```
The end result of this code running once our component mounts is simple: We can access the HTML representing our input element from anywhere inside our component by using self._input. 
  
First, our callback function looks as follows:
```javascript
function(el) {
 self._input = el;
}
```
This anonymous function gets called when our component mounts, and a reference to the final HTML DOM element is passed in as an argument. We capture this argument using the el identifier, but you can use any name for this argument that you want. The body of this callback function simply sets a custom property called _input to the value of our DOM element. To ensure that we create this property on our component, we use the self variable to create a closure—the this in question refers to our component instead of the callback function itself. Phew!

Let’s focus on what we can do now that we have access to our input element. Our goal is to clear the contents of our input element and give focus to it once the form gets submitted. The code for doing that will live in our setNewColor method, so add the following lines:

```javascript
setNewColor(e) {
    ...

    this._input.focus();
    this._input.value = "";

    e.preventDefault();
}
```

Calling this._input.value = "" clears the color we entered. We set focus back to our input element by calling this._input.focus(). All our ref-related work was to simply enable these two lines; we needed some way to have this._input point to the HTML element representing our input element that we defined in JSX. Then we can just call the value property and focus method that the DOM API exposes on this element.

## Simplifying Further with ES6 Arrow Functions

When it comes to working with the ref attribute, using arrow functions to deal with the callback function simplifies matters a bit. This is one of those cases for which I recommend you use an ES6 technique.

When we assigned a property on our component to the referenced HTML element we had to deal with context shenanigans. So, we created a *self* variable initialized to *this*, to ensure that we created the *_input* property on our component. That seems unnecessarily messy.

Using arrow functions, we can simplify it down to the following:

```javascript
<input
     ref={
           (el) => this._input = el
         }>
 </input>
```

## Using Portals

You need to be aware of one more DOM-related trick. So far, we’ve been dealing with HTML only in the context of what our JSX generates, either from a single component or combined through many components. This means we’re limited by the DOM hierarchy our parent components impose on us. Having arbitrary access to any DOM element anywhere on the page doesn’t seem possible. Or is it? As it turns out, you can choose to render your JSX to any DOM element anywhere on the page; you aren’t limited to just sending your JSX to a parent component. The magic behind this wizardry is a feature known as portals.

The way we use a portal is very similar to what we do with our ReactDOM.render method. We specify the JSX we want to render, and we specify the DOM element we want to render to. To see all of this in action, go back to our example and add the following h1 element as a sibling just above where we have our container div element defined:

```html
<body>
 
  <h1 id="colorHeading">Colorizer</h1>
 
  <div id="container"></div>
```

Next add the following within our style tag:

```html
#colorHeading {
  padding: 0;
  margin: 50px;
  margin-bottom: -20px;
  font-family: sans-serif;
}
```
We want to change the value of our h1 element to display the name of the color we are currently previewing. The point to emphasize is that our h1 element is a sibling of the container div element where our app is set to render into.

To accomplish what we’re trying to do, go back to our Colorizer component’s render method and add the following highlighted line to the return statement, after the form onSubmit element:

```javascript
    <ColorLabel color={this.state.bgColor}/>
```

Here we’re instantiating a component called ColorLabel and declaring a prop called color with its value set to our bgColor state property. We haven’t created this component yet, so to fix that, add the following lines just above where we have our ReactDOM.render call:

```javascript
var heading = document.querySelector("#colorHeading");
 
class ColorLabel extends React.Component {
  render() {
    return ReactDOM.createPortal(
      ": " + this.props.color,
      heading
    );
  }
}
```
We are referencing our h1 element with the heading variable. That’s old stuff. For the new stuff, take a look at our ColorLabel component’s render method. More specifically, notice what our return statement looks like. We are returning the result of calling ReactDOM.createPortal():. The ReactDOM.createPortal() method takes two arguments: the JSX to print and the DOM element to print that JSX to. The JSX we are printing is just some formatting characters and the color value we passed in as a prop. The DOM element we are printing all of this to is our h1 element referenced by the heading variable.



