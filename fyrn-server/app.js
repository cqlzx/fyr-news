const express = require('express');
const path = require('path');
const app = express();

const index = require('./routes/index');


app.use('/static', express.static(path.join(__dirname, '../fyrn-client/build/static')));
app.use('/', index);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  res.status(404);
});


module.exports = app;
