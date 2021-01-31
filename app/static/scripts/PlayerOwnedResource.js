import React from 'react';
import axios from 'axios';
import { Form, Card, Button, ListGroup } from 'react-bootstrap';

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
        this.resourceSelectChange = this.resourceSelectChange.bind(this);
        this.selected = {...this.initState};
    }

    spendResourcesClick() {
        const reqHeader = { headers: {'Content-Type': 'application/json'} };
        const reqData = {
            player: this.props.username,
            resources: {...this.selected}
        };
        axios.post(`/store/deposit?player=${this.props.username}`, reqData, reqHeader)
            .then(res => {
                if (res.status >= 200 && res.status < 300) {
                    this.selected = {...this.initState};
                    this.props.refreshState();
                } else {
                    console.log("spend resources failed 1");
                }
            })
            .catch( res => {
                console.log("spend resources failed 2");
            });
    }
//    using janky class variable to avoid rerender - cuz react unmount and rerender doesn't work properly and keeps checkbox checked
    resourceSelectChange(e) {
        const resourceType = e.target.nextElementSibling.textContent.trim();
        let tempState = {...this.selected};
        if (e.target.checked) {
            tempState[resourceType] = this.selected[resourceType] + 1;
            this.selected = tempState;
        } else if (this.selected[resourceType] > 0) {
            tempState[resourceType] = this.selected[resourceType] - 1;
            this.selected = tempState;
        }
    }

    render() {
        let resourceSpreadRender = [];
        if (!!this.props.resourceCards) {
            Object.keys(this.props.resourceCards).forEach(key =>
            {
                let i;
                for(i = 0; i < this.props.resourceCards[key]; i++) {
                    const uniqueHash = Math.random().toString(36).slice(-6); // so react can properly rerender after unmount
                    resourceSpreadRender.push(
                    <ListGroup.Item>
                        <Form.Check
                          type='checkbox'
                          key={key+i+uniqueHash}
                          id={key+i}
                          label={key}
                          onChange={this.resourceSelectChange}
                        />
                    </ListGroup.Item>
                    );
                }
            });
        }

        return (
                 <Card.Body>
                    <Card.Title>Resource Cards</Card.Title>
                    <div className="overflow-auto" style={{height:'220px', border: '1px solid lightgrey', 'border-radius': '5px'}}>
                    <ListGroup ref={c => this.resourceListGroup = c}>
                    {resourceSpreadRender}
                    </ListGroup>
                    </div>
                    <Button className="mt-3" variant="dark" onClick={this.spendResourcesClick}>Spend selected</Button>
                </Card.Body>
        );
    }}
export default PlayerOwnedResource;