import React from 'react';
import './Finished_Answer.css';

const Finished_Answer = ({Qstate, currentAforQ}) => {
  return (
    <div className="answerpopup">
        <strong>
        {Qstate}
        </strong>
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
  );
};

export default Finished_Answer;