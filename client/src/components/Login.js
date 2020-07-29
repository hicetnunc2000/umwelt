import React, { Component } from 'react'
const axios = require('axios')

export default class Login extends Component {

    constructor(props) {
        super(props)

        this.state = {
            login: '',
            pass: ''
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
        axios.post("http://0.0.0.0:5000/register")
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
                <h2>Login Component</h2>
                <input name='login' onChange={this.handleChange} /><br />
                <input name='pass' onChange={this.handleChange} /><br />
                <button onSubmit={this.handleSubmit}>Login</button>
            </div>
        )
    }
}
