// @flow

import React from "react";

import './Sidebar_Leftdown.css';


const updateHash = highlight => {
  debugger;
  window.location.hash = `highlight-${highlight.id}`;
};

function Sidebar_Leftdown({ Qstate, currentAforQ, QID, handleRemove}: Props) {
  return (
    <div className="sidebar_leftdown">
      <div className="description">
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
        {Qstate != null ? (
        <div style={{ padding: "1rem" }}>
          <button onClick={() => handleRemove(QID)}>
          Satisfied?
          </button>
        </div>
      ) : null}
    </div>
  );
}

export default Sidebar_Leftdown;