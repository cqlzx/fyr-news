const cors = require('cors');
const bodyParser = require('body-parser');
const express = require('express');
const path = require('path');

const app = express();
const config = require('./config/config.json');
require('./models/main').connect(config.mongoDbUri);

const AuthCheckMiddleware = require('./middleware/auth_checker');

const passport = require('passport');

app.use(bodyParser.json());
const auth = require('./routes/auth');
const index = require('./routes/index');
const news = require('./routes/news');


app.use(passport.initialize());
const localLoginStrategy = require('./passport/login_passport');
const localSignUpStrategy = require('./passport/signup_passport');
passport.use('local-login', localLoginStrategy);
passport.use('local-signup', localSignUpStrategy);


//TODO: remove after development
app.use(cors());

app.use('/static', express.static(path.join(__dirname, '../fyrn-client/build/static')));
app.use('/', index);
app.use('/auth', auth);
app.use('/news', AuthCheckMiddleware);
app.use('/news', news);

app.use('*', index);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  res.status(404);
});


module.exports = app;
