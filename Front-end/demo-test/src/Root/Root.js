import React from 'react';
import { BrowserRouter } from 'react-router-dom';
import App from '../components/App/App';

const Root = () => (
    <BrowserRouter>
        <App/>
    </BrowserRouter>
);

export default Root;