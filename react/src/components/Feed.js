import React, { Component } from 'react'
import { Card, Button, CardTitle, CardText, Row, Col } from 'reactstrap';

const axios = require('axios')

export default class Feed extends Component {
    constructor(props) {
        super(props)

        this.state = {
            ontology: '',
            feed: []
        }
    }

    componentWillMount = () => {

        axios.get("http://0.0.0.0:5000/api/ontology")
            .then(resp => {
                console.log(resp.data.res)
                this.setState({ ontology: resp.data.res })
            })
            .catch(error => {
                console.log(error);
            })

        axios.get("http://127.0.0.1:5000/api/feed")
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
                <Row>
                    <Col sm="12" md={{ size: 6, offset: 3 }}>
                        <Card body>
                            <CardTitle>Upload Files</CardTitle>
                            <a target="_blank" rel="noopener noreferrer" href={`https://ipfs.io/ipfs/${this.state.ontology}`}>Ontology</a>
                            {
                                this.state.feed.map((e) => {
                                    return (
                                        <div>
                                            <Card body>
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
        )
    }
}
