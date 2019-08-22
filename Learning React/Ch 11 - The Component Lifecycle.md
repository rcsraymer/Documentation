## The Component Lifecycle
In the beginning, we took a very simple view of components and what they do. As you learned more about React and did cooler and more involved things, you came to see that components aren’t all that simple. They help us deal with properties, state, and events, and often are responsible for the well-being of other components as well. Keeping track of everything components do sometimes can be tough.

To help with this, React provides us with lifecycle methods. Unsurprisingly, lifecycle methods are special methods that automatically get called as our component goes about its business. They notify us of important milestones in a component’s life, and we can use these notifications to simply pay attention or change what our component is about to do.

## Meet the Lifecycle Methods
You can think of Lifecycle Methods as glorified event handlers that get called at various points in a component’s life. As with event handlers, you can write some code to do things at those various points.  
  
The lifecycle methods are as follows:

    componentWillMount
    componentDidMount
    componentWillUnmount
    componentWillUpdate
    componentDidUpdate
    shouldComponentUpdate
    componentWillReceiveProps
    componentDidCatch
    render

## The Initial Rendering Phase

Beginning to end, this is the initial rendering phase:  

    Default Props  
    Get State  
    componentWillMount  
    render  
    componentDidMount

## Get the Default Props

This property on the component allows you to specify the default value of this.props. If we wanted to set a name property on our CounterParent component, it could look as follows:

```javascript
CounterParent.defaultProps = {
  name: "Iron Man"
};
```