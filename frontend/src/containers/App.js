import React from "react";
import ReactDOM from "react-dom";

import Lifts from "./Whiteboard/Lifts.js"

const App = () => (
    <React.Fragment>
        <Lifts />
    </React.Fragment >
);
const wrapper = document.getElementById("app");
wrapper ? ReactDOM.render(<App />, wrapper) : null;