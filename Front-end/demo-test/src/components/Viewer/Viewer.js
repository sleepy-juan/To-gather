// @flow

import React, { Component } from 'react';
import URLSearchParams from "url-search-params";
import PdfLoader from "../react-pdf-annotator/PdfLoader";
import PdfAnnotator from "../react-pdf-annotator/PdfAnnotator";
import Tip from "../react-pdf-annotator/Tip";
import Highlight from "../react-pdf-annotator/Highlight";
import Popup from "../react-pdf-annotator/Popup";
import AnswerHighlights from "../AnswerHighlights/AnswerHighlights";
import QuestionHighlights from "../QuestionHighlights/QuestionHighlights";
import Spinner from '../Spinner/Spinner';
import SidebarLeft from "../Sidebar_Left/Sidebar_Left";
import SidebarRight from "../Sidebar_Right/Sidebar_Right"
import SidebarLeftdown from "../Sidebar_Leftdown/Sidebar_Leftdown"
import SidebarRightdown from "../Sidebar_Rightdown/Sidebar_Rightdown"
import FinishedAnswer from "../Finished_Answer/Finished_Answer"
import './Viewer.css';

var newPDF = require('../../assets/turkopticon.pdf');
var client = require('../../client.js');

// this is janky in terms of IDs
const getNextId = () => String(Math.random()).slice(2);
const parseIdFromHash = () => window.location.hash.slice("#highlight-".length);
const resetHash = () => {
	window.location.hash = "";
};


const DEFAULT_URL = '../../assets/turkopticon.pdf';
const searchParams = new URLSearchParams(window.location.search);
const url = searchParams.get("url") || DEFAULT_URL;
const username = "juanlee";

class Viewer extends Component {
	state = {
		highlights: QuestionHighlights[url] ? [...QuestionHighlights[url]] : [], /*여기에 질문한 목록이 들어갑니다*/
		highlights_answer: AnswerHighlights[url] ? [...AnswerHighlights[url]] : [],
		highlights_merged: AnswerHighlights[url] ? [...AnswerHighlights[url]] : [],
		Qstate:null,
		Qstate_ans:null,
		currentAforQ:[""],
		currentAforQ_ans:[""],
		QID:null,
		QID_answer:null
	};

	constructor(){
		super();

		setTimeout(() => this.updateQuestion(), 5000);
	}

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
		return (
			<FinishedAnswer
				Qstate={highlight.comment.text}  
				currentAforQ={[""].concat(highlight.comment.answer)}            
		 	/>
		);
	}


	// on stop clicked
	handleRemove = (username, QID) => {
		const { highlights } = this.state;

		this.setState({
			highlights: highlights.filter(highlight => highlight.id !== QID)
		});

		client.endQuestion(username, QID);
	}

	handleRemove_answer = (QID) => {
		const {highlights, highlights_answer} = this.state;    
		this.setState({
			highlights_answer: highlights_answer.filter(highlight => highlight.id !== QID)
		});
	}


	updateQstate = (question, answer, QID) =>  {
		this.setState({
			Qstate: question,
			currentAforQ: answer,
			QID: QID
		});
	}

	updateQstate_answer = (question, answer, QID) =>  {
		this.setState({
			Qstate_ans: question,
			currentAforQ_ans: answer,
			QID_answer: QID
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

	// update question list
	updateQuestion() {
		var ids = client.getQuestionIds(username);
		var array = [];
		ids.forEach(function(id){
			var question = client.getQuestion(username, id);
			array.push(question);
		});

		this.setState({
			highlights_answer: array,
		});

		setTimeout(() => this.updateQuestion(), 5000);
	}

	getHighlightById(id: string) {
		const { highlights, highlights_answer } = this.state;

		return highlights.find(highlight => highlight.id === id) || highlights_answer.find(highlight => highlight.id === id);
	}


	addHighlight(username: string, highlight: highlight) {
		const { highlights} = this.state;
		const newid = getNextId();
		 
		this.setState({
			highlights: [{ ...highlight, id: newid }, ...highlights],
		});

		client.post(username, { ...highlight, id: newid });
	}

	addtomergeHighlight(highlight: highlight) {
		const { highlights, highlights_answer} = this.state;
		this.setState({
			highlights_merged: [{ ...highlight, id: getNextId() }, ...highlights].concat(highlights_answer)
		});
	}

	syncMerge(){
		const { highlights, highlights_answer } = this.state;
		this.setState({
			highlights_merged: highlights.concat(highlights_answer)
		});

	}


	render() {
		const { highlights, highlights_answer, highlights_merged, Qstate, Qstate_ans, currentAforQ,currentAforQ_ans, QID, QID_answer} = this.state;
		return (
			<div className="App" style={{ display: "flex", height: "100vh" }}>
				<div>
					<SidebarLeft
						highlights={highlights}
						resetHighlights={this.resetHighlights}
						updateQstate = {this.updateQstate}
					/>
					<SidebarLeftdown
					Qstate={Qstate}
					currentAforQ = {currentAforQ}
					QID = {QID}
					handleRemove = {this.handleRemove}
					username = {username}
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
											this.addHighlight(username, { content, position, comment });
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
											onMouseOver={popupContent =>
												setTip(highlight, highlight => popupContent)
											}                      
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
			<div>
				<SidebarRight
						highlights={highlights_answer}
						resetHighlight_answer={this.resetHighlights_answer}
						updateQstate = {this.updateQstate_answer}
					/>
				<SidebarRightdown
					Qstate={Qstate_ans}
					currentAforQ = {currentAforQ_ans}
					QID = {QID_answer}
					handleRemove_answer = {this.handleRemove_answer}
					/>
			</div>
			</div>
		);
	}
}

export default Viewer;






