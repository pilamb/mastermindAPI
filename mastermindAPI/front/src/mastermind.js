var app = new Vue({
  el: '#app',
  delimiters: ['[[', ']]'],
  data: {
    message: 'Hello Vueworld!'
  }
})

var app2 = new Vue({
  el: '#app-2',
  data: {
    message: 'Page loaded at' + new Date().toLocaleString()
  }
})

var app3 = new Vue({
  el: '#app-3',
  data: {
    seen: true
  }
})

var app4 = new Vue({
  el: '#app-4',
  delimiters: ['[[', ']]'],
  data: {
    todos: [
      { text: 'Icons for colors png' },
      { text: 'Add Bootstrap' },
      { text: 'board design' },
      { text: 'Add header with current user' },
    ]
  }
})
