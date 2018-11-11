import {Link} from 'react-router-dom'
import React, { Component } from 'react';
import {withRouter} from 'react-router-dom'

// file: src/components/PhoneForm.js

class NavForm extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      id: '',
    }

    this.submitHandler = this.submitHandler.bind(this)
    this.handleInput = this.handleInput.bind(this)
  }

  handleInput(event) {
    const target = event.target
    this.setState({
      [target.name]: target.value
    })
  }  

  submitHandler(event) {
    event.preventDefault()
    // do some sort of verification here if you need to
    this.props.push('/qna', this.state.id)
  }

  render() {
    return (
      <form onSubmit={this.submitHandler}>
        <input
          type='text'
          name='id'
          value={this.state.what}
          onChange={this.handleInput} />
 		<Link to="/qna" onClick={() => alert(this.state.id)}>
     		<button type="button" >
          Click Me!
     		</button>
 		</Link>      
 	</form>
    )
  }
}

export default withRouter(NavForm)