## Events in React
In most apps, especially the kind of UI-heavy ones you’ll be building, the app will do a ton of things only as a reaction to something. Those somethings could be triggered by a mouse click, a key press, a window resize, or a whole bunch of other gestures and interactions. Events are the glue that makes all of this possible.

To show how this works, we will create an example that hosts a counter that increments each time you click a button.

## Starting Point
```html
<!DOCTYPE html>
<html>
 
<head>
  <meta charset="utf-8">
  <title>Events</title>
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
  <script type="text/babel">
 
  </script>
</body>
 
</html>
```

Now we will add our partially implemented counter example. Add this inside of the script tag below the container div:

```javascript
class Counter extends React.Component {
  render() {
    var textStyle = {
      fontSize: 72,
      fontFamily: "sans-serif",
      color: "#333",
      fontWeight: "bold"
    };
 
    return (
      <div style={textStyle}>
        {this.props.display}
      </div>
    );
  }
}
 
class CounterParent extends React.Component {
  constructor(props) {
    super(props);
 
    this.state = {
      count: 0
    };
  }
 
  render() {
    var backgroundStyle = {
      padding: 50,
      backgroundColor: "#FFC53A",
      width: 250,
      height: 100,
      borderRadius: 10,
      textAlign: "center"
    };
    var buttonStyle = {
      fontSize: "1em",
      width: 30,
      height: 30,
      fontFamily: "sans-serif",
      color: "#333",
      fontWeight: "bold",
      lineHeight: "3px"
    };
 
    return (
      <div style={backgroundStyle}>
        <Counter display={this.state.count} />
        <button style={buttonStyle}>+</button>
      </div>
    );
  }
}
 
ReactDOM.render(
  <div>
    <CounterParent />
  </div>,
  document.querySelector("#container")
);
```

## Making the Button Click Do Something
Each time we click the plus button, we want the value of our counter to increase by 1. What we need to do roughly looks like this:

1. Listen for the click event on the button.

2. Implement the event handler so that we react to the click and increase the value of our this.state.count property that our counter relies on.

In React, you listen to an event by specifying everything inline in your JSX itself. More specifically, you specify inside your markup both the event you’re listening for and the event handler that will get called. To do this, find the return function inside our CounterParent component and make the following highlighted change:

```javascript
return (
  <div style={backgroundStyle}>
    <Counter display={this.state.count}/>
    <button onClick={this.increase} style={buttonStyle}>+</button>
  </div>
);
```
Next, let’s go ahead and implement the increase function (a.k.a. our event handler). Inside our CounterParent component, add the following highlighted lines:

```javascript
    this.state = {
      count: 0
    };
 
    this.increase = this.increase.bind(this);
  }
 
  increase(e) {
    this.setState({
      count: this.state.count + 1
    });
  }
 
  render() {
      ...
```

All we’re doing with these lines is making sure that each call to the increase function increments the value of our this.state.count property by 1. Because we’re dealing with events, our increase function (as the designated event handler) will get access to any event arguments. We’ve set these arguments to be accessed by e, and you can see that by looking at our increase function’s signature (that is, what its declaration looks like). We’ll talk about the various events and their properties in a little bit when we take a detailed look at Events. Lastly, in the constructor, we bind the value of this to the increase function.

## Meet Synthetic Events
In React, when you specify an event in JSX as we did with onClick, you’re not directly dealing with regular DOM events. Instead, you’re dealing with a React-specific event type known as a SyntheticEvent. Your event handlers don’t get native event arguments of type MouseEvent, KeyboardEvent, and so on. They always get event arguments of type SyntheticEvent that wrap your browser’s native event instead.
  
Each SyntheticEvent contains the following properties:  

    boolean bubbles  
    boolean cancelable  
    DOMEventTarget currentTarget  
    boolean defaultPrevented  
    number eventPhase  
    boolean isTrusted  
    DOMEvent nativeEvent  
    void preventDefault()  
    boolean isDefaultPrevented()  
    void stopPropagation()  
    boolean isPropagationStopped()  
    DOMEventTarget target  
    number timeStamp  
    string type  

SyntheticEvent that wraps a MouseEvent will have access to mouse-specific properties such as the following:

    boolean altKey  
    number button  
    number buttons  
    number clientX  
    number clientY  
    boolean ctrlKey  
    boolean getModifierState(key)  
    boolean metaKey  
    number pageX  
    number pageY  
    DOMEventTarget relatedTarget  
    number screenX  
    number screenY  
    boolean shiftKey  

A SyntheticEvent that wraps a KeyboardEvent will have access to these additional keyboard-related properties:

    boolean altKey  
    number charCode  
    boolean ctrlKey  
    boolean getModifierState(key)  
    string key  
    number keyCode  
    string locale  
    number location  
    boolean metaKey  
    boolean repeat  
    boolean shiftKey  
    number which  

## Doing Stuff With Event Properties
We want to increment our counter by 10 when the Shift key on the keyboard is pressed while clicking the plus button with our mouse.  

We can do that by using the shiftKey property  that exists on the SyntheticEvent when using the mouse:

    boolean shiftKey

The way this property works is simple. If the Shift key is pressed when this mouse event fires, then the shiftKey property value is true. Otherwise, the shiftKey property value is false. To increment our counter by 10 when the Shift key is pressed, go back to our increase function and make the following highlighted changes:

```javascript
increase(e) {
  var currentCount = this.state.count;
 
  if (e.shiftKey) {
    currentCount += 10;
  } else {
    currentCount += 1;
  }
 
  this.setState({
    count: currentCount
  });
}
```
