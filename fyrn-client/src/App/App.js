import 'materialize-css/dist/css/materialize.min.css';

import React from 'react';
import logo from './logo.png';
import './App.css';
import NewsPanel from '../NewsPanel/NewsPanel';

class App extends React.Component {
    render() {
        return (
            <div>
                <img className='logo' src={logo} alt='LOGO' />
                <div className='container'>
                    <NewsPanel></NewsPanel>
                </div>
            </div>
        );
    };
}

export default App;