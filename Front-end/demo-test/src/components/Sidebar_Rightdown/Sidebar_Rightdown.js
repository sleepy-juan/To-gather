import React from 'react';
import './Sidebar_Rightdown.css';

const updateHash = highlight => {
  debugger;
  window.location.hash = `highlight-${highlight.id}`;
};

const Sidebar_Rightdown = ({Qstate, currentAforQ, QID, handleRemove_ignore, handleRemove_answer, value, onChange, onCreate}) => {
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
        <div>
        <input value={value} onChange={onChange} placeholder="Please help!"/>
        <div className="create-button-1" onClick={() => handleRemove_ignore(QID)}>
        Ignore
        </div>
        <div className="create-button-2" onClick= {() => handleRemove_answer(QID)}>
      Answer
      </div>
    </div>

    ) : null}

    </div>
  );
};

export default Sidebar_Rightdown;