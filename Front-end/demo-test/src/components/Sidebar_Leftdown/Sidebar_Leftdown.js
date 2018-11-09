// @flow

import React from "react";

import './Sidebar_Leftdown.css';


const updateHash = highlight => {
  debugger;
  window.location.hash = `highlight-${highlight.id}`;
};

function Sidebar_Leftdown({ Qstate, currentAforQ}: Props) {
  return (
    <div className="sidebar_leftdown">
      <div className="description">
        <p>
        {Qstate}
        </p>
        <p>
        {currentAforQ}
        </p>
      </div>

    </div>
  );
}

export default Sidebar_Leftdown;