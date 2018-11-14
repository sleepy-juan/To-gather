import React, {Component} from 'react';
import './Sidebar_Rightdown.css';


const Sidebar_Rightdown = ({Qstate, currentAforQ, QID, handleRemove_answer, handleRemove_ignore, handleAnswer}) => {
  return (
    <div className="sidebar_rightdown">
    <div>
      <div className="description" >
        <p>
        {Qstate}
        </p>
        {currentAforQ.map((answer, index) => (
          <li>
          <div className="answer-list">
            <div>
              <div>{answer}</div>
            </div>
        </div>
          </li>
        )
        )}
      </div>

    </div>
    {Qstate != null ? (
        <form>
        <input onChange={handleAnswer} placeholder="Please help!"/>
        <div className="create-button-1" onClick={() => handleRemove_ignore(QID)}>
        Ignore
        </div>
        <div className="create-button-2" onClick= {() => handleRemove_answer(QID)}>
      Answer
      </div>
    </form>

    ) : null}

    </div>
  );
};

export default Sidebar_Rightdown;