import React from 'react';
import PropTypes from 'prop-types';
import './SignUpForm.css';


const SignUpForm = ({
                       onSubmit,
                       onChange,
                       errors,
                       user
                   }) => (
    <div className="container">
        <div className="card-panel form-panel">
            <form className="col s12" action="/" onSubmit={onSubmit}>
                <h4 className="center-align">Sign Up</h4>
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
                {errors.confirmPassword && <div className="error-message">{errors.confirmPassword}</div>}
                <div className="row">
                    <div className="input-field col s12">
                        <input id="confirmPassword" type="password" name="confirmPassword" className="validate" onChange={onChange}/>
                        <label htmlFor="password">Confirm Password</label>
                    </div>
                </div>
                <div className="row right-align">
                    <button className="btn waves-effect waves-light" type="submit" name="action">Sign Up
                    </button>
                </div>
            </form>
        </div>
    </div>
);

SignUpForm.PropTypes = {
    onSubmit: PropTypes.func.required,
    onChange: PropTypes.func.required,
    errors: PropTypes.object.required,
    user: PropTypes.object.required
};

export default SignUpForm;