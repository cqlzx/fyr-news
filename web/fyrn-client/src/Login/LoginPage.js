import 'materialize-css/dist/css/materialize.min.css';
import 'materialize-css/dist/js/materialize.js';

import React from 'react';
import LoginForm from './LoginForm';

class LoginPage extends React.Component {
    constructor(props) {
        super(props);

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

        //TODO: submit form
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

export default LoginPage;