"use strict";

exports.__esModule = true;

var _react = require("react");

var _react2 = _interopRequireDefault(_react);

require("../../assets/style/Tip.css");
var _extends = Object.assign || function (target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i]; for (var key in source) { if (Object.prototype.hasOwnProperty.call(source, key)) { target[key] = source[key]; } } } return target; };
var _closeurl= require("../../assets/lib/close.png");
var _createurl= require("../../assets/lib/create.png");
var _cancelurl= require("../../assets/lib/cancel.png");
var _saveurl= require("../../assets/lib/done.png");

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var Tip = function (_Component) {
  _inherits(Tip, _Component);

  function Tip() {
    var _temp, _this, _ret;

    _classCallCheck(this, Tip);

    for (var _len = arguments.length, args = Array(_len), _key = 0; _key < _len; _key++) {
      args[_key] = arguments[_key];
    }

    return _ret = (_temp = (_this = _possibleConstructorReturn(this, _Component.call.apply(_Component, [this].concat(args))), _this), _this.state = {
      compact: true,
      text: "",
      emoji: ""
    }, _temp), _possibleConstructorReturn(_this, _ret);
  }

  // for TipContainer
  Tip.prototype.componentDidUpdate = function componentDidUpdate(nextProps, nextState) {
    var onUpdate = this.props.onUpdate;


    if (onUpdate && this.state.compact !== nextState.compact) {
      onUpdate();
    }
  };
  //componentWillMount
  Tip.prototype.componentWillMount = function componentDidUpdate() {
    var editText= this.props.highlight===undefined? this.state.text:
    this.props.highlight.comment.text
    this.setState({ text: editText });
    this.setState({isEdit:this.props.isEdit})
    };
  

  Tip.prototype.render = function render() {
    var _this2 = this;

    var _props = this.props,
        onConfirm = _props.onConfirm,
        onOpen = _props.onOpen,
        onEdit= _props.onEdit,
        highlight = _props.highlight,
        isEdit =_props.isEdit;

    var _state = this.state,
        compact = _state.compact,
        text = _state.text,
        emoji = _state.emoji,
        isEdit= _state.isEdit;

    return _react2.default.createElement(
      "div",
      { className: "Tip" },
      // compact ? _react2.default.createElement(
      //   "div",
      //   {
      //     className: "Tip__compact",
      //     onClick: function onClick() {
      //       onOpen();
      //       _this2.setState({ compact: false });
      //     }
      //   },
      //   // "Add highlight"
      //   _react2.default.createElement(
      //     "img",
      //     {
      //       src:_createurl
      //     },
      //   )
      // ) 
      // :
       _react2.default.createElement(
        "form",
        {
          className: "Tip__card",
          onSubmit: function onSubmit(event) {
            event.preventDefault();
            
            onConfirm({ text: text, emoji: emoji });
          }
        },
        _react2.default.createElement(
          "img",
          {
            src:_closeurl,
            className:"cancel"
          },
        ),
        
        _react2.default.createElement(
          "div",
          null,
          _react2.default.createElement("textarea", {
            width: "50%",
            placeholder: "Enter a question",
            autoFocus: true,
            value:  text,
            onChange: function onChange(event) {
              
              return _this2.setState({ text: event.target.value });
            },
            ref: function ref(node) {
              if (node) {
                node.focus();
              }
            }
          }),
        ),
        _react2.default.createElement(
          "div",
          null,
           _react2.default.createElement("input", { type: "submit", value:"" }),
           _react2.default.createElement("img",   { src:_closeurl, className:"btn_img"}),
           _props.highlight===undefined && compact?null:_react2.default.createElement("img",   { src:_createurl, className:"btn_img",
           onClick: function onclick(event) {
            event.preventDefault();
            var updateText = _extends({}, highlight.comment, {
              text: _state.text,
              emoji: _state.emoji
            });
            onEdit(updateText);
            // return _this2.setState({isEdit:false})
          }},
          
          ),
          // _react2.default.createElement("input", { type: "button", className: "edit" }),
         
        )
      )
    );
  };

  return Tip;
}(_react.Component);

exports.default = Tip;
module.exports = exports["default"];