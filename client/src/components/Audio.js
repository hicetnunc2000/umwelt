import React, { Component } from 'react'

export default class Audio extends Component {

    constructor(props) {
        super(props)

        this.state = {

        }
    }

    render() {
        return (
            <div>
                <audio src={`${}`}></audio>
            </div>
        )
    }
}
