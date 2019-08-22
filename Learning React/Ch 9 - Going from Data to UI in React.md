## Bridging the Gulf Between Your Data and UI
When you’re building your apps, thinking in terms of props, state, components, JSX tags, render methods, and other React-isms might be the last thing on your mind. Most of the time, you’re dealing with data in the form of JSON objects, arrays, and other data structures that have no knowledge (or interest) in React or anything visual.
  
Create a new HTML doc:
```html
<!DOCTYPE html>
<html>
 
<head>
  <meta charset="utf-8">
  <title>From Data to UI</title>
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
    var destination = document.querySelector("#container");

    class Circle extends React.Component {
      render() {
        var circleStyle = {
          padding: 10,
          margin: 20,
          display: "inline-block",
          backgroundColor: this.props.bgColor,
          borderRadius: "50%",
          width: 100,
          height: 100,
        };
 
        return (
          <div style={circleStyle}>
          </div>
        );
      }
    }
 
    ReactDOM.render(
      <div>
        <Circle bgColor="#F9C240" />
      </div>,
      document.querySelector("#container");
    );
  </script>
</body>
 
</html>
```
You should now see a yellow circle in your html.

## Your JSX Can Be Anywhere, Part II
As we learned before, JSX can live outside of a render function so you can store your bgColor in a var like this:

```javascript
var theCircle = <Circle bgColor="#F9C240" />;
 
ReactDOM.render(
  <div>
    {theCircle}
  </div>,
  destination
);
```
You can also create a function that returns a Circle component:
```javascript
function showCircle() {
  var colors = ["#393E41", "#E94F37", "#1C89BF", "#A1D363"];
  var ran = Math.floor(Math.random() * colors.length);

  //  return a Circle with a randomly chosen color
  return <Circle bgColor={colors[ran]} />;
}

ReactDOM.render(
  <div>
    {showCircle()}
  </div>,
  destination
);
```
## Dealing With Arrays
When displaying multiple components, you can't always manually specify them. In most real-world scenarios, the number of components you display is related to the number of items in an array or iterator object you're working with. Suppose we have an array called colors:

```javascript
var colors = ["#393E41", "#E94F37", "#1C89BF", "#A1D363",
              "#85FFC7", "#297373", "#FF8552", "#A40E4C"];
```
We want to create a Circle component for each item in this array (and set the bgColor prop to the value of each array item). We can do this by creating an array of Circle components:

```javascript
var colors ...

var renderData = [];

for (var i = 0; i < colors.length; i++) {
  renderData.push(<Circle bgColor={colors[i]} />);
}

ReactDOM.render(
  <div>
    {renderData}
  ...
```
React makes UI updates really fast by having a good idea of what exactly is going on in your DOM. It does this in several ways, but one really noticeable way is by internally marking each element with some sort of an identifier.
  
When you create elements dynamically (such as what we’re doing with our array of Circle components), these identifiers are not automatically set. We need to do some extra work. That extra work takes the form of a key prop whose value React uses to uniquely identify each particular component.
  
To your for loop above, you can change your renderData method to this:

```javascript
    renderData.push(<Circle key={i + colors} bgColor={colors[i]} />);
```
On each component, we specify our key prop and set its value to a combination of color and index position inside the colors array. This ensures that each component we dynamically create ends up getting a unique identifier that React can then use to optimize any future UI updates.

