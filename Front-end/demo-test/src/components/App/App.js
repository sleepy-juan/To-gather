import React, { Component } from 'react';
import Viewer from '../Viewer/Viewer';
import {Route} from 'react-router-dom';
import Register from '../Register/Register'

class App extends Component {
	state = {
		id:"",
		link:""
	};

  render() {
    return (
     <div>
    	<Route exact path="/" component={Register}/>
		<Route exact path="/qna" component={Viewer}/>      
	</div>
    )
  }
}

export default App;
