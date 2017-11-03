const cors = require('cors');
const express = require('express');
const path = require('path');
const app = express();

const index = require('./routes/index');
const news = require('./routes/news');

//TODO: remove after development
app.use(cors());

app.use('/static', express.static(path.join(__dirname, '../fyrn-client/build/static')));
app.use('/', index);
app.use('/news', news);


// catch 404 and forward to error handler
app.use(function(req, res, next) {
  res.status(404);
});


module.exports = app;
