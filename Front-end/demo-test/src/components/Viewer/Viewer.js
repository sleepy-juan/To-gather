// @flow

import React, { Component } from 'react';
import URLSearchParams from "url-search-params";
import AreaHighlight from "../react-pdf-annotator/AreaHighlight";
import PdfLoader from "../react-pdf-annotator/PdfLoader";
import PdfAnnotator from "../react-pdf-annotator/PdfAnnotator";
import Tip from "../react-pdf-annotator/Tip";
//import Tip_status from "../Tip_status/Tip_status";
import Highlight from "../react-pdf-annotator/Highlight";
import Popup from "../react-pdf-annotator/Popup";
import AnswerHighlights from "../AnswerHighlights/AnswerHighlights";
import Spinner from '../Spinner/Spinner';
import Sidebar_Left from "../Sidebar_Left/Sidebar_Left";
import Sidebar_Right from "../Sidebar_Right/Sidebar_Right"
import Sidebar_Leftdown from "../Sidebar_Leftdown/Sidebar_Leftdown"
import './Viewer.css';
var newPDF = require('../../assets/turkopticon.pdf');

// this is janky in terms of IDs
const getNextId = () => String(Math.random()).slice(2);
const parseIdFromHash = () => window.location.hash.slice("#highlight-".length);
const resetHash = () => {
  window.location.hash = "";
};

const HighlightPopup = ({ comment}) =>

comment.text ? (
    <div className="Highlight__popup">
     
      <Tip
                    onOpen={null}
                    onConfirm={(comment,position) => {
                      this.addHighlight({  position,comment });

                      
                    }}
                  />
    </div>

  ) : null;

const DEFAULT_URL = '../../assets/turkopticon.pdf';
const searchParams = new URLSearchParams(window.location.search);
const url = searchParams.get("url") || DEFAULT_URL;

class Viewer extends Component {
  state = {
    highlights: AnswerHighlights[url] ? [...AnswerHighlights[url]] : [], /*여기에 질문한 목록이 들어갑니다*/
    highlights_answer: AnswerHighlights[url] ? [...AnswerHighlights[url]] : [],
    highlights_merged: AnswerHighlights[url] ? [...AnswerHighlights[url]] : [],
    Qstate:null,
    currentAforQ:null
  };


  onFileChange = e => {
    this.setState({
      file: e.target.files[0],
    });
  }

  onDocumentLoadSuccess = ({ numPages }) => {
    this.setState({
      numPages,
    });
  }

  renderEdit(updateText: object, highlight:object)
  {
    console.log('event',updateText);
    highlight.comment.text= updateText.text;
    this.editHighlight({ highlight});
  }


  renderPopUp(highlight){
    console.log('comment',highlight);
    var comment = highlight.comment.text;
    return (
      
    <Tip
    onOpen ={this.transformSelection}
    isEdit={true}
    onConfirm={(highlight) => {
      this.addHighlight({ highlight});
     
    }} 
    
    // onEdit ={value => this.renderEdit.bind(this,value)} 

    onEdit={updateText => {
      this.renderEdit(
        updateText,
        highlight
      );
    }}
    highlight={highlight}              
     />
  );
  }
  resetHighlights(highlight){
   const { highlights, highlights_answer, highlights_merged, file, numPages } = this.state;
    this.setState({
      highlights: [],
      highlights_merged : highlights_answer
    });
  }

  updateQstate = (question, answer) =>  {
    this.setState({
      Qstate: question,
      currentAforQ: answer
    });
  }

  resetHighlights_answer = () => {
    this.setState({
      highlights: []
    });
  };

  scrollViewerTo = (highlight: any) => {};

  scrollToHighlightFromHash = () => {
    const highlight = this.getHighlightById(parseIdFromHash());

    highlight && this.scrollViewerTo(highlight);
  };

  componentDidMount() {
    window.addEventListener(
      "hashchange",
      this.scrollToHighlightFromHash,
      false
    );
  }

  getHighlightById(id: string) {
    const { highlights, highlights_answer } = this.state;

    return highlights.find(highlight => highlight.id === id) || highlights_answer.find(highlight => highlight.id === id);
  }


  addHighlight(highlight: highlight) {
    const { highlights, highlights_answer, highlight_merged } = this.state;
     
    this.setState({
      highlights: [{ ...highlight, id: getNextId() }, ...highlights],
    });

  }

  addtomergeHighlight(highlight: highlight) {
    const { highlights, highlights_answer, highlights_merged } = this.state;
    this.setState({
      highlights_merged: [{ ...highlight, id: getNextId() }, ...highlights].concat(highlights_answer)
    });
  }

  syncMerge(){
    const { highlights, highlights_answer, highlights_merged } = this.state;
    this.setState({
      highlights_merged: highlights.concat(highlights_answer)
    });

  }


  render() {
    const { highlights, highlights_answer, highlights_merged, Qstate, currentAforQ, file, numPages } = this.state;

    return (
      <div className="App" style={{ display: "flex", height: "100vh" }}>
        <div>
          <Sidebar_Left
            highlights={highlights}
            resetHighlights={this.resetHighlights}
            updateQstate = {this.updateQstate}
          />
          <Sidebar_Leftdown
          Qstate={Qstate}
          currentAforQ = {currentAforQ}
          />
        </div>

        <div
          style={{
            height: "r0vh",
            width: "75vw",
            overflowY: "scroll",
            position: "relative"
          }}
        >
          <PdfLoader url={ newPDF } beforeLoad={<Spinner />}>
            {pdfDocument => (
              <PdfAnnotator
                pdfDocument={pdfDocument}
                enableAreaSelection={event => event.altKey}
                onScrollChange={resetHash}
                scrollRef={scrollTo => {
                  this.scrollViewerTo = scrollTo;

                  this.scrollToHighlightFromHash();
                }}
                url={ url }
                onSelectionFinished={(
                  position,
                  content,
                  hideTipAndSelection,
                  transformSelection
                ) => (
                  <Tip
                    onOpen={transformSelection}
                    onConfirm={comment => {
                      debugger;
                      this.addHighlight({ content, position, comment });
                      this.addtomergeHighlight({ content, position, comment });
                      hideTipAndSelection();
                    }}
                    isEdit={false}
                  />
                )}
                highlightTransform={(
                  highlight,
                  index,
                  setTip,
                  hideTip,
                  viewportToScaled,
                  screenshot,
                  isScrolledTo
                ) => {
                  const component =  (
                    <Highlight
                      isScrolledTo={isScrolledTo}
                      position={highlight.position}
                      comment={highlight.comment}
                    />
                  );

                  return (
                    
                    <Popup
                      popupContent={this.renderPopUp(highlight)}
                      onMouseOver={hideTip}
                      onMouseOut={hideTip}
                      key={index}
                      children={component}
                    />
                    
                  );
                }}
                highlights={highlights_merged}
              />
            )}
          </PdfLoader>
        </div>

      <Sidebar_Right
          highlights={highlights_answer}
          resetHighlight_answer={this.resetHighlights_answer}
        />
      </div>


    );
  }
}

export default Viewer;






