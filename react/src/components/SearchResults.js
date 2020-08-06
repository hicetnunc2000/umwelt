import React, { Component } from 'react'
import { Card, Button, CardTitle, CardText, Row, Col } from 'reactstrap';

import { useParams } from "react-router-dom"
import queryString from 'query-string';
import Feed from './Feed'
import Search from './Search'
const axios = require('axios')

export default class SearchResults extends Component {

    constructor(props) {
        super(props)

        this.state = {
            search: "",
            feed: []
        }
    }


    componentWillMount = () => {

        const query = window.location.pathname.split('/')[2]
        this.setState({ search: query })
        console.log(query)
        axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';
        axios.post("http://127.0.0.1:5000/api/search", { search: query })
            .then(resp => {
                console.log(resp.data.res)
                resp.data.res.map((e) => {
                    this.setState(prevState => ({
                        feed: [...prevState.feed, e]
                    }))
                })
            })
            .catch(error => {
                console.log(error);
            })
    }

    render() {
        return (
            <div>
                <div>
                    <Row>
                        <Col sm="12" md={{ size: 6, offset: 3 }}>
                            <Card body style={{border : "none"}}>
                                {
                                    this.state.feed.map((e) => {
                                        return (
                                            <div>
                                                <Card body style={{borderLeftStyle : "none", borderRightStyle : "none"}}>
                                                    <CardTitle><a target="_blank" rel="noopener noreferrer" href={`https://ipfs.io/ipfs/${e.file_cid}`}>{`${e.title}`}</a></CardTitle>
                                                    <CardText>{e.description}</CardText>
                                                    <CardText>{e.tags}</CardText>
                                                </Card>
                                            </div>
                                        )
                                    })
                                }
                            </Card>
                        </Col>
                    </Row>
                </div>
            </div>
        )
    }
}
