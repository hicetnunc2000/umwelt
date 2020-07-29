import React, { Component } from 'react'
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

        axios.get("http://0.0.0.0:5000/ontology")
            .then(resp => {
                console.log(resp.data.res)
                this.setState({ ontology: resp.data.res })
            })
            .catch(error => {
                console.log(error);
            })

        axios.get("http://127.0.0.1:5000/feed")
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
                <h2>Feed Component</h2>
                <a target="_blank" rel="noopener noreferrer" href={`https://ipfs.io/ipfs/${this.state.ontology}`}>Ontology</a>
                {

                    this.state.feed.map((e) => {
                        return (
                            <div>
                                <p>
                                {e.title}<br />
                                {e.description}<br />
                                {e.tags}<br />
                                <a target="_blank" rel="noopener noreferrer" href={`https://ipfs.io/ipfs/${e.cid}`}>{`https://ipfs.io/ipfs/${e.cid}`}</a>
                                </p>
                            </div>
                        )
                    })

                }
            </div>
        )
    }
}
