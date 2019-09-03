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
  componentDidMount() {
    xhr = new XMLHttpRequest();
    xhr.open("GET", "https://ipinfo.io/json", true);
    xhr.send();
 
    xhr.addEventListener("readystatechange", this.processRequest, false);
  }
 
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

Now we’re getting somewhere! When our component becomes active and the component-DidMount lifecycle method gets called, we make our HTTP request and send it off to the ipinfo.io web service