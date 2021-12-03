import React, { Component } from "react";

import DataProvider from "../../components/DataProvider";
import LiftList from "../../components/LiftList";

class Lifts extends Component {
    render() {
        return (
            <div>
                <DataProvider
                    endpoint="api/movements/"
                    render={data => <LiftList data={data} />}
                />
            </div>
        );
    }
}
export default Lifts;
