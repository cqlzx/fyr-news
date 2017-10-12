import React from 'react';
import './NewsCard.css';

class NewsCard extends React.Component {
    constructor(news) {
        super();
    }

    render() {
        const news = this.props.news;

        return (
            <div className="news-container">
                <div className="row">
                    <div className="col s4 fill">
                        <img className="news-image" src={news.urlToImage} alt="Not showing"/>
                    </div>

                    <div className="col s8">
                        <h5 className="news-title">{news.title}</h5>
                        <div className="news-description">{news.description}</div>
                        <div className="news-tags">
                            {news.source && <div className="chip tag-source">{news.source}</div>}
                            {news.reason && <div className="chip tag-reason">{news.reason}</div>}
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

export default NewsCard;