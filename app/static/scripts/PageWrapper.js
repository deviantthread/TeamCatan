import React from 'react';
import Welcome from "./Welcome";
import axios from 'axios';

class PageWrapper extends React.Component {
    constructor(props) {
        super(props);
        this.state = {username: window.localStorage.getItem('username')};
        this.usernameHandler = this.usernameHandler.bind(this);
    }

    usernameHandler(username) {
        console.log(username);
        axios.put(`/game/player/${username}`)
            .then(res => {
            debugger;
                this.setState({ username });
                window.localStorage.setItem('username', username);
            });
    }

    render() {
        let renderedView;
        if (!!this.state.username) {
            renderedView = "HELLO";
        } else {
            renderedView = <Welcome usernameHandler={this.usernameHandler} />;
        }
        return (
        <div>
            {renderedView}
        </div>
        );
    }}
export default PageWrapper;