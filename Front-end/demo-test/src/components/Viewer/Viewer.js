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
import client from "../../client.js"

var newPDF = require('../../assets/turkopticon.pdf');
//var client = require('../../client.js');

// this is janky in terms of IDs
const getNextId = () => String(Math.random()).slice(2);
const parseIdFromHash = () => window.location.hash.slice("#highlight-".length);
const resetHash = () => {
	window.location.hash = "";
};


const DEFAULT_URL = '../../assets/turkopticon.pdf';
const searchParams = new URLSearchParams(window.location.search);
const url = searchParams.get("url") || DEFAULT_URL;

class Viewer extends Component {
	state = {
		highlights: [], // 왼쪽 사이드바
		highlights_answer: AnswerHighlights[url] ? [...AnswerHighlights[url]] : [], //오른쪽 사이드바
		highlights_merged: AnswerHighlights[url] ? [...AnswerHighlights[url]] : [], //하이라이트 쳐질 거
		Qstate:null,
		Qstate_ans:null,
		currentAforQ:[""],
		currentAforQ_ans:[""],
		QID:null,
		QID_answer:null,
		answer:null,
		highlights_public: [], // 전체공개
		flag_left: false,
		flag_right: false
	};

	constructor(){
		super();

		var cookieData = document.cookie;
		var start_index = cookieData.indexOf("username=");
		var end_index = cookieData.indexOf('\n', start_index);

		if(end_index != -1)
			this.username = cookieData.substring(start_index+9, end_index);
		else
			this.username = cookieData.substring(start_index+9);

		this.updateQuestion();
		this.updateConfirm();
		this.updateHightlights();

		document.title = "To-gather";
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
	handleRemove = (QID) => {
		const { highlights } = this.state;

		this.setState({
			highlights: highlights.filter(highlight => highlight.id !== QID)
		});

		client.endQuestion(this.username, QID);
	}

	handleRemove_ignore = (QID) => {
		var {highlights, highlights_answer, highlights_merged} = this.state;    
		this.setState({
			highlights_answer: highlights_answer.filter(highlight => highlight.id !== QID),
			highlights_merged: highlights_merged.filter(highlight => highlight.id !== QID)
		});
	}

	handleRemove_answer = (QID) => {
		var {highlights, highlights_answer, highlights_merged} = this.state;  

		this.setState({
			highlights_answer: highlights_answer.filter(highlight => highlight.id !== QID),
			highlights_merged: highlights_merged.filter(highlight => highlight.id !== QID)
		});

		var format = this.getHighlightById(QID);
		format.content.user = this.username;
		format.comment.text = this.state.answer;

		client.answer(this.username, format);
	}


	updateQstate = (question, answer, QID) =>  {
		this.setState({
			Qstate: question,
			currentAforQ: answer,
			QID: QID
		});

		var username = this.username;
		
		client.getAnswer(username, QID).then(
			body => (function(body, viewer, question, QID){

			var splited = body.trim().split('\n');
			var data = [];
			var response = '';

			if(splited.length == 1){
				response = splited[0];
			}
			else{
				data = splited.slice(1);
				response = splited[0];
			}

			var questions = data;

			var answer = [];

			while(data.length > 0){
				var size = parseInt(data[0]);
				var format = data.slice(1, size + 1);
				format = client.parseFormat(format.join('\n'))

				answer.push(format.comment.text);

				data = data.slice(size + 1);
			}

			viewer.setState({
				Qstate: question,
				currentAforQ: answer,
				QID: QID,
			});
		})(body, this, question, QID));
	}

	updateQstate_answer = (question, answer, QID) =>  {
		this.setState({
			Qstate_ans: question,
			currentAforQ_ans: answer,
			QID_answer: QID,
		});
	}

	resetHighlights_answer = () => {
		this.setState({
			highlights: []
		});
	};

	/*w질문을 저장하는 함수*/
	handleAnswer = (event) => {
	    const target = event.target
	    this.setState({
	      answer: target.value
	    })
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
		var username = this.username;
		
		client.getQuestionIds(username).then(
			body => (function(body, viewer){

			var splited = body.trim().split('\n');
			var data = [];
			var response = '';

			if(splited.length == 1){
				response = splited[0];
			}
			else{
				data = splited.slice(1);
				response = splited[0];
			}

			var ids = data;

			viewer.setState({
				highlights_answer: [],
			});

			ids.forEach(function(id){
				var format = '';
				client.getQuestion(username, id).then(function(res){
					//console.log("res: " + res);

					var splited = res.trim().split('\n');
					var response = splited[0];
					var format = splited.slice(1);

					format = client.parseFormat(format.join('\n'));

					var array = viewer.state.highlights_answer;
					array.push(format);

					viewer.setState({
						highlights_answer: array,
					});
				});
			});
		})(body, this));
		setTimeout(() => this.updateQuestion(), 5000);
	}

	// update confirm list
	updateConfirm() {
		var username = this.username;
		
		client.getConfirms(username).then(
			body => (function(body, viewer){

			var splited = body.trim().split('\n');
			var data = [];
			var response = '';

			if(splited.length == 1){
				response = splited[0];
			}
			else{
				data = splited.slice(1);
				response = splited[0];
			}

			var ids = data;

			viewer.setState({
				highlights: [],
			});

			ids.forEach(function(id){
				var format = '';
				client.getQuestion(username, id).then(function(res){
					//console.log("res: " + res);

					var splited = res.trim().split('\n');
					var response = splited[0];
					var format = splited.slice(1);

					format = client.parseFormat(format.join('\n'));

					var array = viewer.state.highlights;
					array.push(format);
					viewer.setState({
						highlights: array,
					});
				});
			});
		})(body, this));
		setTimeout(() => this.updateConfirm(), 5000);
	}

	// update highlights
	updateHightlights() {
		var username = this.username;
		
		client.getOwns(username).then(
			body => (function(body, viewer){

			var splited = body.trim().split('\n');
			var data = [];
			var response = '';

			if(splited.length == 1){
				response = splited[0];
			}
			else{
				data = splited.slice(1);
				response = splited[0];
			}

			var ids = data;

			viewer.setState({
				highlights_merged: [],
			});

			ids.forEach(function(id){
				var format = '';
				client.getQuestion(username, id).then(function(res){
					//console.log("res: " + res);

					var splited = res.trim().split('\n');
					var response = splited[0];
					var format = splited.slice(1);

					format = client.parseFormat(format.join('\n'));

					var array = viewer.state.highlights;
					array.push(format);
					viewer.setState({
						highlights_merged: array,
					});
				});
			});
		})(body, this));
		setTimeout(() => this.updateHightlights(), 5000);
	}

	getHighlightById(id: string) {
		const { highlights, highlights_answer } = this.state;

		return highlights.find(highlight => highlight.id === id) || highlights_answer.find(highlight => highlight.id === id);
	}


	addHighlight(highlight: highlight) {
		var { highlights, highlights_answer, highlights_merged} = this.state;
		const newid = getNextId();
		 
		var new_question = { ...highlight, id: newid };

		this.setState({
			highlights: [{ ...highlight, id: newid }, ...highlights],
			highlights_merged: [{ ...highlight, id: newid }, ...highlights_merged]
		});

		client.post(this.username, { ...highlight, id: newid });
	}

	addtomergeHighlight(highlight: highlight) {
		const { highlights, highlights_answer} = this.state;
		this.setState({
			highlights_merged: [{ ...highlight, id: getNextId() }, ...highlights].concat(highlights_answer)
		});
	}

	syncMerge() {
		const { highlights, highlights_answer } = this.state;
		this.setState({
			highlights_merged: highlights.concat(highlights_answer)
		});

	}

	setflagleft = () => {
		const { highlights, highlights_answer, highlights_merged, Qstate, Qstate_ans, currentAforQ,currentAforQ_ans, QID, QID_answer, answer, highlights_public, flag_left, flag_right} = this.state;
		if (flag_left == true) {
			this.setState({
				flag_left: false
			});
		}
		else {
			this.setState({
				flag_left: true
			});
		}
	}

	setflagright = () => {
		const { highlights, highlights_answer, highlights_merged, Qstate, Qstate_ans, currentAforQ,currentAforQ_ans, QID, QID_answer, answer, highlights_public, flag_left, flag_right} = this.state;
		if (flag_right == true) {
			this.setState({
				flag_right: false
			});
		}
		else {
			this.setState({
				flag_right: true
			});
		}
	}


	render() {
		const { highlights, highlights_answer, highlights_merged, Qstate, Qstate_ans, currentAforQ,currentAforQ_ans, QID, QID_answer, answer, highlights_public, flag_left, flag_right} = this.state;
		return (
			<div className="App" style={{ display: "flex", height: "100vh" }}>
				<div>
					<SidebarLeft
						highlights={highlights}
						resetHighlights={this.resetHighlights}
						updateQstate = {this.updateQstate}
						setflagleft = {this.setflagleft}
					/>
					<SidebarLeftdown
					Qstate={Qstate}
					currentAforQ = {currentAforQ}
					QID = {QID}
					handleRemove = {this.handleRemove}
					username = {this.username}
					setflagleft = {this.setflagleft}
					flag_left = {flag_left}
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
						setflagright = {this.setflagright}
					/>
				<SidebarRightdown
					Qstate={Qstate_ans}
					currentAforQ = {currentAforQ_ans}
					QID = {QID_answer}
					handleRemove_answer = {this.handleRemove_answer}
					handleRemove_ignore = {this.handleRemove_ignore}
					handleAnswer = {this.handleAnswer}
					setflagright = {this.setflagright}
					flag_right = {flag_right}
					/>
			</div>
			</div>
		);
	}
}

export default Viewer;






