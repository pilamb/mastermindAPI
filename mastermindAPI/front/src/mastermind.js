var app = new Vue({
  el: '#app',
  delimiters: ['[[', ']]'],
  data: {
    message: 'Hola Vue!'
  }
})

var app2 = new Vue({
  el: '#app-2',
  data: {
    message: 'Usted cargó esta página el ' + new Date().toLocaleString()
  }
})
