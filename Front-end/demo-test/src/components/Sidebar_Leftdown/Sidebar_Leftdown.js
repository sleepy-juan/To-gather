// @flow

import React from "react";

import './Sidebar_Leftdown.css';


const updateHash = highlight => {
  debugger;
  window.location.hash = `highlight-${highlight.id}`;
};

function Sidebar_Leftdown({ Qstate, }: Props) {
  return (
    <div className="sidebar_leftdown">
      <div className="description">
        <p>
        {Qstate}
        </p>
      </div>

    </div>
  );
}

export default Sidebar_Leftdown;