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

