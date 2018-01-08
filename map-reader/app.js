var express = require('express')
var app = express()

app.use('/public', express.static('public'))
app.set('view engine', 'pug');

app.get('/', function (req, res) {
  res.render('index');
})

app.listen(3333, function () {
  console.log('Example app listening on port 3333!')
})