## What is Redux?
Maintaining application state and keeping it consistent with our UI is a major challenge. Solving this is partly why libraries such as React really took off. If you cast a wider net and look beyond just the UI layer, you’ll see that maintaining application state in general is complicated. The typical app has many layers, and each layer has its own dependency on some piece of data that it relies on to do its thing.

To solve this more general problem of maintaining application state, you have Redux. The easiest way to understand how Redux works is just to walk through the various pieces that go into it. The first thing we need is an app.

This app doesn’t have to be anything special. It can be built in React, Angular, Vue, vanilla JS, or whatever happens to be the hot new library or framework this week. Redux doesn’t care how your app is built. It only cares that your app has a magical way for dealing with application state and storing it. In the Redux world, we store all our application state in a single location that we’ll just call the Store.

The thing about the Store is that reading data from it is easy. Getting information into it is a whole another story. You add a new state to (or modify existing state in) the Store by using a combination of actions, which describe what to change, and a reducer, which determines what the final state will be as a result for a given action. 

App -> Action -> Reducer -> Store -> App

Beyond just ease, Redux helps make maintaining your application state predictable.

1. Your entire application’s state is stored in a single location. You don’t have to search across a variety of data stores to find the part of your state you want to update. Keeping everything stored in a single location also ensures that you don’t have to worry about keeping all of this data in sync.

2. Your state should be read-only and can be modified only through actions. As you saw in the diagram earlier, in a Redux world, you need to ensure that random parts of your app can’t access the Store and modify the state stored inside it. The only way our app can modify what is in the Store is by relying on actions.

3. You specify what the final state should be. To keep things simple, your state is never modified or mutated. You use a reducer to specify what the final result of your state should be.

## Building A Simple App Using Redux
The app we’re building to highlight how Redux works will be a really simple console-driven app without any UI. This app will store and display a list of favorite colors. From our app, you’ll be able to add colors and remove colors. That’s pretty much it.

This might seem like a step backward from the UI-rich apps we’ve been building, but this app will tie together all this theoretical Redux knowledge to produce some tangible lines of code. The goal is to simply make sense of Redux. We’ll complicate our world by combining Redux with some UI later.

## Redux Time
Create just a basic loose HTML file. Create favoriteColors.html:

```html
<!DOCTYPE html>
<html>
 
<head>
  <title>Favorite Colors!</title>
  <script src="https://unpkg.com/redux@latest/dist/redux.js"></script>
</head>
 
<body>
  <script>
 
  </script>
</body>
 
</html>
```

## Lights! Camera! Action!
With our Redux library referenced, we need to define our actions. Remember, the action is the only mechanism we have to communicate with our Store. For our app, because we want to add and remove colors, our actions will represent that want in a way the Store will understand.

Inside your script tag, add the following lines:

```javascript
function addColor(value) {
  return {
    type: "ADD",
    color: value
  };
}
 
function removeColor(value) {
  return {
    type: "REMOVE",
    color: value
  };
}
```

We have two functions, addColor and removeColor. They each take one argument and return an action object as a result. For addColor, the action object is the two lines:

```javascript
    type: "ADD",
    color: value
```
Let’s get back to our addColor and removeColor functions. Both really serve just one purpose: to return an action. There’s a more formal name for these functions in the Redux world. They’re known as action creators because they, um, create an action.

## Our Reducer
Our actions define what we want to do, but the reducer handles the specifics of what happens and how our new state is defined. You can think of the reducer as the intermediary between the Store and the outside world, where it does the following three things:

1. Provides access to the Store’s original state

2. Allows you to inspect the action that was currently fired

3. Allows you to set the Store’s new state

You can see all this when you add a reducer to deal with adding and removing colors from the Store. Add the following code after the point where you’ve defined your action creators:

```javascript
function favoriteColors(state, action) {
  if (state === undefined) {
    state = [];
  }

  if (action.type === "ADD") {
    return state.concat(action.color);
  } else if (action.type === "REMOVE") {
    return state.filter(function(item) {
      return item !== action.color;
    });
  } else {
    return state;
  }
}
```

Things you should never do inside a reducer:

1. Mutate its arguments

2. Perform side effects like API calls and routing transitions

3. Call non-pure functions, e.g. Date.now() or Math.random()

Given the same arguments, it should calculate the next state and return it. No surprises. No side effects. No API calls. No mutations. Just a calculation.

You can see this in our code. To add new color values to our state array, we used the concat method, which returns an entirely new array made up of both the old values and the new value we’re adding. Using push would give us the same end result, but it violates our goal of not modifying the existing state. To remove color values, we continue to maintain our goal of not modifying our current state. We use the filter method, which returns a brand new array with the value we want to remove omitted.

## Store Stuff
All that remains now is to tie our actions and the reducer with our Store. First we have to actually create the Store. Below your favoriteColors reducer function, add the following:

```javascript
var store = Redux.createStore(favoriteColors);
```

Here we’re creating a new Store using the createStore method. The argument we provide is the favoriteColors reducer we created a few moments ago. We’ve now come full circle in using Redux to store application state. We have our store, we have our reducer, and we have actions that tell our reducer what to do.

To see everything fully working, we’re going to add (and remove) some colors to the Store. To do this, we use the dispatch method on our store object that takes an action as its argument. Go ahead and add the following lines:

```javascript
store.dispatch(addColor("blue"));
store.dispatch(addColor("yellow"));
store.dispatch(addColor("green"));
store.dispatch(addColor("red"));
store.dispatch(addColor("gray"));
store.dispatch(addColor("orange"));
store.dispatch(removeColor("gray"));
```

Each dispatch call sends an action to our reducer. The reducer takes the action and performs the appropriate work to define our new state. To see the Store’s current state, you can just add the following after all the dispatch calls:


```javascript
console.log(store.getState());
```

We’re almost done here; We have just one more really important thing to cover. In real-world scenarios, you want to be notified each time your application’s state is modified. This push model will make your life much easier if you want to update UI or perform other tasks as a result of some change to the Store. To accomplish this, you have the subscribe method for specifying a function (a.k.a. a listener) that gets called each time the contents of the Store are modified. To see the subscribe method in action, just after you defined the store object, add the following lines:

```javascript
var store = Redux.createStore(favoriteColors);
store.subscribe(render);

function render() {
  console.log(store.getState());
}
```

After you’ve done this, preview your app again. This time, whenever you call dispatch to fire another action, the render function gets called when the Store is modified.