# Challenges With Sending Multiple Properties
You'll need to explicitly define the properties in the ReactDOM.render object and then call {this.props.propertyname} in each class. This causes code bloat and violates the DRY principle. 

# Intro To The Spread Operator

```javascript
var items = ["1", "2", "3"];
 
function printStuff(a, b, c) {
  console.log("Printing: " + a + " " + b + " " + c);
}
```

We want to specify the three values from our items array as arguments to the printStuff function. Here’s one really common way of doing that:

```javascript
printStuff(items[0], items[1], items[2]);
```

With the spread operator, you don't have to specify each item in the array individually whenever passing it on the printStuff function. Here's how to do that:

```javascript
printStuff(...items);
```
The spread operator allows you to unwrap an array into its individual elements.

# A Better Way To Transfer Properties

```javascript
var props = {
  color: "steelblue",
  num: "3.14",
  size: "medium"
};
```
As part of passing these property values to a child component, we manually access each item from our props object:

```javascript
<Display color={this.props.color}
         num={this.props.num}
         size={this.props.size}/>
```
We can leverage the spread operator to unwrap the array and pass it ino the Display component:
```javascript
<Display {...this.props} />
```

Example below:

```javascript
class Display extends React.Component {
  render() {
    return (
      <div>
        <p>{this.props.color}</p>
        <p>{this.props.num}</p>
        <p>{this.props.size}</p>
      </div>
    );
  }
}
 
class Label extends React.Component {
  render() {
    return (
      <Display {...this.props} />
    );
  }
}

class Shirt extends React.Component {
  render() {
    return (
      <div>
        <Label {...this.props} />
      </div>
    );
  }
}
```