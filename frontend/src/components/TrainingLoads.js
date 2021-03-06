import React, { Component } from "react";
import PropTypes from "prop-types";

class TrainingLoads extends Component {
    static propTypes = {
        data: PropTypes.array.isRequired,
        lift: PropTypes.string,

    };
    render() {
        if (this.props.data.length === 0) {
            return (
                <div>Go Lift!</div>
            );
        }
        const one_rep = this.props.lift ? this.props.data[0]["one_rep_max"] : null;
        const fake_rep = this.props.lift ? this.props.data[0]["fake_one_rep"] : null;
        const max = one_rep == 0 ? fake_rep : one_rep;
        const training_percent = [95, 90, 85, 80, 75, 70, 65, 60, 55, 50]
        const training_weights = []
        for (const [index, value] of training_percent.entries()) {
            training_weights.push(
                <div className="level-item has-text-centered" key={index}>
                    <div>
                        <p className="heading">{value}%</p>
                        <p className="title">{Math.round(max * (value / 100))}</p>
                    </div>
                </div>
            )
        }
        const training_loads = this.props.lift ?
            <div className="training-loads">
                <div className="level">
                    <h2 className="title level-item">Training Loads</h2>
                </div>
                <hr />
                <div className="level">
                    <div className="level-left">
                        <div className="level-item has-text-centered">
                            <div>
                                <p className="title">Strength</p>
                                <p className="heading">1-4 reps at 85-95%</p>
                            </div>
                        </div>
                    </div>
                    <div className="level-right">
                        <div className="level-item has-text-centered">
                            <div>
                                <p className="title">Hypertrophy</p>
                                <p className="heading">8-12 reps at 50-75%</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div className="level">
                    {training_weights}
                </div>
                <hr />
            </div> : null;
        return (
            <div>{training_loads}</div>
        );
    }
}

export default TrainingLoads;