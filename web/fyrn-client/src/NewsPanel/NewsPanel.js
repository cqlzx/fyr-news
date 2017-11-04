import React from 'react';
import Auth from '../Auth/Auth';
import NewsCard from "../NewsCard/NewsCard";
import _ from 'lodash';

class NewsPanel extends React.Component {
    constructor() {
        super();

        this.handleScroll = this.handleScroll.bind(this);
        this.state = {news: null, pageNum: 1, loadedAll: false};
    }

    componentDidMount() {
        this.loadMoreNews();
        this.loadMoreNews = _.debounce(this.loadMoreNews, 1000);
        window.addEventListener('scroll', this.handleScroll);
    }

    handleScroll() {
        const scrollY = window.scrollY || window.pageYOffset || document.documentElement.scrollTop;
        if (scrollY + window.innerHeight >= document.body.offsetHeight - 50) {
            console.log('Load more news...');
            this.loadMoreNews();
        }
    }

    loadMoreNews() {
        if (this.state.loadedAll) {
            return;
        }

        let url = 'http://' + window.location.host + '/news/userId/' + Auth.getEmail() + '/pageNum/' + this.state.pageNum;
        const request = new Request(url, {
            method: 'GET',
            cache: false,
            headers: {
                'Authorization': 'bearer ' + Auth.getToken()
            }
        });

        fetch(request)
            .then((res) => res.json())
            .then((news) => {
                if (!news || news.length === 0) {
                    this.setState({loadedAll: true});
                }

                this.setState({
                    news: this.state.news ? this.state.news.concat(news) : news,
                    pageNum: this.state.pageNum + 1
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