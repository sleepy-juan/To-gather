import React from 'react';
import ReactDOM from 'react-dom';
import Root from './Root/Root'
import './index.css';
import App from './components/App/App';
import registerServiceWorker from './registerServiceWorker';
export {default as Viewer} from './components/Viewer/Viewer'
export {default as Register} from './components/Register/Register'

ReactDOM.render(<Root />, document.getElementById('root'));
