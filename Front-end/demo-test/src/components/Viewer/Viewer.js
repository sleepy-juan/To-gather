// @flow

import React, { Component } from 'react';
import URLSearchParams from "url-search-params";
// import {
//   PdfLoader,
//   PdfAnnotator,
//   Tip,
//   Highlight,
//   Popup,
//   AreaHighlight
// } from "/../../react-pdf-annotator/components";

import AreaHighlight from "../react-pdf-annotator/AreaHighlight";
import PdfLoader from "../react-pdf-annotator/PdfLoader";
import PdfAnnotator from "../react-pdf-annotator/PdfAnnotator";
import Tip from "../react-pdf-annotator/Tip";
import Highlight from "../react-pdf-annotator/Highlight";
import Popup from "../react-pdf-annotator/Popup";


//import testHighlights from "../../testHighlights";
import Spinner from '../Spinner/Spinner';
import Sidebar from "../Sidebar/Sidebar";
import Sidebar_Right from "../Sidebar_Right/Sidebar_Right"

import './Viewer.css';
var newPDF = require('../../assets/turkopticon.pdf');
// import type { T_Highlight, T_NewHighlight } from "../../src/types";
// type T_ManuscriptHighlight = T_Highlight;
// type Props = {};
// type State = {
//   highlights: Array<T_ManuscriptHighlight>
// };

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
    
  //   <Tip
  //   onOpen={transformSelection}
  //   onConfirm={comment => {
  //     this.addHighlight({ content, position, comment });

  //     hideTipAndSelection();
  //   }}
  // />
  ) : null;

const DEFAULT_URL = '../../assets/turkopticon.pdf';
const searchParams = new URLSearchParams(window.location.search);
const url = searchParams.get("url") || DEFAULT_URL;

class Viewer extends Component {
  state = {
    highlights: [],
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
  resetHighlights = () => {
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
    const { highlights } = this.state;

    return highlights.find(highlight => highlight.id === id);
  }

  // HOW DOES THIS WORK WITHOUT T_NewHighlight being defined?
  addHighlight(highlight: T_NewHighlight) {
    debugger;
    const { highlights } = this.state;
     
    this.setState({
      highlights: [{ ...highlight, id: getNextId() }, ...highlights]
    });
  }

  // HOW DOES THIS WORK WITHOUT T_NewHighlight being defined?
  editHighlight(highlight: T_NewHighlight) {
    debugger;
    const { highlights } = this.state;
    this.setState({
      highlights: highlights
    });
  }

  updateHighlight(highlightId: string, position: Object, content: Object) {
    this.setState({
      highlights: this.state.highlights.map(h => {
        return h.id === highlightId
          ? {
              ...h,
              position: { ...h.position, ...position },
              content: { ...h.content, ...content }
            }
          : h;
      })
    });
  }
  
  render() {
    const { highlights, file, numPages } = this.state;

    return (
      <div className="App" style={{ display: "flex", height: "100vh" }}>
        <Sidebar
          highlights={highlights}
          resetHighlights={this.resetHighlights}
        />

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
                      this.addHighlight({ content, position, comment });
           
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
                  const isTextHighlight = !Boolean(
                    highlight.content && highlight.content.image
                  );

                  const component = isTextHighlight ? (
                    <Highlight
                      isScrolledTo={isScrolledTo}
                      position={highlight.position}
                      comment={highlight.comment}
                    />
                  ) : (
                    <AreaHighlight
                      highlight={highlight}
                      onChange={boundingRect => {
                        this.updateHighlight(
                          highlight.id,
                          { boundingRect: viewportToScaled(boundingRect) },
                          { image: screenshot(boundingRect) }
                        );
                      }}
                    />
                  );

                  return (
                    
                    <Popup
                      popupContent={this.renderPopUp(highlight)}
                      onMouseOver={popupContent =>
                        setTip(highlight, highlight => popupContent)
                      }
                      onMouseOut={hideTip}
                      key={index}
                      children={component}
                    />
                    
                  );
                }}
                highlights={highlights}
              />
            )}
          </PdfLoader>
        </div>
      <Sidebar_Right
          highlights={highlights}
          resetHighlights={this.resetHighlights}
        />

      </div>

    );
  }
}

export default Viewer;






