To see a sliding menu in action, go here: https://www.kirupa.com/react/examples/slidingmenu_css/index.html.

You’ll see a yellow menu with some navigation links smoothly slide in. If you click a navigation link or anywhere in the yellow region inside that menu, the menu slides back (really smoothly again, of course) and the content behind it reappears. 

## How the Sliding Menu Works
Before we jump into the code, let’s take a few moments to better understand how exactly our sliding menu works. Starting at the very top, we have our page that displays some content. When you decide to bring up the menu (by clicking/tapping the blue circle in our example), the menu magically slides into view.

The way this sliding menu works isn’t as crazy as it seems. The menu is never truly nonexistent; it is simply hidden outside the view. 

Just to the left of the content what we see is our menu, patiently hiding until it is called upon. We do that by shifting the menu as far left as we can until it’s fully out of view. Figuring out how far to shift is easy. Our menu’s size is the same as our browser’s window (a.k.a. the viewport) size because we want the menu to fully cover up whatever is shown. Given that detail, we just shift the menu left by the browser’s width. One way of doing that might be by using some CSS that looks as follows:

```css
#theMenu {
  position: fixed;
  left: 0;
  top: 0;
  transform: translate3d(-100vw, 0, 0);
 
  width: 100vw;
  height: 100vh;
}
```

We set our menu’s position to fixed. This single change gives our menu a whole lot of magical capabilities. For starters, it ensures that normal layout rules no longer apply to it. We can position our menu anywhere we want using normal x and y values, and the menu won’t shift away from where we have it positioned. If that isn’t awesome enough, our menu won’t even display a scrollbar if we happen to hide it somewhere offscreen.

All this is a good thing because we hide our menu offscreen by setting our menu’s left and top properties to 0 and setting our menu’s transform property to a translate3d method with a horizontal value of -100vw. The negative value ensures that we shift the menu left by the amount equivalent to our browser window’s width. While not directly related to position, the size of our menu plays an important role as well. That’s why, in this CSS snippet, we have the width and height properties set with values of 100vw and 100vh, respectively, to ensure that our menu’s size is the same as our browser window’s size.

## What Are These vw and vh Units?

If you’ve never seen the vw and vh units, they stand for viewport width (vw) and viewport height (vh). They’re a bit similar to percentage values. Each unit is 1/100th the width or height of your viewport (what we’ve been simply calling the browser window). For example, a value of 100vw means that its value is the full width of our browser window. Similarly, 100vh refers to a value that is the full height of our browser window.

When the menu is called upon to slide into view, we slide the menu right until its horizontal position is the same as our browser window origin. If we had to look at what the CSS for it might look like, this would be an easy change from what we already have. We simply set our transform property’s translate3d method and set the horizontal position to a value of 0vw.

That might look something like this:

```css
transform: translate3d(0vw, 0, 0);
```

This change ensures that our menu is shifted right from being hidden offscreen (with a horizontal translate value of -100vw) and is now visible. When our menu needs to disappear, we can translate it back:

```css
transform: translate3d(-100vw, 0, 0);
```

The biggest thing we haven’t spoken about is the animation that makes the sliding look cool. This is done using a simple CSS transition that animates the transform property:

```css
transition: transform .3s cubic-bezier(0, .52, 0, 1);
```

## Setting Up The Sliding Menu

The first thing we’re going to do is look at our example in terms of the individual components that will make it up.

At the very top, we have our MenuContainer component. This component is responsible for doing nonvisual things like managing state, hosting our Menu and MenuButton components, and displaying some of the initial text. In the next few sections, we’ll start creating these components and getting the example up and running.

## Getting Started

```console
create-react-app slidingmenu
```

Delete all in public and src folders by using the following command in that respective directory in console:

```console
del /f/q/s *.* > NUL
```

Add index.html in public:

```html
<!DOCTYPE html>
<html>
 
<head>
  <title>Sliding Menu in React</title>
</head>
 
<body>
  <div id="container"></div>
</body>
 
</html>
```

Next create index.js in src:

```javascript
import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import MenuContainer from "./MenuContainer";
 
ReactDOM.render(
  <MenuContainer/>,
  document.querySelector("#container")
);
```

The render call here is responsible for displaying the output of our MenuContainer component into the container div element we specified in HTML a few moments ago. In our import statements, besides pulling in the react and react-dom libraries, we are referencing index.css and our MenuContainer component. That’s all there is to our index.js file.

Next we’re going to create the index.css file in our src folder:

```css
body {
  background-color: #EEE;
  font-family: sans-serif;
  font-size: 20px;
  padding: 25px;
  margin: 0;
  overflow: auto;
}
 
#container li {
  margin-bottom: 10px;
}
```

The last thing we do to get our initial app set up is create our MenuContainer component. Create a file called MenuContainer.js in the src folder and add the following JS and JSX into it:

```javascript
import React, { Component } from "react";
 
class MenuContainer extends Component {
  render() {
    return (
      <div>
        <div>
          <p>Can you spot the item that doesn't belong?</p>
          <ul>
            <li>Lorem</li>
            <li>Ipsum</li>
            <li>Dolor</li>
            <li>Sit</li>
            <li>Bumblebees</li>
            <li>Aenean</li>
            <li>Consectetur</li>
          </ul>
        </div>
      </div>
    );
  }
}
 
export default MenuContainer;
```

## Showing and Hiding the Menu
Our menu is shown or hidden as follows:

1) When you click a button, the menu slides into view
2) When you click anywhere on the menu, the menu slides out of view

We need to maintain some state to keep track of whether the menu is hidden or shown. This state needs to be something we update from both the button and the menu because clicking on either will toggle whether the menu is visible. We need our state to live in a common location that both the menu and the button can access. That common location will be inside our MenuContainer component, so let’s add the code relating to our state logic.

In the MenuContainer.js file, add the constructor and toggleMenu methods just above our render method:

```javascript
constructor(props) {
  super(props);

  this.state = {
    /// You’re storing a variable called visible in your state object
    visible: false
  };
  
  this.toggleMenu = this.toggleMenu.bind(this);
}
/// You’re creating a method called toggleMenu that will be responsible for toggling whether visible is true or false
toggleMenu() {
  this.setState({
    visible: !this.state.visible
  });
}
```

Next up is dealing with the click events on the button and menu. If the goal is to update our state from inside our MenuContainer component, we need to place our event handler inside MenuContainer as well. Go ahead and add the following lines:

```javascript
    this.state = {
      visible: false
    };

    /// Add the following block
    this.handleMouseDown = this.handleMouseDown.bind(this);
    this.toggleMenu = this.toggleMenu.bind(this);
  }

   handleMouseDown(e) {
    this.toggleMenu();

    console.log("clicked");
    e.stopPropagation();
  } 

  toggleMenu() {...
```

When the handleMouseDown method is called, we call toggleMenu, which toggles whether the menu appears. At this point, you’re probably wondering where the actual code for dealing with a click event is. What exactly will trigger a call to handleMouseDown? The answer is, nothing so far! We’ve done things in a bit of a reverse order and defined our event handler first. We handle the association between our event handler and our click event in a few moments when dealing with our button and menu components.

## Creating the Button
In your src folder, create two files called MenuButton.js and MenuButton.css. Open the js file:

```javascript
import React, { Component } from "react";
import './MenuButton.css';
 
class MenuButton extends Component {
  render() {
    return (
      <button id="roundButton"
              onMouseDown={this.props.handleMouseDown}></button>
    );
  }
}
 
export default MenuButton;
```
We define a button element called roundButton, and we associate the onMouseDown event with a prop we are referencing as handleMouseDown. Before moving on, open MenuButton.css and add the following style rules:

```css
#roundButton {
  background-color: #96D9FF;
  margin-bottom: 20px;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  border: 10px solid #0065A6;
  outline: none;
  transition: all .2s cubic-bezier(0, 1.26, .8, 1.28);
}
 
#roundButton:hover {
  background-color: #96D9FF;
  cursor: pointer;
  border-color: #003557;
  transform: scale(1.2, 1.2);
}
 
#roundButton:active {
  border-color: #003557;
  background-color: #FFF;
}
```

Now we instantiate our MenuButton component. Go back to the MenuContainer component and add the following line inside the render method:

```javascript
  return (
    <div>
      <MenuButton handleMouseDown={this.handleMouseDown}/>
    ...
```
Notice that we are passing in a prop called handleMouseDown, and its value is the handleMouseDown event handler that we defined earlier. This ensures that when you click the button inside the MenuButton component, the handleMouseDown method that lives in the MenuContainer component gets called. All of this is great, but our button isn’t very useful without a menu to help slide into view. We’ll fix that next.

# Creating the Menu
It’s time to create our Menu component that will be responsible for all things dealing with the menu. Before we actually create this component, let’s pretend that it already exists and call it from our render method inside our MenuContainer. Add the following call to our (currently imaginary) Menu component just below where you added the call to MenuButton a few short moments earlier:

```javascript  

  toggleMenu() {
    this.setState(
      {
        visible: !this.state.visible
      }
    );
  }

  render() {
    return (
      <div>
        <MenuButton handleMouseDown={this.handleMouseDown}/>
        <Menu handleMouseDown={this.handleMouseDown}
              menuVisibility={this.state.visible}/>
```
Add the import statement for Menu.js as well. Getting back to the Menu component, look at the props you’re passing in. The first prop should look familiar to you. It is handleMouseDown and its value is our handleMouseDown event-handling method. The second prop is called menuVisibility. Its value is the current value of our visible state property. Now let’s go ahead and actually create our Menu component and see, among other things, how these props get used.

In the same src folder we have been partying in for the past few sections, add one file called Menu.js and another file called Menu.css. Inside Menu.js, add the following contents:

```javascript
import React, { Component } from "react";
import "./Menu.css";
 
class Menu extends Component {
  render() {
/// The value of visibility is set early. The value is either hide or show, depending on whether the menuVisibility prop (whose value is specified by our visible state property) is true or false. 
    var visibility = "hide";
 
    if (this.props.menuVisibility) {
      visibility = "show";
    }
 
    return (
/// We have a div element called flyoutMenu with some sample content. In our div element, we call our handleMouseDown event-handling method (passed in via a prop) when the onMouseDown event is overheard. Next, we set a class value on this element; the value is the result of evaluating a variable called visibility. As you might recall, class is a reserved name in JavaScript and you can’t use it directly in our JSX; it has to be specified as className.
      <div id="flyoutMenu"
           onMouseDown={this.props.handleMouseDown}
           className={visibility}>
        <h2><a href="#">Home</a></h2>
        <h2><a href="#">About</a></h2>
        <h2><a href="#">Contact</a></h2>
        <h2><a href="#">Search</a></h2>
      </div>
    );
  }
}
 
export default Menu;
```

While it might not look like it, the code revolving around className plays a really important role in determining whether your menu is actually visible. When we look at our CSS, you’ll see why. Now open Menu.css and add the following style rules into it:

```css
#flyoutMenu {
  width: 100vw;
  height: 100vh;
  background-color: #FFE600;
  position: fixed;
  top: 0;
  left: 0;
  transition: transform .3s
              cubic-bezier(0, .52, 0, 1);
  overflow: scroll;
  z-index: 1000;
}
 
#flyoutMenu.hide {
  transform: translate3d(-100vw, 0, 0);
}
 
#flyoutMenu.show {
  transform: translate3d(0vw, 0, 0);
  overflow: hidden;
}
 
#flyoutMenu h2 a {
  color: #333;
  margin-left: 15px;
  text-decoration: none;
}
 
#flyoutMenu h2 a:hover {
  text-decoration: underline;
}
```

The CSS you see here mostly deals with how our menu itself looks, but the actual showing and hiding of the menu is handled by the #flyoutMenu.hide and #flyoutMenu.show style rules. Which of these style rules becomes active depends entirely on the code we looked at earlier. In our flyoutMenu div element, remember that the class value on the generated HTML (which our CSS maps to) will be either hide or show, depending on what value we set for className.