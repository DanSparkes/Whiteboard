import React, { Component } from "react";
import PropTypes from "prop-types";
import "./TrainingLoads.scss";

class TrainingLoads extends Component {
  static propTypes = {
    one_rep_max: 0,
    lift_list: PropTypes.array.isRequired,
    lift: PropTypes.string,
    max: PropTypes.number,
  };
  render() {
    if (this.props.lift_list.length === 0) {
      return <div>Go Lift!</div>;
    }
    var max = this.props.lift_list[0]["one_rep_max"];
    if (this.props.max > 0) {
      max = this.props.max;
    } else {
      if (
        ["Squat", "Bench", "Deadlift", "Overhead Press"].includes(
          this.props.lift
        ) &&
        max == 0
      ) {
        max = this.props.lift_list[0]["fake_one_rep"];
      } else if (max == 0) {
        for (var i = 0; i < this.props.lift_list.length; i++) {
          if (this.props.lift_list[i]["one_rep_max"] > 0) {
            max = this.props.lift_list[i]["one_rep_max"];
            break;
          }
        }
      }
    }
    const training_percent = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95];
    const training_weights = [];
    for (const [index, value] of training_percent.entries()) {
      training_weights.push(
        <div className="level-item has-text-centered" key={index}>
          <div>
            <p className="heading">{value}%</p>
            <p className="title">{Math.round(max * (value / 100))}</p>
          </div>
        </div>
      );
    }
    const attempts = [
      { reps: 10, percentage: 40 },
      { reps: 10, percentage: 50 },
      { reps: 5, percentage: 60 },
      { reps: 3, percentage: 70 },
      { reps: 3, percentage: 75 },
      { reps: 2, percentage: 80 },
      { reps: 1, percentage: 85 },
      { reps: 1, percentage: 90 },
      { reps: 1, percentage: 95 },
      { reps: 1, percentage: 100 },
      { reps: 1, percentage: 105 },
    ];
    const attempt_weights = [];
    for (const [index, value] of attempts.entries()) {
      attempt_weights.push(
        <div className="level-item has-text-centered" key={index}>
          <div>
            <p className="heading">{value["reps"]} Reps At</p>
            <p className="title">
              {Math.round(max * (value["percentage"] / 100))}
            </p>
          </div>
        </div>
      );
    }
    return (
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
        <div className="level">{training_weights}</div>
        <div className="title has-text-centered">Attempt a new PR!</div>
        <div className="level">
          <div className="level-item has-text-centered">
            <div>
              <p className="heading">10 Reps At</p>
              <p className="title">45</p>
            </div>
          </div>
          {attempt_weights}
        </div>
        <hr />
      </div>
    );
  }
}

export default TrainingLoads;
