import React from "react";
import PropTypes from "prop-types";
import key from "weak-key";

const Table = ({ data }) =>
    !data.length ? (
        <p>Nothing to show</p>
    ) : (
            <div className="column">
                <table className="table is-striped">
                    <thead>
                        <tr>
                            {Object.entries(data[0]["labels"]).map(el => <th key={key(el)}>{el[1]}</th>)}
                        </tr>
                    </thead>
                    <tbody>
                        {data.map(el => (
                            <tr key={el.id}>
                                {Object.entries(data[0]["labels"]).map(val => <td key={key(val)}>{el[val[0]]}</td>)}

                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        );
Table.propTypes = {
    data: PropTypes.array.isRequired
};
export default Table;