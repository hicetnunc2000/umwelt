//rcc
//rconst

import React, { Component } from 'react'
const axios = require('axios')

export default class Upload extends Component {
    constructor(props) {
        super(props)
        this.state = {
            title : '',
            description : '',
            tags : '',
            selectedFile: null
        }
        this.handleChange = this.handleChange.bind(this)
        this.onFileUpload = this.onFileUpload.bind(this)
        this.onFileChange = this.onFileChange.bind(this)
    }

    //state = {
    //    selectedFile: null
    //};

    handleChange = (event) => {

        this.setState({ [event.target.name] : event.target.value }, () => console.log(this.state))

    }

    onFileChange = event => {

        // Update the state 
        this.setState({ selectedFile : event.target.files }, () => console.log(this.state));

    };

    onFileUpload = () => {

        const formData = new FormData();

        const files = this.state.selectedFile
        console.log(this.state.selectedFile);

        Array.from(files).map((e) => formData.append(e.name, e))
        formData.append('state', JSON.stringify(this.state))
        axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';
        axios.post("http://0.0.0.0:5000/upload", formData)
            .then(resp => {
                console.log(resp)
            })
            .catch(error => {
                console.log(error);
            })
    };

    render() {
        return (
            <div>
                <h2>Upload Component</h2>
                <input type="text" name="title" placeholder="title" onChange={this.handleChange} /><br />
                <input type="text" name="description" placeholder="description" onChange={this.handleChange} /><br />
                <input type="text" name="tags" placeholder="tags" onChange={this.handleChange} /><br />
                <input type="file" onChange={this.onFileChange} multiple /><br />
                <button onClick={this.onFileUpload}>
                    Upload
                </button>
            </div>
        )
    }
}