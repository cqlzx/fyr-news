import 'materialize-css/dist/css/materialize.min.css';
import 'materialize-css/dist/js/materialize.js';

import React from 'react';
import PropTypes from 'prop-types';
import SignUpForm from './SignUpForm';

class SignUpPage extends React.Component {
    constructor(props, context) {
        super(props, context);

        this.submitForm = this.submitForm.bind(this);
        this.changeForm = this.changeForm.bind(this);

        this.state = {
            user: {
                email: '',
                password: '',
                confirmPassword: ''
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
        const confirmPassword = this.state.user.confirmPassword;

        console.log('email: ' + email);
        console.log('password: ' + password);
        console.log('confirmPassword: ' + confirmPassword);


        if (password !== confirmPassword) {
            return;
        }

        fetch('http://localhost:3000/auth/signup', {
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
            if (response === 200) {
                this.setState({error: {}});

                this.context.router.replace('login');
            } else {
                response.json().then(data => {
                    console.log(data);
                    const errors = data.error ? data.error : {};
                    errors.summary = data.message;
                    this.setState({errors});
                })
            }
        })
    }

    changeForm(event) {
        const field = event.target.name;
        const user = this.state.user;

        user[field] = event.target.value;

        this.setState({user});

        const errors = this.state.errors;
        if (this.state.user.password !== this.state.user.confirmPassword) {
            errors.confirmPassword = 'Password and Confirm Password don\'t match!';
        } else {
            errors.confirmPassword = '';
        }
        this.setState({errors});
    }

    render() {
        return (
            <SignUpForm
                onSubmit={this.submitForm}
                onChange={this.changeForm}
                errors={this.state.errors}
                user={this.state.user}
            />
        );
    }
}

SignUpPage.contextType = {
    router: PropTypes.object.isRequired
};

export default SignUpPage;