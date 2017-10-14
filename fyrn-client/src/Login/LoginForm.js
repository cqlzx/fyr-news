import React from 'react';
import PropTypes from 'prop-types';
import './LoginForm.css';


const LoginForm = ({
                       onSubmit,
                       onChange,
                       errors,
                       user
                   }) => (
    <div className="container">
        <div className="card-panel form-panel">
            <form className="col s12" action="/" onSubmit={onSubmit}>
                <h4 className="center-align">Login</h4>
                {errors.email && <div className="error-message">{errors.email}</div>}
                <div className="row">
                    <div className="input-field col s12">
                        <input id="email" type="email" name="email" className="validate" onChange={onChange}/>
                        <label htmlFor="email">Email</label>
                    </div>
                </div>
                {errors.password && <div className="error-message">{errors.password}</div>}
                <div className="row">
                    <div className="input-field col s12">
                        <input id="password" type="password" name="password" className="validate" onChange={onChange}/>
                        <label htmlFor="password">Password</label>
                    </div>
                </div>
                <div className="row right-align">
                    <button className="btn waves-effect waves-light" type="submit" name="action">Log In
                        <i className="material-icons right">send</i>
                    </button>
                </div>
                <div className="row right-align">
                    <div>
                        <span>New to FYR News? <a href="/signUp">Sign Up</a> here</span>
                    </div>
                </div>
            </form>
        </div>
    </div>
);

LoginForm.PropTypes = {
    onSubmit: PropTypes.func.required,
    onchange: PropTypes.func.required,
    errors: PropTypes.object.required,
    user: PropTypes.object.required
};

export default LoginForm;