import React, { Component } from 'react'
const axios = require('axios')

export default class Search extends Component {
    constructor(props) {
        super(props)
    
        this.state = {
             search : ''
        }

        this.handleChange = this.handleChange.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)

    }

    handleChange = (e) => {
        e.preventDefault()
        this.setState({ [e.target.name] : e.target.value })

    }

    handleSubmit = () => {
        axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';
        axios.post("http://0.0.0.0:5000/search")
            .then(resp => {
                console.log(resp)
            })
            .catch(error => {
                console.log(error);
            })
    }
    
    render() {
        return (
            <div>
                <input name='search' onChange={this.handleChange} /><br />
                <button onSubmit={this.handleSubmit}>Search</button>
            </div>
        )
    }
}
