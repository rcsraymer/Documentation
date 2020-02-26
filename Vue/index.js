var app = new Vue({
    el: '#app',
    data: {
        message: 'Hello Vue!' /* in console: set app.message to a different value */
    }
})

var app2 = new Vue({
    el: '#app-2',
    data: {
        message: 'You loaded this page on ' + new Date().toLocaleString()
    }
})

var app3 = new Vue({
    el: '#app-3',
    data: {
        seen: true /* enter app3.seen = false in the console. You should see the message disappear */
    }
})

var app4 = new Vue({
    el: '#app-4',
    data: {
        todos: [
            { text: 'Learn JavaScript' },
            { text: 'Learn Vue' },
            { text: 'Build Something Awesome' }
            /* In the console, enter app4.todos.push({ text: 'New item' }). You should see a new item appended to the list. */
        ]
    }
})

var app5 = new Vue({
    el: '#app-5',
    data: {
        message: 'Hello Vue.js!'
    },
    methods: {
        reverseMessage: function () {
            this.message = this.message.split('').reverse().join('')
        }
    }
})
