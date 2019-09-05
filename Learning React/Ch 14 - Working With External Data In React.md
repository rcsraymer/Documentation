## Web Request 101
The HTTP protocol provides a common language that allows your browser and a bunch of other things to communicate with all the servers that make up the Internet. The requests your browser makes on your behalf using the HTTP protocol are known as HTTP requests, and these requests go well beyond simply loading a new page as you are navigating. A common (and whole lot more exciting!) set of use cases revolves around updating your existing page with data resulting from a HTTP request.

For example, you might have a page where you’d like to display some information about the currently logged-in user. This is information your page might not have initially, but it is information your browser will request when you’re interacting with the page. The server will respond with the data and update your page with that information.

To get information about the user, here’s our HTTP request:

```javascript
GET /user
Accept: application/json
```

For that request, here’s what the server might return:

```json
200 OK
Content-Type: application/json
 
{
  "name": "Kirupa",
  "url": "http:https://www.kirupa.com"
}
```
This back-and-forth happens a bunch of times, and it’s all fully supported in JavaScript. This ability to asynchronously request and process data from a server without requiring a page navigation/reload has a term: Ajax (or AJAX, if you want to shout). This acronym stands for Asynchronous JavaScript and XML. 

In JavaScript, the object that is responsible for allowing you to send and receive HTTP requests is the weirdly named XMLHttpRequest. This object allows you to do several things that are important to making web requests:

        1. Send a request to a server

        2. Check on the status of a request

        3. Retrieve and parse the response from the request

        4. Listen for the readystatechange event that helps you react to the status of your request

XMLHttpRequest does a few more things, but those aren’t important to deal with right now.

## IT’S REACT TIME!
Now that you have a good enough understanding of how HTTP requests and the XMLHttpRequest object work, it’s time to shift our focus to the React side. I should warn you, though, that React brings very little to the table when it comes to working with external data. React is primarily focused on the presentation layer (a.k.a. the V in MVC). We’ll be writing regular, boring JavaScript inside a React component whose primary purpose is to deal with the web requests we’ll be making. We’ll talk more about that design choice in a little bit, but let’s get the example up and running first.

## Getting Started
The first step is to create a new React app. From your command line, navigate to the folder where you want to create your new project and enter the following:

```console
create-react-app ipaddress
```

You want to start from a blank slate, so you’re going to delete a lot of things. First, delete everything under your public folder. Next, delete everything inside your src folder. Don’t worry: You’ll fill them back with content you care about in a few moments, starting with your HTML file.

Inside the public folder, create a new file called index.html. Add the following content into it:

```html
<!DOCTYPE html>
<html>
 
<head>
  <title>IP Address</title>
</head>
 
<body>
  <div id="container">
 
  </div>
</body>
 
</html>
```

Next, go to your src folder and create a new file called index.js. Inside this file, add the following:

```javascript
import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import IPAddressContainer from "./IPAddressContainer";
 
var destination = document.querySelector("#container");
 
ReactDOM.render(
    <div>
        <IPAddressContainer/>
    </div>,
    destination
);
```

This is the script entry point for our app, and it contains the boilerplate references to React, ReactDOM, a nonexistent CSS file, and a nonexistent IPAddressContainer component. We also have the ReactDOM.render call that is responsible for writing our content to the container div element we defined in our HTML a few moments ago. Inside the src folder, create the index.css file and add the following style rule into it:

```css
body {
  background-color: #FFCC00;
}
```
## Getting The IP Address

Next on our plate is to create a component whose job it is to fetch the IP address from a web service, store it as state, and then share that state as a prop to any component that requires it. Let’s create a component to help. Inside your src folder, add a file called IPAddressContainer.js and then add the following lines inside it:

```javascript
import React, { Component } from "react";
 
class IPAddressContainer extends Component {
  render() {
    return (
      <p>Nothing yet!</p>
    );
  }
}
 
export default IPAddressContainer;
```
The lines you just added don’t do a whole lot. They just print the words Nothing yet! to the screen. That’s not bad for now, but let’s go ahead and modify the code to make the HTTP request by adding the following changes:

```javascript
var xhr;
 
class IPAddressContainer extends Component {
  constructor(props) {
    super(props);

    this.state = {
      ip_address: "..."
    };
 
    this.processRequest = this.processRequest.bind(this);
  }

// When our component becomes active and the component-DidMount lifecycle method gets called, we make our HTTP request and send it off to the ipinfo.io web service:

  componentDidMount() {
    xhr = new XMLHttpRequest();
    xhr.open("GET", "https://ipinfo.io/json?token=2277ce4bac0347", true);
    xhr.send();
 
    xhr.addEventListener("readystatechange", this.processRequest, false);
  }

/// When we hear a response back from the ipinfo service, we call the processRequest function to help us deal with the result:

  processRequest() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      var response = JSON.parse(xhr.responseText);
 
      this.setState({
        ip_address: response.ip
      });
    }
  }

  render() {
    return (
      <div>Nothing yet!</div>
    );
  }
};
```

Next, modify the render call to reference the IP address value stored by our state:

```javascript
render() {
    return (
      <div>{this.state.ip_address}</div>
    );
  }
```

## Kicking the Visuals Up a Notch
We created a component that handles all the HTTP requesting shenanigans, and we know that it returns the IP address when called. Now we’re going to format the output a bit so that it doesn’t look as plain as it does now.

To do that, we won’t add HTML elements and styling-related details to our IPAddressContainer component’s render method. Instead, we’ll create a new component whose only purpose will be to deal with all of that.

Add a new file called IPAddress.js in your src folder. Then edit it by adding the following content into it:

```javascript
import React, { Component } from "react";
 
class IPAddress extends Component {
  render() {
    return (
      <div>
        Blah!
      </div>
    );
  }
}
 
export default IPAddress;
```

Here we’re defining a new component called IPAddress that will be responsible for displaying the additional text and ensuring that our IP address is visually formatted exactly the way we want. It doesn’t do much right now, but that will change really quickly.

We first want to modify this component’s render method to look as follows:

```javascript
    return (
      <div>
        <h1>{this.props.ip}</h1>
        <p>( This is your IP address...probably :P )</p>
      </div>
    );
  }
}
```
The highlighted changes should be self-explanatory. We’re putting the results of a prop value called ip inside an h1 tag, and we’re displaying some additional text using a p tag. Besides making the rendered HTML a bit more semantic, these changes ensure that we can style them better.

To get these elements styled, add a new CSS file to the src folder called IPAddress.css. Inside this file, add the following style rules:

```css
h1 {
  font-family: sans-serif;
  text-align: center;
  padding-top: 140px;
  font-size: 60px;
  margin: -15px;
}
p {
  font-family: sans-serif;
  color: #907400;
  text-align: center;
}
```

Add the following highlighted line to IPAddress.js:

```javascript
import "./IPAddress.css";
```

All that remains is to use our IPAddress component and pass in the IP address. The first step is to ensure that the IPAddressContainer component is aware of the IPAddress component by referencing it. At the top of IPAddressContainer.js, add the following highlighted line:

```javascript
import IPAddress from "./IPAddress";
```

The second (and last!) step is to modify the render method as follows:

```javascript
class IPAddressContainer extends Component {
    .
    .
    .
  render() {
    return (
      <IPAddress ip={this.state.ip_address}/>
    );
  }
}
```

