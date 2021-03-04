import React, { Component } from "react";
import PropTypes from "prop-types";
import DataProvider from "./DataProvider";
import Table from "./Table";
import TrainingLoads from "./TrainingLoads";
import ModalForm from "./Modal";

class LiftList extends Component {
  constructor() {
    super();

    this.state = {
      lift: null,
      endpoint: "api/lifts/",
      max: 0,
    };
  }
  static propTypes = {
    data: PropTypes.array.isRequired,
  };

  handleChange = (e) => {
    this.setState({ max: 0 });
    this.setState({ lift: e.target.value });
    this.setState({ endpoint: "api/lifts/" + e.target.value });
  };

  resetEndpoint = (e) => {
    this.setState({ lift: null });
    this.setState({ endpoint: "api/lifts/" });
  };

  liftHandler = (lift) => {
    this.setState({ lift: lift });
    this.setState({ endpoint: "api/lifts/" + lift });
  };

  maxLiftSetter = (lift) => {
    if (lift["fake_one_rep"] > 0) {
      this.setState({ max: lift["fake_one_rep"] });
    } else {
      this.setState({ max: lift["one_rep_max"] });
    }
  };

  render() {
    return (
      <div>
        <div className="columns">
          {this.props.data.map((el) => (
            <div className="column" key={el.id}>
              <button
                className={
                  el.name === this.state.lift ? "button is-primary" : "button"
                }
                onClick={this.handleChange}
                value={el.name}
              >
                {el.name}
              </button>
            </div>
          ))}
          <div className="column">
            <button
              className={
                this.state.lift === null ? "button is-primary" : "button"
              }
              onClick={this.resetEndpoint}
            >
              All Lifts
            </button>
          </div>
        </div>
        <DataProvider
          endpoint={this.state.endpoint}
          render={(lifts) => (
            <div>
              <TrainingLoads
                lift_list={lifts}
                lift={this.state.lift}
                max={this.state.max}
              />
              <Table lift_list={lifts} maxLiftSetter={this.maxLiftSetter} />
            </div>
          )}
        />
        <div id="lift-modal" style={{ marginTop: "auto" }}>
          <ModalForm handler={this.liftHandler} />
        </div>
      </div>
    );
  }
}
export default LiftList;
