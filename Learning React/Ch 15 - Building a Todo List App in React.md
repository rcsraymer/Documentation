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
Right now, our app doesn’t do a whole lot. It doesn’t look like much, either. We’ll deal with the functionality in a little bit, but first let’s get the various UI elements up and running. That isn’t very complicated for our app. First we’ll get our input field and button to appear. This is all done by using the div, form, input, and button elements.

All of that will live inside a component we’ll call TodoList. In your src folder, add a file called TodoList.js. Inside this file, add the following:

```javascript
import React, { Component } from "react";
 
class TodoList extends Component {
  render() {
    return (
      <div className="todoListMain">
        <div className="header">
          <form>
            <input placeholder="enter task">
            </input>
            <button type="submit">add</button>
          </form>
        </div>
      </div>
    );
  }
}
 
export default TodoList;
```

You can see a bunch of JSX that gets the form elements up and running. To use the newly created TodoList component, let’s go back to index.js and reference it to see how our app looks now. Go ahead and make the following two changes:

```javascript
...
import TodoList from "./TodoList";
...
ReactDOM.render(
  <div>
    <TodoList/>
...
```

## Building the Rest of the App
As you can imagine, getting the initial UI elements to show up is the easy part. Tying up all the visuals with the underlying data is where the real work lies. This work can roughly be divided into five parts:

    1. Adding items

    2. Displaying items

    3. Styling

    4. Removing items

    5. Animating items as they are added or removed

Individually, all of these little implementation details are easy to wrap your brain around. When you put them together, you need to watch out for a few things. We’ll look at all that and more in the following sections.

## Adding Items
The first major task to tackle is setting up the event handlers and default form-handling behavior to allow us to add an item. Go back to the form element and make the following highlighted change:

```javascript
        <div className="header">
          <form onSubmit={this.addItem}>
            <input placeholder="enter task">
```
We listen for the submit event on the form itself, and we call the addItem method when that event is overheard. Notice that we aren’t listening for any event on the button itself. This is because our button has a type attribute set to submit. This is one of those HTML trickeries in which clicking on the button whose type is submit is the equivalent of firing the submit event on the form.

Now it’s time to create our addItem event handler that will get called when our form gets submitted. Add the following highlighted lines just above where we have our render function defined:

```javascript
class TodoList extends Component {
  constructor(props) {
    super(props);

     this.addItem = this.addItem.bind(this);
  }

   addItem(e) {

  }
...
```
All we did was define our addItem event handler and ensure that the keyword resolves properly. We still haven’t done anything remotely close to actually adding a task, so let’s start by first defining our state object in the constructor:

```javascript
constructor(props) {
  super(props);

  this.state = {
    items: []
  }; 

  this.addItem = this.addItem.bind(this);

}
```
We’re just defining an items array/property that will be responsible for storing the various items that you can enter. All that’s left to do now is read the entered value from our input element and store it in our items array when the user submits it. The only complication here is actually reading the value from a DOM element. We will use a loophole via refs.

In our render function, make the following highlighted change:

```javascript
        <form onSubmit={this.addItem}>
          <input ref={(a) => this._inputElement = a}
                 placeholder="enter task">
```

Here we’re storing a reference to our input element in the appropriately named _inputElement property. To state this differently, anywhere inside this component where we want to access our input element, we can do so by accessing _inputElement. Now it’s time to fill out our addItem function with the following content:

```javascript
addItem(e) {
// We create a variable called itemArray to store the current value of our items state object. 
  var itemArray = this.state.items;
  
// Next we check to see if our _inputElement element has any content. If it's empty, we don't do anything.
  if (this._inputElement.value !== "") {

// If our _inputElement has some text entered we add that text to our itemArray. We aren’t just adding the entered text. We’re actually adding an object that contains both the entered text and a unique key value that’s set by the current time (Date.now()). 
    itemArray.unshift({
      text: this._inputElement.value,
      key: Date.now()
    });

// We’re setting our state’s items property to the value of itemArray. We’re clearing the value of our input element to make room for the next todo item.
    this.setState({
      items: itemArray
    });
 
    this._inputElement.value = "";
  }
 
  console.log(itemArray);

// We’re overriding this event’s default behavior. The reason has to do with how form submission works. By default, when you submit a form, the page reloads and clears everything out. We definitely don’t want that. By calling preventDefault, we block the default behavior. 
  e.preventDefault();
}
```

You can check the browser console to see the state object correctly populating with each new todo item that is added.

## Displaying the Items

Having our todo items show up only in the console might be exciting for some of your users, but I’m pretty certain that most probably want to see these items displayed directly on the page. To do this, we’re going to rely on another component. To get started, let’s call this component TodoItems, specify it in our TodoList component’s render method, and pass in our items array as a prop.

```javascript
...
        </form>
      </div>
      <TodoItems entries={this.state.items}/>
    </div>
```

After you’ve done this, add the import statement to the top of the document as well:

```javascript
import React, { Component } from "react";
import TodoItems from "./TodoItems";

class TodoList extends Component {
```

In the src directory, create a new file called TodoItems.js and add the following content into it:

```javascript
import React, { Component } from "react";
 
class TodoItems extends Component {
  constructor(props) {
    super(props);
 
    this.createTasks = this.createTasks.bind(this);
  }
  
  // In our render function, we’re taking the list of todo items (passed in as entries) and turning them into JSX/HTML-ish elements. We do that by calling map on our items and relying on the createTasks function:

  createTasks(item) {
    return <li key={item.key}>{item.text}</li>
  }
  
  // The value stored by our listItems variable is an array of li elements that contain the appropriate content to print. Notice that we’re setting the key attribute—whose value, as you recall, we set earlier using Date.now()—on each element, to make it easier for React to keep track of the elements. We turn this list of elements into something we can show onscreen with the following:

  render() {
    var todoEntries = this.props.entries;
    var listItems = todoEntries.map(this.createTasks);
 
    return (
      <ul className="theList">
        {listItems}
      </ul>
    );
  }
};
 
export default TodoItems;
```

## Styling our App
In the src folder, create a new stylesheet called TodoList.css and add the following style rules into it:

``` css
.todoListMain .header input {
  padding: 10px;
  font-size: 16px;
  border: 2px solid #FFF;
  width: 165px;
}
.todoListMain .header button {
  padding: 10px;
  font-size: 16px;
  margin: 10px;
  margin-right: 0px;
  background-color: #0066FF;
  color: #FFF;
  border: 2px solid #0066FF;
}
.todoListMain .header button:hover {
  background-color: #003399;
  border: 2px solid #003399;
  cursor: pointer;
}
.todoListMain .theList {
  list-style: none;
  padding-left: 0;
  width: 250px;
}
.todoListMain .theList li {
  color: #333;
  background-color: rgba(255,255,255,.5);
  padding: 15px;
  margin-bottom: 15px;
  border-radius: 5px;
}
```

In TodoList.js, add a reference to this stylesheet at the top:

```javascript
import "./TodoList.css";
```

## Removing Items

What we can’t do is remove items after they’ve been added. We’re going to allow users to remove items by clicking on them directly. This seems straightforward to implement, right? The only thing to watch out for involves where to put all our code. The items we click on are defined in TodoItems.js. The actual logic for populating the items lives in our state object in TodoList.js. To give you a preview of what to expect, we will be partaking in some shenanigans as we pass things between both of those components.

First we need to set up the event handler for dealing with the click event. Change the return statement under createTasks to look as follows:

```javascript
createTasks(item) {
  return <li onClick={() => this.delete(item.key)}
             key={item.key}>{item.text}</li>
}
```
We’re simply listening to the click event and associating it with an event handler called delete. What might be new is our approach for passing arguments to the event handler. Because of how event arguments and event handlers deal with scope, we work around all those issues using an arrow function that allows us both to maintain the default event argument and pass in our own arguments. After you’ve made this change, you need to define the delete event handler. Make the following changes:

```javascript
class TodoItems extends Component {
    constructor(props) {
        super(props);

        this.createTasks = this.createTasks.bind(this);
    }

    delete(key) {
        this.props.delete(key);
    }
```
Here we define a function called delete that takes our argument for the item key. To ensure that this resolves properly, we explicitly bind this in the constructor. Notice that our delete function doesn’t actually do any deleting. It just calls another delete function passed into this component via props. We’ll work backward from here and deal with that next.

In TodoList.js, take a look at our render function. When calling TodoItems, let’s specify a prop called delete and set it to the value of a function called deleteItem:

```javascript
      </div>
      <TodoItems entries={this.state.items}
                 delete={this.deleteItem}/>
    </div>
  );
```

This change ensures that our TodoItems component now has knowledge of a prop called delete. This also means that our delete function we added in TodoList actually connects. All that remains is actually defining our deleteItem function so that it can deal with deleting an item.

First, go ahead and add the deleteItem function to your TodoList component. You can add it anywhere, but my preference is to put it just below where our addItem function lives:

```javascript
deleteItem(key) {
  var filteredItems = this.state.items.filter(function(item) {
    return (item.key !== key);
  });
 
  this.setState({
    items: filteredItems
  });
}
```

We are passing the key from our clicked item all the way here, and we check this key against all the items we’re storing currently via the filter method. We create a new array called filteredItems that contains everything except the item we are removing. This filtered array is then set as our new items property on our state object.

The last thing we need to do is deal with the usual shenanigans surrounding this. Make the following change in the constructor:

```javascript
constructor(props) {
  super(props);
 
  this.state = {
    items: []
  };
 
  this.addItem = this.addItem.bind(this);
  this.deleteItem = this.deleteItem.bind(this);
}
```

This ensures that all references to this inside deleteItem will reference the correct thing. Now we have just one more thing to do before we can declare victory in deleting items. Open TodoList.css and make the following highlighted change and style rule addition:

```css
.todoListMain .theList li {
  color: #333;
  background-color: rgba(255,255,255,.5);
  padding: 15px;
  margin-bottom: 15px;
  border-radius: 5px;
 
  transition: background-color .2s ease-out;
}
 
.todoListMain .theList li:hover {
  background-color: pink;
  cursor: pointer;
}
```

This provides the hover effect when you move the mouse cursor over the item that you want to remove. With this change done, our functionality to remove an item should be complete. 

## Animation
The React community has come up with a handful of lightweight animation libraries that make animating adding and deleting elements really easy. One such library is Flip Move. Among many things, this library makes animating the addition and removal of list elements simple.

To use this library, we need to first add it to our project. From the command line, make sure you are still in the same location as our todolist project and run the following command:

```console
npm i -S react-flip-move
```

After you’ve done this, in TodoItems.js, add the following import statement at the top:

```javascript
import FlipMove from 'react-flip-move';
```

Now all that’s left is to tell our FlipMove component to animate our list of items. In our render function, make the following highlighted change:

```javascript
  return (
    <ul className="theList">
      <FlipMove duration={250} easing="ease-out">
        {listItems}
      </FlipMove>
    </ul>
  );
```