const jwt = require('jsonwebtoken');
const User = require('mongoose').model('User');
const PassportLocalStrategy = require('passport-local').Strategy;
const config = require('../config/config.json');

module.exports = new PassportLocalStrategy({
    usernameField: 'email',
    passwordField: 'password',
    session: false,
    passReqToCallback: true
}, (req, email, password, done) => {
    const userData = {
        email: email.trim(),
        password: password
    };

    //Find user in DB by email
    return User.findOne({email: userData.email}, (err, user) => {
        if (err) {
            return done(err);
        }

        if (!user) {
            const error = new Error('Incorrect email or password.');

            error.name = 'IncorrectCredentialErrors';

            return done(error);
        }

        return user.comparePassword(userData.password, (passwordError, isMatched) => {
            if (passwordError) {
                return done(passwordError);
            }

            if (!isMatched) {
                const error = new Error('Incorrect email or password.');

                error.name = 'IncorrectCredentialErrors';
            }

            const payload = {
                sub: user._id,
            };

            // Create a token
            const token = jwt.sign(payload, config.jwtSecret);
            const data = {
                name: user.email
            };

            return done(null, token, data);
        })
    })
});