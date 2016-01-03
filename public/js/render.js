var React = require('react');
var ReactDOM = require('react-dom');

var TweetBox = React.createClass({
  getInitialState: function() {
      console.log('init state');
    return {data: []};
  },
  loadCommentsFromServer: function() {
    $.ajax({
      url: this.props.url,
      dataType: 'json',
      cache: false,
      success: function(data) {
        this.setState({data: data});
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
  },
  componentDidMount: function() {
    this.loadCommentsFromServer();
  },
  render: function() {
      return (
        <div className="commentBox">
          <h1>Retweets</h1>
          <TweetList data={this.state.data} />
        </div>
      );
    }
});

var TweetList = React.createClass({
    render: function () {
        var tweetNodes = this.props.data.map(function (comment) {
            return (
            <Tweet user_name={ comment.user_name } text={comment.text} image_url= { comment.image_url } >
                { comment.text }
            </Tweet>
      );
    });

return (
    <div className="commentList" >
        { tweetNodes }
    </div>
    );
  }
});

var Tweet = React.createClass({
    render: function () {
        return (
            <div className="tweet" >
            <img src={this.props.image_url} alt="user profile image" />
            <div className="textDiv">
            <h3 className="tweetAuthor" >
            { this.props.user_name }
            < /h3>
            < h2 > { this.props.text } < /h2>
            </div>
            < /div>
    );
  }
});

ReactDOM.render(
    <TweetBox url="/api/getTweets" />,
    document.getElementById('content')
);