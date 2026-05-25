import { useEffect, useState } from "react";
import API from "../services/api";

function ReviewPage() {

  const [records, setRecords] = useState([]);

  useEffect(() => {

    fetchRecords();

  }, []);

  const fetchRecords = async () => {

    const response = await API.get(
      "/records/"
    );

    setRecords(response.data);
  };

  const approveRecord = async (id) => {

    await API.post(`/approve/${id}/`);

    fetchRecords();
  };

  const rejectRecord = async (id) => {

    await API.post(`/reject/${id}/`);

    fetchRecords();
  };

  return (

    <div className="page-container">

      <div className="card">

        <h1 className="title">
          Review Records
        </h1>

        <table className="review-table">

          <thead>

            <tr>

              <th>ID</th>
              <th>Activity</th>
              <th>Status</th>
              <th>CO2e</th>
              <th>Suspicious</th>
              <th>Actions</th>

            </tr>

          </thead>

          <tbody>

            {records.map((record) => (

              <tr key={record.id}>

                <td>{record.id}</td>

                <td>
                  {record.activity_type}
                </td>

                <td>{record.status}</td>

                <td>{record.co2e}</td>

                <td>
                  {record.suspicious_flag
                    ? "Yes"
                    : "No"}
                </td>

                <td>

                  <button
                    className="approve-btn"
                    onClick={() =>
                      approveRecord(record.id)
                    }
                  >
                    Approve
                  </button>

                  <button
                    className="reject-btn"
                    onClick={() =>
                      rejectRecord(record.id)
                    }
                  >
                    Reject
                  </button>

                </td>

              </tr>
            ))}

          </tbody>

        </table>

      </div>

    </div>
  );
}

export default ReviewPage;