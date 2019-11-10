import React, { Component } from 'react';
import Modal from 'react-modal';
import PropTypes from "prop-types";

import Form from "./Form";
import DataProvider from "./DataProvider";

const customStyles = {
    content: {
        top: '50%',
        left: '50%',
        right: 'auto',
        bottom: 'auto',
        marginRight: '-50%',
        transform: 'translate(-50%, -50%)'
    }
};

// Make sure to bind modal to your appElement (http://reactcommunity.org/react-modal/accessibility/)
Modal.setAppElement('body')

class ModalForm extends Component {
    constructor() {
        super();

        this.state = {
            modalIsOpen: false
        };

        this.openModal = this.openModal.bind(this);
        this.afterOpenModal = this.afterOpenModal.bind(this);
        this.closeModal = this.closeModal.bind(this);
    }
    static propTypes = {
        handler: PropTypes.func,
    };

    openModal() {
        this.setState({ modalIsOpen: true });
    }

    afterOpenModal() {
        // references are now sync'd and can be accessed.
        this.subtitle.style.color = '#f00';
    }

    closeModal() {
        this.setState({ modalIsOpen: false });
    }

    render() {
        return (
            <div>
                <button onClick={this.openModal} className="button is-info">Record Lift</button>

                <Modal
                    isOpen={this.state.modalIsOpen}
                    onAfterOpen={this.afterOpenModal}
                    onRequestClose={this.closeModal}
                    style={customStyles}
                    contentLabel="Lift!"
                >
                    <div className="modal-card">
                        <header className="modal-card-head">
                            <p className="modal-card-title" ref={subtitle => this.subtitle = subtitle}>Enter your Lift!</p>
                            <button className="delete" aria-label="close" onClick={this.closeModal}></button>
                        </header>
                        <section className="modal-card-body">
                            <DataProvider
                                endpoint="api/movements/"
                                render={data => <Form
                                    data={data}
                                    endpoint="api/lifts/"
                                    handler={this.props.handler}
                                    closeFunc={this.closeModal} />}
                            />
                        </section>
                        <footer className="modal-card-foot">
                            <button className="button" onClick={this.closeModal}>Cancel</button>
                        </footer>
                    </div>
                </Modal>
            </div>
        );
    }
}

export default ModalForm;