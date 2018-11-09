// @flow

import React from "react";

import './Sidebar_Left.css';
import test from './test'



const updateHash = highlight => {
  debugger;
  window.location.hash = `highlight-${highlight.id}`;
};


function Sidebar({ highlights, resetHighlights, updateQstate}: Props) {
  debugger;
  return (
    <div className="sidebar_left">
      <div className="description">
        <h2>To-gather</h2>
        <p>
          To ask at the question, just drag the point that you are confused and add a question!
        </p>
      </div>


      <ul className="sidebar__highlights">
        {highlights.map((highlight, index) => (
          <li
            key={index}
            className="sidebar__highlight"
            onClick={() => {
              updateHash(highlight);
            }
          }
          >
          <div className="goto_status_button" onClick={() => updateQstate(highlight.comment.text, highlight.comment.answer, highlight.id)}
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
        </div>

          </li>
        )
        )}
      </ul>
    </div>
  );
}

export default Sidebar;