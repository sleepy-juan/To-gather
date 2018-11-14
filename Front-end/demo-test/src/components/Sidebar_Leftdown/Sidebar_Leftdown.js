import React from 'react';
import './Sidebar_Leftdown.css';

const updateHash = highlight => {
  window.location.hash = `highlight-${highlight.id}`;
};

const Sidebar_Leftdown = ({Qstate, currentAforQ, QID, handleRemove, value, onChange, onCreate, username}) => {
  return (
    <div className="sidebar_rightdown">
      <div className="description">
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
        )}
      </div>

      {Qstate != null ? (
        <div>
        <div className="create-button-3" onClick={() => handleRemove(username, QID)}>
        Stop
        </div>
    </div>

    ) : null}
    </div>
  );
};

export default Sidebar_Leftdown;