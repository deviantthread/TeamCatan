import React from 'react';
import axios from 'axios';
import { Form, Card, Button, ListGroup, InputGroup, FormControl, Container, Row, Col, Image, CardGroup } from 'react-bootstrap';

class PlayerOwnedResource extends React.Component {
    constructor(props) {
        super(props);
        this.initState = {
            Brick: 0,
            Ore: 0,
            Sheep: 0,
            Wheat: 0,
            Wood: 0
        };
        this.spendResourcesClick = this.spendResourcesClick.bind(this);
        this.minusClick = this.minusClick.bind(this);
        this.plusClick = this.plusClick.bind(this);
        this.sendCardToPlayerClick = this.sendCardToPlayerClick.bind(this);
        this.selected = {...this.initState};
        this.Brick = React.createRef();
        this.Ore = React.createRef();
        this.Sheep = React.createRef();
        this.Wheat = React.createRef();
        this.Wood = React.createRef();
        this.state = {...this.initState};
    }
    sendCardToPlayerClick(e) {
        const reqHeader = { headers: {'Content-Type': 'application/json'} };
        const reqData = {
            playerFrom: this.props.username,
            playerTo: this.otherPlayerListRef.value,
            resources: this.state
        };
        axios.post(`/player/sendCardsToPlayer`, reqData, reqHeader)
            .then(res => {
                if (res.status >= 200 && res.status < 300) {
                    this.setState({...this.initState});
                    this.props.refreshState();
                } else {
                    console.log("spend resources failed 1");
                }
            })
            .catch( res => {
                console.log("spend resources failed 2");
            });
    }

    spendResourcesClick() {
        const reqHeader = { headers: {'Content-Type': 'application/json'} };
        const reqData = {
            player: this.props.username,
            resources: this.state
        };
        axios.post(`/store/deposit`, reqData, reqHeader)
            .then(res => {
                if (res.status >= 200 && res.status < 300) {
                    this.setState({...this.initState});
                    this.props.refreshState();
                } else {
                    console.log("spend resources failed 1");
                }
            })
            .catch( res => {
                console.log("spend resources failed 2");
            });
    }
    minusClick(e) {
        const resourceType = e.target.dataset.resource;
        const currentQty = parseInt(this[resourceType].current.textContent);
        const newQty = currentQty > 0 ? currentQty-1 : 0;

        let updateState = {};
        updateState[resourceType] = newQty;
        this.setState(updateState);
    }

    plusClick(e) {
        const resourceType = e.target.dataset.resource;
        const currentQty = parseInt(this[resourceType].current.textContent);
        const newQty = currentQty < this.props.resourceCards[resourceType] ? currentQty + 1 : currentQty;

        let updateState = {};
        updateState[resourceType] = newQty;
        this.setState(updateState);
    }

    render() {
        let resourceSpreadRender2 = [];
        let totalCount = 0;
        if (!!this.props.resourceCards) {
            Object.keys(this.props.resourceCards).forEach(key =>
            {
                totalCount += this.props.resourceCards[key];
                resourceSpreadRender2.push(
                <Card>
                    <Card.Img src={"/static/images/" + key + ".png"} alt="Card image"/>
                    <Card.Body>
                    <Card.Text className="text-center">{this.props.resourceCards[key]} in hand</Card.Text>
                        <div className="d-flex justify-content-center">
                            <div>
                                <Button variant="outline-info" data-resource={key} onClick={this.minusClick}>-</Button>
                            </div>
                            <div className="align-self-center px-2" ref={this[key]} onChange>
                                {this.state[key]}
                            </div>
                            <div>
                                <Button variant="outline-info" data-resource={key} onClick={this.plusClick}>+</Button>
                            </div>
                        </div>
                    </Card.Body>
                </Card>
                );
            });
        }

        let otherPlayerList;
        if (!!this.props.otherPlayerNames) {
            otherPlayerList = this.props.otherPlayerNames.map((otherPlayer) => {
                return (
                    <option data-otherplayer={otherPlayer}>{otherPlayer}</option>
                );
            });
        }
        return (
        <Card.Body>
            <Card.Title>Resource Cards ({totalCount})</Card.Title>
            <CardGroup>
            {resourceSpreadRender2}
            </CardGroup>
            <Button className="mt-3" variant="dark" onClick={this.spendResourcesClick}>Spend selected</Button>
            <InputGroup className="mt-3">
                <Form.Control as="select" ref={c => this.otherPlayerListRef = c}>
                {otherPlayerList}
                </Form.Control>
                <InputGroup.Append>
                    <Button variant="dark" onClick={this.sendCardToPlayerClick}>Send</Button>
                </InputGroup.Append>
            </InputGroup>
        </Card.Body>
        );
    }}
export default PlayerOwnedResource;