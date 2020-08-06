import React, { Component } from 'react'
import { Redirect, useHistory } from 'react-router-dom'
import { InputGroup, InputGroupAddon, Button, Input, Card, Row, Col } from 'reactstrap';
import 'bootstrap/dist/css/bootstrap.css';

const axios = require('axios')

export default class Search extends Component {
    constructor(props) {
        super(props)

        this.state = {
            search: '',
            redirect: false
        }

        this.handleChange = this.handleChange.bind(this)
        this.onSubmit = this.onSubmit.bind(this)

    }

    handleChange = (e) => {
        e.preventDefault()
        this.setState({ [e.target.name]: e.target.value })

    }

    componentDidMount = () => {
        console.log(this.state.redirect)
    }

    onSubmit = (e) => {
        e.preventDefault()

        this.setState({
            redirect: true
        })

        console.log(this.state.redirect)

    }

    renderRedirect = () => {
        if (this.state.redirect) {
            return <Redirect to={`/search/${this.state.search}`} />
        }
    }

    render() {

        return (
            <div >
                {this.renderRedirect()}
                <Row>
                    <Col sm="12" md={{ size: 6, offset: 3 }}>
                        <Card body style={{ border: "none" }}>
                            <form onSubmit={this.onSubmit}>
                                <InputGroup>
                                    <Input name="search" onChange={this.handleChange} />
                                    <InputGroupAddon addonType="append">
                                        <Button type="submit" color="secondary" >Search</Button>
                                    </InputGroupAddon>
                                </InputGroup>
                            </form>
                        </Card>
                    </Col>
                </Row>
            </div >
        )
    }
}
