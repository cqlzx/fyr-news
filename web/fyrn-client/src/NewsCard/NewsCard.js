import React from 'react';
import Auth from '../Auth/Auth';
import './NewsCard.css';

class NewsCard extends React.Component {
    constructor(news) {
        super();
        this.directToUrl = this.directToUrl.bind(this);
    }

    directToUrl(url) {
        event.preventDefault();
        this.sendClickLog();
        window.open(this.props.news.url, '_blank');
    }

    sendClickLog() {
        const url = 'http://localhost:3000/news/userId/' + Auth.getEmail()
                  + '/newsId/' + this.props.news.digest;

        const request = new Request(encodeURI(url), {
          method: 'POST',
          headers: {
            'Authorization': 'bearer ' + Auth.getToken(),
          },
          cache: false});

        fetch(request);
    }

    render() {
        const news = this.props.news;

        return (
            <div className="news-container" onClick={this.directToUrl}>
                <div className="row">
                    <div className="col s4 fill">
                        <img className="news-image" src={news.urlToImage} alt="Not showing"/>
                    </div>

                    <div className="col s8">
                        <h4 className="news-title">{news.title}</h4>
                        <div className="news-description">{news.description}</div>
                        <div className="news-tags">
                            {news.source && <div className="chip green tag">{news.source}</div>}
                            {news.reason && <div className="chip light-blue tag">{news.reason}</div>}
                            {news.time && <div className="chip amber tag">{news.time}</div>}
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

export default NewsCard;