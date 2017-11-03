import React from 'react';
import PropTypes from 'prop-types';
import Auth from '../Auth/Auth';
import './Base.css';

const Base = ({ children }) => (
    <div>
        <nav className="nav-bar indigo lighten-1">
            <div className="nav-wrapper">
              <a href="/" className="brand-logo">FYR News</a>
              <ul id="nav-mobile" className="right hide-on-med-and-down">
                  {
                      Auth.isAuthenticated() ?
                          (
                          <div>
                              <li><a>{Auth.getEmail()}</a></li>
                              <li><a href="/logout">Log out</a></li>
                         </div>
                          )
                          :
                          (
                          <div>
                              <li><a href="/login">Log In</a></li>
                              <li><a href="/signup">Sign Up</a></li>
                          </div>
                          )
                  }
              </ul>
            </div>
        </nav>
        <br />
        { children }
    </div>
);

Base.propTypes = {
  children: PropTypes.object.isRequired
};

export default Base;