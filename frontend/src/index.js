import React from "react";
import ReactDOM from "react-dom";

import Lifts from "./containers/Whiteboard/Lifts"

const App = () => (
    <React.Fragment>
        <Lifts />
    </React.Fragment >
);
const wrapper = document.getElementById("app");
wrapper ? ReactDOM.render(<App />, wrapper) : null;
