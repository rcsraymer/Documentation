## Challenges
Single-page apps are different from the more traditional multipage apps that you see everywhere. The biggest difference is that navigating a single-page app doesn’t involve going to an entirely new page. Instead, your pages (commonly known as views in this context) typically load inline within the same page itself.
 
The hard part isn’t loading the content itself. That’s relatively easy. The hard part is making sure that single-page apps behave in a way that is consistent with what your users are accustomed to. More specifically, when users navigate your app, they have some expectations:

1. The URL displayed in the address bar should always reflect the thing users are viewing.

2. Users expect to be able to use the browser’s back and forward buttons successfully.

3. Users should be able to navigate to a particular view (a.k.a. deep link) directly using the appropriate URL.

To deal with all of this, you have a bucket full of techniques commonly known as routing. With routing, you try to map URLs to destinations that aren’t physical pages, such as the individual views in your single-page app. That sounds complicated, but fortunately, a bunch of JavaScript libraries can help with this. One such JavaScript library is the star of this tutorial, React Router(https://github.com/reactjs/react-router). React Router provides routing capabilities to single-page apps built in React. 

## Getting Started

```console
npx create-react-app react_spa
cd react_spa
```

Normally, this is where we start messing around with deleting the existing content to start from a blank slate. We’ll do that, but first, we’re going to install React Router. To do that, run the following command:

```console
npm i react-router-dom --save
```
This copies the appropriate React Router files and registers it in our package.json so that our app is aware of its existence. That’s good stuff, right?

It’s time to clean up the project to start from a clean slate. From inside your react_spa folder, delete everything inside your public and src folders. Now, let’s create the index.html file that will serve as our app’s starting point. In your public folder, create a file called index.html and add the following contents into it:

```html
<!DOCTYPE html>
<html>
 
<head>
  <meta charset="utf-8">
  <meta name="viewport"
        content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <title>React Router Example</title>
</head>
 
<body>
  <div id="root"></div>
</body>
 
</html>
```

Next, in your src folder, create a file called index.js:

```javascript
import React from "react";
import ReactDOM from "react-dom";
import Main from "./Main";
 
ReactDOM.render(
  <Main/>,
  document.getElementById("root")
);
```

Our ReactDOM.render call lives here, and we’re rendering our Main component…which doesn’t exist yet. The Main component will be the starting point for our SPA expedition using React Router, and you’ll see how beginning with the next section.

## Building Our Single Page App

### Displaying the Initial Frame
When building an SPA, a part of your page will always remain static. This static part, also referred to as an app frame, could be one invisible HTML element that acts as the container for all of your content, or it could include some additional visual things such as a header, a footer, or navigation. In our case, our app frame will be a component that contains UI elements for our navigation header and an empty area for content to load in.

Inside our src folder, create a new file called Main.js and add the following content into it:

```javascript
import React, { Component } from "react";
 
class Main extends Component {
  render() {
    return (
      <div>
        <h1>Simple SPA</h1>
        <ul className="header">
          <li><a href="/">Home</a></li>
          <li><a href="/stuff">Stuff</a></li>
          <li><a href="/contact">Contact</a></li>
        </ul>
        <div className="content">
 
        </div>
      </div>
    );
  }
}
 
export default Main;
```
Take a look at what we have here. We have a component called Main that returns some HTML. That’s it. To see what we have so far in action, type npm start and see what’s going on in your browser.

### Creating Our Content Pages
Our app will have three pages of content. This content will be just a simple component that prints out some JSX. Let’s get that created and out of the way. First, create a file called Home.js in the src directory and add the following content:

```javascript
import React, { Component } from "react";
 
class Home extends Component {
  render() {
    return (
      <div>
        <h2>HELLO</h2>
        <p>Cras facilisis urna ornare ex volutpat, et
        convallis erat elementum. Ut aliquam, ipsum vitae
        gravida suscipit, metus dui bibendum est, eget rhoncus nibh
        metus nec massa. Maecenas hendrerit laoreet augue
        nec molestie. Cum sociis natoque penatibus et magnis
        dis parturient montes, nascetur ridiculus mus.</p>
 
        <p>Duis a turpis sed lacus dapibus elementum sed eu lectus.</p>
      </div>
    );
  }
}
 
export default Home;
```

Next create a file called stuff.js in the same location:

```javascript
import React, { Component } from "react";
 
class Stuff extends Component {
  render() {
    return (
      <div>
        <h2>STUFF</h2>
        <p>Mauris sem velit, vehicula eget sodales vitae,
        rhoncus eget sapien:</p>
        <ol>
          <li>Nulla pulvinar diam</li>
          <li>Facilisis bibendum</li>
          <li>Vestibulum vulputate</li>
          <li>Eget erat</li>
          <li>Id porttitor</li>
        </ol>
      </div>
    );
  }
}
 
export default Stuff;
```

Then, contact.js:

```javascript
import React, { Component } from "react";
 
class Contact extends Component {
  render() {
    return (
      <div>
        <h2>GOT QUESTIONS?</h2>
        <p>The easiest thing to do is post on
        our <a href="http://forum.kirupa.com">forums</a>.
        </p>
      </div>
    );
  }
}
 
export default Contact;
```

## Using React Router
Now we need to tie all of these components together to create our app. This is where React Router comes in. To start using it, go back to Main.js and ensure that your import statements look as follows:

```javascript
import React, { Component } from "react";
import {
  Route,
  NavLink,
  HashRouter
} from "react-router-dom";
import Home from "./Home";
import Stuff from "./Stuff";
import Contact from "./Contact";
```

We are importing Route, NavLink, and HashRouter from the react-router-dom NPM package installed earlier. In addition, we’re importing our Home, Stuff, and Contact components because we’ll be referencing them as part of loading our content.

React Router works by defining what I call a routing region. Inside this region are two things:

1. Your navigation links

2. The container to load your content into

The first thing to do is define the routing region. Inside our Main component’s render method, add the following lines:

```javascript
class Main extends Component {
  render() {
    return (
      <HashRouter>
        <div>
          <h1>Simple SPA</h1>
          <ul className="header">
            <li><a href="/">Home</a></li>
            <li><a href="/stuff">Stuff</a></li>
            <li><a href="/contact">Contact</a></li>
          </ul>
          <div className="content">
 
          </div>
        </div>
      </HashRouter>
    );
  }
}
```
The HashRouter component provides the foundation for the navigation and browser history handling that routing is made up of. Next we need to define our navigation links. We already have list elements with the a element defined. We need to replace them with the more specialized NavLink component, so go ahead and make the following  changes:

```javascript
          <ul className="header">
            <li><NavLink to="/">Home</NavLink></li>
            <li><NavLink to="/stuff">Stuff</NavLink></li>
            <li><NavLink to="/contact">Contact</NavLink></li>
          </ul>
```

For each link, pay attention to the URL we’re telling our router to navigate to. This URL value (defined by the to prop) acts as an identifier to ensure that the right content gets loaded. We match the URL with the content by using a Route component. Go ahead and add the following:

```javascript
          <div className="content">
            <Route exact path="/" component={Home}/>
            <Route path="/stuff" component={Stuff}/>
            <Route path="/contact" component={Contact}/>
          </div>
```

As you can see, the Route component contains a path prop. The value you specify for the path determines when this route is going to be active. When a route is active, the component specified by the component prop gets rendered. For example, when we click on the Stuff link (whose path is /stuff as set by the NavLink component’s to prop), the route whose path value is also /stuff becomes active. This means the contents of our Stuff component get rendered.

We use exact path for the Home content to ensure that the Route is active only if the path is an exact match for what is being loaded. If we do not use exact path and use path instead, we will see the Home content added to the Stuff and Contact content.

## Adding Some CSS
Create src/index.css:

```css
body {
  background-color: #FFCC00;
  padding: 20px;
  margin: 0;
}
h1, h2, p, ul, li {
  font-family: sans-serif;
}
ul.header li {
  display: inline;
  list-style-type: none;
  margin: 0;
}
ul.header {
  background-color: #111;
  padding: 0;
}
ul.header li a {
  color: #FFF;
  font-weight: bold;
  text-decoration: none;
  padding: 20px;
  display: inline-block;
}
.content {
  background-color: #FFF;
  padding: 20px;
}
.content h2 {
  padding: 0;
  margin: 0;
}
.content li {
  margin-bottom: 10px;
}
```
At the top of index.js, add the import statement to reference this stylesheet:

```javascript
import Main from "./Main";
import "./index.css"; 
```

## Highlighting the Active Link

Right now, it’s hard to tell which link corresponds to content that is currently loaded. Having some sort of a visual cue would be useful. The creators of React Router have already thought of that. When you click a link, a class value of active is automatically assigned to it.

All we really have to do, then, is add the appropriate CSS that lights up when an element has a class value of active set on it. To make this happen, go back to index.css and add the following style rule toward the bottom of your document:

```css
.active {
  background-color: #0009FF;
}
```

After you have added this rule and saved your document, go back to your browser and click around on the links in our example. You’ll see that the active link whose content is displayed is highlighted with blue. Notice also that our Home link is always highlighted. That isn’t correct. The fix is simple: Just add the exact prop to the NavLink component representing our Home content:

```javascript
<li><NavLink exact to="/">Home</NavLink></li>
```