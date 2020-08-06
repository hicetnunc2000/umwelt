import React, { Component } from 'react'
import Search from './Search'
import { Card, Col, Row } from 'reactstrap'

export default class Home extends Component {
    constructor(props) {
        super(props)

        this.state = {

        }
    }

    render() {
        return (
            <div>
                <Row>
                    <Col sm="12" md={{ size: 6, offset: 3 }}>
                        <Card body style={{border : "none"}}>
                            <img style={{  height: "30%", width: "30%", margin: "auto" }}src={require("../umwelt.png")} />
                        </Card>
                    </Col>
                </Row>
                <Search />

            </div>
        )
    }
}
