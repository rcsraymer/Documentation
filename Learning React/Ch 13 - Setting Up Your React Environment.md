## The Performance Conundrum
The downside to relying on the DOM to convert JSX to actual Javascript is performance hits for end users. The solution is to set up your dev environment so that the JSX-JS conversion is handled as a default part of your app being built.

With this solution, your browser will load your app and will only deal with an already converted JavaScript file. It will use a combination of Node, Babel and Webpack. Luckily, this will already be packaged in a solution created by Facebook.

## Meet Create React
The Create React project (https://github.com/facebookincubator/create-react-app) came about and greatly simplified the process of setting up your React environment. You just run a few commands on your command line, and your React project is automatically created with all the proper behind-the-scenes configurations.

To get started, make sure that you have Node installed. Then open your command prompt and install your Create React project:

```console
npm install -g create-react-app
```

Once your installation has completed, it’s time to create our new React project. Navigate to the folder where you want to create your new project—this can be your desktop, a location under Documents, and so on. When you’ve navigated to a folder in your command line, enter the following to create a new project at this location:

```console
create-react-app helloworld
```

Navigate to your app and run the following to test your app:
```console
npm start
```

## Making Sense of What Happened
Right now, we just see whatever default content the create-react-app command generated for us. That isn’t very helpful. First, let’s take a look at what exactly gets generated.

The index.html in your public folder gets loaded in your browser. If you take a look at this file, you’ll realize that it’s very basic. The important part to look at is the div element with an id value of root. This is where the contents of our React app ultimately get printed to. Speaking of that, the contents of our React app with all the JSX are contained inside the src folder. The starting point for our React app is contained in index.js.

```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';
 
ReactDOM.render(<App />, document.getElementById('root'));
registerServiceWorker();
```

Notice the ReactDOM.render call that looks for the root element we called out inside index.html. You’ll also see a bunch of import statements at the top of the page. These import statements are part of something in JavaScript known as modules. The goal of modules is to divide the functionality of your app into increasingly smaller pieces. When it comes time to use a piece, you import only what you need instead of everything and the entire kitchen sink. Some of the modules you import are a part of code in your project. Other modules, like React and ReactDOM, are external to your project but still capable of being imported. 

In our code right now, we’re importing both the React and React-DOM libraries. That should be familiar from when we included the script tags for them earlier. We’re also importing a CSS file, a service worker script that we’ll reference as registerServiceWorker, and a React component that we’ll reference as App.

Our App component seems like our next stop, so to see what’s inside it, open App.js

```javascript
import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
 
class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
      </div>
    );
  }
}
 
export default App;
```

Notice that our App.js file has import statements of its own. Some, such as the one for React and Component, seem necessary, given what our code is doing. The last line here is interesting: export default app. It contains the export command and the name that our project will use to identify the exported module. You’ll use this exported name when importing the App module in other parts of the project, such as index.js. Closing out what this file is doing, it also imports an image and CSS file that are needed to make this page work.

You’ve now seen a different way of structuring code using some potentially new keywords. What’s the purpose of all of this? These modules, import statements, and export statements are just niceties to make our app’s code more manageable. Instead of having everything defined in one giant file, you can break your code and related assets across multiple files. Depending on which files you reference and what files get loaded ahead of other files, our mysterious build process (currently kicked off with an npm start) can optimize the final output in a variety of ways that we don’t need to worry about.

## Creating Our HelloWorld App
Go to your SRC directory and delete all the files you see there. Then create a new file called index.js:

```javascript
import React from "react";
import ReactDOM from "react-dom";
import HelloWorld from "./HelloWorld";
 
ReactDOM.render(
    <HelloWorld/>,
    document.getElementById("root")
);
```

Now we need to create the HelloWorld component. In the same src directory that we’re in right now, create a file called HelloWorld.js.

```javascript
import React, { Component } from "react";
 
class HelloWorld extends Component {
  render() {
    return (
      <div className="helloContainer">
        <h1>Hello, world!</h1>
      </div>
    );
  }
}
 
export default HelloWorld;
```

Now run npm start. Our example is working now, but it looks a little too plain. Let’s fix that by adding some CSS. Create a stylesheet called index.css, and add the following style rule into it:

```html
body {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  margin: 0;
}
```
In this approach for building apps, creating the stylesheet is only one part of what you have to do. The other part requires you to reference the newly created index.css in the index.js file. Open index.js and add the highlighted import statement for it:

```javascript
import "./index.css";
```

The last thing we want to do is make our text appear in a more stylish fashion. We could add the appropriate style rules to index.css itself, but the more appropriate solution is to create a new CSS file that we reference only in our HelloWorld component. The end result of both approaches is identical, but you want to get into the practice of grouping related files (and their dependencies) together, as part of being a better developer.

Create a new file called HelloWorld.css inside the src folder. Add the following style rule into it:

```html
h1 {
    font-family: sans-serif;
    font-size: 56px;
    padding: 5px;
    padding-left: 15px;
    padding-right: 15px;
    margin: 0;
    background: linear-gradient(to bottom,
                                white 0%,
                                white 62%,
                                gold 62%,
                                gold 100%);
}
```

All that’s left is to reference this stylesheet in the HelloWorld.js file, so open that file and add the highlighted import statement:

```javascript
import "./HelloWorld.css";
```
## Creating A Production Build
We’re almost done. We’ve got just one more thing left to do. So far, we’ve been building this app in development mode. In this mode, our code isn’t minified and some of the things run in a slow/verbose setting so that we can debug issues more easily. When it’s time to send the app live to our real users, we want the fastest and most compact solution possible. For that, we can go back to the command line and enter the following:

```console
npm run build
```

When this has completed, you can follow the onscreen prompts to deploy it to your server or just test it locally using the popular serve node package.

Take some time to look through the files built in the /build folder.

```console
The build folder is ready to be deployed.
You may serve it with a static server:

  npm install -g serve
  serve -s build
```