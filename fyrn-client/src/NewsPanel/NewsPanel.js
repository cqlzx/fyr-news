import React from 'react';
import NewsCard from "../NewsCard/NewsCard";


class NewsPanel extends React.Component {
    constructor() {
        super();

        this.state = {news: null};
    }

    componentDidMount() {
        this.loadNews();
    }

    loadNews() {
        let url = 'http://' + window.location.host + '/news';
        const request = new Request(url, { method: 'GET', cache: false});

        fetch(request)
            .then((res) => res.json())
            .then((news) => {
                this.setState({
                    news: this.state.news ? this.state.news.concat(news) : news
                })
            })
    }

    renderNews() {
        const news_list = this.state.news.map((news) => {
            return (
                <a className="collection-item" key={news.digest}>
                    <NewsCard news={news}/>
                </a>
            );
        });

        return (
            <div className="collection">
                {news_list}
            </div>
        );
    }

    render() {
        if (this.state.news) {
            return (
                <div>
                    {this.renderNews()}
                </div>
            );
        } else {
            return (
                <div id="news-loading">
                    Loading...
                </div>
            );
        }
    }
}

export default NewsPanel;