## Managing React State with Redux
The way Redux plugs into your React app is as straightforward as calling a few Redux APIs from your React code. Just two steps are involved:

1. Give your app a reference to the Redux store.

2. Map the action creators, dispatch functions, and state as props to whatever component needs data from the Store.

## Our Counter App
We will make a simple counter app that will have a plus button and a minus button to increase or decrease a counter value.

## Integration
1. The first step of providing access to our Redux store is handled by the Provider component.

2. The second step of granting any interested components access to our dispatch and actions is handled by the Connect component.

ReactDOM.render
      |
   Provider -> Store
      |
     App
      |
   Connect -> Dispatches & Actions
      |                 |
   Counter <------------|

%he Provider component is the gateway to getting Redux functionality in our React app. It is responsible for storing a reference to the Store and ensuring that all components in our app have a way of accessing it. It is able to do that by being the top-most component in your component hierarchy.

The Connect component is a bit more interesting. It isn’t a full-blown component in the traditional sense. It’s known as a Higher Order Component (https://reactjs.org/docs/higher-order-components.html), or HOC, as the cool kids say it. HOCs provide a consistent way to extend the functionality of a preexisting component by simply wrapping it and injecting their own additional functionality into it. Think of this as the React-friendly way to mimic what the extends keyword does when working with ES6 classes. Looking at our diagram, the end result is that, thanks to the Connect HOC, our Counter component has access to any actions and dispatch calls needed to work with the Redux Store, without you having to write any special code to access it. The Connect HOC takes care of that.

## Getting Started

```console
create-react-app reduxcounter
npm install redux
npm install react-redux
```

## Building the App
Delete all files from src and public folders. Create public\index.html:

```html
<!DOCTYPE html>
<html>
 
<head>
  <title>Redux Counter</title>
</head>
 
<body>
  <div id="container">
 
  </div>
</body>
 
</html>
```

Now create src\index.js:

```javascript
import React, { Component } from "react";
import ReactDOM from "react-dom";
import { createStore } from "redux";
import { Provider } from "react-redux";
import counter from "./reducer";
import App from "./App";
import "./index.css";
 
var destination = document.querySelector("#container");
 
// Store
var store = createStore(counter);
 
ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  destination
);
```

We’re first initializing our Redux store and using our trustworthy createStore method that takes a reducer at its argument. Our reducer is referenced by the counter variable, and if you look at our import statements, it is defined in a file called reducer.js. We’ll deal with that in a few moments.

After creating our Store, we provide it as a prop to our Provider component. The Provider component is intended to be used as the outermost component in our app, to help ensure that every component has access to the Redux Store and related functionality.

Next, let’s create our reducer. You already saw that our reducer is referenced by the counter variable and lives inside a file called reducer.js—which doesn’t exist. Let’s fix that by first creating a file called reducer.js in the src folder.

```javascript
// Reducer
function counter(state, action) {
  if (state === undefined) {
    return { count: 0 };
  }
 
  var count = state.count;
 
  switch (action.type) {
    case "increase":
      return { count: count + 1 };
    case "decrease":
      return { count: count - 1 };
    default:
      return state;
  }
}
 
export default counter;
```

Our reducer is pretty simple. We have a count variable that we initialize to 0 if our state is empty. This reducer will deal with two action types: increase and decrease. If the action type is increase, we up our count value by 1. If our action type is decrease, we decrease our count value by 1 instead.

Inside the src folder, create a new file called App.js. Inside, add the following:

```javascript
import { connect } from "react-redux";
import Counter from "./Counter";
 
// Map Redux state to component props
function mapStateToProps(state) {
  return {
    countValue: state.count;
  };
}
 
// Action
var increaseAction = { type: "increase" };
var decreaseAction = { type: "decrease" };
 
// Map Redux actions to component props
function mapDispatchToProps(dispatch) {
  return {
    increaseCount: function() {
      return dispatch(increaseAction);
    },
    decreaseCount: function() {
      return dispatch(decreaseAction);
    }
  };
}
 
// The HOC
var connectedComponent = connect(
  mapStateToProps,
  mapDispatchToProps
)(Counter);
 
export default connectedComponent;
```

The main purpose of the code here is to turn all the Redux-specific hooks into something we can use in React. More specifically, we provide all those hooks as props that our component can easily consume through two functions, called mapStateToProps and mapDispatchToProps.

First up is our mapStateToProps function:

This function subscribes to all Store updates and gets called when anything in our Store changes. It returns an object that contains the Store data you want to transmit as props to a component. In our case, what we’re transmitting is pretty simple: an object that contains a property called countValue whose value is represented by our old count property from the Store.

Providing the Store value as props is only one part of what we need to do. The next part is to give our component access to the action creators and actions, also in the form of props. 

The really interesting stuff happens with mapDispatchToProps. We return an object containing the name of the two functions our component can call to dispatch a change to our Store. The increaseCount function fires off a dispatch with an action type of increase. The decreaseCount function fires off a dispatch with an action type of decrease. If you look at the reducer we added a few moments ago, you can see how either of these function calls will affect the value of count we’re storing in our Store.

All that remains now is to ensure that whatever component we want to provide all these props to has some way of actually receiving them. That is where the magical connect function comes in.

This function creates the magical Connect HOC we talked about earlier. It takes our mapStateToProps and mapDispatchToProps functions as arguments, and it passes all of that into the Counter component, which you also specify. 

Our Counter component gets access to increaseCount, decreaseCount, and countValue. The only strange thing is that there’s no render function or equivalent in sight. All of that is handled automatically by React and its treatment of HOC.

We’re almost done! It’s time to get our Counter component up and running. In your src directory, add a file called Counter.js. Put the following into it:

```javascript
import React, { Component } from "react";
 
class Counter extends Component {
  render() {
    return (
      <div className="container">
        <button className="buttons"
                onClick={this.props.decreaseCount}>-</button>
        <span>{this.props.countValue}</span>
        <button className="buttons"
                onClick={this.props.increaseCount}>+</button>
      </div>
    );
  }
}
 
export default Counter;
```

This will probably be the most boring component you’ve seen in quite some time. We’ve already talked about how our Connect HOC sends down props and other related shenanigans to our Counter component. You can see those props in use here to display the counter value or call the appropriate function when our plus or minus buttons are clicked.

The last thing we need to do is define our CSS file to style our counter. In the same src folder we’ve been working in all this time, create a file called index.css. Inside this file, add the following style rules:

```css
body {
  margin: 0;
  padding: 0;
  font-family: sans-serif;
  display: flex;
  justify-content: center;
  background-color: #8E7C93;
}
 
.container {
  background-color: #FFF;
  margin: 100px;
  padding: 10px;
  border-radius: 3px;
  width: 200px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
 
.buttons {
  background-color: transparent;
  border: none;
  font-size: 16px;
  font-weight: bold;
  border-radius: 3px;
  transition: all .15s ease-in;
}
 
.buttons:hover:nth-child(1) {
  background-color: #F45B69;
}
 
.buttons:hover:nth-child(3) {
  background-color: #C0DFA1;
}
```