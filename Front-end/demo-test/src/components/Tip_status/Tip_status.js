// @flow

import React from "react";

import './Tip_status.css';

// what is this shit???
// import type { T_Highlight } from "../../src/types";
// type T_ManuscriptHighlight = T_Highlight;
// type Props = {
//   highlights: Array<T_ManuscriptHighlight>,
//   resetHighlights: () => void
// };

const updateHash = highlight => {
  debugger;
  window.location.hash = `highlight-${highlight.id}`;
};

function Sidebar({ highlights, resetHighlights }: Props) {
  return (
    <div className="sidebar">
      <ul className="sidebar__highlights">
        {highlights.map((highlight, index) => (
          <li
            key={index}
            className="sidebar__highlight"
            onClick={() => {
              updateHash(highlight);
            }}
          >
            <div>
              <strong>{highlight.comment.text}</strong>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Sidebar;