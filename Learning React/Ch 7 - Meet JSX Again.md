# JSX Quirks To Remember
## Evaluating Expressions
JSX is treated like JavaScript. As you’ve seen a few times already, this means that you aren’t limited to dealing with static content. The values you return can be dynamically generated. All you have to do is wrap your expression in curly braces:

```javascript
class Stuff extends React.Component {
  render() {
    return (
      <h1>Boring {Math.random() * 100} content!</h1>
    );
  }
}
```
## Returning Multiple Elements
When you return multiple items, you might or might not have to deal with one detail, depending on the version of React you are targeting. You need to specify a key attribute and a unique value for each item:

```javascript
class Stuff extends React.Component {
  render() {
    return (
      [
        <p key="1">I am</p>,
        <p key="2">returning a list</p>,
        <p key="3">of things!</p>
      ]
    );
  }
}
```
This helps React better understand which element it is dealing with and whether to make any changes to it. How do you know whether you need to add the key attribute? React tells you. You’ll see a message similar to the following printed to your Dev Tools Console: Warning: Each child in an array or iterator should have a unique “key” prop.

You also have another (and, arguably, better) way to return multiple elements. This involves something known as fragments. The way you use it looks as follows:

```javascript
class Stuff extends React.Component {
  render() {
    return (
      <React.Fragment>
        <p>I am</p>
        <p>returning a list</p>
        <p>of things!</p>
      </React.Fragment>
    );
  }
}
```
## Comments

```javascript
ReactDOM.render(
  <div className="slideIn">
    <p className="emphasis">Gabagool!</p>
    {/* I am a child comment */}
    <Label/>
  </div>,
  document.querySelector("#container")
);
```
## CAPITALIZATION, HTML ELEMENTS, AND COMPONENTS
Capitalization is important. To represent HTML elements, ensure that the HTML tag is lowercase:

```javascript
ReactDOM.render(
  <div>
    <section>
      <p>Something goes here!</p>
    </section>
  </div>,
  document.querySelector("#container")
);
```
When you want to represent components, the component name must be capitalized:

```javascript
ReactDOM.render(
  <div>
    <MyCustomComponent/>
  </div>,
  document.querySelector("#container")
);
```