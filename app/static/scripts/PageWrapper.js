import React from 'react';
import Welcome from "./Welcome";
import GameView from "./GameView";
import axios from 'axios';

class PageWrapper extends React.Component {
    constructor(props) {
        super(props);
        this.state = {username: window.localStorage.getItem('username')};
        this.usernameSetHandler = this.usernameSetHandler.bind(this);
        this.usernameUnsetHandler = this.usernameUnsetHandler.bind(this);
    }

    usernameSetHandler(username) {
        axios.put(`/game/player/${username}`)
            .then(res => {
                this.setState({ username });
                window.localStorage.setItem('username', username);
            });
    }
    usernameUnsetHandler() {
        this.setState({ username : null });
        window.localStorage.removeItem('username');
    }
    render() {
        let renderedView;
        if (!!this.state.username) {
            renderedView = <GameView username={this.state.username} usernameUnsetHandler={this.usernameUnsetHandler}/>;
        } else {
            renderedView = <Welcome usernameHandler={this.usernameSetHandler} />;
        }
        return (
        <div>
            {renderedView}
        </div>
        );
    }}
export default PageWrapper;