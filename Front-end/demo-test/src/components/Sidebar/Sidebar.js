// @flow

import React from "react";

import './Sidebar.css';

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
      <div className="description">
        <h2>To-gather</h2>
        <p>
          To ask a question, just drag the point that you are confused and add a question!
        </p>
      </div>

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
              {highlight.content.text ? (
                <blockquote style={{ marginTop: "0.5rem" }}>
                  {`${highlight.content.text.slice(0, 90).trim()}…`}
                </blockquote>
              ) : null}
              {highlight.content.image ? (
                <div
                  className="highlight__image"
                  style={{ marginTop: "0.5rem" }}
                >
                  <img src={highlight.content.image} alt={"Screenshot"} />
                </div>
              ) : null}
            </div>
            <div className="highlight__locationwindow.">
              Page {highlight.position.pageNumber}
            </div>
          </li>
        ))}
      </ul>
      {highlights.length > 0 ? (
        <div style={{ padding: "1rem" }}>
          <button onClick={resetHighlights}>
            Reset highlights
          </button>
        </div>
      ) : null}
    </div>
  );
}

export default Sidebar;
