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
    };
  }
  static propTypes = {
    data: PropTypes.array.isRequired,
  };

  handleChange = (e) => {
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
          render={(data) => (
            <div>
              <TrainingLoads lift_list={data} lift={this.state.lift} />
              <Table data={data} />
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
