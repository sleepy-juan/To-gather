import {Link} from 'react-router-dom'
import React, { Component } from 'react';
import {withRouter} from 'react-router-dom'
import './Register.css';

function onChange(value, option) {
   console.log('selected ${value}', option);
}

class NavForm extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      id: '',
    }

    this.submitHandler = this.submitHandler.bind(this)
    this.handleInput = this.handleInput.bind(this)

    document.title = "To-gather";
  }

  handleInput(event) {
    const target = event.target
    this.setState({
      [target.name]: target.value
    })
  }  

  saveCookie(){
    console.log("cookie");

    var userdata = "username=" + this.state.id + ";";
    document.cookie = userdata;
}

  submitHandler(event) {
    event.preventDefault()
    // do some sort of verification here if you need to
  }

  render() {
    return (
      <div>
      <div className="register_submit">
          <form onSubmit={this.submitHandler}>
          <div className="register_input">
            <input
              type='text'
              name='id'
              value={this.state.what}
              onChange={this.handleInput} />
              </div>
           <Link to="/qna" onClick={() => this.saveCookie()}>
           <div className="button">
        Click me!
        </div>
           </Link>      
        </form>
        </div>
                <div style={{textAlignVertical: "center",textAlign: "center",}}> Please select your characteristics. </div> <div style={{textAlignVertical: "center",textAlign: "center",}}>These characteristics would help you to get answers from other users! :)</div>
        <div>
        <body className="select_group">
          <select name = "school" multiple>
            <optgroup label = "DORM">
            <option value="Heemang"> Heemang
            </option>
            <option value="Areum"> Areum </option>
            </optgroup>
          </select>
          <select name = "grade" multiple>
          <optgroup label = "GRADE">
            <option value="1"> 1 </option>
            <option value="2"> 2 </option>
            <option value="3"> 3 </option>
            <option value="4"> 4 </option>
          </optgroup>
          </select>
          <select name = "major" multiple>
          <optgroup label = "MAJOR">
            <option value="CS"> CS </option>
            <option value="MAS"> MAS </option>
            <option value="ME"> ME </option>
          </optgroup>
          </select>
          <select name = "location" multiple>
          <optgroup label = "LOCATION">
            <option value="KOREA"> KOREA </option>
            <option value="FOREIGNER"> FOREIGNER </option>
          </optgroup>
          </select>
          <select name = "club" multiple>
          <optgroup label = "CLUB">
            <option value="ART"> ART </option>
            <option value="MUSIC"> MUSIC </option>
            <option value="EXERCISE"> EXERCISE </option>
          </optgroup>
          </select>
        </body>
        </div>
      </div>
    )
  }
}

export default withRouter(NavForm)