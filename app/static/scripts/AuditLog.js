import React from 'react';
import axios from 'axios';
import { Accordion, Card, ListGroup } from 'react-bootstrap';

class AuditLog extends React.Component {
    constructor(props) {
        super(props);
        this.refreshState = this.refreshState.bind(this);
        this.state = {};
    }

    componentDidMount() {
        this.refreshState();
        this.refreshTimer = setInterval(()=> this.refreshState(), 1000);
    }

    componentWillUnmount() {
        clearInterval(this.refreshTimer);
        this.refreshTimer = null;
    }

    refreshState() {
        axios.get(`/auditLog`)
            .then(res => {
                if (res.status >= 200 && res.status < 300) {
                    if (!this.state.time || res.data.time > this.state.time) {
                        this.setState(res.data);
                    }
                } else {
                    this.props.usernameUnsetHandler();
                }
            })
            .catch( res => {
                console.log("catch");
                this.props.usernameUnsetHandler();
            });
    }

    render() {
        let auditLogListGroupItems;
        if (this.state.auditLog) {
            auditLogListGroupItems = this.state.auditLog.map((line) => {
                return (
                    <ListGroup.Item>
                        {line}
                    </ListGroup.Item>
                );
            });
        }
        return (
            <Accordion style={{width:'100%'}}>
                <Card>
                    <Accordion.Toggle as={Card.Header} eventKey="0">
                        Audit Log &#9660;
                    </Accordion.Toggle>
                    <Accordion.Collapse eventKey="0">
                        <Card.Body>
                            <ListGroup>
                                {auditLogListGroupItems}
                            </ListGroup>
                        </Card.Body>
                    </Accordion.Collapse>
                </Card>
            </Accordion>
        );
    }}
export default AuditLog;