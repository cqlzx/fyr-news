const jwt = require('jsonwebtoken');
const User = require('mongoose').model('User');
const config = require('../config/config.json');

module.exports = (req, res, next) => {
    console.log('auth_checker: req: ' + req.headers);

    if (!req.headers.authorization) {
        return res.status(401).end();
    }

    const token = req.headers.authorization.split(' ')[1];

    console.log('auth_checker: token: ' + token);

    // Decode token using secret
    return jwt.verify(token, config.jwtSecret, (error, decoded) => {
        if (error) {
            return res.status(401).end();
        }

        //Check if user exists
        return User.findById(decoded.sub, (userError, user) => {
            if (userError || !user) {
                return res.status(401).end();
            }

            return next();
        });
    })
};