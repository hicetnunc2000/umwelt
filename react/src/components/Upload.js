//rcc
//rconst

import React, { Component } from 'react'
import { CustomInput, Form, FormGroup, Label, Input, FormText } from 'reactstrap'
import { Card, Button, CardTitle, CardText, Row, Col } from 'reactstrap';
const axios = require('axios')

export default class Upload extends Component {
    constructor(props) {
        super(props)
        this.state = {
            title: '',
            description: '',
            tags: '',
            selectedFile: null,
            cid: '',
            uploaded : false
        }
        this.handleChange = this.handleChange.bind(this)
        this.onFileUpload = this.onFileUpload.bind(this)
        this.onFileChange = this.onFileChange.bind(this)
    }

    //state = {
    //    selectedFile: null
    //};

    handleChange = (event) => {

        this.setState({ [event.target.name]: event.target.value }, () => console.log(this.state))

    }

    onFileChange = event => {

        // Update the state 
        this.setState({ selectedFile: event.target.files }, () => console.log(this.state));

    };

    onFileUpload = () => {

        const formData = new FormData();

        const files = this.state.selectedFile
        console.log(this.state.selectedFile);

        Array.from(files).map((e) => formData.append(e.name, e))
        formData.append('state', JSON.stringify(this.state))
        axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';
        axios.post("http://0.0.0.0:5000/api/upload", formData)
            .then(resp => {
                console.log(resp.data   )
                this.setState({
                    cid: resp.data.res.json_cid
                })
            })
            .catch(error => {
                console.log(error);
            })
        this.setState({
            uploaded : true
        })
    };

    renderResponse = () => {

        if (this.state.uploaded) {
            return (
                <Row>
                    <Col sm="12" md={{ size: 6, offset: 3 }}>
                        <Card body style={{border : "none"}}>
                            <a href={`https://ipfs.io/ipfs/${this.state.cid}`} >{this.state.cid}</a>
                        </Card>
                    </Col>
                </Row>
            )
        }

    }

    render() {
        return (
            <div className="center">
                <Row>
                    <Col sm="12" md={{ size: 6, offset: 3 }}>
                        <Card body>
                            <CardTitle>Upload Files</CardTitle>
                            <Form>
                                <FormGroup row>
                                    <Col sm={12}>
                                        <Input type="text" name="title" placeholder="Title" onChange={this.handleChange} />
                                    </Col>
                                </FormGroup>
                                <FormGroup>
                                    <Input type="textarea" name="description" placeholder="Description" onChange={this.handleChange} />
                                </FormGroup>
                                <FormGroup row>
                                    <Col sm={12}>
                                        <Input type="text" name="tags" placeholder="Hashtags" onChange={this.handleChange} />
                                    </Col>
                                </FormGroup>
                                <FormGroup>
                                    <CustomInput type="file" onChange={this.onFileChange} multiple />
                                </FormGroup>
                                <FormGroup row>
                                    <Col sm={2}>
                                        <Button outline color="secondary" onClick={this.onFileUpload}>Submit</Button>
                                    </Col>
                                </FormGroup>
                            </Form>
                        </Card>
                    </Col>
                </Row>
                {this.renderResponse()}
            </div>
        )
    }
}