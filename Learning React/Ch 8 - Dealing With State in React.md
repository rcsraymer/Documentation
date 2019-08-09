# Using State
Your properties are considered immutable once they’ve been set. For many interactive scenarios, you don’t want that. You want to be able to change aspects of your components as a result of some user interaction (or some data getting returned from a server or a billion other things).

Create a new html file:
```html
<!DOCTYPE html>
<html>
 
<head>
  <meta charset="utf-8">
  <title>Dealing with State</title>
  <script src="https://unpkg.com/react@16/umd/react.development.js"></script>
  <script src="https://unpkg.com/react-dom@16/umd/react-dom.development.js"></script>
  <script src="https://unpkg.com/babel-standalone@6.15.0/babel.min.js"></script>
</head>
 
<body>
  <div id="container"></div>
 
  <script type="text/babel">
    class LightningCounter extends React.Component {
      render() {
        return (
          <h1>Hello!</h1>
        );
      }
    }
 
    class LightningCounterDisplay extends React.Component {
      render() {
        var divStyle = {
          width: 250,
          textAlign: "center",
          backgroundColor: "black",
          padding: 40,
          fontFamily: "sans-serif",
          color: "#999",
          borderRadius: 10
        };
 
        return (
          <div style={divStyle}>
            <LightningCounter/>
          </div>
        );
      }
    }
 
    ReactDOM.render(
      <LightningCounterDisplay/>,
      document.querySelector("#container")
    );
  </script>
</body>
 
</html>
```

Now let’s take a few minutes to look at what our existing code does. First, we have a component called LightningCounterDisplay. The bulk of this component is the divStyle object, which contains the styling information responsible for the cool rounded background. The return function returns a div element that wraps the LightningCounter component. 
  
The last thing to look at is our ReactDOM.render method. It just pushes the LightningCounterDisplay component to our container element in our DOM. That’s pretty much it. The end result is the combination of markup from our ReactDOM.render method and the LightningCounterDisplay and LightningCounter components.

## Getting Our Counter On
We’re going to be using a setInterval function that calls some code every 1000 milliseconds (a.k.a. 1 second). That “some code” is going to increment a value by 100 each time it’s called.
  
To make this all work, we’re relying on three APIs that our React component exposes:
  
1) componentDidMount

This method gets called just after our component gets rendered (or mounted, as React calls it).

2) setState

This method allows you to update the value of the state object.

## Setting the Initial State Value

Instead of creating a variable, we want to create a state object, make a strikes variable a property of it, and ensure that we set all of this up when our component is getting created. The component we want to do all this to is LightningCounter.

```javascript
class LightningCounter extends React.Component {
  constructor(props) {
    super(props);
 
    this.state = {
      strikes: 0
    };
  }
 
  ...
```
We specify our state object inside our LightningCounter component’s constructor. This runs way before your component gets rendered. We’re telling React to set an object containing our strikes property (initialized to 0).


Let’s visualize our strikes property. In our render method, make the following highlighted change:

```javascript
      render() {
        return (
          <h1>{this.state.strikes}</h1>
        );
      }
    }
```
## Setting Our Timer and Setting State
We will now be getting our timer going and incrementing our strikes property. We will use the setInterval function to increase the strikes property by 100 every second. We are going to do all of this immediately after our component has been rendered using the built-in componentDidMount method.

Additionally, you'll need to explicitly bind the timerTick function to our component.  


```javascript
    class LightningCounter extends React.Component {
        constructor(props) {
            super(props);

            this.state = {
                strikes: 0
            };

            this.timerTick = this.timerTick.bind(this);
        }    
    
    timerTick() {
        this.setState({
            strikes: this.state.strikes + 100
        });
    }

    componentDidMount() {
        setInterval(this.timerTick, 1000);
    }

    render() {
        ...
    }
}
```


