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

## Getting the Default Props
This property on the component allows you to specify the default value of *this.props*. If we wanted to set a name property on our CounterParent component, it could look as follows:

```javascript
CounterParent.defaultProps = {
  name: "Iron Man"
};
```

This gets run before your component is even created or any props from parent components are passed in.

## Getting the Default State

This step happens inside your component’s constructor. You get the chance to specify the default value of *this.state* as part of your component’s creation:

```javascript
constructor(props) {
  super(props);
 
  console.log("constructor: Default state time!");
 
  this.state = {
    count: 0
  };
 
  this.increase = this.increase.bind(this);
}
```
Notice that we’re defining our state object and initializing it with a count property whose value is 0.

*componentWillMount*  
This is the last method that gets called before your component gets rendered to the DOM. There’s an important point to note here: If you call setState inside this method, your component will not re-render.

*render*  
This one should be very familiar to you by now. Every component must have this method defined, and it is responsible for returning some JSX. If you don’t want to render anything, simply return null or false.

*componentDidMount*  
This method gets called immediately after your component renders and gets placed on the DOM. At this point, you can safely perform any DOM querying operations without worrying about whether your component has made it. If you have any code that depends on your component being ready, you can specify all of that code here as well.  
  
With the exception of the render method, all of these lifecycle methods can fire only once. That’s quite different from the methods you see next.

## The Updating Phase

After your components get added to the DOM, they can potentially update and re-render when a prop or state change occurs. During this time, a different collection of lifecycle methods gets called. 

## Dealing with State Changes

First, let’s look at a state change. As we mentioned earlier, when a state change occurs, your component calls its *render* method again. Any components that rely on the output of this component also get their *render* methods called. This is done to ensure that the component is always displaying the latest version of itself. All of that is true, but it’s only a partial representation of what happens.
  
When a state change happens, the following lifecycle methods are called:
  
    shouldComponentUpdate  
    componentWillUpdate  
    render  
    componentDidUpdate

Here's what these lifecycle methods do:

*shouldComponentUpdate*  
Sometimes you don’t want your component to update when a state change occurs. This method allows you to control this updating behavior. If you use this method and return a true value, the component will update. If this method returns a false value, this component will skip updating.

*componentWillUpdate*  
This method gets called just before your component is about to update. Nothing too exciting happens here. One point to note is that you can’t change your state by calling this.setState from this method.

*render*  
If you didn’t override the update via shouldComponentUpdate, the code inside render gets called again to ensure that your component displays itself properly.

*componentDidUpdate*  
This method gets called after your component updates and the render method has been called. If you need to execute any code after the update takes place, this is the place to stash it.

## Dealing with Prop Changes
The other time your component updates is when its prop value changes after it has been rendered into the DOM. In this scenario, the lifecycle methods that follow get called:

    componentWillReceiveProps  
    shouldComponentUpdate  
    componentWillUpdate  
    render  
    componentDidUpdate  

The only new method here is *componentWillReceiveProps*. This method receives one argument, and this argument contains the new prop value that is about to be assigned to it.

## The Unmounting Phase
The last phase to look at is when your component is about to be destroyed and removed from the DOM.  

Only one lifecycle method is active here, and that is *componentWillUnmount*. You perform cleanup-related tasks here, such as removing event listeners and stopping timers. After this method gets called, your component is removed from the DOM and you can say goodbye to it.

