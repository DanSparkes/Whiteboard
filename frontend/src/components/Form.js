import React, { Component } from "react";
import PropTypes from "prop-types";
import Select from 'react-select';

class Form extends Component {
    static propTypes = {
        endpoint: PropTypes.string.isRequired,
        data: PropTypes.array.isRequired,
        handler: PropTypes.func,
        closeFunc: PropTypes.func,
    };
    state = {
        lift_name: null,
        weight: 0,
        reps: 0
    };
    handleChangeSelection = lift_name => {
        this.setState({ lift_name });
    };
    handleChange = e => {
        this.setState({ [e.target.name]: e.target.value });
    };
    handleSubmit = e => {
        e.preventDefault();
        const { lift_name, weight, reps } = this.state;
        let one_rep_max = 0;
        let fake_one_rep = 0;
        if (reps == 1) {
            one_rep_max = weight;
        } else {
            fake_one_rep = weight * (1 + reps / 30);
        }
        let name = lift_name.label;
        const lift = { name, one_rep_max, fake_one_rep };
        const conf = {
            method: "post",
            body: JSON.stringify(lift),
            headers: new Headers({ "Content-Type": "application/json" })
        };
        fetch(this.props.endpoint, conf).then(response => console.log(response));
        this.props.handler(name)
        this.props.closeFunc()
    };
    render() {
        const { lift_name, weight, reps } = this.state;
        const lift_list = this.props.data.map(el => (
            { value: el.id, label: el.name }
        ));
        return (
            <div className="column">

                <form onSubmit={this.handleSubmit}>
                    <div className="field">
                        <label className="label">Name</label>
                        <div className="control">
                            <Select
                                options={lift_list}
                                name="lift_name"
                                onChange={this.handleChangeSelection}
                                value={lift_name}
                            />
                        </div>
                    </div>
                    <div className="field">
                        <label className="label">Weight</label>
                        <div className="control">
                            <input
                                className="input"
                                type="text"
                                name="weight"
                                onChange={this.handleChange}
                                value={weight}
                                required
                            />
                        </div>
                    </div>
                    <div className="field">
                        <label className="label">Reps</label>
                        <div className="control">
                            <input
                                className="input"
                                type="text"
                                name="reps"
                                onChange={this.handleChange}
                                value={reps}
                                required
                            />
                        </div>
                    </div>
                    <div className="control">
                        <button type="submit" className="button is-info">
                            Submit
            </button>
                    </div>
                </form>
            </div>
        );
    }
}
export default Form;