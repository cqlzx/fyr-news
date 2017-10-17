import React from 'react';
import './NewsCard.css';

class NewsCard extends React.Component {
    constructor(news) {
        super();
    }

    directToUrl(url) {
        window.open(url, '_blank');
    }

    render() {
        const news = this.props.news;

        return (
            <div className="news-container" onClick={() => this.directToUrl(news.url)}>
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