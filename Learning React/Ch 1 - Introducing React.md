# Automatic UI State Management
The final or end state of your UI is what matters in React.

React takes care of everything else. It figures out what needs to happen to ensure that your UI is represented properly so that all that state-management stuff is no longer your concern.

# Lightning-Fast DOM Manipulation
React modifies an in-memory virtual DOM. Manipulating this virtual DOM is extremely fast, and React takes care of updating the real DOM when the time is right. It does so by comparing the changes between your virtual DOM and the real DOM, figuring out which changes actually matter, and making the fewest number of DOM changes needed to keep everything up-to-date in a process called reconciliation.

# APIs to Create Truly Composable UIs
Instead of treating the visual elements in your app as one monolithic chunk, React encourages you to break your visual elements into smaller and smaller components

# Visuals Defined Entirely in JavaScript
By having your UI defined entirely in JavaScript, you get to use all the rich functionality JavaScript provides for doing all sorts of things inside your templates. You are limited only by what JavaScript supports, not limitations imposed by your templating framework.

# Just the V in an MVC Architecture
Instead, React works primarily in the View layer, where all of its worries and concerns revolve around keeping your visual elements up-to-date. This means you’re free to use whatever you want for the M and C parts of your MVC (a.k.a. Model-View-Controller) architecture. This flexibility allows you to pick and choose technologies you are familiar with, and it makes React useful not only for new web apps you create, but also for existing apps you’d like to enhance without removing and refactoring a whole bunch of code.