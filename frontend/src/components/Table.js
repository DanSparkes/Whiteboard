import React from "react";
import PropTypes from "prop-types";
import key from "weak-key";

const Table = ({ lift_list, maxLiftSetter }) =>
  !lift_list.length ? (
    <p>Nothing to show</p>
  ) : (
    <div className="column">
      <table className="table is-striped">
        <thead>
          <tr>
            {Object.entries(lift_list[0]["labels"]).map((el) => (
              <th key={key(el)}>{el[1]}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {lift_list.map((el) => (
            <tr key={el.id} onClick={() => maxLiftSetter(el)}>
              {Object.entries(lift_list[0]["labels"]).map((val) => (
                <td key={key(val)}>{el[val[0]]}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
Table.propTypes = {
  lift_list: PropTypes.array.isRequired,
  maxLiftSetter: PropTypes.func.isRequired,
};

export default Table;
