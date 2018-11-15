import React from 'react';
import './Sidebar_Leftdown.css';

const Sidebar_Leftdown = ({Qstate, currentAforQ, QID, handleRemove, value, onChange, onCreate, username, setflagleft, flag_left}) => {
  return (
    <div className="sidebar_rightdown">
      <div className="description">
      {flag_left ? (<div>
        <p>
        {Qstate}
        </p>
        {currentAforQ.map((answer, index) => (
          <li>
          <div className="answer-list_left">
            <div>
              <div>{answer}</div>
            </div>
        </div>
          </li>
        )
        )} </div>) : null}
      </div>
      {((Qstate != null) && flag_left) ? (
        <div>

        <div className="create-button-3" onClick={() => 
          {handleRemove(username, QID);
           setflagleft();
           handleRemove(QID)}}>
        Stop
        </div>
    </div>

    ) : null}
    </div>
  );
};

export default Sidebar_Leftdown;