import 'materialize-css/dist/css/materialize.min.css';
import 'materialize-css/dist/js/materialize.js';

import React from 'react';
import PropTypes from 'prop-types';
import LoginForm from './LoginForm';
import Auth from '../Auth/Auth';


class LoginPage extends React.Component {
    constructor(props, context) {
        super(props, context);

        this.submitForm = this.submitForm.bind(this);
        this.changeForm = this.changeForm.bind(this);

        this.state = {
            user: {
                email: '',
                password: ''
            },
            errors: {
                // email: 'email error',
                // password: 'password error'
            }
        }
    }

    submitForm(event) {
        event.preventDefault();

        const email = this.state.user.email;
        const password = this.state.user.password;

        console.log('email: ' + email);
        console.log('password: ' + password);

        fetch('http://localhost:3000/auth/login', {
            method: 'POST',
            cache: false,
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                'email': this.state.user.email,
                'password': this.state.user.password
            })
        }).then(response => {
            if (response.status === 200) {
                this.setState({error: {}});

                response.json().then(data => {
                    console.log(data);
                    Auth.authenticateUser(data.token, email);
                    this.context.router.replace('/');
                });
            } else {
                console.log('login fail!');

                response.json().then(data => {
                   const error = data.error ? data.error : {};
                   error.summary = data.message;
                   this.setState({error});
                });
            }
        });
    }

    changeForm(event) {
        const field = event.target.name;
        const user = this.state.user;

        user[field] = event.target.value;

        this.setState({user});
    }

    render() {
        return (
            <LoginForm
                onSubmit={this.submitForm}
                onChange={this.changeForm}
                errors={this.state.errors}
                user={this.state.user}
            />
        );
    }
}

LoginPage.contextTypes = {
    router: PropTypes.object.isRequired
};

export default LoginPage;